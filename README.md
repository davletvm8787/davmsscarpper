
**JobScrapper** is a simple, yet comprehensive, job scraping library.


## Features

- Scrapes job postings from **Kimeta**, **Indeed**, **Glassdoor**, **Google**, & **ZipRecruiter** simultaneously
- Aggregates the job postings in a dataframe
- Proxies support to bypass blocking


### Installation

```
pip install -U python-jobspy
```

_Python version >= [3.10](https://www.python.org/downloads/release/python-3100/) required_

### Usage

```python
import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "kimeta", "zip_recruiter", "glassdoor", "google"],
    search_term="software engineer",
    google_search_term="software engineer jobs near San Francisco, CA since yesterday",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,
    country_indeed='USA',
    
    # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel
```

### Output

```
SITE           TITLE                             COMPANY           CITY          STATE  JOB_TYPE  INTERVAL  MIN_AMOUNT  MAX_AMOUNT  JOB_URL                                            DESCRIPTION
indeed         Software Engineer                 AMERICAN SYSTEMS  Arlington     VA     None      yearly    200000      150000      https://www.indeed.com/viewjob?jk=5e409e577046...  THIS POSITION COMES WITH A 10K SIGNING BONUS!...
indeed         Senior Software Engineer          TherapyNotes.com  Philadelphia  PA     fulltime  yearly    135000      110000      https://www.indeed.com/viewjob?jk=da39574a40cb...  About Us TherapyNotes is the national leader i...
linkedin       Software Engineer - Early Career  Lockheed Martin   Sunnyvale     CA     fulltime  yearly    None        None        https://www.linkedin.com/jobs/view/3693012711      Description:By bringing together people that u...
linkedin       Full-Stack Software Engineer      Rain              New York      NY     fulltime  yearly    None        None        https://www.linkedin.com/jobs/view/3696158877      Rain’s mission is to create the fastest and ea...
zip_recruiter Software Engineer - New Grad       ZipRecruiter      Santa Monica  CA     fulltime  yearly    130000      150000      https://www.ziprecruiter.com/jobs/ziprecruiter...  We offer a hybrid work environment. Most US-ba...
zip_recruiter Software Developer                 TEKsystems        Phoenix       AZ     fulltime  hourly    65          75          https://www.ziprecruiter.com/jobs/teksystems-0...  Top Skills' Details• 6 years of Java developme...
```

### Parameters for `scrape_jobs()`

```plaintext
Optional
├── site_name (list|str): 
|    linkedin, zip_recruiter, indeed, glassdoor, google
|    (default is all)
│
├── search_term (str)
|
├── google_search_term (str)
|     search term for google jobs. This is the only param for filtering google jobs.
│
├── location (str)
│
├── distance (int): 
|    in miles, default 50
│
├── job_type (str): 
|    fulltime, parttime, internship, contract
│
├── proxies (list): 
|    in format ['user:pass@host:port', 'localhost']
|    each job board scraper will round robin through the proxies
|
├── is_remote (bool)
│
├── results_wanted (int): 
|    number of job results to retrieve for each site specified in 'site_name'
│
├── easy_apply (bool): 
|    filters for jobs that are hosted on the job board site (LinkedIn easy apply filter no longer works)
│
├── description_format (str): 
|    markdown, html (Format type of the job descriptions. Default is markdown.)
│
├── offset (int): 
|    starts the search from an offset (e.g. 25 will start the search from the 25th result)
│
├── hours_old (int): 
|    filters jobs by the number of hours since the job was posted 
|    (ZipRecruiter and Glassdoor round up to next day.)
│
├── verbose (int) {0, 1, 2}: 
|    Controls the verbosity of the runtime printouts 
|    (0 prints only errors, 1 is errors+warnings, 2 is all logs. Default is 2.)

├── linkedin_fetch_description (bool): 
|    fetches full description and direct job url for LinkedIn (Increases requests by O(n))
│
├── linkedin_company_ids (list[int]): 
|    searches for linkedin jobs with specific company ids
|
├── country_indeed (str): 
|    filters the country on Indeed & Glassdoor (see below for correct spelling)
|
├── enforce_annual_salary (bool): 
|    converts wages to annual salary
|
├── ca_cert (str)
|    path to CA Certificate file for proxies
```

```
├── Indeed limitations:
|    Only one from this list can be used in a search:
|    - hours_old
|    - job_type & is_remote
|    - easy_apply
│
└── LinkedIn limitations:
|    Only one from this list can be used in a search:
|    - hours_old
|    - easy_apply
```

## Supported Countries for Job Searching

### **Kimeta**

LinkedIn searches globally & uses only the `location` parameter. 

### **ZipRecruiter**

ZipRecruiter searches for jobs in **US/Canada** & uses only the `location` parameter.

### **Indeed / Glassdoor**

Indeed & Glassdoor supports most countries, but the `country_indeed` parameter is required. Additionally, use the `location`
parameter to narrow down the location, e.g. city & state if necessary. 

You can specify the following countries when searching on Indeed (use the exact name, * indicates support for Glassdoor):

|                      |              |            |                |
|----------------------|--------------|------------|----------------|
| Argentina            | Australia*   | Austria*   | Bahrain        |
| Belgium*             | Brazil*      | Canada*    | Chile          |
| China                | Colombia     | Costa Rica | Czech Republic |
| Denmark              | Ecuador      | Egypt      | Finland        |
| France*              | Germany*     | Greece     | Hong Kong*     |
| Hungary              | India*       | Indonesia  | Ireland*       |
| Israel               | Italy*       | Japan      | Kuwait         |
| Luxembourg           | Malaysia     | Mexico*    | Morocco        |
| Netherlands*         | New Zealand* | Nigeria    | Norway         |
| Oman                 | Pakistan     | Panama     | Peru           |
| Philippines          | Poland       | Portugal   | Qatar          |
| Romania              | Saudi Arabia | Singapore* | South Africa   |
| South Korea          | Spain*       | Sweden     | Switzerland*   |
| Taiwan               | Thailand     | Turkey     | Ukraine        |
| United Arab Emirates | UK*          | USA*       | Uruguay        |
| Venezuela            | Vietnam*     |            |                |


## Notes
* Indeed is the best scraper currently with no rate limiting.  
* All the job board endpoints are capped at around 1000 jobs on a given search.  
* LinkedIn is the most restrictive and usually rate limits around the 10th page with one ip. Proxies are a must basically.

## Frequently Asked Questions

---
**Q: Why is Indeed giving unrelated roles?**  
**A:** Indeed searches the description too.

- use - to remove words
- "" for exact match

Example of a good Indeed query

```py
search_term='"engineering intern" software summer (java OR python OR c++) 2025 -tax -marketing'
```

This searches the description/title and must include software, summer, 2025, one of the languages, engineering intern exactly, no tax, no marketing.

---

**Q: Received a response code 429?**  
**A:** This indicates that you have been blocked by the job board site for sending too many requests. All of the job board sites are aggressive with blocking. We recommend:

- Wait some time between scrapes (site-dependent).
- Try using the proxies param to change your IP address.

---

### JobPost Schema

```plaintext
JobPost
├── title
├── company
├── company_url
├── job_url
├── location
│   ├── country
│   ├── city
│   ├── state
├── description
├── job_type: fulltime, parttime, internship, contract
├── job_function
│   ├── interval: yearly, monthly, weekly, daily, hourly
│   ├── min_amount
│   ├── max_amount
│   ├── currency
│   └── salary_source: direct_data, description (parsed from posting)
├── date_posted
├── emails
└── is_remote

Linkedin specific
└── job_level

Linkedin & Indeed specific
└── company_industry

Indeed specific
├── company_country
├── company_addresses
├── company_employees_label
├── company_revenue_label
├── company_description
└── company_logo
```