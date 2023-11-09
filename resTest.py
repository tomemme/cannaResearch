import requests
from bs4 import BeautifulSoup
from Bio import Entrez
from urllib.parse import quote

# Function to scrape titles from a given URL and search query
def scrape_titles(url, search_query):
    if "pubmed.ncbi.nlm.nih.gov" in url:
        # Encode the search query for PubMed
        print("------Pubmed")
        encoded_query = quote(search_query)

        # Provide your email address to comply with NCBI's usage policies
        Entrez.email = "swimaster22@gmail.com"

        # Perform the PubMed search using the encoded query
        handle = Entrez.esearch(db="pubmed", term=encoded_query)
        record = Entrez.read(handle)

        # Get the list of PubMed IDs
        pubmed_ids = record["IdList"]

        # Define the maximum number of results you want (5 in this case)
        max_results = 5

        # Fetch and print the PMID and TI for each PubMed ID, up to the maximum
        for i, pubmed_id in enumerate(pubmed_ids):
            if i >= max_results:
                break
            handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="medline", retmode="text")
            record = handle.read().splitlines()
            pmid = None
            title = None
            for line in record:
                if line.startswith("PMID"):
                    pmid = line.split("- ")[1]
                elif line.startswith("TI  - "):
                    title = line[6:]
                if pmid and title:
                    break
            if pmid and title:
                print(f"PMID: {pmid}")
                print(f"TI: {title}\n")

    elif "scholar.google.com" in url:
        # Send an HTTP GET request to Google Scholar
        print("------Scholar")
        url = f"https://scholar.google.com/scholar?q={search_query}"

        response = requests.get(url)

        # Define the maximum number of results you want (5 in this case)
        max_results = 1

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the titles of the search results
        results = soup.find_all("h3", class_="gs_rt")
        counter = 0
        for result in results:
            if counter > max_results:
                break
            counter = counter + 1
            print(result.get_text())
    
    #next journal and so on.
    elif "jcannabisresearch.biomedcentral.com" in url:
        # Send an HTTP GET request to the next URL
        print("------Jcannabis")
        url = f"https://jcannabisresearch.biomedcentral.com/articles?q={search_query}"
        response = requests.get(url)

        # Define the maximum number of results you want (adjust as needed)
        max_results = 2

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the titles of the search results
        results = soup.find_all("h3", class_="c-listing__title")
        counter = 0
        for result in results:
            if counter >= max_results:
                break
            title = result.get_text(strip=True)
            if title:
                print(title)
                counter += 1

    elif "academic.oup.com/journals" in url:
        # Send an HTTP GET request to the next URL
        print("------Academic")
        url = f"https://academic.oup.com/journals?q={search_query}"
        response = requests.get(url)

        # Define the maximum number of results you want (adjust as needed)
        max_results = 2

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the titles of the search results
        results = soup.find_all("h4", class_="sri-title customLink al-title at-sr-item-title-link")
        counter = 0
        for result in results:
            if counter >= max_results:
                break
            title = result.get_text(strip=True)
            if title:
                print(title)
                counter += 1

    #elif "www.jstor.org" in url:
        

# Example usage:
search_query = input("Enter the search query: ").strip()
urls_to_search = [
    "https://pubmed.ncbi.nlm.nih.gov/",
    "https://scholar.google.com/",
    "https://jcannabisresearch.biomedcentral.com/",
    "https://academic.oup.com/journals",
    "https://www.jstor.org/",
]

for url in urls_to_search:
    scrape_titles(url, search_query)
