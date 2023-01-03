# garagecrawler
Bot which searches real estate websites for garage mentions.

It uses a real estate agency network as a starting ground for searching approximately 200 real estate agencies in the Berlin-Brandenburg area of Germany.

## Motivation
Find real estate agencies which offer garages within their portfolio or actual offers of houses/apartments with a garage.

## Procedure and setup
The bot is designed for going through subpages of the agencies where it can expect offers or descriptions of the real estate agencies portfolio.  
It is then looking for the keyword `garage` mentioned in these sites. 

## Result
The essential information you get is the `target_url` entries as here is where the `garage` keyword was found.  

The following data is being summarized into a `csv` spreadsheet:
- crawling depth
- referer url
- referred url (`target_url`)
- domain of `target_url`

## Usability
Generally, the bot can easily be modified for other searches. For that, the search keyword or phrase as well as the start hub aggregator can be exchanged for your desired aim. 

## Get started
After the development setup has been established (see below), go to the `spiders` directory and run with

`scrapy runspider garagecrawler.py`

The result will be saved under `garagecrawler-result.csv`

## Development setup
Required is
- Scrapy: https://github.com/scrapy/scrapy
- tldextract: https://github.com/john-kurkowski/tldextract

```sh
pip install scrapy
pip install tldextract
```

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)
