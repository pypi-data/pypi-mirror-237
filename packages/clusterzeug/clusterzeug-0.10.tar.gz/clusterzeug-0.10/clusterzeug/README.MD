# Some functions for clustering 

## Tested against Windows / Python 3.11 / Anaconda

## pip install clusterzeug

```python


from clusterzeug import (
    birchcluster,
    gaussianmixture,
    opticscluster,
    hdbscancluster,
    dbscan,
    agglomerativeclustering,
    spectralclustering,
    kmeanscluster,
    minibatchkmeanscluster,
    afinity_propagation,
    mean_shift,
)
import numpy as np
import random
data = np.array(
    [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(100)],
    dtype=np.int64,
)
a1 = birchcluster(data, n_clusters=10)
a2 = gaussianmixture(data, n_components=5)
a3 = opticscluster(data, min_samples=5)
a4 = hdbscancluster(data, min_cluster_size=5)
a5 = dbscan(data, eps=0.5, min_samples=5)
a6 = agglomerativeclustering(data, n_clusters=10)
a7 = spectralclustering(data, n_clusters=10)
res = kmeanscluster(data, n_clusters=10)
print(res)
res2 = minibatchkmeanscluster(data, n_clusters=10)
print(res2)
aff = afinity_propagation(data, damping=0.5, preference=-10)
print(aff)
ms = mean_shift(data,bandwidth=2.0)
print(ms)

```