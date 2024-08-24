# CannaResearch

CannaResearch is a Python-based project designed to scrape and analyze research articles from various online sources such as PubMed, Google Scholar, and specialized journals related to your search queries. The project uses web scraping techniques to extract article titles and relevant information, making it easier to gather data for research purposes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Scrape Titles:** Extract titles from PubMed, Google Scholar, and other research journals.
- **Multi-Source Search:** Perform searches across multiple platforms with a single query.
- **Customizable Output:** Modify the number of results displayed and the sources queried.
- **Selenium Integration:** Automate browser interactions for websites that require JavaScript execution.

### Installation

```bash
git clone https://github.com/tomemme/cannaResearch.git
cd cannaResearch
```

## Usage
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python resTest.py   # call code
>Enter the search query: 
```
![GUI](https://github.com/tomemme/cannaResearch/blob/main/ResearchResult.PNG)

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

-Fork the project
-Create your feature branch (git checkout -b feature/my-new-feature)
-Commit your changes (git commit -am 'Add some feature')
-Push to the branch (git push origin feature/my-new-feature)
-Create a new Pull Request