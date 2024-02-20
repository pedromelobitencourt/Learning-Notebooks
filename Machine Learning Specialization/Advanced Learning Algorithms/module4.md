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

## Continuous valued features

Features that can value any number

Let's add the *weight* feature to our cat classifier

**How to split on the weight feature?**

We could split the data based on whether or not the data is less than *x* pounds. It will be job to the learning algorithm to choose

Test some *x* values and choose the one that gives the highest information gain

![continous-valued-features-decision-trees](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/decision_tree_continuous_features.png)


## Regression Trees

We are going to generalize decision trees to be regression algorithms, so that we can predict a number

Now, we have three features (*ear shape*, *face shape* and *whiskers*) to predict the *weight* of the animal (target output *y*)

![regression-tree](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/regression_tree_1.png)

In the leaf nodes, we'll have some examples weights, so we get the average of them and it'll be the predicted value

![regression-tree-example](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/regression_tree_2.png)

### Choosing a split

Now, instead of reducing entropy, we want to reduce the variance of the weights of each subset

![regression-tree](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/regression_tree_3.png)


# Tree Ensembles

## Using multiple decision trees

One of the weakness of using only one decision tree is that decision tree can be highly sensitive to small changes in the data

So, the solution is to build lots of decision trees (**tree ensemble**)

For instance, changing a cat with roundy face, pointy ears and absence of whiskers to roundy face, floppy ears and presence of whiskers makes the root feature be *whiskers* instead of *ear shape*

So, you can build totally different sub-trees just because of one feature. This makes the algorithm not just **robust**

![decision-tree-is-not-robust](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/decision_tree_not_robust.png)

* **Tree Ensemble**: collection of multiple trees

In tree ensemble, you have *x* decision trees, put them to predict the new data, then they *vote* (majority). It makes less sensitive to small changes

![tree-ensemble](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/tree_ensemble_1.png)

## Sampling with replacement

![sampling-with-replacement](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/sampling_with_replacement_1.png)

We are going to construct multiple random training sets that are all slightly different from our original training set

1. Pick a random training example

2. Note it down

3. Put it back to the *bag*

4. Repeat

It's okay to get repeated training examples. Now, you have a new training set that are similar to the original one, but also different a little bit

## Random Forest Algorithm

**Random Forest** algorithm is one powerfull tree ensemble algorithm

### Generating a tree sample

A common choice of *B* is 64 to 128

You store the built decision trees and make them all predict (*vote*)

![bagged-decision-tree](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/bagged_decision_tree.png)

In a certain point, having too many decision trees, doesn't give additional returns, just slows down the computation

You could end up with the same feature as the root in lots of decision trees, so there is one modification to turn it into **Random Forest** algorithm


When *n* is **large**, a common choice of *k* is sqrt(n)

The sampling with replacement procedure causes the algorithm to explore a lot of small changes to the data

![random-forest](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/random_forest_1.png)

## XGBoost

It's a slightly changed random forest algorithm, that runs very quick

You focused on misclassied examples

We're going to look at the decision trees we've trained so far and look at what we're still not yet doing well

So, we focused on the subset of examples we're not yet doing well on and get a new decision tree

![boosted-trees](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/boosted_trees.png)

Rather than doing sampling with replacement XGBoost assigns different weights to different training examples. So, it doesn't actually need to generate a lot of randomly chosen training sets

![XGBoost](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module4/XGBoost_1.png)

```
# Classication

from xgboost import XGBClassifier

model = XGBClassifier()

model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
```

```
# Regression

from xgboost import XGBRegressor

model = XGBRegressor()

model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
```