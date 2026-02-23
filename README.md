

 Project Overview
Ye project ek **web scraping tool** hai jo HTML parsing ke zariye job postings extract karta hai. BeautifulSoup library use karke job title, company name, location, aur job link collect kiye jate hain aur phir CSV file mein store kiye jate hain.

 Features
- **HTML Parsing**: BeautifulSoup se raw HTML ko structured format mein convert karna.  
- **Job Blocks Extraction**: Specific HTML tags aur classes identify karke multiple job postings ek list mein store karna.  
- **Looping Through Jobs**: For loop ke zariye har job block process karna.  
- **Data Extraction**: Har job ke liye variables banake job title, company, city/location, aur job link extract karna.  
- **Error Handling**: Try/Except ka use karke missing data handle karna taake program crash na ho.  
- **CSV Storage**: Extracted data ko row‑wise `jobs.csv` file mein save karna.

 Workflow
1. **Fetch HTML Response**  
   Website se HTML content fetch karna.  
2. **Parse HTML**  
   BeautifulSoup se HTML parse karna.  
3. **Find Job Blocks**  
   `find_all()` se job postings ke div blocks identify karna.  
4. **Extract Job Data**  
   Har job ke liye title, company, location, aur link variables mein store karna.  
5. **Error Handling**  
   Agar koi field missing ho to `"Not Found"` assign karna.  
6. **Save to CSV**  
   Har job ek nayi row ke form mein `jobs.csv` file mein likhna.

---

 Example Output (CSV)
```
Job Title,Company,City,Link
Software Engineer,ABC Corp,Lahore,http://example.com/job1
Data Analyst,XYZ Ltd,Karachi,http://example.com/job2
```

---

 Requirements
- Python 3.x  
- Libraries: `requests`, `beautifulsoup4`, `csv`

 How to Run
```bash
pip install requests beautifulsoup4
python scraper.py
```

---

  

