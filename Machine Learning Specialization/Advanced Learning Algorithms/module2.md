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


# Multiclass Classification

Multiclass Classification problems refer to classification problems that you can have more than 2 output labels

![multiclass-classification-example](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/multiclass_classification_example.png)

## Softmax

The **Softmax** regression algorithm is a generalization of logistic regression (which is a binary classification algorithm) to the multiclass classification context

![softmax-computation](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/softmax_computation.png)

![softmax-cost-function](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/softmax_cost_function.png)


### Using softmax to handwriting recognition of the numbers

![softmax-handwriting-recognition](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/softmax_handwriting_recognition.png)

Don't use the code below, because there's a better version of it

1. Specify the model

```
model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units=15, activation='relu'),
    Dense(units=10, activation='softmax')
])
```

2. Specify the loss and cost

```
model.compile(loss=SparseCategoricalCrossentropy())
```


### Improved implementation of softmax

Because the computer has only finite amount of memory to store numbers, the result can have more or less numerical round-off error

Although, the way we were using to calculate the cost function for softmax is correct, there is a different way of formulating it that reduces the numberical round-off errors leading to more accurate computations in tensorflow

For Logistic Regression:

```
model = Sequential([
    Dense(units=25, activation='sigmoid'),
    Dense(units=15, activation='sigmoid'),
    Dense(units=10, activation='linear')
])

# loss
model.compile(loss=BinaryCrossentropy(from_logits=True))
model.fit(X, Y, epochs=100)

# fit
logits = model(X)

# predict
f_x = tf.nn.softmax(logits)
```

It could be done in the previous way as well since numerical round-off error doesn't impact too much logistic regression, in contrast to softmax regression

![logistic-regression-numerical-round-off-error](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/logistic_regression_numerical_round_off_error.png)


For softmax regression:

```
model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units=15, activation='relu'),
    Dense(units=10, activation='linear')
])

model.compile(loss=SparseCategoricalCrossEntropy(from_logits=True))

# fit
model.fit(X, Y, epochs=100)

# predict
logits = model(X)
f_x = tf.nn.softmax(logits)
```

![softmax-numerical-round-off-error](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/softmax_numerical_round_off_error.png)

This gives the TensorFlow the ability to rearrange terms and compute this in a more numerically **accurate** way

### Classification with multiple outputs

* Also called as **multilabel classification**

Given an input, there can be multiple outputs

![multilabel-classification-example1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/multilabel_classification1.png)

**How to builda multilabel classification model?**

* You can treat each output as a separate machine learning problems

* Train one single neural network with 3 outputs

![multilabel-classification-example2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/multilabel_classification2.png)

# Additional Neural Network Concepts

## Advanced Optimization

**Gradient Descent** is an optimization algorithm that is widely used and was the foundation of many algorithms. But there are other optimization algorithms that are even better and faster than gradient descent

An algorithm that is better and faster than the gradient descent is **Adam** algorithm. It automatically increases the learning rate α if we are taking tiny little steps in a similar direction over and over. However, if we are taking big steps (large α) and they don't follow a similar direction over and over, it decreases the learning rate α

* **ADAM**: Adaptative Moment Estimation

This algorithm uses a different learning rate α for every parameter of your model

![adam-algorithm1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/adam_algorithm1.png)

```
# it's worth trying fewer values for this initial learning rate α

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
```

Adam algorithm is more robust than the gradient descent algorithm to the exact choice of learning rate that you pick, although it's worth tuning this variable

## Additional Layer Types

* **Convolutional Layer**: each neuron only looks at part of the previous layer's output
    * It speeds up computation
    * It needs less training data (less prone to overfitting)

![convolutional-layer-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/convolutional_layer1.png)

![convolutional-layer-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/convolutional_layer2.png)

* **Dense Layer**: each neuron gets its inputs all the activations from the previous layer


# Backpropagation

## How is the derivative computed?

![derivative-example-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/derivative_example1.png)

![derivative-example-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/derivative_example2.png)

**Compute derivative in Python**

```
import sympy

J, w = sympy.symbols('J,w') # J and w are math symbols
J = w**2 # function

# Derivative
dJ_dw = sympy.diff(J,w)

# If w is 2
dJ_dw.subs([w, 2])
```


## Computation Graph

It's how programming frameworks like TensorFlow automatic compute derivatives of your neural network

It's a set of nodes and edges

![computation-graph-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/computation_graph1.png)

Computing the derivatives is a right-to-left process, that is why it's called **back prop**

The first step of back prop will ask if the value of *d*, how much will the value of *J* chance?

![computation-graph-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/computation_graph2.png)

Backprop is an efficient way to compute derivatives