# Data Exploration

Understanding the different types of data and data structures helps to know what type of data is right for the question we're answering

# Collect Data

Tons of data is being generated all around the world

Every piece of information is data and all data is a result of our activity in the world

We can generate data by collecting information. This kind of generation and collection comes with a few more things to think about: it needs to be done with consideration to **ethics**, maintaining people's right and privacy

One example is **survey data**

## How data is collected?

* Interviews

* Observations

* Forms

* Questionnaires

* Surveys

* Cookies (to track people's activity and interests, it's the most effective method)

## Data collection consideration

For instance, let's have a question as example: What's causing increased rush hour traffic in our city?

**How the data will be collected?**

We might use our observations of traffic patterns to count the number of cars on city streets in particular times

**Choose data sources**

* First-party data: data collected by an individual or group using their own resources (preferred source since we know exacty where the data came from)

* Second-party data: data collected by a group directly from its audience and then sold (for example, an organization which led traffic pattern studies in our city, it's still a reliable source and with experience with traffic analysis)

* Third-party data: data collected by outside sources who dit not collect it directly (less reliable one, but it can be useful, so you must check bias, accuracy and credibility)

Every data has to be inspected for accuracy and trustworthiness

**What data to use?**

Data that can help solve problems

**How much data to collect?**

* Population: all possible data values in a certain dataset

* Sample: part of a population that is representative of the population

How to choose the sample depends on our project

**Select the right data type**

Dates of traffic records stored in a data format

**Determine the time frame**

Use historical data


# Differentiate Data Formats and Structures

* **Qualitative data**: data that can't be counted, measured or easily expressed using numbers
    * Nominal data: data that is categorized without a set order (it doesn't have a sequence)
    * Ordinal data: data with a set order or scale

* **Quantative data**: data that can be measured or counted and expressed using numbers
    * Discrete data: data that is counted and has a limited number of values, partial measurements (half star) aren't allowed
    * Continuous data: data that is measured and can have almost any numeric value

* **Internal data**: data that lives within a company's own systems (more reliable and easier to collect)

* **External data**: data that lives and is generated outside of an organization

* **Structured data**: data that is stored in a particular format such as rows and columns (spreadsheets, tables)

* **Unstructured data**: data that is not organized in any easily identifiable manner (audio files, video files)

Most of the data being generated right now is unstructured data, such as: audio files, video files, emails, photos, social media. They can be hard to work on, but most of the time we'll be working with structured data since the unstructured data will most likely be structured for analysis

Stuctured data works nicely with a **data model** and makes data visualization easy

* **Data model**: model that is used for organizing data elements and how they relate to one another, providing a map of how data is organized

* **Data elements**: pieces of information, such as people's names

![structured-and-unstructured-data](/Data%20Analytics/Prepare%20Data%20for%20Exploration/assets/module1/structured_unstructured_data_1.png)

The lack of structure makes unstructured data difficult to search, manage, and analyze. But recent advancements in artificial intelligence and machine learning algorithms are beginning to change that. Now, the **new challenge** facing data scientists is making sure these tools are **inclusive** and **unbiased**

## Data Modeling

**Data modeling** is the process of creating diagrams that visually represent how data is organized and structured

The visual representations are called **data models**

Different users might have different data needs, but the data model gives them an understanding of the structured as a whole

### Levels of data modeling

1. Conceptual data modeling: it gives a high-level view of the data structure and it doesn't contain technical details

2. Logical data modeling: it focuses on the technical details of a database such as relationships, attributes and entities

3. Physical data modeling: it depicts how a database operates. It defines all entities and attributes useeds


### Data-modeling techniques

Two common methods are:

* **Entity Relationship Diagram (ERD)**

* **Unified Modeling Language (UML)**


# Explore Data Types, Fields and Values

* **Data Type**: a specific kind of data attribute that tells what kind of value the data is

Data types in spreadsheets can be one of 3 things:

* Number (you can change the format to currency...)

* Text or string (there can be numbers, but not those used in calculations)

* Boolean

Rows can also be called **records** and columns can be called **fields**

But, in some contexts, **field** can mean a specific value

* **Wide data**: data in which every data subject has a single row with multiple columns to hold the values of various attributes of the subject
    * It lets us quickly identify and compare columns

* **Long data**: data in which each row is one time point per subject, so each subject will have data in multiple rows
    * Great format for storing and organizing data when there's multiple variables for each subject at each time point that we want to observe
    * We can analyze all of this data using fewer coluns
    * If we added a new variable, we'd need only one more columns

## Data Transformation

**Data transformation** is the process of changing the data's format, structure or values

Data transformation usually involves:

* Adding, copying or replicating data

* Deleting fields or records

* Standardizing the names of variables

* Renaming, moving or combining columns in a database

* Joining one set of data with another

* Saving a file a different format

**Why to transform data?**

* Data Organization: better organized data is easier to use

* Data Compatibility: different applications or systems can then use the same data

* Data Migration: data with matching formats can be moved from one system to another

* Data Merging: data with the same organization can be merged together

* Data Enhancement: data can be displayed with more detailed fields

* Data Comparison: apples-to-apples comparisons of the data can then be made