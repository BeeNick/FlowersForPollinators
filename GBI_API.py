"""
Author BeeNick
2022

Script of functions for Global Biotic Interactions APIs
Github https://github.com/globalbioticinteractions/globalbioticinteractions
Repo https://github.com/globalbioticinteractions/globalbioticinteractions.git

"""

import requests
import pandas

def download_GBI_interactions_data(source_taxa, interaction_type, format_type = 'csv', \
                              timeout = 5, **kwargs):
    """
    Download data fron Global Biotic Interactions database
    :param source_taxa: the taxa we are intereste in
    :param interaction_type: the type of interaction of the taxa we are searching for
    :param format_type: the type of the resutls format, available are: csv, tsv, json, json.v2, dot
    :param timeout: timeout for the API call
    :param kwargs: dictionary of others parameters for the API call (as example offset)
    :return: returs a list of status and content of the API request
    """

    # Set base endpoint for GBI data
    root_endpoint = "https://api.globalbioticinteractions.org/interaction"
    # Set basic parameters
    parameters = {'sourceTaxon' : source_taxa, \
                  'interactionType' : interaction_type, \
                  'type' : format_type}
    # Merge the basic parameters with the others eventual parameters
    parameters = {**parameters, **kwargs}

    search_by_interaction_request = requests.get(root_endpoint, \
                                    params = parameters, timeout = timeout)

    return([search_by_interaction_request.status_code, search_by_interaction_request.content])


