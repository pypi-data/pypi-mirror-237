import os
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans
from blobBgone.featureHandler import featureHandler
from blobBgone.eval import eval

def BlobBGone_legacy(path:str = None, key:str = "*", return_IDs:bool = False, regularization_method:str = 'standardize', custom_feature_weights:dict = {'MAX_DIST':1, 'CV_AREA':1, 'SPHE':1, 'ELLI':1, 'CV_DENSITY':1}, verbose:bool = True):    
    """Standalone implementation of the Blob-B-Gone method for removing blobs from Single Particle Tracking data.

    Args:
        path (str, optional): Indicate the path to the directory containing the data files as .npy with the format [Z,Y,X,T]. Technically, the sequence of spatial axes is trivial, as we use a point cloud approach. Defaults to None.
        return_IDs (bool, optional): Flag if you want to merely return the IDs of tracks belonging to either cluster. Defaults to False.
        regularization_method (str, optional): Flag the method to be used for regularization from ['standardize', 'normalize', 'force_raw']. Defaults to 'standardize'.
        custom_feature_weights (dict, optional): Set custom feature weights to be used for clustering. Defaults to {'MAX_DIST':1, 'CV_AREA':1, 'SPHE':1, 'ELLI':1, 'CV_DENSITY':1}.
        verbose (bool, optional): Flag the verbosity while clustering. Defaults to True.

    Returns:
        blobs, free (featureHandler or int): Returns either the feature handler objects of the two clusters or the IDs of the two clusters.
    """
    # Grab the files
    files = featureHandler.grab_files(path = path, key = key, dtype=".npy")
    if verbose:
        print(f"Found {len(files)} files in the '{files[0].split(os.sep)[-2]}' directory.")
        
    # Setup the task list
    task_list = [featureHandler.from_npy(path = file, verbose = False) for file in files]
    
    if verbose:
        print("\nExtracting features...")
    # Extract features
    features = []
    for task in task_list:
        task.extract()
        features.append(task.to_array())

    # Regularize the features
    features = featureHandler.regularize_output(features, method = regularization_method)
    assert np.all(np.isfinite(features)), "NaN values still present in features."

    # Grab weights
    weights = np.array([custom_feature_weights[feature] for feature in task_list[0].features.__dict__.keys()])

    if verbose:
        print("\nClustering...")
    # Cluster the features
    clustering_FH  = KMeans(
        n_clusters = 2,
        init = 'k-means++',
        n_init = 'auto',
        max_iter = 300,
        verbose = 0,
        random_state = None,
        )
    fit_predict_FH = clustering_FH.fit_predict(features*weights)
    
    cluster_1 = [task_list[i] for i in range(len(task_list)) if fit_predict_FH[i] == 0]
    cluster_2 = [task_list[i] for i in range(len(task_list)) if fit_predict_FH[i] == 1]
    comb = [cluster_1, cluster_2]
    
    ## Evaluate Blobbness ##
    # this is an experimental metric that attempts to decide what cluster is the blob cluster
    if verbose:
        print("\nBlob-score is being calculated...\n")
    c1_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_1])
    c2_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_2])
    if verbose:
        print("Cluster 1 Blob-score: {:.2f}".format(c1_blobbness))
        print("Cluster 2 Blob-score: {:.2f}".format(c2_blobbness))
        print("Blob-score ratio: 1 : {:.2f}".format(max([c1_blobbness, c2_blobbness])/min([c1_blobbness, c2_blobbness])))
        print(
            "Silhouette Coefficient: %0.3f"
            % metrics.silhouette_score(features, fit_predict_FH, metric="euclidean")
        )
        
        print("\nCluster {} has been estimated to be the blob cluster.".format(np.argmax([c1_blobbness, c2_blobbness])+1))

    if not return_IDs:
        blobs = [task for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
        free =  [task for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
        return blobs, free

    blobs = [task.ID for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
    free =  [task.ID for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
    return blobs, free

## Class definition of BlobBGone ##

class blobBgone(object):
    __verbose:bool
    __regularization:str
    __custom_weights:dict
    
    __task_list:list
    __blob_IDs:list
    __free_IDs:list
    __blobs:list
    __free:list
    
    ## Initialization ##
    def __init__(self, task_list:list, 
                 verbose:bool = True) -> None:
        self.__verbose = verbose
        self.__custom_weights = {'MAX_DIST':1, 'CV_AREA':1, 'SPHE':1, 'ELLI':1, 'CV_DENSITY':1}
        self.__task_list = task_list
        self.__regularization = "standardize"
        self.__blob_IDs = None
        self.__free_IDs = None
        self.__blobs = None
        self.__free = None
        
        self.__post_init__()
    
    ## Execute after initialization ##
    def __post_init__(self):
        self.__sort_by_ID()
    
    ## Properties ##
    @property
    def verbose(self):
        return self.__verbose
    @verbose.setter
    def verbose(self, verbose:bool):
        self.__verbose = verbose
        return print("Verbosity has been set to {}.".format(verbose))
    
    @property
    def regularization(self):
        return self.__regularization
    @regularization.setter
    def regularization(self, regularization:str):
        try:
            assert regularization in ['standardize', 'normalize', 'force_raw']
        except AssertionError as error:
            print(error)
            print("The regularization method must be in ['standardize', 'normalize', 'force_raw'].")
            
        self.__regularization = regularization
        return print("Regularization method has been set to {}".format(regularization))
    
    @property
    def task_list(self):
        return self.__task_list
    @task_list.setter
    def task_list(self, task_list:list):
        self.__task_list = task_list
        return print("Task list has been updated.")
    
    @property
    def blobs(self):
        try:
            assert self.__blobs is not None, "Blob cluster not yet extracted."
        except AssertionError as error:
            print(error)
            return print("Please call the 'run' method first.")
        return self.__blobs
    @blobs.setter
    def blobs(self, *args, **kwargs):
        return print("blobs attribute is read-only.")
    
    @property
    def free(self):
        try:
            assert self.__free is not None, "Free cluster not yet extracted."
        except AssertionError as error:
            print(error)
            return print("Please call the 'run' method first.")
        return self.__free
    @free.setter
    def free(self, *args, **kwargs):
        return print("free attribute is read-only.")
    
    @property
    def blob_IDs(self):
        try:
            assert self.__blob_IDs is not None, "Blob cluster not yet extracted."
        except AssertionError as error:
            print(error)
            return print("Please call the 'run' method first.")
        return self.__blob_IDs
    @blob_IDs.setter
    def blob_IDs(self, *args, **kwargs):
        return print("blob_IDs attribute is read-only.")
    
    @property
    def free_IDs(self):
        try:
            assert self.__free_IDs is not None, "Free cluster not yet extracted."
        except AssertionError as error:
            print(error)
            return print("Please call the 'run' method first.")
        return self.__free_IDs
    @free_IDs.setter
    def free_IDs(self, *args, **kwargs):
        return print("free_IDs attribute is read-only.")
        
    ## Class Methods ##
    @classmethod
    def from_npy(cls, path:str = None, key:str = "*",
                 verbose:bool = True) -> None:
        
        files = featureHandler.grab_files(path = path, key = key, dtype=".npy")
        if verbose:
            print(f"Found {len(files)} files in the '{files[0].split(os.sep)[-2]}' directory.")
            
        task_list = [featureHandler.from_npy(path = file, verbose = False) for file in files]
        if verbose:
            print(f"{len(task_list)} tasks have been created.")
        
        return cls(task_list = task_list, verbose = verbose)
    
    @classmethod
    def from_pointCloud(cls, pointCloud:np.ndarray, 
                        verbose:bool = True) -> None:
        
        task_list = [featureHandler.from_pointCloud(pointCloud = pointCloud, verbose = False)]
        if verbose:
            print(f"{len(task_list)} tasks have been created.")
        
        return cls(task_list = task_list, verbose = verbose)
    
    ## Main Function ##
    def run(self):

        # Extracting Features
        features = self.__extract_features()
        
        # Regularize the features
        features = self.__regularize_features(features=features)
 
        # Grab weights
        features = self.__apply_custom_weights(features)

        # Cluster the features
        if self.__verbose:
            print("\nClustering...")
            
        clustering_FH  = KMeans(
            n_clusters = 2,
            init = 'k-means++',
            n_init = 'auto',
            max_iter = 300,
            verbose = 0,
            random_state = None,
            )
        fit_predict_FH = clustering_FH.fit_predict(features)
        
        cluster_1 = [self.task_list[i] for i in range(len(self.task_list)) if fit_predict_FH[i] == 0]
        cluster_2 = [self.task_list[i] for i in range(len(self.task_list)) if fit_predict_FH[i] == 1]
        comb = [cluster_1, cluster_2]
        
        ## Evaluate Blobbness ##
        if self.__verbose:
            print("\nBlob-score is being calculated...\n")
        c1_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_1])
        c2_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_2])
        
        if self.__verbose:
            print("Cluster 1 Blob-score: {:.2f}".format(c1_blobbness))
            print("Cluster 2 Blob-score: {:.2f}".format(c2_blobbness))
            print("Blob-score ratio: 1 : {:.2f}".format(max([c1_blobbness, c2_blobbness])/min([c1_blobbness, c2_blobbness])))
            print(
                "Silhouette Coefficient: %0.3f"
                % metrics.silhouette_score(features, fit_predict_FH, metric="euclidean")
            )
            
            print("\nCluster {} has been estimated to be the blob cluster.".format(np.argmax([c1_blobbness, c2_blobbness])+1))

        self.__blobs = [task for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
        self.__free =  [task for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
        self.__blob_IDs = [task.ID for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
        self.__free_IDs =  [task.ID for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
        return print("Blob-B-Gone has finished running.\n\nGet the results with the 'blobs' and 'free' attributes\nor via the 'blob_IDs' and 'free_IDs' attributes.")
    
    ## Evaluation ##
    def plot_PCA(self, include_eigenvectors:bool = True, absolute:bool = False):
        combined_features, labels = self.__construct_labels()
        return eval.plot_PCA(features = self.__apply_custom_weights(self.__regularize_features(combined_features)), 
                             labels = labels, 
                             feature_keywords = list(self.__task_list[0].features.__dict__.keys()), 
                             include_eigenvectors=include_eigenvectors,
                             absolute = absolute)
    
    ## Advanced User Only ##
    @property
    def custom_weights(self):
        return self.__custom_weights
    @custom_weights.setter
    def custom_weights(self, custom_weights:dict):
        try:
            assert isinstance(custom_weights, dict), "custom_weights must be a dictionary."
            assert set(custom_weights.keys()) == set(self.task_list[0].features.__dict__.keys()), "custom_weights must have the same keys as the features."
        except AssertionError as error:
            print(error)
            return print("Default weights will be used.")
        self.__custom_weights = custom_weights
    
    ## Helper Functions ##
    def __sort_by_ID(self):
        self.__task_list = sorted(self.__task_list, key=lambda x: x.ID)
        if self.__verbose:
            print("Task list has been sorted by ID.")
        return
    
    def __extract_features(self):
        if self.__verbose:
            print("\nExtracting features...")
        # Extract features
        features = []
        for task in self.task_list:
            task.extract()
            features.append(task.to_array())
        return features
    
    def __regularize_features(self, features:np.ndarray):
        if self.__verbose:
            print("\nRegularizing features...")
        features = featureHandler.regularize_output(features, method = self.__regularization)
        assert np.all(np.isfinite(features)), "NaN values still present in features."
        return features
    
    def __apply_custom_weights(self, features:np.ndarray):
        weights = np.array([self.__custom_weights[feature] for feature in list(self.__task_list[0].features.__dict__.keys())])
        if weights.all() == 1:
            if self.__verbose:
                print("No custom weights have been applied.")
            return features
        if self.__verbose:
            print("Custom weights have been applied.")
        return features*weights
    
    def __construct_labels(self):
        try:
            assert self.__blobs is not None, "Blob cluster not yet extracted."
            assert self.__free is not None, "Free cluster not yet extracted."
        except AssertionError as error:
            print(error)
            return print("Please call the 'run' method first.")

        if self.__verbose:
            print("\n Collecting features...")
        combined_features = np.concatenate(([task.to_array() for task in self.__blobs], 
                                            [task.to_array() for task in self.__free]))
        if self.__verbose:
            print("\n Constructing labels...")
        labels = np.concatenate((np.zeros(len(self.__blobs)), np.ones(len(self.__free))))
        return combined_features, labels
    

        
    