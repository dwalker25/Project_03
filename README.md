# Project_03

## Ebay Scraper Overview
This program "scrapes" the data from Ebay webpages to identify the following 6 given parameters for each search result: `name`, `free returns`, `items sold`, `status`, `price`, and `shipping`. The program uses the following libraries: `argparse`, `requests`, `Beautiful Soup`, and `json`. The program uses `argparse` to obtain the user input for the Ebay search term and number of webpages, `requests` to obtain web data from the specified URL, `Beautiful Soup` to process the web data, and `json` to write the formatted data output to a new JSON file. 

## How to Use the Command Line
There are two operations that the user can control from the command line.
First, the user can specify their desired search term to obtain information from Ebay. For example, the user may be interested in searching the keyword "hammer" to analyze the products available. The user should enter "hammer" at the end fo the **ebay-dl.py** file path, as shown below:
```
$ python3 ebay-dl.py "plush bear"
```

#### This program was designed from a [course project](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03). 
