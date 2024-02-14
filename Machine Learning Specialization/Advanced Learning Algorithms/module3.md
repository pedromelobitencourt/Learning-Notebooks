# Advice for applying machine learning

You've implemented regularized linear regression on housing prices

But it makes unacceptably large errors in predictions. What to do next?

* Get more training examples
* Try smaller sets of features
* Try getting additional features
* Try adding polynomial features
* Try decreasing λ
* Try increasing λ

So, we're going to learn some **diagnostics** that are tests that we can run to gain insight into what is/isn't working with a learning algorithm, to gain guidance into improving its performance

Diagnostics can take time to implement but doing so can be a very good use of time

## Evaluating and choosing models

Let get as an example we're building a model to predict house pricing. Our model fits the training data well, but it fails to generalize to new examples not in the training set. And if we have 4 features (or more than 3), size in feet<sup>2</sup>, # of bedrooms, # of floors and age of home, we can't plot the model. We need some more **systematic** way to evaluate how well your model is doing

One way is, instead of training your model with the entire training set, you could split it into two subsets, training set and a test set. Usually 70% or 80% of your data will be in the training subset.

![train-test-cost-error-functions-linear-regression](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/train_test_cost_error_functions_linear_regression.png)

*J<sub>train</sub>(w, b)* will be low, but if *J<sub>test</sub>(w, b) is high, it's not good to generalize

Now, the train/test procedure for classification problem will be:

![train-test-cost-error-functions-classification](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/train_test_cost_error_functions_classification1.png)

![train-test-cost-error-functions-classification](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/train_test_cost_error_functions_classification2.png)

We can use a technique to automatically choose the good model for your machine learning algorithm

The training set error *J<sub>train</sub>(w, b)* is likely lower than the actual generalization error. So, it is not so important to evaluate it. Futhermore, *J<sub>test</sub>(w, b)* is a better estimate of how well the model will generalize

For instance, you could select 10 models, from degree 1 up to degree 10 and get their cost test functions *J<sub>test</sub>(w, b)*. Then, you look at all cost functions and see which one gives the lowest value. Maybe, this one is the fifth one.

Then, how well does the model perform?

J<sub>test</sub>(w, b) is likely to be an optimistic estimate of generalization error, because an extra parameter d (degree of polynomial) was chosen using the test set. Then, this procedure is flawed and not recommended

To automatically choose a model, you split the data set into three different subsets (training set, cross validation set and test set)

The name **cross validation** refers that this is an extra dataset that we're going to use to check or cross check the validity or the accuracy of different models

It can be named: **validation set**, **development set** or **dev set**

![cross-validation-set](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/cross_validation_set1.png)

![cross-validation-error](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/cross_validation_set2.png)

Then, to choose a model from many options, you get the one that has the lowest *J<sub>cv</sub>(w, b)*. Moreover, its *J<sub>test</sub>(w, b)* can be used to estimate generalization error

So, let's sum up. We fit the parameters *w* and *b* using the training set, then we choose a parameter *d* (polynomial degree) using the cross validation set. So up to this point we haven't fit any parameters to the test set (fair estimate of generalization error)

**Another example:**

![cross-validation-example-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module3/cross_validation_example1_1.png)

Maybe for a handwriting recognition problem, we consider three different models. To help decide how many layers should do the neural network have and how many hidden units per layers should have, you can train three of these models and get some parameters *w* and *b*. Then, we can evaluate the neural network performance using *J<sub>cv</sub>* using our cross validation set. Then, we'd pick the model with the lowest cross validation error. Moreover, if we want to report an estimate of the generalization error, we would use the test set giving the *J<sub>test</sub>*

Because we haven't made any decisions using the test set, it ensures that it is a fair and not optimistic estimate for generalization error