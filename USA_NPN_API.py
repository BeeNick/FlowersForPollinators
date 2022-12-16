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

from API_utils import *

class USANPNData:
    """
    Class for USA National Phenology Network database API
    """

    def __init__(self):
        self.species_root_endpoint = "http://www.usanpn.org/npn_portal/species/getSpecies"

    def request_species_data(self, format_type: str = 'json', timeout: int = 5) -> list:
        """
        Request species data from USA National Phenology Network database
        :param format_type: the type of the resutls format, available are: json, xml
        :param timeout: timeout for the API call
        :return: returs a list of status and content of the API request
        """
        parameters = {}

        species_request_list = web_request_get_data(f"{species_root_endpoint}.{format_type}",
                                                    parameters, timeout)

        return species_request_list

    def get_bin_species_data(self, format_type: str = 'json', timeout: int =5,
                             force_download: bool = False, save: bool=True) -> bytes:
        """
        Download data fron USA National Phenology Network database
        :param format_type: the type of the resutls format, available are: json, xml
        :param timeout: timeout for the API call
        :return: returs a list of status and content of the API request
        """

        default_file_name = f"All_species_{format_type}.bin"

        parameters = {}

        return_binary_data = get_external_db_data(default_file_name,
                                                  f"{self.species_root_endpoint}.{format_type}",
                                                  parameters, timeout,
                                                  force_download, save)

        return return_binary_data


