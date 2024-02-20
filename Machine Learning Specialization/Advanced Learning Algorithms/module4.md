# Decision Trees

Let's have an example a Cat Classification Example (get an image and tell if it's a cat or not)

There are 3 features: *ear shape*, *face shape* and *whiskers*. They are **categorical (discrete values)**.

The ear shape can have 2 values: pointy or floppy

The face shape can have 2 values: round or not round

The whisper feature can have 2 values: present or absent

![cat-classification-example](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/cat_classification_1.png)

On the decision tree, when we get a new example, we start off on the root of the tree. We will look on the feature written inside the node. Then, based on the value of the feature, we'll either go left or go right and so on until we reach a leaf node

There are a **root node**, **decision nodes** and **leaf nodes** (predictions)

![cat-classification-decision-tree](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/cat_classification_2.png)


## Learning Process

Given a training set of cats and dogs, the first step is to:
* Define the feature that will be the root node

Then, we'll split the training examples on 2 halves. 

After that, based on the left branch, we have to define what next feature to put there, then splitting the left examples again in two halves. So, based on the examples output, we can add a leaf node if every example on that group is a cat or dog

**Remember that we are splitting in TWO halves because each feature has only 2 possible values**

![cat-classification-decision-tree](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/cat_classification_3.png)

### Decisions to make

1. How to choose what feature to split on at each node?
* The algorithm will choose a feature to the node in a way that maximize **purity** (get to subsets that are as close as possible to all cats or all dogs)

![decisions-to-make](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/decisions_to_make_1.png)

2. When do you stop splitting?
* When a node is 100% one class

* When splitting a node will result in the tree exceeding a max depth (number of hops to do from a root node to that particular node)
    * in order to not make the tree too big
    * make it small to get less prone to overfitting
    * when improvements in purity score are below a threshold
    * when number of examples in a node is below a threshold


# Decision Tree Learning

## Measuring purity

We're going to measure the impurity by a function called **entropy function (H(fraction))**

Entropy is a measure of impurity (*mixed*)

If the fraction p<sub>1</sub> is half, it's very very bad (entropy = 1). Otherwise, if it's 0 or 1, it's very good (entropy = 0)

![entropy](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/entropy_1.png)

![entropy-equation](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/entropy_2.png)


## Choosing a split: information gain

When building a decision tree, the way we are going to decide what feature to split on at a node will be based on what choice of feature reduces the entropy

**Information Gain** is the reduction of entropy

There will be the entropy on the left branch and on the right branch

**How to choose between models using those entropies?**

If there's a node with many examples in it with high entropy, that seems worse than a node with few examples in it with high entropy

We'll combine the entropy on the left branch and on the right branch using weighted mean (average weighted entropy). Then, we subtract this value from the root entropy. This is the information gain

So, we'd split based on the highest information gain

If the information gain, that is, the reduction of entropy is low, you may stop splitting based on a threshold

![information-gain](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/information_gain_1.png)

![information-gain](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/information_gain_2.png)

## Putting it together

**Overall process of building a decision tree**

1. Start with all training examples at the root node

2. Calculate Information Gain for all possible features and pick the one with the highest information gain

3. Split the dataset according to selected feature and create left and right branches of the tree

4. Keep repeating splitting process until stopping criteria is met: (using features not used before)
    * When a node is 100% one class
    * When splitting a node will result in the tree exceeding a max depth
    * When number of examples in a node is below a threshold
    * Information gain from additional splits is less than threshold

The way of computing decision trees starting at the root is the same as computing the decision tree in the left and right sub-branches


## Using one-hot encoding of categorical features

In the examples, we've seen so far, each of the features could take on only one of two values

**But what if we can have features than can take on more than two possible values?**

Now, the *ear shape* can be floppy, oval or pointy (3 possible values)

So, if you use this feature to split on, you will have 3 subsets of the data (3 sub-branches)

For that, we are going to use **One-hot Encoding**

Instead of having a feature that can have 3 possible values, we are going to have 3 features. One feature determines if the animal has pointy ears, another one will define if it has roundy ears and the last one will determine if it has oval ears

![one-hot-encoding](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/one_hot_encoding_1.png)

* **One Hot Encoding**: if a categorical feature can take on *k* values, create *k* binary features (0 or 1 valued)

* **Hot Feature**: the feature that will take the value 1

The idea of using One-hot Encoding still applies to encode categorical features in neural networks