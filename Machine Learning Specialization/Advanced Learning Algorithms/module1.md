# Neural Networks Intuition

Its objective initially was to make a software to mimic the human brain

Some applications are:

* Speech recognition

* Computer vision

* Natural language processing

* Product recommendation

All of human thought is from neurons sending eletrical impulses and sometimes forming new connections to new neurons

Each neuron has some *inputs* where it receives impulses from other neurons. Then, it carries out some computation and will send the output to other neurons by eletrical inputs

![neurons-in-brain](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/neurons_in_brain.png)


A neuron takes one or more inputs, it does some computations and outputs something

When building a model, you want to simulate many of neurons at the same time

![biological-neuron-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/biological_neuron1.png)


**Why Artificial Neural Network became popular *now*?**

Now, we have a lot more data digitalized than before. Futhermore, the traditional AI models (such as: linear regression, logistic regression) performance does not keep going up with more data that you feed them, that is, they're not able to scale with the new amount of data and take effective advantage of it

![why-to-use-neural-network-now](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/why_neural_network_now.png)

## Demand Prediction

We'll see an example about demand prediction. We want to know if a certain product will be top seller or not

* **Activation**: how much a neuron is sending a high output to other neurons downstream from it

![demand-prediction-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/demand_prediction1.png)

Now, we'll have 4 inputs (**input layer**): price, shipping cost, marketing and material. We have to take as accountability three aspects: affordability, awareness and perceived quality. So, we could build a neuron for each aspects (activations).

For affordability, we take as inputs *price* and *shipping cost*

For awareness, we take as input *marketing*

For perceived quality, we take as inputs *material* and *price*

These 3 neurons grouped are called **layer**

* **Layer**: it's a grouping of neurons which takes as inputs the same or similar features and that in turn outputs a few numbers (activation values) together

Then, we wire those neurons to another one (**output layer**) that outputs the probability of being a top seller

![demand-prediction-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/demand_prediction2.png)

In practice, every neuron in a certain layer will have access to every feature from the previous layer

For example, the *affordability* neuron may learn to ignore marketing and material and focus only the most relevant inputs

![demand-prediction-3](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/demand_prediction3.png)

* The layer that is neither the input layer nor the output layer is called **hidden layer**

When building your model, some decisions you have to make is: how many hidden layers it will have and how many neurons each hidden layer will have (questions of the architecture of the neural network)

Multiple hidden layers are also called **multilayer perceptron**

![multiple-hidden-layers](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/multiple_hidden_layers1.png)

Let's see a face recognition example:

![face-recognition-example](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/face_recognition_example.png)

In the first hidden layer, it may be neurons that are looking for very short lines or edges in the image

In the second hidden layer, it may be neurons that might learn to group together lots of short lines or segments to look for face parts

In the third hidden layer, it may be neurons that are aggregating different parts of faces to detect a face


# Neural Network Model

Each neuron of a hidden layer is just implementing a logistic regression function

Let's see how it is made a hidden layer neuron computation:

![neural-network-hidden-layer-computations](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/neural_network_hidden_layer_computations.png)

Now, we're going to see how it is made a output layer neuron computation:

![neural-network-output-layer-computations](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/neural_network_output_layer_computations.png)

The superscript is the number of the layer

The subscript is the number of the current neuron of the layer

After the last computations, if you're making a binary prediction, you can make a condition test to classificate the inputs depending on a threshold

![neural-network-prediction](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/neural_network_prediction.png)

We can call neurons as *hidden units*

![neural-network-layer-notation](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/neural_network_layer_notation.png)

*g* can also be called **activation function** (the activation function is not necessarily the sigmoid function)

## Forward Propagation

![forward-propagation-step1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/forward_propagation_1.png)

![forward-propagation-step2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/forward_propagation_2.png)

![forward-propagation-step3](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/forward_propagation_3.png)


# TensorFlow Implementation

It's one of the leading frameworks to implementing deep learning algorithms

**How can we implement inferencing code using TensorFlow?**

One of the most remarkable things about neural network is that the same algorithm can be applied to so many different applications

Let's see another example. Imagine you have a dataset that contains the duration and the temperature of coffee roasting as inputs and the output is whether the roasted coffee is good or not

![coffee-roasting-example-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/coffee_roasting_example_1.png)

![coffee-roasting-example-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/coffee_roasting_example_2.png)

**Dense** is the type of the layer we are using. There are lots more types of layers

Now let's see how to build the model for number handwriting recognition (is it a 1?):

![handwriting-recognition-example-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/handwriting_recognition_1.png)

## Data in TensorFlow

![numpy-matrix-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/numpy_matrix_1.png)

All of these are 2D vectors, even if it's 1 x n matrix

![numpy-matrix-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/numpy_matrix_2.png)

## Building a Neural Network

We can string together sequentially layers that we've created using **Sequential** command

![building-a-neural-network-architecture](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/building_neural_network_architecture.png)

As we know, to create the layers, we do:

```
layer_1 = Dense(units=3, activation="sigmoid")
layer_2 = Dense(units=3, activation="sigmoid")
```

Then, to group together these layers, we do the following:

```
model = Sequential([layer_1, layer_2])
```

*x* and *y* are our training sets. To train the model, after we string together the needed layers, we do the following commands:

```
model.compile(...)
model.fit(x, y)
```

Then, to predict some data we do the following:

```
model.predict(x_new)
```


# Neural Network Implementation in Python

Let's see how to do a forward propagation using Numpy

![forward-propagation-implementation-1](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/forward_propagation_implementation1.png)

Each column of *w* corresponds to an unit

We can do it in a more general way:

![forward-propagation-implementation-2](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/forward_propagation_implementation2.png)

# AGI (Artificial General Intelligence)

![AGI-vs-ANI](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/AGI-vs-ANI.png)

# Vectorization

![for-loops-vs-vectorization](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/vectorization1.png)

There are exactly 2 ways of writing the same dot product:

![dot-product-two-ways](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module1/dot_product.png)

## Matrix Multiplication in Numpy

To transpose a matrix, you do the following command:

```
A = np.array([1, -1, .1], [2, -2, .2])
AT = A.T
```

To multiply matrices:

```
W = np.array([3, 5, 7, 9], [4, 6, 8, 0])
Z = np.matmul(AT, W)

# OR

Z = AT @ W
```