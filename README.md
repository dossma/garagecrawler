# garagecrawler
Bot which searches real estate websites for mentions of "garage".

It uses a real estate agency network as a starting ground for searching approximately 200 real estate agencies in the Berlin-Brandenburg area of Germany.

## Motivation
Find real estate agencies which offer garages within their portfolio or actual offers of houses/apartments with a garage.
It is useful if you are looking to buy, rent or sell a garage or if you want to find a housing offer which includes a garage.
Furthermore, it can be used as a lead aggregator in case such information may be of interest for your business.  

## Procedure and setup
The bot is designed for going through subpages of the agencies where it can expect offers or descriptions of the real estate agencies portfolio.  
It is then looking for the keyword `garage` mentioned in these sites. 

## Result
The essential information you get is the `target_url` entries as here is where the `garage` keyword was found.  

The following data is being summarized into a `csv` spreadsheet:
- crawling depth
- referer url
- referred url (`target_url`)
- domain of referred url

## Usability
Generally, the bot can easily be modified for other searches. For that, the search keyword or phrase as well as the start hub aggregator can be exchanged for your desired aim. 

## Get started
After the development setup has been established (see below), go to the `spiders` directory and run with

`scrapy runspider garagecrawler.py`

The result will be saved under `garagecrawl-result.csv`

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
