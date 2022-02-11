# Reddit title reader

## Introduction

The following script opens up a virtual version of the chrome browser, scrolls trough the given url and reads all titles of a given html class and finally stores the titles in a .csv. This repository includes two scripts:

- **reddit-extractor.py** which extracts the data from a given url
- **succession-analysis.ipynb**, an example of how to use the script. In this case I used the reddit-extractor to get titles of a very popular reddit thread [r/SuccessionTV](https://www.reddit.com/r/SuccessionTV/) based on a HBO tv series and counted which character is mentioned the most in the post titles of the sub-reddit.

## Usage

### Insert custom url to extract data from
For this you will have to open **reddit-extractor.py** and
1. Replace the url in `driver.get("https://www.reddit.com/r/SuccessionTV/top/?t=all")` to your url
2. Also replace the html tags in `titles = soup.find_all("h3",class_="_eYtD2XCVieq6emjKBH3m")` to the correspoding tags you want to extract. (Inspect the html tags in the browser for example)
3. Run code again and it should print you a .csv for the post titles you choose to extract.



``
