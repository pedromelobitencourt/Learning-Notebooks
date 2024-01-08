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