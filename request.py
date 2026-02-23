import requests
from setup import var1 #url import ho gha
response = requests.get(var1)
request_status=response.status_code
response_data=response.text


if request_status==200:
    print("Website Open Successfully!")
else:
    print("Not Open",request_status)

print(response_data)#This gives all raw data of html
print(request_status)# this gives server response

""" form bs4 import Beautiful_soup
soup=Beautiful_soup(response_data,"html.parser") """
from bs4 import BeautifulSoup   # ✔ spelling sahi
soup = BeautifulSoup(response_data, "html.parser")   # ✔ parser ka naam sahi
#print(soup.title.text)#Website title
for h1 in soup.find_all("h1"):
         print(h1.text)
# Shows all h1 headers
print(soup.get_text()[:300])#shows only first 300 characters
job_blocks=soup.find_all("div", class_="job_card")# class aik specific  keyword hota hai directly access nai hota so why we used _
if job_blocks:
      print("job found:",len(job_blocks))

for job in job_blocks:
    # Find tags
    job_title_tag = job.find("h2", class_="job_title")
    company_tag = job.find("div", class_="company_name")
    location_tag = job.find("span", class_="location")
    city_tag = job.find("span", class_="city")
    link_tag = job.find("a", href=True)

    # Safe extraction with if/else
    if job_title_tag:
        job_title = job_title_tag.get_text(strip=True)
    else:
        job_title = "Not Found"

    if company_tag:
        company_name = company_tag.get_text(strip=True)
    else:
        company_name = "Not Found"

    if location_tag:
        location = location_tag.get_text(strip=True)
    else:
        location = "Not Found"

    if city_tag:
        city = city_tag.get_text(strip=True)
    else:
        city = "Not Found"

    if link_tag:
        job_link = link_tag["href"]
    else:
        job_link = "Not Found"

    # Print results
    print("Title:", job_title)
    print("Company:", company_name)
    print("Location:", location)
    print("City:", city)
    print("Link:", job_link)
    print("-" * 40)
    #we also use try excep instead of if else to handle this error
import csv

# Open file in append mode
with open("jobs.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Example loop
    for job in job_blocks:
        try:
            job_title = job.find("h2", class_="job_title")
        except:
            job_title = "Not Found"

        try:
            company_name = job.find("div", class_="company_name")
        except:
            company_name = "Not Found"

        try:
            city = job.find("span", class_="city")
        except:
            city = "Not Found"

        try:
            job_link = job.find("a", href=True)
        except:
            job_link = "Not Found"

        # Write one row to CSV
        writer.writerow([job_title, company_name, city, job_link])