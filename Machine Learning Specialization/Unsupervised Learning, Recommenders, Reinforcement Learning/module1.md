# Clustering

A **clustering** algorithm looks at a number of data points and automatically finds data points that are related or similar to each other

In contrast to supervised learning, unsupervised learning algorithm receives only the inputs *x*, that is, the training set only contains the *x* parameter. Hence, as long as we don't have the output labels, we can't tell the algorithm what it's the right answer

Instead of this, we're going to ask the algorithm to find something (a structure) *interesting* about the data

A clustering algorithm looks at a dataset and check if it can grouped into **clusters** (groups of points that are similar to each other)

![clustering-algorithm](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/clustering_algorithm1.png)

## Applications of clustering

* Grouping similar news

* Market segmentation

* DNA analysis

* Astronomical data analysis

## K-means Algorithms

* **Cluster Centroids**: centers of the clusters

Firstly, the algorithm guesses (randomly) two centers of the two clusters (considering that we specify the number of it)

Then, it repeatly does two things:
1. Assign points to cluster centroids
    * It will go to each of the data points and verify if it is closer to a cluster of another, then assign the point to the closer cluster
2. Move cluster centroids
    * It will take an average of the points of each cluster, then

![k-means-step1](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means_1.png)
![k-means-step2](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means_2.png)

At a certain time, there'll be no more changes to the points or to the centroids, then, at this point, the k-means clustering algorithm has converged, since applying the 2 steps doesn't result in any more changes

![k-means](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means_3.png)

**Algorithm**

1. Randomly initialize K cluster centroids *u1*, *u2*, ..., *uk*
2. Repeat
    * Assign points to cluster centroids (we want to minimize ||x[i] - uk||²)
    ```
    for i = 1 to m:
        c[i] = index (from 1 to K) of cluster centroid closest to x[i]
    ```