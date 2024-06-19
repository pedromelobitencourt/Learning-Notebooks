# Problem to Approach

Data Science combines statistics, technology and domain expertise to extract insights from vast data

However, despite of the increase of computing power and easier access to data, we often have some challenges:

* Misunderstanding of business questions

* Not knowing how to apply the data to resolve the business problem correctly

Adopting a methodology, helps to solve this kind of issues

**Methodology** is a system of methods used in a particular area of study. It is a guideline for decision-making during the scientific process

**Data Science Methodology** includes:

* Perform data collection

* Creation of measurement strategies

* Comparisons of data analysis methods

## Data Science Methodology by John Rollins

There are 10 stages, they are:

* **Business Understanding**: 
    * What is the problem that you are trying to solve?

* **Analytic Approach**:
    * How can you use data to answer the business question?

* **Data Requirements**:
    * What data do you need to answer the question?

* **Data Collection**: 
    * Where is the data sourced from and how will you receive the data?

* **Data Understanding**:
    * Does the data you collected represent the problem to be solved?

* **Data Preparation**:
    * What additional work is required to manipulate and work with the data?

* **Modeling**: 
    * When you apply data visualizations, do you see answers that address the business problem?

* **Evaluation**: 
    * Does the data model answer the initial business question or must you adjust the data?

* **Deployment**: 
    * Can you put the model into practice?

* **Feedback**: 
    * Can you get constructive feedback from the data and the stakeholder to answer the business question?

Asking questions is the **cornerstone** of success in Data Science. It helps you define the issue and determine your approach

## Business Understanding

Establishing a clearly defined question starts with understanding the **goal** of the person who is asking the question

Once the goal is clarified, the next piece of the puzzle is to figure out the objectives that are in support of the goal

By breaking down the objectives, structured discussions can take place where priorities can be identified in a way that can lead to organizing and planning on how to tackle the problem

### Case Study

The question being asked is: **What is the best way to allocate the limited healthcare budget to maximize its use in providing quality care?**

Before even starting to collect data, the goals and objectives needed to be defined

* **Goals**: to provide quality care without increasing costs

* **Objectives**: to review the process to identify inefficiencies

It was found that approximately 30% of individuals who finish rehab treatment would be readmitted to a rehab center within one year; and that 50% would be readmitted within five years

After reviewing some records, it was discovered that the patients with congestive heart failure were at the top of the readmission list

To gain the business understanding that would guide the analytics team in formulating and performing their first project, the data scientists can propose and deliver an on-site workshop to kick things off

Then, four business requirements can be established for the model to be developed:

1. Predicting readmission outcomes for patients with congestive heart failure

2. Assessing readmission risk

3. Understanding the sequence of events leading to the predicted outcomes

4. Implementing an easy-to-understand process for new patients concerning their readmission risk

## Analytic Approach

The approach involves seeking clarification from the person who is asking the question so as to pick the most appropriate path or approach

Pick an analytic approach based on the question type

If the question is to determine the probabilities of an action, **use a predictive model**

If the question is to show relationships, **use a descriptive model** (clusters)

If the question requires a yes/no answer, **use a classification model**

### Case Study

For the case study, a decision tree classification model was used to identify the combination of conditions leading to each patient's outcome

The decision tree classifier provides both the predicted outcome, as well as the likelihood of that outcome, based on the proportion at the dominant outcome

From this information, the analysts can obtain the readmission risk or the likelihood of a yes for each patient

## Data Requirements

This section can be seen as cooking with data. Each step is critical in making the meal

If the problem that needs to be solved is the recipe, so to speak, and data is an ingredient, then the data scientist needs to identify: which ingredients are required, how to source or to collect them, how to work with them and how to prepare the data to meet the desired outcome

Let's define the data requirements for decision-tree classification. This includes identifying the necessary data content, formats and sources for initial data collection

### Case Study

Let's select a suitable patient cohort from the health insurance providers member base

In order to compile the complete clinical histories, 3 criteria were identified:

* A patient needed to be admitted as in-patient within the provider service area (to have access to the necessary information)

* Focus on patients with a primary diagnosis of congestive heart failure during one full year

* A patient must have had continuous enrollment for at least six months (prior to the primary admission for congestive heart failure)

Hence, the content, formats, representations were defined

Congestive heart failure patients with other significant medical conditions were excluded from the study, because their data could skew the analysis

* One record per patient with columns representing variable

* Content covering all aspects of each patient's clinical history


## Data Collection

After the initial data collection is performed, an assessment by the data scientist takes place to determine whether or not they have what they need

Some data might be more difficult to obtain or cost more than initially thought

In this phase, the data requirements are revised and decisions are made as to whether or not the collection requires more or less data

After the data is collected, the data scientist will have a good understanding of what they will be working with. Techniques such as decriptive statistics and visualization can be applied to the data set, to assess the content, quality and initial insights about the data

**Gaps** in data will be identified and plans to either fill or make substitutions will have to be made


### Case Study

**Collecting data** requires that you know the source or know where to find the data elements that are needed

In the context of our case study, this includes: demographic, clinical and coverage information of patients, provider information, claims records as well as pharmaceutical and other information related to all the diagnoses of the congestive heart failure patients

Let's say that certain drug information was also needed, but that data source was not yet integrated with the rest of the data sources

This leads to an important point: it is alright to defer decisions about unavailable data and attempt to acquire it at a later stage

For example, this can even be done after getting some intermediate results from the predictive modeling.

If those results suggest that the drug information might be important in obtaining a good model, then the time to try to get it would be invested

**DBAs and programmers often work together to extract data from various sources and then merge it**

At this state, if necessary, data scientists and analytics team members can discuss various ways to better manage their data, including automating certain processes in the database, so that data collection is easier and faster