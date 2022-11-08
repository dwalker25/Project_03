# Project_03

## Ebay Scraper Overview
This program "scrapes" the data from Ebay webpages to identify the following 6 given parameters for each search result: `name`, `free returns`, `items sold`, `status`, `price`, and `shipping`. The program uses the following libraries: `argparse`, `requests`, `Beautiful Soup`, and `json`. The program uses `argparse` to obtain the user input for the Ebay search term and number of webpages, `requests` to obtain web data from the specified URL, `Beautiful Soup` to process the web data, and `json` to write the formatted data output to a new JSON file. 

## How to Use the Command Line
There are two operations that the user can control from the command line.

### 1
First, the user must specify their desired search term to obtain information from Ebay. For example, the user may be interested in searching the keyword "charger" to analyze the products available. The user should enter "charger" at the end of the **ebay-dl.py** file path, as shown below:
```
$ python3 ebay-dl.py "charger"
```

Note: If the search term contains multiple words, the entire search term must be contained within quotes or else only the first word will be inputted. This is shown below:
```
$ python3 ebay-dl.py "plush bear"
```

### 2
Second, the user can optionally specify how many webpages they want to process. The default number is *10 webpages* of search results. However, perhaps the user is only interested in the *top 3 webpages* for "plush bear". The user should enter `--num_pages=3` in the command line, as shown below:
```
$ python3 ebay-dl.py "plush bear" --num_pages=3
```

## My Project
For my project, I generated 3 different JSON files (plush bear.json, christmas lights.json, cake.json) and uploaded them to this repository. I did not use the optional command of changing the number of webpages. Here are the commands I used to do so for each, respectively.

```
$ python3 ebay-dl.py "plush bear"

$ python3 ebay-dl.py "christmas lights"

$ python3 ebay-dl.py "cake"
```


#### This program was designed from a [course project](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03). 
