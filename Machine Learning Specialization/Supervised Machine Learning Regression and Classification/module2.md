# Multiple Linear Regression

It can use, not only one feature, but a lot of features

It's not multivariate regression

In the house price example, we had only the size of the house (x1). What if we have the number of bedrooms (x2), number of floors (x3), age of home (x4) as well?

* **x<sub>j</sub>**: j<sup>th</sup> feature
* **n**: number of features
* **x<sup>i</sup>**: features of i<sup>th</sup> training example
* **x<sub>j</sub><sup>i</sup>**: value of feature j in i<sup>th</sup> training example

Now, the model will be:

* **f<sub>w, b</sub>** = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + w<sub>3</sub>x<sub>3</sub> + w<sub>4</sub>x<sub>4</sub> + b

* b: base price

Example: f<sub>w, b</sub> = 0.1x<sub>1</sub> + 4x<sub>2</sub> + 10x<sub>3</sub> - 2x<sub>4</sub> + 80


In a more general way:

* **f<sub>w, b</sub>** = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + w<sub>n</sub>x<sub>n</sub> + b = w · x + b

* **Vector *w***: w = [w<sub>1</sub> + w<sub>2</sub> + w<sub>3</sub> + ... + w<sub>n</sub>]

* **Vector *x***: x = [x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + ... + x<sub>n</sub>]
 
* **b**: number


Vector *w* and *b* are the parameters of the model


## Vectorization

It will make your code shorter and make it run more efficiently

Vectorization will also take advantage of modern numerical linear algebra libraries as well as GPU hardware. GPU can actually help you execute your code much more quickly

### Example

w = [w<sub>1</sub> + w<sub>2</sub> + w<sub>3</sub>]

b is a number

x = [x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub>]

```
w = np.array([1.0, 2.5, -3.3])
b = 4
x = np.array([10, 20, 30])
```

* Without vectorization 1:

**f<sub>w, b</sub>** = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + w<sub>3</sub>x<sub>3</sub> + b

```
f = w[0] * x[0] +
    w[1] * x[1] +
    w[2] * x[2] + b
```

What if n == 100000? It will be inefficent for you to code and for your computer to run


* Without vectorization 2:

```
f = 0
for j in range(0, n):
    f = f + w[j] * x[j]
f = f + b
```

It doesn't use **vectorization** and it's not that efficient


* With vectorization:

**f<sub>w, b</sub>** = w · x + b

```
f = np.dot(w, x) + b
```

Especially when *n* is large, this will run much faster

Now, the code is **shorter** and runs **faster**

It runs faster, because, behind the scenes, the numpy dot function is able to use **parallel** hardware in your computer (whether you're using CPU or GPU)


### How a Vectorization Algorithm may Work Behind the Scenes

* Without vectorization:

It runs sequentially...

![without-vectorization](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/without_vectorization_1.png)

It calculates these computations one step at a time

* With vectorization

In a **single** step, it multiples each pair of *w* and *x*
Then, after that, the computer takes those numbers and uses specialized hardware to add them all very efficiently

It will run efficiently and **scale** well to large datasets or to train large models

![with-vectorization](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/with_vectorization.png)

### Vectorization on Gradient Descent

**Gradient Descent with Vectorization**

![gradient-descent-with-vectorization-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/gradient_descent_with_vectorization1.png)

![gradient-descent-with-vectorization-2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/gradient_descent_with_vectorization2.png)

It will be done all at once. It's very good for large datasets or to train large models


**Gradient Descent without Vectorization**

![gradient-descent-without-vectorization](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/gradient_descent_without_vectorization.png)


## Gradient Descent for Multiple Linear Regression

We have to repeat the following:

![gradient-descent-formulas1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/gradient_descent_formulas1.png)

![gradient-descent-formulas2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/gradient_descent_formulas2.png)

*w* and *x* are now vectors


### An Alternative to Gradient Descent (Normal Equation)

* It only works for Linear Regression

* Solve for *w* and *b* without iterations

* It may be used in machine learning libraries that implement linear regression

* Gradient Descent is the recommended method for finding parameters *w* and *b*

Some disvantages are:

* It doesn't generalize to other learning algorithms

* It's slow when number of features is large (> 10000)


# Gradient Descent in Practice

**Feature Scaling** is a technique that enables to Gradient Descent to run much faster

For example, if a feature ranges from large numbers and another feature from small numbers, we have to determine great parameters *w* for both. If not, the result may not be reasonable

![feature-scaling-example](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/feature_scaling1.png)


For example:

In a Scatterplot, the horizontal axis is in a much larger scale than the vertical one

In a Contourplot, the horizontal axis has a much narrow range whereas the vertical axis takes on larger values

![feature-scaling-example-2](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/feature_scaling2.png)

In a case similar to that, when you run the gradient descent, because the contour is so narrow and so "tall", it may ended up bouncing back and forth for a long time before it can find the global minimum

![without-feature-scaling](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/without_feature_scaling.png)

In situations like this, an useful thing to do is to scale the features. This means performing some transformations in your training data, so that x<sub>1</sub> and x<sub>2</sub> will now range from 0 to 1

It can speed up the Gradient Descent Algorithm very significantly

![with-feature-scaling](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/with_feature_scaling.png)

## How to perform Feature Scaling

One way is:

    if 300 <= x <= 2000, you can divide x by 2000 (maximum x), so: 0.15 <= x <= 1

Another way is to use **Mean Normalization**:

    Rescale the features, so that they are centered around zero (in this way, they will have negative and positive values)

    To do it:
        * find the average (the mean: μ)
        * x = (x - μ) / (maxX - minX) for every x


Another way is to use **Z-score Normalization**:

    First, calculate the **standard deviation** of the feature (σ) and the average (μ)

    x = (x - μ) / σ for every x

When performing a Feature Scaling, you want to:

* Aim for about -1 <= x <= 1 for each feature x

or

* Aim for about -3 <= x <= 3

Rescale when the feature ranges a lot, for instance from -100 to 100 in comparison with other features that ranges much less

    0 <= x1 <= 3: okay, no rescaling

    -2 <= x2 <= 0.5: okay, no rescaling

    -100 <= x3 <= 100: too large, rescale

    -0.001 <= x4 <= 0.001: too small, rescale

    98.6 <= x5 <= 105: too large in comparison, rescale


## Checking Gradient Descent for Convergence

How can we tell if the gradient descent is converging, that is, helping you to find the best parameters?

We could use a Learning Curve, that is, in the vertical axis is the cost function and, in the horizontal one, it's the number of iterations

It helps you to see how your cost function is performing after each iteration of gradient descent

If your gradient descent is working properly, then the cost function *J* should decrease after each iteration

If *J* increases in, at least, one iteration, that means that either the α is chosen poorly (usually large α) or there is a bug in the code

Also, by observing the Curve, you can see that, after some iterations, the curve is leveling off and is no longer decreasing much (the curve is almost flattening out, that is, it's almost converged)

![learning-curve](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/learning_curve.png)


Another way is to use **Automatic Convergence Test**

Let ε be 10<sup>-3</sup>

If *J(w, b)* decreases by <= ε in one iteration, declare convergence

Finding the right ε, that is, the right threshold is pretty difficult, it's recommended to use the graphical way



## Choosing the Right Learning Rate

If α is too small, the gradient descent will run **very slowly**

If α is too large, the gradient descent **may not** even converge

If your Learning Curve went up and down a lot or, at least, once (after one iteration) it went up, that can mean that there is a **bug** in the code or the **learning rate α** is too large

* **Tip**: with a small enough α, *J(w, b)* should decrease on every iteration. So set α a very small value to verify if the cost function is decreasing on every iteration. If not, that means that there is a bug in the code

![learning-rate-problems-1](/Machine%20Learning%20Specialization/Supervised%20Machine%20Learning%20Regression%20and%20Classification/assets/module2/learning_rate_problems1.png)

As well, try some values of α, such as: 0.001, 0.01, 0.1, 1... 

For each value of α, you should run gradient descent to plot the cost function based on the number of iterations to determine which value that seems to decrease the cost rapidly and consistently

Test really big α too to try to get the best one 