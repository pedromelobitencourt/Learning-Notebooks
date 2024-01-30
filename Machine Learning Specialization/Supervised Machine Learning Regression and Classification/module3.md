# Classification with Logistic Regression

With classification, the variable y can take on only one of a small possible values

The problems that the variable y can only be one of two values (classes/categories) are called **binary classification**

The classes *yes* and *no* can be represented as **true** and **false** or **1** and **0** or **presence** and **absence**. In the case of linear regression *y* would not have been limited to 2 values, but could have been any value 

The true class can be called the **positive class**, and the false class can be called the **negative class**

Some examples:

![classification-example1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/classification_example1.png)


## How to build a classification algorithm?

Linear regression predicts all values between 0 and 1 or less than 0 and greater than 1

So, using a linear regression, you could say that:
* f(x) < 0.5 -> ŷ = 0
* f(x) >= 0.5 -> ŷ = 1

But it can lead to wrong answers, since another training example could shift the decision boundary by using the same threshold

![classification-example2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/classification_example2.png)


## Logistic Regression

It fits a S-shaped curve to the dataset

In the tumor example, the y variable is always 0 or 1

![classification-example2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/classification_logistic_regression1.png)

Usually, it's used the **logistic/sigmoid function**

![sigmoid-function](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/sigmoid_function.png)


### Building our Logistic Algorithm

![logistic-algorithm1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_algorithm1.png)

![logistic-algorithm2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_algorithm2.png)


**Interpretation of Logistic Regression Output**

Think of it as the *probability* that the class is 1

For example,

If *x* is "tumor size", *y* is 0 (not malignant) or 1 (malignant) and f<sub>w, </sub><sub>b</sub>(x) = 0.7, then there is 70% chance that y = 1, that is, 30% chance that y = 0

P(y = 0) + P(y = 1) = 1

* **f<sub>w, </sub><sub>b</sub>(x) = P(y = 1|x;w,b)**: probability that *y* is 1, given input *x*, parameters *w* and *b*


## Decision Boundary

So, since the sigmoid function output ranges between 0 and 1, you have to determine a threshold to decide if it's **1** or **0**

For instance, you could say that:
* f<sub>w, </sub><sub>b</sub>(x) >= 0.5 -> ŷ = 1
* f<sub>w, </sub><sub>b</sub>(x) < 0.5 -> ŷ = 0


When is f<sub>w, </sub><sub>b</sub>(x) >= 0.5?
* when g(z) >= 0.5 -> z >= 0 -> wx + b >= 0


**Another example:**

Lets say that there are 2 features, and the red-crosses is when the output is **1** and the blue circles is when the output is **0**, like shown below:

![decision-boundary1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/decision_boundary1.png)

In this example, we have the following function:

**f<sub>w, </sub><sub>b</sub>(x) = g(z) = g(w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + b)**

There is an interesting line called **decision boundary**. It's the line when *wx + b = 0*. That's the line that you are almost neutral about whether *y* is 0 or *y* is 1. You could say, as well, that if a sample is in the right side of it, it predicts **1** and if a sample is in the left side of it, it predicts **0**

When w<sub>1</sub> = 1, w<sub>2</sub> = 1 and b = -3, it's the line where *z = x<sub>1</sub> + x<sub>2</sub> -3*

![decision-boundary2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/decision_boundary2.png)


**What if the decision boundary is no longer a straight line?**

![decision-boundary3](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/decision_boundary3.png)

Let's say our function is:
**f<sub>w, </sub><sub>b</sub>(x) = g(z) = g(w<sub>1</sub>x<sub>1</sub><sup>2</sup> + w<sub>2</sub>x<sub>2</sub><sup>2</sup> + b)**

then, if w<sub>1</sub> = 1, w<sub>2</sub> = 1 and b = -1:

z = x<sub>1</sub><sup>2</sup> + x<sub>2</sub><sup>2</sup> -1 = 0

z = x<sub>1</sub><sup>2</sup> + x<sub>2</sub><sup>2</sup> = 1

This turns out to be a circle of radius equal to 1

![decision-boundary4](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/decision_boundary4.png)

When z > 1, it predicts that *y* is 1
When z < 1, it predicts that *y* is 0

Logistic Regression can learn how to fit really complex data


# Cost Function for Logistic Regression

The *Squared Cost Function* is not an **ideal** cost function for Logistic Regression

![logistic-regression-training-set](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_regression_training_set.png)

Given this training set, how can we choose parameters *w* and *b*?

If we use the Squared Error Cost Function for Logistic Regression, we would get something like this:

![squared-error-cost-function-with-logistic-regression](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/squared_error_logistic_function.png)

This is a non-convex cost function. If we try to use gradient descent, there are a lot of **local minima**, then it can be harder or impossible to get to the **global minima**.

There is another cost function that can make the cost plot convex again, then the gradient descent is guaranteed to converge to the global minima.

Let's call the term inside the summation of the squared error cost function (1/2(f<sub>w, b</sub>(x<sup>i</sup>, y<sup>i</sup>))) as LOSS on a single example

* **Loss**: L(f<sub>w, b</sub>(x<sup>i</sup>, y<sup>i</sup>))

The **Logistic Loss Function** is:

![logistic-loss-function](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_loss_function.png)

Let's analyze when **y = 1**:

We are just interest when 0 <= y <= 1 of the function

* If the model function predicts 1, then the loss is 0 (very close to the right answer)

* If the model predicts 0.5, then the loss is a bit higher

* If the model predicts 0.1, then the loss is almost infinity

* Loss is lowest when f<sub>w, b</sub> (x<sup>i</sup>) predicts close to true label y<sup>i</sup>

![logistic-loss-function1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_loss_function1.png)


Let's analyze when **y = 0**:

We are just interest when 0 <= y <= 1 of the function

* If the model function predicts 0 or very close to 0, the loss will be very small (very close to zero)

* If the model predicts 1, then the loss will be very high (close to infinity)

The loss is the model **penalization**

![logistic-loss-function2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/logistic_loss_function2.png)

Now, the cost function will be **convex**, so the gradient descent will be able to take us to the global minimum

## Simplified Loss Function for Logistic Regression

Remember that in our examples, y can only take the values of either one or zero

It's **completely** the same thing as the other one (same result)

![simplified-logistic-loss-function](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/simplified_logistic_loss_function1.png)

![simplified-logistic-loss-function](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/simplified_logistic_loss_function2.png)

This function was derived from statistics, using a statistics principle: **Maximum Likelihood Estimation**


# Gradient Descent for Logistic Regression

We're going to find the values of parameters *w* and *b* that minimize the cost function *J*, applying **gradient descent** for it

* *x<sub>j</sub>* is the jth feature

![gradient-descent-logistic-regression-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/gradient_descent_logistic_regression1.png)

![gradient-descent-logistic-regression-2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/gradient_descent_logistic_regression2.png)


# The Problem of Overfitting

* **Bias**: the algorithm has undefit the data. There is a clear pattern in the training data that the algorithm is just unable to capture

* **Underfitting (high bias)**: when the model does not fit the training data set well

* **Generalization**: when the model fits well the training set and even on other examples that are not in the set. We want that our algorithm **generalize** well (make good predictions even on brand new examples)

* **Overfitting (high variance)**: when the model fits the training set extremely well. It doesn't look like that the model will generalize to new examples

* Overfitting may cause the algorithm to perform poorly

![overfitting-on-regression1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/overfitting_regression1.png)

![overfitting-on-classification1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/overfitting_classification1.png)


## Addressing Overfitting

1. Collect more training examples

2. Select features to include/exclude (**feature selection**): the algorithm may overfit the training set if there are few data and you include all features

3. **Regularization**: you could make a parameter of a feature smaller or bigger depending on its importance, allowing to have all the features. Usually, it doesn't make any difference to regularize the parameter *b*

### Regularization

If you have a lot of features, you may not know which are the most important features and which ones to penalize. So the way regularization is implemented is to penalize all of the features (all *w<sub>j</sub>* parameters)

So to penalize them, we do the following to the cost function:

![cost-function-regularization](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/cost_function_regularization.png)

You could add: + (λ/2m)b<sup>2</sup>, but it makes little difference

The first term is the **mean squared error** and its objective is to fit the data and the second part is the **regularization term** and its objective is to keep *w<sub>j</sub>* small to minimize the overfitting

* **λ**: regularization parameter. λ > 0. It balances both goals: fit data and keep *w<sub>j</sub>* small

If λ is very small, *w<sub>j</sub>* can be very large and the model may overfit the data

If λ is very large, *w<sub>j</sub>* can be very small (close to zero), so it may underfit -> f(x) = b


### Regularized Linear Regression

Gradient descent for regularized linear regression is:

![gradient-descent-for-regularized-linear-regression](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/regularized_gradient_descent_linear_regression.png)

![gradient-descent-for-regularized-linear-regression](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/regularized_gradient_descent_linear_regression2.png)

If you observe with cautious, you notice that what regularization does is lightly decrease the value of w<sub>j</sub>

![regularization-on-cost-function](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/regularization_on_cost_function.png)

![regularized-linear-regression-question](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module3/regularized_linear_regression_question.png)