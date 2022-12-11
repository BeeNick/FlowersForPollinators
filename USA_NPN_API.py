"""
Author BeeNick
2022

USA NPN APIs's calls tests
Script of functions for USA NPN APIs's call semplification

USA National Phenology Network
Website https://usanpn.org/data/overview
Github https://github.com/usa-npn/

Advanced Phenology Information System (APIS)
NASA Repo https://git.earthdata.nasa.gov/projects/APIS

"""

import requests



def download_USA_NPN_species( format_type = 'json', timeout = 5):
    """
       Download data fron USA National Phenology Network database
       :param format_type: the type of the resutls format, available are: json, xml
       :param timeout: timeout for the API call
       :return: returs a list of status and content of the API request
    """

    root_endpoint = "http://www.usanpn.org/npn_portal/species/getSpecies"

    species_request = requests.get(f"{root_endpoint}.{format_type}", timeout = timeout)

    return([species_request.status_code, species_request.content])