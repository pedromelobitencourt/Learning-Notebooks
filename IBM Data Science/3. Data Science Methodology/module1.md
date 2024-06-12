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