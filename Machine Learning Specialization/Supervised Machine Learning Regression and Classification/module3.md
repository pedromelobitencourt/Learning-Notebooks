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