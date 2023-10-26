'''
File: urls.py
Author: Michael Lucky
Date: September 13, 2023
Description: Module to abstract the urls used in the company_scraper project, this will allow for easier maintenance, scalability, and integration. This module will be used as an interface for the urls to scrape from.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

# ONLY CHANGE THIS IF A URL IS NO LONGER VALID AND NEEDS TO BE UPDATED. COMPANY NAME CHANGES SHOULD BE DONE IN THE NAMES MODULE

import jelloow_names.names as n

def agency_websites() -> list[str]:
    
    urls = {}
    for name, agency in n.agency_names().items():
        for url in agency.get('website'):
            urls[f'{url}'] = name

    return urls

def agency_goodfirms() -> list[str]:

    urls = {}
    for name, agency in n.agency_names().items():
        for alias in agency.get('goodfirms'):
            urls[f'https://www.goodfirms.co/company/{alias}'] = name

    return urls

def agency_sortlist() -> dict[str, str]:

    urls = {}
    for name, agency in n.agency_names().items():
        for alias in agency.get('sortlist'):
            urls[f'https://www.sortlist.com/agency/{alias}'] = name
    
    return urls

def agency_linkedin() -> list[str]:

    urls = {}
    for name, agency in n.agency_names().items():
        for alias in agency.get('linkedin'):
            urls[f'https://www.linkedin.com/company/{alias}'] = name

    return urls

def agency_urls() -> list[str]:
    urls = {}
    urls.update(agency_websites())
    urls.update(agency_goodfirms())
    urls.update(agency_sortlist())
    urls.update(agency_linkedin())
    return urls

def brand_urls() -> list[str]:
    
    # currently used for testing purposes
    return ['https://www.jelloow.com']