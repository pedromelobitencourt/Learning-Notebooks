# Big Data and Data Mining

The availability of vast amounts of data and the competitive advantage that analyzing it brings has triggered digital transformations throughout many industries

Digital transformation is not simply duplicating existing processes in digital form. The in-depth analysis of how the business operates helps organizations to discover how to improve their processes and operations and harness the benefits of integrating data science into their workflows

## Cloud Computing

* It's the delivery of on-demand computing resources (networks, servers, storage, applications, services, data centers) over the internet on a pay-for-use basis

* Applications and data that users can access over the Internet rather than locally

* Then, there is no need to purchase applications and install them on local computer

* Enables users to work collaboratively

### Cloud Computing Characterists

* **On-demand self-service**: you can access cloud resources using a simple interface without a requiring human interaction

* **Broad Network Access**: cloud computing resources can be accessed via the network

* **Resource Pooling**: it's what gives cloud providers economies of scale, which makes the cloud cost-efficient
    * Using a multitenant model, computing resources are pooled to serve multiple consumers and cloud resources are dynamically assigned and reassigned according to demand, without the consumers needing to know the physical location of these resources

* **Rapid Elasticity**: it implies that you can access more resources when you need them and scale back when you don't

* **Measured Service**: you only pay for what you use or reserve as you go. Resource usage is monitored, measured and reported transparently based on consumer utilization


### Cloud Deployment Models

It indicates where the infrastructure resides, who owns and manages it and how cloud resources and services are made available to users

* **Public**: It's when you leverage cloud services over the open internet on hardware owned by the cloud provider, but its usage is shared by other companies

* **Private**: The cloud infrastructure is provisioned for exclusive use by a single organization

* **Hybrid**: Mix of both public and private clouds, working together seamlessly


### Cloud Service Models

* **Infrastructure as a Service (IaaS)**: you can access the infrastructure and physical computing resources such as servers, networking, storage and data center space without the need to manage and operate them

* **Platform as a Service (PaaS)**: you can access the platform that comprises the hardware and software tools that are usually needed to develop and deploy applications to users over the Internet

* **Software as a Service (SaaS)**: it's a software licensing and delivery model in which software and applications are centrally hosted and licensed on a subscription basis

Using cloud enables you to get instant access to open-source technologies without the need to install and configurey them locally

Using the cloud also gives you access to the most up-to-date tools and libraries without the worrying of maintaining them and ensuring that they are up-to-date


## Foundations of Big Data

Big Data refers to the dynamic, large and disparate volumes of data being created by people, tools and machines

It requires new, innovative and scalable technology to collect, host and analytically process the vast amount of data gathered

### The V's of Big Data

* **Velocity**: It's the speed at which data accumulates. Data is being generated extremely fast

* **Volume**: It's the scale of the data or the increase in the amount of data stored
    * Drivers of volume are: the increase in data sources, higher resolution sensors and scalable infrastructure

* **Variety**: It's the diversity of the data. Different types of data, the data comes from different sources, machines, people and processes
    * Drivers are: mobile technologies, social media, wearable technologies, geo technologies, video...

* **Veracity**: It's the quality and the origin of data and its conformity to facts and accuracy
    * Attributes are: consistency, completeness, integrity and ambiguity
    * Drivers are: cost and need for traceability

* **Value**: It's our ability and need to turn data into value


## Hadoop

In a big data cluster, you take the data and slice it into pieces. The, you distribute, replicate or triplicate each piece and send it (the pieces of these files) to a lot of computers

Each computer would run the program on its little piece of the file and send the results back. The result would then be sorted and those results would then be redistributed back to another process

The first process is called **map** or **mapper process**

The second process is called **reduce process**

The big data clusters scale linearly. If you have twice as many servers, you handle twice as many data and you get twice the performance

**Hadoop** is an open-source software framework designed for distributed storage and processing of large datasets using a cluster of computers

Hadoop is built to scale from single servers to thousands of machines, each offering local computation and storage. The framework is known for its ability to handle vast amounts of data in a fault-tolerant and reliable manner.

### How does Data Science differ from traditional subjects like Statistics?

Most of components of Data Science have been around for decades (Calculus, Linear Algebra, Algebra, Statistics, Programming, Databases...)

But now we have computational capabilities to combine them and apply some new techniques (such as: Machine Learning) and we can take really large data sets

### Big Data Processing Tools

The Big Data processing technologies provide ways to work with large sets of structured, semi-structured and unstructured data

* **Apache Hadoop**: a collection of tools that provides distributed storage and processing of big data
    * Node: it's a single computer
    * Cluster: a collection of nodes
    * It offers reliable, scalable and cost-effective solution for storing data with no format requirements
    * It incorporates emerging data formats not traditionally used in data warehouses
    * Improved data access and analysis
    * Data offload and consolidation
    * HDFS is a storage system for big data that runs on multiple commodity hardware connected through a network. It provides scalable and reliable big data storage by partitioning files over multiple nodes, allowing parallel access to them. Also it replicates file blocks on different nodes to prevent data loss
    * Fast recovery from hardware failures, because HDFS is built to detect faults and automatically recover
    * Access to streaming data

* **Apacha Hive**: a data warehouse for data query and analysis build on top of Hadoop
    * software for reading, writing and managing large data set files that are stored directly in either HDFS or other data storage systems
    * queries have high latency
    * read-based: not suitable for transaction processing that involves a high percentage of write operations

* **Apache Spark**: a distributed analytics framework for complex real-time data analytics
    * designed to extract and process large volumes of data for a wide range of applications (interactive analytics, streams processing, machine learning, data integration)
    * Has in-memory processing which increases speed of computation
    * Provides interfaces for major programming languages
    * Can access data in a large variety of data sources


## Data Mining

### Goal Set

* The first step in **data mining** is set up goals for the exercise
    * you must idedntify the keys questions that need to be answered

* You must determine, in advance, the expected level of accuracy and usefulness of the results obtained from data mining
    * high levels of accuracy from data mining would cost more
    * beyond a level of accuracy, you do not gain much

* The cost-benefit trade-off is always instrumental in determining the goals and scope of the data mining exercise

### Selecting Data

* The output of a data mining exercise largely depends upon the quality of data used

* There may be times that data may not be readily available for data mining
    * in such cases, you must identify other sources of data or even plan new data collection initiatives

### Preprocessing Data

* Often raw data are messy, containing erroneous or irrelevant data

* Sometimes, even with relevant data, information is missing

* You must identify irrelevant attributes of data and expunge such attributes from further consideration

* At the same time, identifying the erroneous aspects of the data set and flagging them as such is necessary

* Lastly, you must develop a formal method of dealing with missing data and determine whether the data is missing randomly or systematically
    * if the data is missing randomly, a simple set of solutions would suffice
    * if the data are missing in a systematic way, you must determine the impact of missing data on the results
        * For example, a particular subset of individuals in a large data set may have refused to disclose their income. Findings relying on an individual's income as input would exclude details of those individuals whose income was not reported. This would lead to systematic biases in the analysis

### Transforming Data

* Determine the appropriate format in which data must be stored

* An important consideration in data mining is to reduce the number of attributes needed to explain the phenomena
    * This may require transforming data using Data Reduction Algorithms (such as PCA) without a significant loss in information

* Variables may need to be transformed to help explain the phenomenon being studied

* Often, you need to transform variables from one type to another


### Storing Data

* The data must be stored in a format that gives unrestricted and immediate read/write privileges to the data scientist

* During data mining, new variables are created, which are written back to the original database


### Mining Data

* This step covers data analysis methods (including parametric and non-parametric methods, and machine learning algorithms)

* A good starting point is **data visualization**

### Evaluating Mining Results

* Formal evaluation could include testing the predictive capabilities of the models on observed data to see how effective and efficient the algorithms have been in reproducing data

* You share yor results with stakeholders

This entire process should be conducted iteratively as your results from this iteration will inform further data mining efforts

## Glossary

* **Analytics**: The process of examining data to draw conclusions and make informed decisions is a fundamental aspect of data science

* **Big Data**: Vast amount of structured, semi-structured and unstructured data are characterized by its volume, velocity, veracity, variety and value

* **Big Data Cluster**: A distributed computing environment comprising thousands or tens of thousands of interconnected computers that collectively store and process large data sets

* **Broad Network Access**: The ability to access cloud resources via standard mechanisms and platforms (such as mobile devices, laptops and workstations over networks)

* **Cloud Computing**: The delivery of on-demand computing resources over the Internet on a pay-for-use basis

* **Cloud Deployment Models**: Categories that indicate where cloud infrastructure resides, who manages it and how cloud resources and services are made available to users

# Deep Learning and Machine Learning

### Big Data

The terms refers to data sets that are so massive, so quickly built and so varied that they defy traditional analysis methods, such as you might perform with a relational database

### Data Mining

It refers to the process of automatically searching and analyzing data, discovering previously unrevealed patterns

It involves preprocessing the data to prepare it and transforming it into an appropriate format

Once this is done, insights and patterns are extracted using various tools and techniques, ranging from **Data Visualization**, **Machine Learning** and **Statistical Models**

### Machine Learning

Machine Learning is a subset of AI that uses computer algorithms to analyze data and make intelligent decisions based on what it has learned, without being explicitly programmed

Machine Learning algorithms are trained with large sets of data and they learn from examples

It enables machines to solve problems on their own and make accurate predictions


### Deep Learning

Deep Learning is a specialized subset of Machine Learning that uses layered neural networks to simulate human decision-making

Deep Learning algorithms can label and categorize information and identify patterns


### Neural Networks

It takes inspiration from biological neural networks, although they work quite a bit differently

A Neural Network is collection of small computing units called *neurons*, that take incoming data and learn to make decisions over time


### Artificial Intellingence and Data Science

Data Science is the process and method for extracting knowledge and insights from large volumes of data. It involves mathematics, statistical analysis, machine learning and more

Data Science can use many of the AI techniques to derive insight from data (it can use Machine Learning and Deep Learning for example)

## Generative AI and Data Science

**Generative AI** is a subset of AI that focuses on producing new data rather than just analyzing existing data

It allows computers to create content, such as: images, music, language, code, mimicking creations by people

### How does Generative AI work?

Deep Learning models like *Generative Adversarial Networks* (GANs) and *Variational Auto-encoders* (VAEs) are at the foundation of this technique

These models create new instances that replicate the underlying distribution of the original data by learning patterns from enormous volumes of data

Some applications are:

* Natural Language Processing like OpeanAI's GPT-3

* In healthcare, Generative AI can synthesize medical images, aiding in the training of medical professionals

* Generative AI can create unique and visually artworks

* Generate realistic environments, characters

**But how does data scientists use Generative AI?**

**Synthetic Data**

Building data models takes a lot of data and sometimes data sets may not have enough data to build a model

Consequently, interest in **synthetic data** as a tool for analysis and model creation has increased due to recent developments in generative AI, since Data scientists can augment their data sets using generative AI to create synthetic data

Synthetic data is created with similar properties as the real data, such as its distribution, clustering and many other factors the AI learned about

**Code Automation**:

Data scientists, researches and analysts frequently don't have enough time to conceive, develop and evaluate a small number of hypotheses, leaving many other possibilities untested. Then, with Generative AI, data scientists can leverage generative AI to generate and test software code for construction analytical models

With code automation, the data scientists can focus on higher-level tasks such as identifying and clarifying the problem the models intend to solve and evaluating hypotheses from a wider range of data sources

**Uncover Insights**

Generative AI can generate accurate business insights and comprehensive reports, making it possible to update these insights as the data evolves (automate updates)

It can autonomously explore data to uncover hidden patterns and insights that might go unnoticed

## Neural Networks and Deep Learning

Neural Networks attempt to mimic the neurons and how our brain actually functions

A Neural Network would have some inputs that would come in. These inputs would be fed into different processing nodes. These nodes would do some transformation on them and aggregate them and they could go to another level of nodes and so on...

Finally an output would come out

Before, in the 90s, people did not use neural networks so much, because it was computationally very expensive

All of sudden, everything's changed when **Deep Learning** appeared

Deep Learning is Neural Network in steroids. Humor aside, Deep Learning is Neural Network with multiple layers. It requires a lot of computer power to solve those layers

Now, computers require GPU (Graphic Processing Unit) to use Deep Learning as long as there are a lot of algebra and linear algebra calculations involved in

Deep Learning algorithms become more efficient as the amount of data increases in volume, unlike other machine learning algorithms which tend to plateau

### Deep Learning Applications

* Speech Recognition

* People Recognition

* Classifying images

### Machine Learning Applications

* Recommender Systems

* Classifications

* Cluster Analysis

* Predictive Analytics

* Fraud Detection

## Regression

It identifies correlation between inputs and outputs

In medical science, regression models are being used to develop more effective medicines, improve the methods for operations and optimize resources for small and large hospitals

We can use regression to predict house prices depending on a lot of features. We could conclude the following:

* **Size of Homes**: The regression analysis confirmed that larger homes sell for more than smaller homes. This correlation was quantified, showing the magnitude of the price increase associated with additional square footage

* **Additional Features**: The study found that an additional bathroom contributes more to the price of a house than an additional bedroom. The marginal increase in housing prices was higher for an additional bathroom, highlighting the specific value-added by this feature

* **Proximity to Transport Infrastructure**: 
    * **subways**: Homes located closer to subway stations sold for higher prices compared to those farther away. Proximity to subways was positively correlated with housing prices

    * **highways/freeways**: In contrast, homes near highways or freeways sold for less than those located farther from such infrastructure. The negative impact on housing prices was quantified in the analysis

* **Proximity to Shopping Centers**: The impact of proximity to large shopping centers on housing prices was found to be nonlinear
    * Houses very close (less than 2.5 km) to shopping centers sold for less than those located farther away.

    * Houses located within a moderate distance (between 2.5 km and 5 km) from shopping centers sold for more than those farther away, indicating an optimal distance range for positive impact on housing prices

* **Distance from Downtown**: Housing values in Toronto were found to decline with increasing distance from the downtown area. The regression analysis quantified this decline, providing precise measurements of the impact of distance from the city center on property values

### Glossary

* **Bayesian Analysis**: A statistical technique that uses Bayes' theorem to update probabilities based on new evidence

* **Business Insights**: Accurate insights and reports generated by generative AI. It can be updated as data evolves, enhancing decision-making and uncovering hidden patterns

* **Cluster Analysis**: The process of grouping similar data points together based on certain features or attributes

* **Market Basket Analysis**: Analyzing which goods tend to be bought together. It's often used for marketing insights

* **Predictive Analytics**: Using machine learning techniques to predict future outcomes or events