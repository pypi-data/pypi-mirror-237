import numpy as np
from sklearn.cluster import (
    KMeans,
    MiniBatchKMeans,
    AffinityPropagation,
    MeanShift,
    SpectralClustering,
    AgglomerativeClustering,
    DBSCAN,
    OPTICS,
    Birch,
)
import numexpr
from sklearn.cluster._hdbscan import hdbscan
from sklearn.mixture import GaussianMixture


def kmeanscluster(data, n_clusters=10, **kwargs):
    r"""
    Perform K-Means clustering on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): The number of clusters to form.
        **kwargs: Additional keyword arguments for the KMeans model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    kmeans = KMeans(n_clusters=n_clusters, **kwargs)
    kmeans.fit(data)
    labels = kmeans.labels_
    results = {}
    for c in range(n_clusters):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def minibatchkmeanscluster(data, n_clusters=10, **kwargs):
    """
    Perform Mini-Batch K-Means clustering on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): The number of clusters to form.
        **kwargs: Additional keyword arguments for the MiniBatchKMeans model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    kmeans = MiniBatchKMeans(n_clusters=n_clusters, **kwargs)
    kmeans.fit(data)
    labels = kmeans.labels_
    results = {}
    for c in range(n_clusters):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def afinity_propagation(data, damping=0.1, preference=-30, **kwargs):
    """
    Perform clustering using Affinity Propagation on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        damping (float): Damping parameter for the Affinity Propagation model.
        preference (float): Preference parameter for the Affinity Propagation model.
        **kwargs: Additional keyword arguments for the AffinityPropagation model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    affinity_propagation = AffinityPropagation(
        damping=damping, preference=preference, **kwargs
    )

    affinity_propagation.fit(data)
    labels = affinity_propagation.labels_
    results = {}
    for c in np.unique(labels):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def mean_shift(data,bandwidth=2.0, **kwargs):
    """
    Perform clustering using Mean Shift on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        bandwidth (float): Bandwidth parameter for the Mean Shift model.
        **kwargs: Additional keyword arguments for the MeanShift model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """

    mean_shift = MeanShift(bandwidth=bandwidth, **kwargs)
    mean_shift.fit(data)
    labels = mean_shift.labels_
    results = {}
    for c in np.unique(labels):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def spectralclustering(data, n_clusters=10, **kwargs):
    """
    Perform clustering using Spectral Clustering on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): The number of clusters to form.
        **kwargs: Additional keyword arguments for the SpectralClustering model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    spectral_cluster = SpectralClustering(n_clusters=n_clusters, **kwargs)
    labels = spectral_cluster.fit_predict(data)
    results = {}
    for c in range(n_clusters):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def agglomerativeclustering(data, n_clusters=10, **kwargs):
    """
    Perform clustering using Agglomerative Clustering on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): The number of clusters to form.
        **kwargs: Additional keyword arguments for the AgglomerativeClustering model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    agglomerative_cluster = AgglomerativeClustering(n_clusters=n_clusters, **kwargs)
    labels = agglomerative_cluster.fit_predict(data)
    results = {}
    for c in range(n_clusters):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def dbscan(data, eps=0.5, min_samples=5, **kwargs):
    """
    Perform clustering using DBSCAN (Density-Based Spatial Clustering of Applications with Noise) on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        eps (float): The maximum distance between two samples for them to be considered as in the same neighborhood.
        min_samples (int): The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
        **kwargs: Additional keyword arguments for the DBSCAN model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    dbscan_cluster = DBSCAN(eps=eps, min_samples=min_samples, **kwargs)
    labels = dbscan_cluster.fit_predict(data)
    results = {}
    for c in np.unique(labels):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def hdbscancluster(data, min_cluster_size=5, **kwargs):
    """
    Perform clustering using HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        min_cluster_size (int): The minimum number of samples in a cluster.
        **kwargs: Additional keyword arguments for the HDBSCAN model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    hdbscan_cluster = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, **kwargs)
    labels = hdbscan_cluster.fit_predict(data)
    results = {}
    for c in np.unique(labels):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def opticscluster(data, min_samples=5, **kwargs):
    """
    Perform clustering using OPTICS (Ordering Points To Identify the Clustering Structure) on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.
        **kwargs: Additional keyword arguments for the OPTICS model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    optics_cluster = OPTICS(min_samples=min_samples, **kwargs)
    labels = optics_cluster.fit_predict(data)
    results = {}
    for c in np.unique(labels):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def gaussianmixture(data, n_components=5, **kwargs):
    """
    Perform clustering using Gaussian Mixture Models on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_components (int): The number of mixture components.
        **kwargs: Additional keyword arguments for the GaussianMixture model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    gaussian_mixture = GaussianMixture(n_components=n_components, **kwargs)
    labels = gaussian_mixture.fit_predict(data)
    results = {}
    for c in range(n_components):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results


def birchcluster(data, n_clusters=10, **kwargs):
    """
    Perform clustering using BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies) on the given data.

    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): The number of clusters to form.
        **kwargs: Additional keyword arguments for the Birch model.

    Returns:
        dict: A dictionary of clusters with data points assigned to each cluster.
    """
    birch_cluster = Birch(n_clusters=n_clusters, **kwargs)
    labels = birch_cluster.fit_predict(data)
    results = {}
    for c in range(n_clusters):
        results[c] = data[
            numexpr.evaluate(
                f"labels == {c}", local_dict={"labels": labels}, global_dict={}
            )
        ]
    return results

