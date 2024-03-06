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
    * Assign points to cluster centroids (we want to minimize the distance ||x[i] - uk||²)
    ```
    for i = 1 to m:
        c[i] = index (from 1 to K) of cluster centroid closest to x[i]
    ```

    * Move cluster centroids
    ```
    for k = 1 to K:
        uk = average (mean) of points assignedr to cluster k # on x and y axis
    ```

There is a corner case to this algorithm: what if a cluster has 0 training set examples assigned to it?

That cluster will try to get the average of zero points but that is not defined

If that ever happens, the most common thing to do is eliminating that cluster. On the other hand, in case you need that cluster, you could randomly reinicialize and hopes that cluster gets assigned to some points

### K-means for clusters that are not well separated

For instance, a company wants to defined the size of small, medium and large t-shirts. For that, it gets data about the height and weight of its customers. Then, you run k-means algorithm to get 3 clusters of that data (customer's height and weight)

![k-means-not-well-separated-data](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-not-well-separated-data.png)

### Optimization Objective

![k-means-optimization-objective](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-optimization-objective.png)

The k-means cost functions is called **distortion**

In every single iteration, the distortion must go down or stay the same. Otherwise, there's a bug in the code

You could stop the algorithm when it stops decreasing the cost function or when the cost function rate reaches a minimum limit