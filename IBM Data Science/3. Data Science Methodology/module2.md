# From Understanding to Preparation

## Data Understanding

**Data Understanding** encompasses all activities related to constructing the dataset

In order to understand the data related to congestive heart failure admissions, descriptive statistics needed be to run against the data columns that would become variables in the model

First, these statistics included hurst, univariates and statistics on each variable, such as: mean, median, minimum, maximum and standard variation

Second, pairwise correlations were used to see how closely certain variables were related and which ones, if any, were very highly correlated, meaning that they would be essentially **redundant** (only one is relevant for modeling)

Third, histograms of the variables were examined to understand their distributions

**Histograms** are a good way to understand how values or a variable are distributed and which sorts of data preparation may be needed to make the variable more useful in a model

Furthermore, the univariates, statistics and histograms are also used to assess data quality. From the information provided, certain values can be re-coded or perhaps even dropped if necessary (such as when a certain variable has missing value)

The question becomes: does *missing* mean anything? Sometimes a missing value might mean *no*, *0* or, at other times, it means *we don't know*


Initially, the meaning of *congestive heart failure admission* was decided on the basis of a primary diagnosis of congestive heart failure. But working through the data understanding stage revealed that the initial definition was not capturing all of the congestive heart failure admissions that were expected (based on clinical experience). This meant looping back to the data collection stage and adding a secondary and tertiary diagnoses and **bulding a more comprehensive definition of congestive heart failure definition**

## Data Preparation

In a sense, Data Preparation is similar to washing freshly picked vegetables in so far as unwanted elements, such as dirt or imperfection, are removed

Together with Data Collect and Data Understanding, Data Preparation is the most time-consuming phase of a data science project

Automating some of the data collection and preparation processes in the database, can reduce this time. This time saving translates into increased time for data scientists to focus on creating models

Transforming the data in the Data Preparation phase is the process of getting the data into a state where it may be easier to work with

To work effeciently with the data, it must be prepared in a way that addresses missing or invalid values and removes duplicates, toward ensuring that everything is formatted properly


**Feature Engineering** is the process of using the domain knowledge of the data to create features that make the machine learning model works

### Case Study

An important first step in Data Preparation process was to actually define congestive heart failure

This sounds easy at first, but defining it precisely is not straightfoward

First, the set of diagnosis-related group codes needed to be identified. We also needed to consider that congestive heart failure is only one type of heart failure (clinical guidance may be needed to get the right codes)

The next step involved defining re-admission criteria for the same condition

The timing of events needed to be evaluated in order to define whether a particular congestive heart failure admission was an initial admission or a congestive heart failure re-admission

Based on clinical expertise, a time period of 30 days was set for readmission

Next, the records that were in transactional format were aggregated (the data included multiple records of each patient). Then, all the transactional records were aggregated to the patient level, yielding a single record for each patient (many new columns were created). Aggregating to the patient level also meant merging it with other patient data, such as: age, gender...

During discussions around data preparation, a **literary review** on congestive heart failure was also undertaken to see whether any important data elements were overlooked. The literary review on congestive heart failure involved looping back to data collection stage to add a few more indicators for conditions and procedures

The result was the creation of one table containing a single record per patient, with many columns representing the attributes about the patient.

The **dependent variable** (or **target**) was congestive heart failure re-admission within 30 days following discharge from a hospitalization for congestive heart failure, with an outcome of *yes* or *no*


# From Modeling to Evaluation

## Data Modeling

**Data Modeling** focuses on developing models that are either descriptive or predictive

An example of a **descriptive model** might examine things like: if a person did this, then they are likely to prefer that

A **predictive model** tries to yield *yes* or *no* or *stop* or *go* outcomes

The data scientist uses a training set for predictive modelling. A training set is a set of historical data in which the outcomes are already known

In this stage, the data scientist will play around different algorithms to ensure that the variables in play are really required

In John Rollins Data Science Methodology, the framework is geared to do three things:

* First, understand the problem at hand

* Second, select an analytic approach or model to solve the problem

* Third, obtain, understand, prepare and model the data

### Case Study

With a prepared training set, the first decision tree classification model for congestive heart failure readmission can be built

In the first model, the overall accuracy in classifying the *yes* and *no* outcomes is 85%. It sounds good, but only represents 45% of the *yes* group

**How could we improve the model accuracy in classifying *yes* outcomes?**

For Decision Tree Classification, the best parameter to adjust is the relative cost of the misclassified *yes* and *no* outcomes

When a true non-readmission is misclassified and action is taken to reduce that patient's risk, the cost of that error is the wasted intervention. The statistians call this a **type I** error or a **false positive**

When a true readmission is misclassified and no action is taken to reduce that risk, then the cost of that error is the readmission and all of its attended cost, plus the trauma of the patient. This is a **type II** error or a **false negative**

So, we can see that the costs of the two different kinds of misclassification errors can be quite different. For this reason, it's reasonable to adjust the relative weights of misclassifying the *yes* and *no* outcomes. The default is 1-to-1, but the decision tree algorithm allows the setting of a higher value for *yes*

For the second model, the relative cost was set at 9-to-1. This is a very high ratio, but it gives more insight to the model's behaviour. This time, the model correctly classified 97% of the *yes*, but at the expense of a very low accuracy on the *no*

## Evaluation

A model evaluation goes hand-in-hand with model building as such

Evaluation allows the quality of the model to be **assessed**, but it's also an opportunity to see if it **meets the initial request**

**Model Evaluation** can have two main phases:

* **Diagnostic Measures phase**: it's used to ensure the model is working as intended
    * If the model is a predictive model, a decision tree can be used to evaluate if the answer the model can output is aligned to the initial design. It can be used to see where there are areas that require adjustments
    * If the model is a descriptive model, one in which relationships are being assessed, then a testing set with known outcomes can be applied and the model can be refined as needed

* **Statistical Significance Testing**: This type of evaluation can be applied to the model to ensure that the data is being properly handled and interpreted within the model

### Case Study

Four models were built with four different relative misclassification costs

Each value of this model-building parameter increases the true positive rate, or sensitivity, of the accuracy in predicting yes, at the expense of lower accuracy in predicting no, that is, an increasing false positive rate

**Which model is best based on tuning this parameter?**

For budgetary reasons, the risk-reducing intervention could not be applied to most or all congestive heart failure patients, many of whom would not have been readmitted anyway

On the other hand, the intervention would not be as effective in improving patient care as it should be, with not enough high-risk congestive heart failure patients targeted

**How do we determine which model was optimal?**

The optimal one is the one giving the maximum separation between the blue ROC curve relative to the red base line

**ROC** stands for **Receiver Operating Characteristic curve**. ROC curve is a useful diagnostic tool in determining the optimal classification model. This curve quantifies how well a binary classification model performs