import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the fake jobs page
URL = "https://realpython.github.io/fake-jobs"

# Create a connection to SQLite database
def create_database():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    # Create the jobs table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        job_description TEXT,
        application_link TEXT,
        UNIQUE(job_title, company_name, location)  -- Avoid duplicate jobs
    )
    ''')
    
    conn.commit()
    conn.close()

# Scrape job listings from the website
def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    
    for job_card in soup.find_all("div", class_="card-content"):
        job_title = job_card.find("h2", class_="title").text.strip()
        company_name = job_card.find("h3", class_="company").text.strip()
        location = job_card.find("p", class_="location").text.strip()

    

        # Handle missing description
        job_description_tag = job_card.find("div", class_="content")  # Fixed class name
        job_description = job_description_tag.text.strip() if job_description_tag else "No description available"

        # Handle missing application link
        application_link_tag = job_card.find("a", class_="card-footer-item")
        application_link = application_link_tag["href"] if application_link_tag else "No link available"
        
        job_listings.append((job_title, company_name, location, job_description, application_link))
    
    return job_listings

# Save jobs to the database with incremental updates
def save_jobs_to_db(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    for job in jobs:
        job_title, company_name, location, job_description, application_link = job
        
        # Check if the job already exists
        cursor.execute('''
        SELECT job_description, application_link FROM jobs 
        WHERE job_title=? AND company_name=? AND location=?
        ''', (job_title, company_name, location))
        
        existing_job = cursor.fetchone()
        
        if existing_job:
            # Update only if job description or application link has changed
            if existing_job != (job_description, application_link):
                cursor.execute('''
                UPDATE jobs 
                SET job_description=?, application_link=? 
                WHERE job_title=? AND company_name=? AND location=?
                ''', (job_description, application_link, job_title, company_name, location))
        else:
            # Insert new job
            cursor.execute('''
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ''', job)
    
    conn.commit()
    conn.close()

# Filter jobs based on location or company name
def filter_jobs(location=None, company_name=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    
    if location:
        query += " AND location=?"
        params.append(location)
    
    if company_name:
        query += " AND company_name=?"
        params.append(company_name)
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    
    conn.close()
    return results

# Export filtered results to CSV
def export_jobs_to_csv(jobs, filename="filtered_jobs.csv"):
    if not jobs:
        print("No jobs found to export.")
        return

    df = pd.DataFrame(jobs, columns=["ID", "Job Title", "Company Name", "Location", "Description", "Application Link"])
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

# Main function to run all steps
if __name__ == "__main__":
    print("Creating database...")
    create_database()
    
    print("Scraping jobs...")
    job_data = scrape_jobs()
    print(f"Scraped {len(job_data)} job listings.")
    
    print("Saving jobs to database...")
    save_jobs_to_db(job_data)
    print("Database updated.")

    print("Filtering jobs in 'Remote' location...")
    filtered_jobs = filter_jobs(location="Remote")
    
    if filtered_jobs:
        print(f"Exporting {len(filtered_jobs)} jobs to CSV...")
        export_jobs_to_csv(filtered_jobs)
    else:
        print("No jobs found for the given filter.")
