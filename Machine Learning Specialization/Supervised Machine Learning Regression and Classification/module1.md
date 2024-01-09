# Overview of Machine Learning

Machine Learning had grown up as a subfield of AI, in order to build intelligent machines

Machine learn to do things by itself

* AGI (Artificial General Intelligence): machines as intelligent as normal people


# Supervised and Unsupervised Machine Learning

* **Machine Learning**: "Field of study that gives computers the ability to learn without being explicitly programmed" - Arthur Samuel

In general, the more opportunities you give a learning algorithm to learn, the better it will perform

The two major types of machine learning algorithms are:
* **Supervised learning**: it's the most used one in real-world applications and it has rapid advancements

* **Unsupervised learning**

* **Recommender systems**

* **Reinforcement learning**

## Supervised Machine Learning

You give your learning algorithm examples to learn from and they include the right answers (the correct label (output) for the current input)

Input to Output mappings

By seeing the correct pairs of input and desired output, the learning algorithm learns how to take the input alone without the output label and gives a reasonably accurate prediction or guess of the input

* **Regression**: predict a number from infinitely many possible numbers

* **Classification**: predict a small number of categories (few possible outputs and not necessarily numbers)

    * Class (category): the output

## Unsupervised Learning

It's given data that isn't associated with any output labels

Data only comes with inputs, but not outputs to learn from. For this reason, the algorithm needs to find a structure in the data

It has to find patterns or something interesting in unlabeled data

It's called **unsupervised** because we're not trying to quote some right answer for every input

* **Clustering**: it places the unlabeled data into different clusters, based on similar information

* **Anomaly Detection**: find unusual data points

* **Dimensionality Reduction**: compress data (usually from a big dataset) using fewer numbers, losing as little information as possible

Examples of unsupervised learning:
* Set of news articles found on the web, group them into sets of articles about the same story

* Given a database of customer data, **automatically** discover market segments and group customers into different market segments


# Regression Model

Predicts numbers

For example, you have a dataset about the price of a house based on its size in feet squared. You want to estimate the value of a house given its size

You could plot a graph using the data and build a linear regression model for the dataset. Your model will fit a straight line to the data

You could also build a data table

It's a supervised learning model, because you're training the model giving a data that has the right answers

* **Training set**: data used to train the model (it could be represented in a graph or table and it includes the *feature* and *target* variables)

* **x**: "input" variable / feature
* **y**: "output" variable / "target variable"
* **m**: number of training examples
* **(x, y)**: single training example
* **(x^i, y^i)**: ith training example

To train the model, you feed the training set, both the input features and targets to your learning algorithm. Then your algorithm will produce some function *f*. The *f*'s objective is to get a new input x and output or predict or estimate *ŷ* (prediction) - It may not be the true value, but an estimation

The function *f* is called the **model**

How to represent *f* ? / What is the math formula we're going to use to compute it?

*f<sub>w, b</sub>(x)* = wx + b: **line equation** - linear regression with **one** variable (single feature x) = **univariate linear regression**

## Cost Function

It tells how well the model is doing, so we can try to get it to do better

*w* and *b* are the parameters (coefficients or weights) of the model. They are the variable of the model you can adjust during training in order to improve the model

*w* is the slope of the line: w = Δy/Δx

*b* is also called y-intersect

You want to choose good parameters, so that the line fits the data well (passing through or somewhere close to the training examples)

### How to find values of *w* and *b* so that the estimated target is closed to the true y

First, we should know a manner to how to measure how well a line fits the training data. We're going to construct a cost function

cost function = error = J(w, b) = ∑ (ŷ<sup>i</sup> - y<sup>i</sup>)² * (1/2m)

It's *2m* because it's meant to make some of later calculations look neater (convention)

It is also called the **Squared error cost function**

It can be used other cost functions depending on the application

We want to choose a *w* and *b* so that the J(w, b) is as smallest as possible, that is, values *w* and *b* that minimize J(w, b)


## Cost Function Visualization

When considering only the parameter *w* of the model function, it has a U shape like below:

![cost-function-parameter-w](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/cost_function_U_shape.png)

But what if we consider both parameters, *w* and *b*?

![cost-function-parameters-w-and-b](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/cost_function_w_and_b.png)

Now it is a 3D dimension graph, but it also has a "soup" shape

We could use *contour plots* also to visualize the cost function *J(w, b)*. In it, each point of an elipse has the same value of *J*

![contour-plot](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/contour_plot.png)

The minimum *J* is at the center of the smallest elipse

Instead of visually choosing the values, we could use an efficient algorithm that automatically finds the values of parameters *w* and *b* that give the best fit. This algorithm already exists and it is called **gradient descent**. Gradient descent and some variations of it are not only used for linear regression, but some of the biggest and most complex models in AI (such as: the most advanced neural network models - deep learning models)


# Train the Model with Gradient Descent

It's a more systematic way to find the values of *w* and *b*, that results in the smallest value of the cost function *J*

We'll have some function *J(w, b)* and we want to minimize it. The cost function could have more than two parameters. For instance, *J(w1, w2, w3, w4, ..., wn, b)*

* We start with some *w* and *b* - a common choice is to set them both to zero

* Keep changing *w* and *b* to reduce *J(w, b)*

* Until we settle at or near a minimum (there can be more than a minimum depending on the cost function)

With a squared error cost function we always end up with a bow shape plot 

If we're in a top of a hill (starting point), we should ask: where should a do a baby step in order to get to a valley as efficient as possible? - This baby step is called **the direction of steepest descent**. We end up in a **local minima**, not necessarilly the **global minima**

![gradient-descent-steps](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_steps.png)

## How to implement a Gradient Descent Algorithm

1. ![gradient-descent-step-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_step1.png)
    * **α**: learning rate - how big the step to go downhill
    * **Derivative**: which direction to take the step

2. ![gradient-descent-step-2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_step2.png)

You are going to repeat those 2 steps simultaneosly until it converges (reaches the local minimum - when *w* and *b* no longer change much)

* **Converge**: slope = 0

Here is the correct update implementation:

![gradient-descent-correct-update-implementation](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_update_implementation.png)

Let's see an example with only *w*:

1. ![gradient-descent-example-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_example1.png)
    
    * We could see the partial derivative as the linear tangent line

### How to choose the Learning Rate (α)?

The learning rate (α) will have a huge impact on the efficiency of the gradient descent

If α is too small, you will decrease or increase *w* just a little bit (you will decrease or increase the cost of *J*, but very slowly) - You may need a lot of steps to get to the minimum

![small-learning-rate](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_small_learning_rate.png)

If α is too large, you will decrease or increase *w* A LOT - It can increase the distance of the minimum. You can get further and further from the local minimum

So it can overshoot (never recach the minimum), that it, it may fail to converge (diverge)

![large-learning-rate](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_large_learning_rate.png)


What if your *w* is already at a local minimum, but there is a better local minimum or even a global minimum?

![gradient-descent-already-on-local-minimum](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_already_on_local_minimum.png)

As we approach a local minimum, we take smaller and smaller steps, because the partial derivative becomes smaller, so the update steps become smaller (so it doesn't matter if the learning rate is fixed)


## Gradient Descent for Linear Regression

1. ![gradient-descent-for-linear-regression-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_linear_regression_1.png)

2. Repeat until convergence
    ![gradient-descent-for-linear-regression-2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_linear_regression_2.png)


Depending on where you initialize the parameters *w* and *b*, you can end up at different local minima.

However, if your cost function is a squared error cost function, it will never have more than one local minimum. You can say that functions that only have one local minimum is called a **convex function**, so it will always converge to the global minimum

### Running the Gradient Descent Algorithm

![running-gradient-descent](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module1/gradient_descent_running.png)

* **Batch**: each step of gradient descent uses **all** the training examples

So, you can call the algorithm **Batch Gradient Descent**, although there is other gradient descent algorithms that uses only a **subset** of the training examples