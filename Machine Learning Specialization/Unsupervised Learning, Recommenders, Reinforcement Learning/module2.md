# Recommender Systems

## Collaborative Filtering

**Making recommendations** is one of the topics that has received quite a bit of attention in academia, but the commercial impact and the actual number of practical use cases of recommended systems seems to be vastly greater than the amount of attention it has received in academia

Many sites will recommend things to you that they think you may want to buy or movies that you want to watch. The value that comes through these recommendations is very large

In the typical recommended system, you have some number of users and some number of items.

For example, in a movie website, the users can rate the movies using zero to five stars. In this case, the movies are the items

* **n<sub>u</sub>**: the number of users

* **n<sub>m</sub>**: the number of movies

* **r(i, j) = 1** if user *j* has rated movie *i*

* **y<sup>(i, j)</sup>** = rating given by user *j* to movie *i* (defined only if r(i, j) = 1)

With this framework for recommended systems, one possible way to approach the problem is to look at the movies that the users have not rated, then try to predict how users would rate movies. Doing so, we can try to recommend to users things that they are more likely to rate as five stars

### Using per-item Features

Firstly, let's assume that we have some extra information about the items (in this case movies), such as: the genre

For this, each movie has two features for example:

* **x<sub>1</sub>**: how much of the movie is a romance movie

* **x<sub>2</sub>**: how much of the movie is an action movie

They're like membership functions (of fuzzy systems)

* **n**: the number of features of each movies

* **x<sup>(1)</sup>** = [ feature1 of movie1, feature2 of movie1]

For user 1, we could predict the rating for movie i as: 

w<sup>j</sup> x<sup>i</sup> + b<sup>j</sup> (just like linear regression)

![predict-user-j-rating-for-movie-i](/assets/module2/predict-user-j-rating-for-movie-i.png)

So, there is a different linear regression model for each user

* **m<sup>(j)</sup>**: the number of movies rated by user *j*

The cost function for learning the parameters w<sup>j</sup> and b<sup>j</sup> for user j is the following:

![cost-function](/assets/module2/cost-function1.png)

We must minimize the cost function

It turns out that for recommender systems it would be convenient to actually eliminate the division by m<sup>j</sup> term

![cost-function](/assets/module2/cost-function2.png)

But how can we learn the parameters w, b for all users?

We have to minimize the following cost function:

![cost-function-for-learning-all-users-parameters](/assets/module2/cost-function3.png)

If you use gradient descent algorithm or any other optimization algorithm, you'll have a pretty good set of parameters for predicting movie ratings for all the users

## Collaborative Filtering Algorithm

What if we don't have the features x<sub>i</sup>?

Firstly, let's assume that we have the parameters *w* and *b* for all users. Having them, how can we get reasonable features for each movie?

We could obtain those features *x* using linear systems

![collaborative-filtering](/assets/module2/collaborative-filtering1.png)

As well, to get the values *x*, we can use a cost function and try to minimize it:

![cost-function-for-features-x](/assets/module2/cost-function-features-x.png)

But we could only come up with this equation, because we knew the features *w* and *b*. If we didn't know the parameters *w* and *b* and the features *x*, we could use the following approach:

![cost-function-for-features-and-parameters](/assets/module2/cost-function-features-parameters.png)

To minimize this cost function, we could:

* use Gradient Descent

![gradient-descent-using-collaborative-filtering-algorithm](/assets/module2/gradient-descent-collaborative-filtering-algorithm.png)

**Collaborative Filtering** is gathering the data from multiple users to help you predict ratings

### Binary Labels

Many important applications of recommeder systems involve **Binary Label** where instead of a user giving you zero to five stars, they give you a SENSE of if they like the item of not

In the following example, 1 could mean that the user hit like or favorite button on that particular movie or that it watched the movie until the end

![binary-label](/assets/module2/binary-labels-1.png)

![binary-labels-examples](/assets/module2/binary-labels-examples.png)

For Binary Labels, we are going to predict that the probability of **y<sup>(i, j)</sup>** = 1. This is given by **g(w<sup>j</sup>x<sup>i</sup> + b<sup>j</sup>)**, where g(z) is the **sigmoid function**

The cost function for Binary Application is:

![binary-application-for-cost-function](/assets/module2/binary-application-cost-function.png)