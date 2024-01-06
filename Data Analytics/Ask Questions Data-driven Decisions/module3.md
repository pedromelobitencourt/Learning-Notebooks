# Work with spreadsheets

## Spreadsheets tasks

What to do after you have all the data

* Organize your data
    * Pivot table (well organized and very organized)
        * Sorting and filtering data: focus only on the datka you need

* Calculate your data
    * Formulas
    * Functions

## Spreadsheets and the data life cycle

* **Plan** for the users who will work within a spreadsheet by developing organizational standards. This can mean formatting your cells, the headings you choose to highlight, the color scheme, and the way you order your data points. When you take the time to set these standards, you will improve communication, ensure consistency, and help people be more efficient with their time.

* **Capture** data by the source by connecting spreadsheets to other data sources, such as an online survey application or a database. This data will automatically be updated in the spreadsheet. That way, the information is always as current and accurate as possible.

* **Manage** different kinds of data with a spreadsheet. This can involve storing, organizing, filtering, and updating information. Spreadsheets also let you decide who can access the data, how the information is shared, and how to keep your data safe and secure. 

* **Analyze** data in a spreadsheet to help make better decisions. Some of the most common spreadsheet analysis tools include formulas to aggregate data or create reports, and pivot tables for clear, easy-to-understand visuals. 

* **Archive** any spreadsheet that you don’t use often, but might need to reference later with built-in tools. This is especially useful if you want to store historical data before it gets updated. 

* **Destroy** your spreadsheet when you are certain that you will never need it again, if you have better backup copies, or for legal or security reasons. Keep in mind, lots of businesses are required to follow certain rules or have measures in place to make sure data is destroyed properly.	


### Open Data Sources Online

* World Bank

* World Health Organization

* Google Public Data Explorer

* U.S Census Bureau


# Formulas in the spreadsheets

You start a formula with "=" sign in the cell that you want the calculation

* +: Addition
* -: Subtraction
* *: Multiplication
* /: Division

**Cell reference:** a cell or a range of cells in a worksheet that can be used in formula

* Contain the letter of the column and the number of the row

* VLOOKUP: seaches for a certain value in a column to return a corresponding piece of information

## Errors and fixes

* #DIV/0!: a formula is trying to divide a value in a cell by 0 or by an empty cell
    * Solution: 
        * =IFERROR function: =IFERROR(B4/A4, "some warning")

        ![div0-error](/Data%20Analytics/Ask%20Questions%20Data-driven%20Decisions/assets/div0-error.png)

* #ERROR: a formula can't be interpreted as input (also known as parsing error)
![error-error](/Data%20Analytics/Ask%20Questions%20Data-driven%20Decisions/assets/error-error.png)
    * Solution: missing comma (a delimiter) => =SUM(B2:B6, C2:C6)

* #N/A: data in formula can't be found by spreadsheet (data doesn't exist) -> It can occur when using functions such as VLOOKUP

* #NAME?: a formula or function name isn't understood

* #NUM!: a formula or function calculation can't be performed as specified

* #VALUE!: a general error that could indicate a problem with a formula or referenced cells

* #REF!: a formula is referencing a cell that is no longer valid or has been removed


# Functions in the spreadsheets

Preset command that automatically performs a specific process or task using data 

**Ranges:** B2:E2 -> It includes cells from B2 to E2

* SUM: We can separate by a comma to sum more cells or range of cells

* AVERAGE

* COUNT

* MAX

* MIN


# Save time with structured thinking

It's very important to define the problem before solving it

* Problem-domain: the specific area of analysis that encompasses every activity affecting or affected by the problem

**Structured thinking:** it's the process of recognizing the current problem or situation, organizing available information, revealing gaps and opportunities, and identifying the options

**Scope of Work:** an agreed-upon outline of the work you're going to perform on a project, such as: work details, reports and schedules

If you have missed any variable, it's recommended to redo your work, since it can lead to inaccurate conclusions


**Milestones** are significant tasks that will confirm along your timeline to help everyone know the project is on track

**Reports** notify everyone as you finalize deliverables and meet milestones

**Timelines** include due dates for when deliverables, milestones and/or reports are due

**Deliverables** are items or tasks you will complete before you can finish the project