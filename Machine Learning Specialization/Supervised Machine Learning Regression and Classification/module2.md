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