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


# Recommender Systems Implementation Detail

## Mean Normalization

Normalization can help the algorithm to run faster

In the next example, a new user was added. It has not rated any movie yet. If you were to train a collaborative filtering algorithm on the data, since we are trying to make the parameter *w* small (because of the regularization term), and run the algorithm, the parameters *w* and *b* for the new user (Eve) will be 0

Moreover, as long as the new user hasn't rated any movie yet and the regularization term tries to minimize *w*, *w* will be 0 for the new user. This will mean that the new user has rated every movie as 0 and it will not be very helpful

![new-user-example](./assets/module2/new-user-example.png)

Mean Normalization will help the algorithm comes up with better prediction of the movie ratings for a new user that hasn't rated any movies

Firstly, well turn the dataset into a 2d-matrix. For each row (movie), we'll compute the average rating that was given to it

We'll store the average ratings into a μ vector. Then, for each movie, we're going to subtract each rating that was given to it by its average rating and this will be our new **y** matrix

Doing so, we predict: **w<sup>j</sup>x<sup>i</sup> + b<sup>b</sup> + u<sub>i</sub>**

Now, the *w* and *b* parameters for the new user won't be 0, but the average rating of each movie and this will be more reasonable than giving 0

It turns out that by normalizing the mean of the different movie ratings to be zero, the optimization algorithm for the recommender system will also run just a little bit faster but it does make the algorithm behave much better for users who have rated no movies or just a small numbers of it

You could also normalize by the columns. It depends on the application which one is more reasonable. In this example, it would mean predicting the rating of a movie that hasn't been rated by any user

![mean-normalization](/assets/module2/mean-normalization1.png)

## TensorFlow Implementation

TensorFlow is not only a tool for neural network, but for other learning algorithms as well

One of many great things TensorFlow does is calculate optimally the derivatives needed for gradient descent

**Auto Diff**

```
w = tf.Variable(3.0) # initializing the parameter w
x = 1.0
y = 1.0 # target value
alpha = 0.01 # learning rate

iterations = 30

# Automatically computes the derivatives
for iter in range(iterations):
    # Use TensorFlow's Gradient tape to record the steps
    # used to compute the cost J, to enable auto differentiation
    with tf.GradientTape() as tape:
        fwb = w*x # f(x)
        costJ = (fwb - y)**2

    # Use the gradient tape to calculate the gradients
    # of the cost with respect to the parameter w
    [dJdw] = tape.gradient( costJ, [w] )

    # Run one step of gradient descent by updating
    # the value of w to reduce the cost
    w.assign_add(-alpha * dJdw)
```

The implementations of our recommender system example will be the following:

```
# Instantiate an optimizer
optimizer = keras.optimizers.Adam(learning_rate=1e-1)

iterations = 200
for iter in range(iterations):
    with tf.GradientTape() as tape:
        # Compute the cost (forward pass is included in cost)
        # Figure out automatically the derivatives
        # Record the sequence of operations used to compute the cost
        cost_value = cofiCostFuncV(X, W, b, Ynorm, R,
            num_users, num_movies, lambda)

    # Use the gradient tape to automatically retrieve
    # the gradients of the trainable variable with respect to
    # the loss
    # Compute the derivative
    grads = tape.gradient( cost_value, [X, W, b] )

    # Run one step of gradient descent by updating
    # the value of the variables to minimize the loss
    optimizer.apply_gradients( zip(grads, [X, W, b]) )
```

![tensor-flow-implementation](./assets/module2/tensorflow-implementation1.png)

# Finding Related Items

In practice, the features x<sup>i</sup> of item i are quite hard to interpret

Collectively, the features x<sup>1</sup>, x<sup>2</sup>, x<sup>3</sup>, ..., x<sup>n</sup> do convey something about what that movie is like

If you want to find other items related to item i, you have to find **item k** with x<sup>**(k)**</sup> (a vector) similar to x<sup>(i)</sup>

**How can we determine if x<sup>(k)</sup> is similar to x<sup>(i)</sup>?**

![related-items-equation](./assets/module2/related-items-equation1.png)

Then, you could return the 'z' most related items to the user 

## Limitations of Collaborative Filtering

### Cold Start Problem

* How to rank new items that few users have rated?

* How to show something reasonable to new users who have rated few items?

### Use Side Information about Items or Users

It doesn't give us a natural way to use side information or additional information about items or users

* **Items**: Genre, movie stars, studio, ...

* **User**: Demographics (age, gender, location), expressed preferences, ...


# Content-based Filtering Algorithm

* **Collaborative Filtering**: recommend items to you based on ratings of users who gave similar ratings as you

* **Content-based Filtering**: recommend items to you based on features of user and item to find good match. It requires having some features of each user as well as some features of each items and it uses those features to try to try to decide which items and users might be a good match for each other

### Examples of user and item features

* **X<sub>u</sub><sup>(j)</sup>**: user features such as: age, gender, country, movies watched, average rating per genre

* **X<sub>m</sub><sup>(i)</sup>**: movie features such as: year, genre/genres, reviews, average ratings

Now, we're going to predict the rating of user j on movie i as:

**V<sub>u</sub><sup>(j)</sup> V<sub>m</sub><sup>(i)</sup>**

* **V<sub>u</sub><sup>(j)</sup>**: list of numbers computed from the features of user j

* **V<sub>m</sup><sup>(i)</sup>**: list of numbers computed from the features of movie i

If we're able to come up with good choice of those vectors, then hopefully the dot product of them will be a good prediction of the rating that a user j gives to a movie i

For example, the values of V<sub>u</sub><sup>(j)</sup> could represent the users preferences, how much user j likes romance movies, how much user j likes action movies...

The same could be said for V<sub>m</sup><sup>(i)</sup>. Its values could represent the movies features, such as: how much movie i is a romance movie...

X<sub>u</sub><sup>(j)</sup> can have different size than X<sub>m</sub><sup>(i)</sup>

V<sub>u</sub><sup>(j)</sup> must have the same size as V<sub>m</sub><sup>(i)</sup>, since we're going to do a dot product of them

## Deep Learning for Content-based Filtering

A good way to implement Content-based Filtering is to use **Deep Learning**

To compute the V<sub>u</sub> and V<sub>m</sub> vectors, we are going to use neural network

The first neural network will be called **user network**

In this neural network, the input will be the vector X<sub>u</sub>. Then, there are some few Dense layers (128 units, 64 units, 32 units). In this example, the output layer V<sub>u</sub> will have 32 units

The second neural network will be called **movie network**

In this neural network, the input will be the vector X<sub>m</sub>. Then, there are some few Dense layers (256 units, 128 units, 32 units). In this example, the output layer V<sub>m</sub> will have 32 units 

As mentioned, the output layer of both, user and movie network, must have the same size

Finally, we are going to predict the rating of user j in movie i as: **V<sub>u</sub><sup>(j)</sup> V<sub>m</sub><sup>(i)</sup>**
