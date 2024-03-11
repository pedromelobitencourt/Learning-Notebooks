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

**How does the algorithm randomly initialize the cluster centroids?**

Initially, you must choose a value K < m, being m the number of training examples

Then, randomly choose K random examples. So, you would set u1, u2, ..., uk to these K examples

Depending on which cluster centroids you end up choosing, you might get different results, since k-means could *stop* in a local minima, in which k-means is trying to minimize the distortion cost function, but with the unfortunate choice of initialization it ended up stuck in a local minimum

![k-means-random-initialization](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-random-initialization1.png)

Consequently, you can give k-means algorithm multiple shots to try to find the global minimum. But what if you run it thrice and get 3 different solutions? You'd have to compute the cost function of each solution, then pick up the one with the lowest cost value

The number of times to run k-means is about 50-1000. Running it more than 1000 gets too expensive

![k-means-random-initialization](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-random-initialization2.png)

**How to define how many clusters to use?**

The answer is quite ambiguous, since different people may have different answers and, unsupervised learning algorithm, you're not given the right answers

![k-means-number-of-clusters](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-number-of-clusters1.png)

There is a method called *elbow method*

You run k-means algorithm with different number of clusters, let's say from 1 to 8, and calculate the distortion cost function. Let's say that the cost function decreases very rapidly until the number of clusters equal to 3. Then, you're number of cluster should be 3.

The elbow method is not recommeded as the cost function may decrease very smoothly, so you can't define with precision the *right* number of clusters

But you can't choose the number K based only on the cost function as long as always the largest K will result in the lowest cost function value

![k-means-number-of-clusters](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/k-means-number-of-clusters2.png)

Often, you want to get clusters for some later purpose, then you should evaluate k-means algorithm based on how well it performs on that later purpose

For instance, let's define t-shirt sizing. Based on the data of your customers, you may define 3 t-shirt sizes or 5 ones, then you have to decide based on the business. Maybe there's a tradeoff of how well the t-shirts will fit based on how many sizes are there, but there will be more cost as well if there is more sizes


# Anomaly Detection

An **anomaly detection** algorithm looks at a dataset of normal events and learns to detect or to raise a red flag for if there is an unusual or anomalous event

For instance, let's say we're detecting anomaly of aircraft engines, given the heat generated (x<sub>1</sub>) and the vibration intensity (x<sub>2</sub>). Most of aircraft engines work well, so we train our algorithm. Then, when we have a new engine x<sub>test</sub>, we run this test in the algorithm to verify if it's okay or not. If there's an anomaly, we should inspect the engine further

![anomaly-detection](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly-detection1.png)

The most common technique is called **density estimation**

It builds a model that calculate the probability of x being seen in the dataset. Then, it makes regions of high probability, medium probability, low probability...

With the new data example, you compute the probability of it, then if it is lower than a limit, you could say it is an anomaly for example. Otherwise, it's okay

![density-estimation](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/density-estimation1.png)

![anomaly-detection-applications](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly-detection2.png)

## Gaussian (Normal) Distribution

To build an anomaly detection algorithm, we are going to use **Gaussian Distribution**

![gaussian-distribution](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/gaussian_distribution1.png)

On the right side, you have a histogram with for instance 100 examples. The curve on the left indicates that, independing on how many examples you have, if you had to draw a histogram of these examples (let's say infinite), you would end up with the curve of the left side

The Gaussian Distribution area is 1

The mean value μ affects the **center of the distribution**

The variance value σ affects the **width and the height** of the Gaussian Distribution

![gaussian-distribution-example](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/gaussian_distribution_example1.png) 

We are going to build a model or estimate the probability for p(x), given:

* the training set: { x<sup>1</sup>, x<sup>2</sup>, ..., x<sup>m</sup> }

* each example x<sup>i</sup> has n features

Then, our model will be:

p(x) = p(x<sub>1</sub>; μ<sub>1</sub>, σ<sub>1</sub><sup>2</sup>) * p(x<sub>2</sub>; μ<sub>2</sub>, σ<sub>2</sub><sup>2</sup>) * ... * p(x<sub>n</sub>; μ<sub>n</sub>, σ<sub>n</sub><sup>2</sup>)

We are assuming that the features x<sub>1</sub>, x<sub>2</sub> and so on up to x<sub>m</sub> are **statistically independent**, but it works fine even when the features are not statistically independent

## Anomaly Detection Algorithm

The algorithm will tend to flag an example as anomalous if 1 or more features are very small or very large relative to what it has seen in the training set

For each of the features x<sub>j</sub>, we're fitting a Gaussian Distribution

![anomaly-detection-algorithm](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly_detection_algorithm.png)

![anomaly-detection-example](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly_detection_example.png)

## The Importance of Real-number Evaluation

When developing machine learning algorithms (choosing features, parameters...), making decisions is much easier if you have a way of evaluating your learning algorithm

For instance, if you can change some values rapidly and then compute some value for each change, you could evaluate easily what is the best feature/parameter change

Let's imagine that we have some labeled data that represent some features of aircraft engines and the output of each engine is whether the engine is flawed or not

If we had 10000 examples of good engines and 20 examples of flawed engines, we could put 6000 good examples in the training set, 2000 good examples and 10 flawed ones in the cross validation set and 2000 good examples and 10 flawed ones in the test set

Then, you could use the cross validation set to tune the threshold ε and the features x<sub>j</sub>

Futhermore, you could use the test set to evaluate your tuning for example

So, the training set should have only non-anomalous data, whereas cross validation and the test set should have mostly non-anomalous data and few anomalous data. Regarding it, your algorithm would be primarilly an unsupervised learning algorithm, because the training set doesn't really have labeled data since the training set only has non-anomalous examples

**But don't worry if there are some few anomalous examples in the training set**

Some people also separate the data set into only 2 sets, a training set and a cross validation set. All training data set is composed by only non-anomalous data just as the other alternative

But use this method only if you have really few anomalous examples, because there is a high risk of overfitting

There are some possible evaluation matrics:

* True positive, false positive, true negative, false negative
* Precision/Recall
* F<sub>1</sub> score

### Anomaly Detection vs Supervised Learning

![anomaly-detection-versus-supervised-learning](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly_detection_vs_supervised_learning1.png)

![anomaly-detection-versus-supervised-learning](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly_detection_vs_supervised_learning2.png)

### Choosing what features to use

In contrast to supervised learning that the algorithm can determine what features to ignore, to prioritize or how to scale a feature and to take the best advantage of the features we give to it, anomaly detection which learns from unlabeled data is harder for the algorithm to figure out what features to ignore

So, carefully choosing the features is more important for anomaly detection than supervised learning approaches

Try to make sure that the features you give to the learning algorithm are more or less Gaussian

If any feature is not Gaussian, you can change it to make it a little bit more Gaussian

To see the distribution of a feature, you can use the command:

```
plt.hist(x)
```

In some cases, it will result in a Gaussian Distribution but in other cases it won't. So, you can transform your feature to make it more gaussian

Some ways of doing it is:

```
x1 -> log(x1)
x2 -> log(x2 + c), where c is a constant
x3 -> sqrt(x3)
x4 -> x4^(1/3)
```

So, you can try some ways and change the constant or other numbers and see which one gives the *more gaussian*

### Error analysis for anomaly detection

One of the most common problem is: p(x) is comparable for normal and anomalous examples, that is, p(x) is large for both

If you use, for instance, only one feature, some anomaly may seem fine. So, what you could do is adding one more feature to the data set

The development process will often go through is: to train the model and then to see what anomallies in the cross validation set the algorithm is failing to detect. Then, look at those examples to see if that can inspire the creation of new features that would allow the algorithm to spot that examples takes on unusually large or unusually small values on the new features, so it can successfully flag those examples as anomalies

![error-analysis-anomaly-detection](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly-detection-error-analysis.png)

![anomaly-detection-error-analysis](/Machine%20Learning%20Specialization/Unsupervised%20Learning,%20Recommenders,%20Reinforcement%20Learning/assets/module1/anomaly-detection-error-example.png)

In the above example, it's unusually that the CPU is high but the network traffic is low, so we created a feature for this case