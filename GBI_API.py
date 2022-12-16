"""
Author BeeNick
2022

Script of functions for Global Biotic Interactions APIs
Github https://github.com/globalbioticinteractions/globalbioticinteractions
Repo https://github.com/globalbioticinteractions/globalbioticinteractions.git

"""

from API_utils import *


class GBIInteraction:
    """
    Class for Global Biotic Interactions APIs
    """

    def __init__(self):
        self.root_endpoint = "https://api.globalbioticinteractions.org/interaction"

    def request_data(self, source_taxa: str, interaction_type: str, format_type: str = 'csv',
                                      timeout: int = 5, **kwargs: object) -> list:
        """
        Request data from Global Biotic Interactions database
        :param source_taxa: the taxa we are intereste in
        :param interaction_type: the type of interaction of the taxa we are searching for
        :param format_type: the type of the resutls format, available are: csv, tsv, json, json.v2, dot
        :param timeout: timeout for the API call
        :param kwargs: dictionary of others parameters for the API call (as example offset)
        :return: return a list of status and content of the API request
        """

        parameters = {'sourceTaxon': source_taxa,
                      'interactionType': interaction_type,
                      'type': format_type}

        # Merge the basic parameters with the others eventual parameters
        parameters = {**parameters, **kwargs}

        search_by_interaction_request_list = web_request_get_data(root_endpoint,
                                                                  parameters,
                                                                  timeout)

        return search_by_interaction_request_list

    def get_bin_data(self, source_taxa: str, interaction_type: str, format_type: str = 'csv',
                     timeout: int = 5, force_download: bool = False, save: bool=True,
                     **kwargs: object) -> bytes:
        """
        Retrive binary data from Global Biotic Interactions database
        :param source_taxa: the taxa we are intereste in
        :param interaction_type: the type of interaction of the taxa we are searching for
        :param format_type: the type of the resutls format, available are: csv, tsv, json, json.v2, dot
        :param timeout: timeout for the API call
        :param force_download: by default the function search for the latest downloaded data, this parameter allow
                to force a new download of the data
        :param save: save the possibly downloaded data in a file
        :param kwargs: dictionary of others parameters for the API call (as example offset)
        :return: a binary file with the requested information from GBI
        """

        default_file_name = f"{interaction_type}_{source_taxa}_{format_type}.bin"

        parameters = {'sourceTaxon': source_taxa,
                      'interactionType': interaction_type,
                      'type': format_type}

        # Merge the basic parameters with the others eventual parameters
        parameters = {**parameters, **kwargs}

        return_binary_data = get_external_db_data(default_file_name, self.root_endpoint, parameters, timeout,
                                                  force_download)

        return return_binary_data







