
#### version 1
import requests
from bs4 import BeautifulSoup

# Define your search query
search_query = "cannabis tricomes"

# Send an HTTP GET request to Google Scholar
url = f"https://scholar.google.com/scholar?q={search_query}"


response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the titles of the search results
results = soup.find_all("h3", class_="gs_rt")
for result in results:
    print(result.get_text())

#####version2
# import requests
# from bs4 import BeautifulSoup

# # Define a list of URLs to search
# search_urls = [
#     "https://pubmed.ncbi.nlm.nih.gov/",
#     "https://jcannabisresearch.biomedcentral.com/",
#     "https://scholar.google.com/scholar?q=",
#     "https://academic.oup.com/journals",
#     "https://www.jstor.org/"
# ]

# # Define your search query
# search_query = "cannabis research"

# # Iterate through the list of URLs
# for url in search_urls:
#     print(f"Searching {url} for '{search_query}'")

#     # Send an HTTP GET request to the current URL
#     response = requests.get(url)

#     # Parse the HTML response
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract and print the titles of the search results based on the website's structure
#     if "pubmed.ncbi.nlm.nih.gov/" in url:
#         results = soup.find_all("h3")
#         for result in results:
#             print(result.get_text())
#     elif "biomedcentral.com" in url:
#         results = soup.find_all("h2", class_="c-teaser__title")
#         for result in results:
#             print(result.get_text())
#     elif "scholar.google.com" in url:
#         results = soup.find_all("h3", class_="gs_rt")
#         for result in results:
#             print(result.get_text(),
#                   print('here'))
#     # Add more elif blocks for other websites as needed

#     # Add a separator between search results from different URLs
#     print("\n" + "="*50 + "\n")

