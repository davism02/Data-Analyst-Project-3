
## Data-Analyst-Project-3

#Purpose
The purpose of this project is to anlyze the factors which impact salaries in the field of data analytics and to use this information to create a website to assist job seekers in their research.  

Background & General Info

It’s no secret that the novel coronavirus 2019 (COVID-19) outbreak is deeply affecting the lives of millions around the world, both directly and indirectly. The United States alone has shed nearly 10 million jobs in the past two weeks due to the COVID-19 shutdown.

However, surveys indicate that the data teams are long yet to see widespread layoffs or furloughs at this time, particularly among larger companies. So, strike at the jobs while it lasts?

We have created a website that precisely helps people look for data analyst jobs nationwide. Our website lets users get whole picture of data analysts job openings nationwide, including size of employer, location, industry and estimated salary range.


## Data sources:
For our website, we used data analyst job postings dataset from Kaggle, which contains data of salary estimate, location, company rating, job description and more for job in the United States. Our dataset had more than 2000 rows and 16 columns. While going through our data we were able to decide that we will do visualizations around job opening by location, employer's size and estimated range of salary.


## Application:
Python (Jupyter Notebook, Pandas)
JavaScript Libraries (Plotly, Leaflet)
HTML/ CSS
Excel

## DATA SET:
This data set is taken from Kaggle where and it is Scrapped from GlassDoor platform which is famous for it employment service.  There are 2253 jobs and 15 job positn fields in the dataset.  
The data has these features 
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company Name
* Location
* Headquarters
* Size
* Founded
* Type of ownership
* Industry
* Sector
* Revenue
* Competitors
* Easy Apply
## DATA CLEANING:
[Cleaning Data jupyter Notebook](https://github.com/davism02/Data-Analyst-Project-3/blob/main/ETL/data_cleaning.ipynb)
In this stage of project cleaned data and made specific changes like 
* Simplified the **Job Title** into a smaller version of it.
* Made salary feature by removing these **Glassdoor Estimate** and **k or $** for fitting it to a mdoel.
* Took the length of the description instead of taking the description as the whole.
* Made **Level** feature to describe the seniority of the job position.
* Created **Min salary** and **Max salary** feature to better understand the data
* Created a Avg Salary feature which we will use in prediction.
* And made many more changes which can be viewed in the DA Cleaned data csv.

##  Exploratory Data Analysis(EDA):
[Exploring Data jupyer Notebook](https://github.com/davism02/Data-Analyst-Project-3/blob/main/ETL/analyzing_df_all.ipynb)
We were interested in relationships of salaries based on  job titles, locations, and sectors.  We segmented the data based on job title. 
Performed Exploratory Data Analysis on the cleaned data and got a lot of insights, few of them are 

![Top Hiring Locations](Website/Job Location with their Salary range.png)
![Job Skill](Website/job_title_skill_us.png)
![Correlation Matrix](Website/resultmatrix.png)

There is a high correlation between SQL and Python, Tableau and SQL and Pyton an Tableau. There is also a high correlation with these skills and average salary. 



## [Webpage](https://davism02.github.io/Data-Analyst-Project-3/Website/index.html)


