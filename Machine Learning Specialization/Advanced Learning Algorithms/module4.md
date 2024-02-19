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