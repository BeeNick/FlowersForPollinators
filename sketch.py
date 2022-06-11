"""
Author BeeNick
2022

Global Biotic Interactions APIs's calls tests
Github https://github.com/globalbioticinteractions/globalbioticinteractions
Repo https://github.com/globalbioticinteractions/globalbioticinteractions.git

"""
import requests
from GBI_API import *

###Search by intercation type
#Set base endpoint
root_endpoint = "https://api.globalbioticinteractions.org/interaction"
#Set a taxa of interest
source_taxa = "Gossypium herbaceum herbaceum"
#Set an interaction of interest
interaction = "ecologicallyRelatedTo"
#Set format type, allowed: csv, tsv, json, json.v2, dot
format_type = 'csv'
#Make the API call
search_by_interaction_request = requests.get(root_endpoint,
        params = {'sourceTaxon' : source_taxa,
                  'interactionType' : interaction,
                  'type' : format_type})

print( search_by_interaction_request.status_code )

open('test_search_by_interaction_request.csv', 'wb').write(search_by_interaction_request.content)

search_by_interaction_list = download_GBI_interactions_data(source_taxa,
                                                            interaction,
                                                            format_type)
#Status
print(search_by_interaction_list[0])

#Check
print('results match? ' , search_by_interaction_list[1] == search_by_interaction_request.content )