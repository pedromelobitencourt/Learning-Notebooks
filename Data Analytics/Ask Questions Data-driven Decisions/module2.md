# Understanding the power of data

* Data-inspired decision-making: explore different data sources to find out what they have in common

* Algorithm: a process or a set of rules to be followed for a specific task

Every single action that we do in this world is triggering off some amount of data, and most of that data is meaningless until someone adds some interpretation of it or someone adds a narrative around it

Both **data-driven** and **data-inspired** approaches are rooted in the idea that data is inherently valuable for making a decision. Well-curated data can provide information to  decision-makers that improves the quality of their decisions. 

Data does not make decisions, but it does improve them.

## Data-driven decisions

he phrase “data-driven decisions” means exactly that: Data is used to arrive at a decision. This approach is limited by the quantity and quality of readily-available data. If the quality and quantity of the data is sufficient, this approach can far improve decision-making.

But if the data is insufficient or biased, this can create problems for decision-makers. Potential dangers of relying entirely on data-driven decision-making can include overreliance on historical data, a tendency to ignore qualitative insights, and potential biases in data collection and analysis

### Example

A/B testing is a simple example of collecting data for data-driven decision-making. For example, a website that sells widgets has an idea for a new website layout they think will result in more people buying widgets. For two weeks, half of their website visitors are directed to the old site; the other half are directed to the new site. After those two weeks, the analyst gathers the data about their website visitors and the number of widgets sold for analysis. This helps the analyst understand which website layout resulted in more widget sales. If the new website performed better in producing widget sales, then the company can confidently make the decision to use the new layout!


## Data-inspired decisions

Data-inspired decisions include the same considerations as data-driven decisions while adding another layer of complexity. They create space for people using data to consider a broader range of ideas: drawing on comparisons to related concepts, giving weight to feelings and experiences, and considering other qualities that may be more difficult to measure. Data-inspired decision-making can avoid some of the pitfalls that data-driven decisions might be prone to. 


### Example

A customer support center gathers customer satisfaction data (often known as a “CSAT” score). They use a simple 1–10 score along with a qualitative description in which the customer describes their experience. The customer support center manager wants to improve customer experience, so they set a goal to improve the CSAT score. They start by analyzing the CSAT scores and reading each of the descriptions from the customers. Additionally, they interview the people working in the customer support center. From there, the manager formulates a strategy and decides what needs to improve the most in order to raise customer satisfaction scores. While the manager certainly relies on the CSAT data in the decision-making process, input of support center representatives and other qualitative information informs the approach as well.


**Quantitative data**: specific and objective measures of numerical facts, in other words, things you can measure

* The what?
* How many?
* How often?

Numbers can be visualized as charts or graphs


**Qualitative data**: subjective or explanatory measures of qualities and characteristics, things that can't be measured by numerical data

* Why?

It gives a more high-level understanding, add context

You can use, in a problem, quantitative and qualitative data. For instance: customer's review

### Quantitative

* How many negative reviews are there?
* What's the average rating?
* How many of these reviews use the same keywords?


### Qualitative

* Why are customers insatisfied?
* How can we improve their experience?


![quantitative-data-versus-qualitative-data](/Data%20Analytics/Ask%20Questions%20Data-driven%20Decisions/assets/quantitative-qualitative.png)


You are a data analyst for a chain of movie theaters. Your manager wants you to track trends in:

* Movie attendance over time

* Profitability of the concession stand

* Evening audience preferences 

Assume quantitative data already exists to monitor all three trends. 


### Movie attendance over time

Starting with the historical data the theater has through its loyalty and rewards program, your first step is to investigate what insights you can gain from that data. You look at attendance over the last 3 months. But, because the last 3 months didn’t include a major holiday, you decide it is better to look at a full year’s worth of data. As you suspected, the quantitative data confirmed that average attendance was 550 per month but then rose to an average of 1,600 per month for the months with holidays. 

The historical data serves your needs for the project, but you also decide that you will resume the analysis again in a few months after the theater increases ticket prices for evening showtimes. 


### Profitability of the concession stand

Profit is calculated by subtracting cost from sales revenue. The historical data shows that while the concession stand was profitable, profit margins were razor thin at less than 5%. You saw that average purchases totaled $20 or less. You decide that you will keep monitoring this on an ongoing basis. 

Based on your understanding of data collection tools, you will suggest an online survey of customers so they can comment on the food at the concession stand. This will enable you to gather even more quantitative data to revamp the menu and potentially increase profits. 


### Evening audience preferences

Your analysis of the historical data shows that the 7:30 PM showtime was the most popular and had the greatest attendance, followed by the 7:15 PM and 9:00 PM showtimes. You may suggest replacing the current 8:00 PM showtime that has lower attendance with an 8:30 PM showtime. But you need more data to back up your hunch that people would be more likely to attend the later show.

Evening movie-goers are the largest source of revenue for the theater. Therefore, you also decide to include a question in your online survey to gain more insight. 


### Qualitative data for all three trends plus ticket pricing

Since you know that the theater is planning to raise ticket prices for evening showtimes in a few months, you will also include a question in the survey to get an idea of customers’ price sensitivity. 

Your final online survey might include these questions for qualitative data:

* What went into your decision to see a movie in our theater today? (movie attendance)

* What do you think about the quality and value of your purchases at the concession stand? (concession stand profitability)

* Which showtime do you prefer, 8:00 PM or 8:30 PM, and why do you prefer that time? (evening movie-goer preferences)

* Under what circumstances would you choose a matinee over a nighttime showing? (ticket price increase)



# Follow the evidence

## Data presentation tools

### Reports

Report: static collection of data given to stakeholders periodically

* Pros:
    * High-level historical data
    * Easy to design
    * Pre-cleaned and sorted data

* Cons:
    * Continual maintenance 
    * Less visual appealing
    * Static

* Pivot table: It is a data summarization tool that is used in data processing. Pivot tables are used to summarize, sort, re-organize, group, count, total, or average data stored in a database

### Dashboard

* Dashboard: monitors live, incoming data

* Pros:
    * Dynamic, automatic and interactive
    * More stakeholders access
    * Low maintenance

* Cons:
    * Labor-intensive design
    * Can be confusing
    * Potentially unclean data


Metrics can be used to turn data into useful information

**Metric:** single, quantifyable type of data that can be used for measurement

Metrics are, usually, used with formulas

**Metric goal:** a measurable goal set by a company and evaluated by metrics


## Tools for visualizing the data

### Spreadsheets

Google Workspace and Microsoft Office Suite both offer spreadsheet applications. You’ve worked with Google Sheets in this course, and it’s very similar in function to Microsoft Excel. If you want to compare some of the features of Sheets to Excel, check out the Microsoft video 
Create a chart from start to finish.

Both Sheets and Excel are go-to choices for creating static charts and graphs. They offer basic data visualization capabilities that are often enough for simple visualizations. In addition, you can use them to  clean, sort, and filter data. And both offer a range of chart types, graphing tools, and pivot tables for creating effective data visualizations. These charts are easy to manage; they update when the source data is updated, so they don’t require much manual intervention once implemented. 

Sheets and Excel are connected to other apps in their product suites. Google Docs and Slides are very similar to Microsoft Word and Powerpoint, for example. You can incorporate data visualizations from Sheets or Excel into reports and documents in Docs and Word. Presentation programs such as Slides and Powerpoint allow you to create engaging presentations that include data visualizations so you can share insights in a presentation format. Learn more about the power of this interconnectivity among Google tools in the article 
Link a chart, table, or slides to Google Docs or Slides


### Tableau

Tableau is used to create powerful and interactive visualizations, making it an excellent choice for data visualizations such as live dashboards. Tableau also makes it easy to create charts, graphs, and dashboards in a drag-and-drop interface. The application  supports a wide range of data sources and provides advanced analytics capabilities. These features allow for in-depth exploration of data trends and patterns. 

Tableau is particularly useful for creating visualizations using huge datasets, like in this 
World Happiness Report
 by Sustainable Development Solutions which uses global reporting data on different countries' happiness ratings. Likewise, this visualization of 
Population and Housing State Data
 from 2020 United States Census Data compares population rates in the United States and available housing. 

Tableau is widely known and used for its versatility and power, but it can take quite a bit of time to learn to use Tableau effectively. Soon, you’ll begin practicing with Tableau. But if you’d like to check it out now, there is a free environment you can access at 
Tableau Public. 


## Design compelling dashboards

Dashboards are powerful visual tools that help you tell your data story. A dashboard is a tool that monitors live, incoming data. It organizes information from multiple datasets into one central location, offering huge time savings. Data analysts use dashboards to track, analyze, and visualize data in order to answer questions and solve problems. 

![dashboards-pros](/Data%20Analytics/Ask%20Questions%20Data-driven%20Decisions/assets/dashboards-pros.png)


## Create a dashboard

1. Identify the stakeholders who need to see the data and how they will use it

2. Design the dashboard (what should be displayed)

Use these tips to help make your dashboard design clear and easy to follow:

* Use a clear header to label the information
* Add short text descriptions to each visualization
* Show the most important information at the top

3. Create mockups if desired

A mockup is a simple draft of a visualization used for planning a dashboard and evaluating its progress. This is optional, but a lot of data analysts like to sketch out their dashboards before creating them. 

4. Select the visualizations

You have a lot of options here. Which visualizations you select depends on the data story you are telling. If you need to show a change in values over time, line charts or bar graphs might be the best choice. If your goal is to show how each part contributes to the whole amount being reported, a pie or donut chart is probably a better choice. 

5. Create filters as needed

Filters show certain data while hiding the rest of the data in a dashboard. This can be a big help to identify patterns while keeping the original data intact. It’s common for data analysts to use and share the same dashboard, but manage their part of it with a filter. To dig deeper into filters and find an example of filters in action, visit Tableau’s page on Filter Actions. This is a useful resource to save and come back to when you start practicing using filters in Tableau on your own.