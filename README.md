# German Railway Delay & Reliability Analytics

## Phase 1 --- Data Analyst Project

> **Goal:** Analyze real Deutsche Bahn railway data to understand
> delays, punctuality, reliability, and operational patterns using
> Python, SQL, PostgreSQL, and Power BI.

------------------------------------------------------------------------

## 1. Project Overview

This project analyzes real railway data from Deutsche Bahn to answer
practical business questions about train punctuality and service
reliability.

The project starts as a **Data Analyst portfolio project**.

Later, the same project can be extended into a **Data Engineering /
Real-Time Data Platform**.

### Project progression

``` text
PHASE 1 — DATA ANALYST
DB API
   ↓
Python / Pandas
   ↓
Data Cleaning
   ↓
PostgreSQL
   ↓
SQL Analysis
   ↓
Power BI
   ↓
Business Insights

PHASE 2 — DATA ENGINEERING
API Automation
   ↓
ETL / ELT
   ↓
dbt
   ↓
Data Quality Tests
   ↓
Docker
   ↓
Cloud

PHASE 3 — REAL-TIME
Real-Time API / GTFS-RT
   ↓
Kafka
   ↓
Streaming Pipeline
   ↓
Monitoring
   ↓
Cloud Data Platform
```

------------------------------------------------------------------------

# 2. Business Problem

Railway delays affect passengers, connections, railway operators, and
transportation planning.

The objective of this project is to use real data to understand:

-   How often trains are delayed
-   How severe delays are
-   Which stations experience more delays
-   Which times of day have more delays
-   How punctuality changes by train type
-   How reliability differs between weekdays and weekends
-   How often cancellations or operational disruptions occur

The analysis should focus on **evidence from the data**, rather than
assumptions.

------------------------------------------------------------------------

# 3. Main Business Questions

The project should answer the following questions.

### Punctuality

1.  What percentage of trains are on time?
2.  What is the average delay?
3.  What is the median delay?
4.  What percentage of trains are delayed by more than 5, 10, or 15
    minutes?

### Time

5.  Which hours of the day have the highest average delays?
6.  Are delays different during morning and evening peak hours?
7.  Are weekends more or less punctual than weekdays?

### Stations

8.  Which stations have the highest average delays?
9.  Which stations have the highest percentage of delayed trains?
10. Are some stations consistently associated with larger delays?

### Train Types

11. How does punctuality differ between ICE, IC, RE, and other available
    train categories?
12. Which train categories experience the largest delays?

### Reliability

13. Which stations or services are the most reliable?
14. How frequently do cancellations occur?
15. How does railway performance change over time?

------------------------------------------------------------------------

# 4. Important Definitions

Before analyzing the data, define the metrics clearly.

### On-time

For this project, initially define a train as **on time** when:

``` text
delay < 5 minutes
```

This definition can later be changed and tested.

### Delayed

``` text
delay >= 5 minutes
```

### Severely delayed

Initially:

``` text
delay >= 15 minutes
```

These thresholds are project definitions for analysis. Document any
changes in the methodology.

------------------------------------------------------------------------

# 5. Key Performance Indicators (KPIs)

The Power BI dashboard should eventually contain:

  KPI                 Description
  ------------------- ---------------------------------------------
  Total Trips         Number of train observations
  Average Delay       Mean delay in minutes
  Median Delay        Median delay in minutes
  On-Time %           Percentage below the chosen delay threshold
  Delayed %           Percentage above the chosen delay threshold
  Severe Delay %      Percentage with delay \>= 15 minutes
  Cancellation Rate   Percentage of cancelled services
  Stations Analyzed   Number of stations
  Train Types         Number of train categories

------------------------------------------------------------------------

# 6. Data Source

The primary source for Phase 1 is the **official Deutsche Bahn API**.

Deutsche Bahn Developer Portal:

https://developers.deutschebahn.com/

Timetables API:

https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables

The project should use real DB data and document:

-   API/source name
-   Collection date
-   API endpoint used
-   Parameters
-   Data fields
-   Any limitations
-   Data transformation steps

### Important

Never commit API credentials to GitHub.

Do NOT put API keys directly inside Python files.

Use environment variables instead:

``` text
DB_CLIENT_ID=your_client_id
DB_API_KEY=your_api_key
```

Add your `.env` file to `.gitignore`.

------------------------------------------------------------------------

# 7. Technology Stack

## Programming

-   Python
-   Pandas
-   NumPy

## Database

-   PostgreSQL
-   SQL

## Visualization

-   Power BI
-   Matplotlib
-   Seaborn or Plotly (optional)

## Development

-   Jupyter Notebook
-   VS Code
-   Git
-   GitHub

## Future phases

-   dbt
-   pytest
-   Docker
-   Kafka
-   AWS / Azure
-   Data quality monitoring

------------------------------------------------------------------------

# 8. Recommended Project Structure

Create the project with the following structure:

``` text
german-railway-analytics/
│
├── README.md
├── .gitignore
├── requirements.txt
├── .env.example
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_exploration.ipynb
│   ├── 03_data_cleaning.ipynb
│   └── 04_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_cleaning.py
│   └── analysis.py
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_exploration.sql
│   ├── 03_kpis.sql
│   └── 04_analysis.sql
│
├── dashboard/
│   └── railway_dashboard.pbix
│
├── docs/
│   ├── data_dictionary.md
│   └── methodology.md
│
└── tests/
    └── test_data_quality.py
```

------------------------------------------------------------------------

# 9. Phase 1 Workflow

## Step 1 --- Define the business problem

Document:

-   Business objective
-   Stakeholders/users
-   Questions to answer
-   KPIs
-   Definitions

Do this before writing analysis code.

------------------------------------------------------------------------

## Step 2 --- Understand the API

Study:

-   Authentication
-   Endpoints
-   Request parameters
-   Response format
-   Rate limits
-   Error responses
-   Available fields

Create a small test request before collecting large amounts of data.

------------------------------------------------------------------------

## Step 3 --- Collect a Small Sample

Do NOT start by downloading a huge amount of data.

First collect a small sample from one or a few stations.

Example workflow:

``` text
API
 ↓
Request
 ↓
JSON response
 ↓
Inspect structure
 ↓
Pandas DataFrame
```

The first objective is to understand the data.

------------------------------------------------------------------------

# 10. Data Exploration

Before cleaning the data, investigate it.

Questions to answer:

-   How many rows are there?
-   How many columns?
-   What are the data types?
-   Which columns contain missing values?
-   Are there duplicate records?
-   What values exist for train type?
-   What values exist for station?
-   Are timestamps consistent?
-   Are delays negative?
-   Are there cancelled services?
-   Are there unexpected values?

Useful Pandas commands:

``` python
df.head()
df.shape
df.info()
df.describe()
df.isna().sum()
df.duplicated().sum()
df.nunique()
```

Do not clean the data blindly.

First understand it.

------------------------------------------------------------------------

# 11. Data Cleaning

Typical cleaning tasks may include:

-   Convert timestamps to datetime
-   Standardize column names
-   Handle missing values
-   Remove invalid records
-   Remove unintended duplicates
-   Convert delay values to numeric
-   Standardize train categories
-   Validate station identifiers
-   Create useful derived columns

Example:

``` text
scheduled_time
actual_time

        ↓

delay_minutes
```

Then create analytical fields such as:

``` text
date
year
month
weekday
hour
is_weekend
is_delayed
is_severely_delayed
```

------------------------------------------------------------------------

# 12. Data Quality Checks

Even in the Data Analyst phase, perform basic data-quality checks.

Examples:

### Missing values

``` python
df.isna().sum()
```

### Duplicate records

``` python
df.duplicated().sum()
```

### Invalid delays

Check for:

``` text
NULL
unexpected negative values
extremely large values
incorrect data types
```

### Timestamp validation

Check:

``` text
scheduled_time
actual_time
timezone
date consistency
```

Document every important cleaning decision.

------------------------------------------------------------------------

# 13. PostgreSQL Data Model

After cleaning, load the data into PostgreSQL.

A simple first model could contain:

### trips

``` text
trip_id
train_number
train_type
service_date
```

### stations

``` text
station_id
station_name
```

### trip_stops

``` text
trip_id
station_id
scheduled_arrival
actual_arrival
scheduled_departure
actual_departure
arrival_delay_minutes
departure_delay_minutes
cancelled
```

This structure can later be improved during the Data Engineering phase.

------------------------------------------------------------------------

# 14. SQL Analysis

Use SQL to answer business questions.

Examples:

### Average delay

``` sql
SELECT
    AVG(arrival_delay_minutes) AS avg_delay
FROM trip_stops;
```

### Delay by station

``` sql
SELECT
    station_id,
    AVG(arrival_delay_minutes) AS avg_delay
FROM trip_stops
GROUP BY station_id
ORDER BY avg_delay DESC;
```

### Delay by hour

``` sql
SELECT
    EXTRACT(HOUR FROM scheduled_arrival) AS hour,
    AVG(arrival_delay_minutes) AS avg_delay
FROM trip_stops
GROUP BY hour
ORDER BY hour;
```

### On-time percentage

``` sql
SELECT
    100.0 * AVG(
        CASE
            WHEN arrival_delay_minutes < 5 THEN 1
            ELSE 0
        END
    ) AS on_time_percentage
FROM trip_stops;
```

The exact SQL will depend on the final database schema.

------------------------------------------------------------------------

# 15. Python Analysis

Use Python/Pandas for deeper exploration and visualization.

Possible analyses:

``` text
Delay distribution
Delay by hour
Delay by weekday
Delay by station
Delay by train type
Cancellation patterns
Daily trends
Weekly trends
Outlier analysis
```

Example:

``` python
df.groupby("train_type")["delay_minutes"].mean()
```

------------------------------------------------------------------------

# 16. Power BI Dashboard

Create a dashboard called:

# German Railway Reliability Dashboard

### Page 1 --- Executive Overview

KPIs:

``` text
Average Delay
On-Time %
Delayed %
Cancellation Rate
Total Trips
```

Charts:

-   Delay trend over time
-   Delay distribution
-   Delay by train type

------------------------------------------------------------------------

### Page 2 --- Station Analysis

Visuals:

-   Average delay by station
-   Delayed percentage by station
-   Station volume
-   Station trend

Add filters for:

``` text
Date
Station
Train Type
Weekday
Hour
```

------------------------------------------------------------------------

### Page 3 --- Time Analysis

Visuals:

-   Delay by hour
-   Delay by weekday
-   Morning vs evening
-   Daily/weekly trend

------------------------------------------------------------------------

# 17. Business Insights

Do not simply create charts.

Every important visualization should lead to an observation.

Example:

``` text
Observation:
Average delay increases during the evening period.

Evidence:
The average delay between 17:00–20:00 is higher than during
the early afternoon.

Possible explanation:
Further investigation is required. The analysis should not
assume the cause without supporting data.
```

Separate:

``` text
FACT
from
INTERPRETATION
from
HYPOTHESIS
```

This is an important Data Analyst skill.

------------------------------------------------------------------------

# 18. Portfolio Requirements

The final GitHub repository should demonstrate:

### Technical skills

-   Python
-   Pandas
-   SQL
-   PostgreSQL
-   Data cleaning
-   Data validation
-   Data visualization
-   Power BI
-   Git/GitHub

### Analytical skills

-   Business-question definition
-   KPI design
-   Exploratory Data Analysis
-   Statistical thinking
-   Trend analysis
-   Segmentation
-   Data storytelling
-   Business recommendations based on evidence

------------------------------------------------------------------------

# 19. Git Workflow

Use Git from the beginning.

Example:

``` bash
git init

git add .

git commit -m "Initial project structure"

git branch -M main

git remote add origin <YOUR_GITHUB_REPOSITORY>

git push -u origin main
```

Use meaningful commits:

``` text
Add project structure
Add DB API client
Add initial data exploration
Clean timestamp fields
Add delay calculations
Create PostgreSQL schema
Add SQL KPI queries
Create Power BI dashboard
Update project documentation
```

------------------------------------------------------------------------

# 20. Environment Setup

Create a virtual environment:

``` bash
python -m venv .venv
```

Activate it.

### Windows

``` bash
.venv\Scripts\activate
```

### Linux / macOS

``` bash
source .venv/bin/activate
```

Install packages:

``` bash
pip install pandas numpy requests sqlalchemy psycopg2-binary jupyter matplotlib plotly python-dotenv
```

Save dependencies:

``` bash
pip freeze > requirements.txt
```

------------------------------------------------------------------------

# 21. Environment Variables

Create:

``` text
.env
```

Example:

``` text
DB_CLIENT_ID=your_client_id
DB_API_KEY=your_api_key
```

Create:

``` text
.env.example
```

with:

``` text
DB_CLIENT_ID=
DB_API_KEY=
```

Never commit `.env`.

Your `.gitignore` should include:

``` text
.env
.venv/
__pycache__/
*.pyc
```

------------------------------------------------------------------------

# 22. Data Privacy and Responsible Use

Use the official API according to its terms and rate limits.

Do not expose:

-   API credentials
-   Personal information
-   Private credentials
-   Access tokens

Document the source and collection date.

If the API data changes over time, record the date/time when the data
was collected.

------------------------------------------------------------------------

# 23. Definition of Done --- Phase 1

Phase 1 is complete when:

-   [ ] Project repository created
-   [ ] DB API access configured
-   [ ] Small real dataset collected
-   [ ] Data structure documented
-   [ ] Data dictionary created
-   [ ] Data quality issues identified
-   [ ] Data cleaned with Python
-   [ ] Clean data loaded into PostgreSQL
-   [ ] SQL analysis completed
-   [ ] KPIs calculated
-   [ ] Python analysis completed
-   [ ] Power BI dashboard created
-   [ ] Business insights documented
-   [ ] README updated
-   [ ] GitHub repository organized
-   [ ] Project can be explained in an interview

------------------------------------------------------------------------

# 24. Interview Preparation

Be able to explain:

### Business

> What problem were you solving?

### Data

> Where did the data come from?

### Python

> How did you clean and transform the data?

### SQL

> How did you calculate the KPIs?

### Data Quality

> How did you identify invalid or missing records?

### Visualization

> Why did you choose these charts?

### Business Insight

> What did the data tell you?

### Limitations

> What cannot your analysis prove?

### Future Development

> How would you turn this into a real-time data engineering platform?

The last question connects Phase 1 directly to Phase 2.

------------------------------------------------------------------------

# 25. Future Development

After completing Phase 1, extend the project.

## Phase 2 --- Data Engineering

``` text
DB API
 ↓
Automated ingestion
 ↓
Raw data storage
 ↓
ETL / ELT
 ↓
PostgreSQL
 ↓
dbt
 ↓
Data quality tests
 ↓
Automated pipeline
```

Potential technologies:

-   Python
-   PostgreSQL
-   dbt
-   Airflow
-   Docker
-   pytest
-   GitHub Actions

## Phase 3 --- Real-Time Data Engineering

``` text
DB / GTFS-RT
 ↓
Kafka
 ↓
Streaming processing
 ↓
Real-time database
 ↓
Monitoring
 ↓
Dashboard
```

Potential technologies:

-   Kafka
-   Spark/Flink
-   AWS/Azure
-   Docker
-   Prometheus/Grafana

------------------------------------------------------------------------

# 26. Learning Strategy

Do not try to learn every technology before starting.

Learn each tool when the project requires it.

Recommended order:

``` text
1. Python basics
       ↓
2. Pandas
       ↓
3. Data cleaning
       ↓
4. SQL
       ↓
5. PostgreSQL
       ↓
6. Exploratory Data Analysis
       ↓
7. Power BI
       ↓
8. Git/GitHub
       ↓
9. Data quality
       ↓
10. Data Engineering
```

The objective is not to collect tools.

The objective is to demonstrate that you can take:

``` text
RAW DATA
   ↓
CLEAN DATA
   ↓
ANALYSIS
   ↓
INSIGHT
   ↓
BUSINESS DECISION SUPPORT
```

------------------------------------------------------------------------

# 27. First Task

Start small.

### Task 01

1.  Create the GitHub repository.
2.  Create the folder structure.
3.  Create a Python virtual environment.
4.  Create `.gitignore`.
5.  Create `.env.example`.
6.  Register for Deutsche Bahn API access.
7.  Make one test API request.
8.  Save the raw response locally.
9.  Open the response and understand its structure.
10. Do not start Power BI or PostgreSQL yet.

### First milestone

``` text
Can I retrieve real Deutsche Bahn data
and explain what every important field means?
```

Once that is achieved, move to **data exploration and cleaning**.

------------------------------------------------------------------------

## Project Principle

> **Understand the data before analyzing the data.**
>
> **Understand the business question before building the dashboard.**
>
> **Never claim an insight that the data cannot support.**
