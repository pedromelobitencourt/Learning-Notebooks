# Neural Network Training

```
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(units=25, activation='sigmoid'),
    Dense(units=15, activation='sigmoid'),
    Dense(units=1, activation='sigmoid'),
])

from tensorflow.keras.losses import BinaryCrossentropy

model.compile(loss=BinaryCrossentropy)
```

With the *compile* function, we compile the model using a specific loss function

Now, to train the model:

```
model.fit(X, Y, epochs=100)
```

* **epochs**: number of steps in gradient descent

There are three steps in the model training:

1. Specify how to compute output given the input x

    model = Sequential([...])
    ![create-the-model-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/create_model_step.png)
2. Specify loss and cost

    model.compile(loss=BinaryCrossentropy) # Binary Cross Entropy

    L(f(x), y) = -ylog(f(x)) - (1-y)log(1 - f(x))
    ![loss-and-cost-functions-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/cost_loss_functions_step.png)
3. Train on data to minimize J(w, b)
    
    model.fit(X, Y, epochs=100)
    ![gradient-descent-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/gradient_descent_step.png)

There are a lot more loss function, such as: MeanSquaredError (for regression problems)


# Activation Functions

So far, we've been using only the sigmoid function as the activation function in the hidden and output layers. But if you use other activation functions, your neural network model can become much more powerful. For example, an unit can represent the awareness to a clothe and it can be low, popular, viral or completely viral. So, only 2 possible outputs are not wishable.

An activation function that is very used is *g(z) = max(0, z)*. This activation functions is called **ReLU** (rectified linear unit)

![common-activation-functions](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/common_activation_functions.png)

Usually, when some teams are using Linear Activation Function, they say that they're not using any activation function

## How to choose activation functions

You can use different activation functions for different neurons in your neural network

### Activation functions in the output layer

When doing a **binary classification**, the sigmoid function will be the most natural choice on the output layer

When trying to predict how much a stock price will variate today compared to yesterday, you could use a **linear activation function** (the output can be negative or positive)

If you're predicting something that cannot have negative value, you could choose **ReLU** function (the output can only be positive)

```
Dense(units=1, activation='sigmoid', name='l1')
Dense(units=1, activation='relu', name='l2')
Dense(units=1, activation='linear', name='l3')
```

### Activation functions in the hidden layers

Usually, the most common activation function choice in hidden layers is ReLU

The machine learning engineers often use the ReLU function, because it's faster to compute and because only the left side of the graph is completely flat, whereas the left and right side of sigmoid function are flat, then gradient descent will be really slow

* If you use linear activation function in all units (hidden and output layers), the model will be equivalent to linear regression

* If you use linear activation function in all units in hidden layers and sigmoid function in output layer, the model will be equivalent to logistic regression