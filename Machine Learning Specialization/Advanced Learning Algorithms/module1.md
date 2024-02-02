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

* **Layer**: it's a grouping of neurons whicch takes as inputs the same or similar features and that in turn outputs a few numbers (activation values) together

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

In the second hidden layer, it may be neurons that might learn to group together lots of short lines or segments to look for parts faces

In the third hidden layer, it may be neurons that are aggregating different parts of faces to detect a face
