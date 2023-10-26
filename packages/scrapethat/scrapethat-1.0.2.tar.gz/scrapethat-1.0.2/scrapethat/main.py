from bs4 import BeautifulSoup
import requests
import pandas as pd
import cloudscraper

def read_html(link):
    """
    Read and parse HTML content from a given link.

    Args:
        link (str): The URL to fetch HTML from.

    Returns:
        BeautifulSoup: Parsed HTML content.
    """
    response = requests.get(link)
    return (BeautifulSoup(response.text, 'html'))

def read_cloud(link):
    """
    Read and parse HTML content using a CloudScraper instance.

    Args:
        link (str): The URL to fetch HTML from.

    Returns:
        BeautifulSoup: Parsed HTML content.
    """
    scraper = cloudscraper.create_scraper()
    response = scraper.get(link)
    return (BeautifulSoup(response.text, 'html'))

def get_texts(link_nodes):
    """
    Extract text content from a list of HTML link nodes.

    Args:
        link_nodes (list): List of HTML link nodes.

    Returns:
        list: Extracted text content.
    """
    return ([x.text for x in link_nodes])

def strip_texts(my_texts):
    """
    Strip leading and trailing whitespaces from a list of text strings.

    Args:
        my_texts (list): List of text strings.

    Returns:
        list: Text strings with leading and trailing spaces removed.
    """
    return ([x.strip() for x in my_texts])

def get_links(link_nodes):
    """
    Extract href attributes from a list of HTML link nodes.

    Args:
        link_nodes (list): List of HTML link nodes.

    Returns:
        list: List of href attributes.
    """
    return ([x['href'] for x in link_nodes])

def paste0(base_link, numbers):
    """
    Concatenate a base link with a list of numbers to create new links.

    Args:
        base_link (str): Base URL.
        numbers (list): List of numbers to concatenate.

    Returns:
        list: List of concatenated URLs.
    """
    return ([f'{base_link}{s}' for s in numbers])

def fromjson(link):
    """
    Fetch JSON data from a given link.

    Args:
        link (str): The URL to fetch JSON data from.

    Returns:
        dict: Parsed JSON data.
    """
    response = requests.get(link)
    return (response.json())

