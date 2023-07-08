# Scrapo
## Github Scraper



Web scraper to get defails of watchers and stargazers of the given repo
Details fetched
- Github nick name
- real name
- number of followers 
- account URL

> Sort accounts in descending order


## Tech

Github scraper uses the following technologies

- [Python] - 
- [Beautiful Soup] - Library for HTML web scraping


## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies

```sh
pip install requests
pip install html5lib
pip install bs4
pip install argparse
```



## Usage

Open your favorite Terminal and run these commands.

- Either run the .exe file inside scripts folder (Windows)
```sh
scrapo --url https://github.com/dotnet/Scaffolding --peopleType stargazers --outfile "results.csv"
```

Run through following commands:

```sh
python main.py --url https://example.com --peopleType [watchers/stargazers] --outfile [output CSV file path]
```

### Sample Commands
```sh
python main.py  --url https://github.com/dotnet/Scaffolding --peopleType stargazers
```



