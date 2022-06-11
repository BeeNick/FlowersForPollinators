"""
Author BeeNick
2022

Global Biotic Interactions APIs's calls tests
Github https://github.com/globalbioticinteractions/globalbioticinteractions
Repo https://github.com/globalbioticinteractions/globalbioticinteractions.git

"""
from urllib import request
import requests 


###Search by intercation type
#Set base endpoint
root_endpoint = "https://api.globalbioticinteractions.org/interaction"
#Set a taxa of interest
source_taxa = "Gossypium herbaceum herbaceum"
#Set an interaction of interest
interaction = "ecologicallyRelatedTo"
#Make the API call
search_by_interaction_request = requests.get(f'{root_endpoint}?sourceTaxon={source_taxa}&interactionType={interaction}')

print( search_by_interaction_request.status_code )

print( search_by_interaction_request.content )

