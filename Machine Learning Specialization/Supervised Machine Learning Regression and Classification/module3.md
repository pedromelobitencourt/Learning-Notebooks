# Classification with Logistic Regression

With classification, the variable y can take on only one of a small possible values

The problems that the variable y can only be one of two values (classes/categories) are called **binary classification**

The classes *yes* and *no* can be represented as **true** and **false** or **1** and **0** or **presence** and **absence**

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