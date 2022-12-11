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
# Set base endpoint
root_endpoint = "https://api.globalbioticinteractions.org/interaction"
# Set a taxa of interest
source_taxa = "Gossypium herbaceum herbaceum"
# Set an interaction of interest
interaction = "ecologicallyRelatedTo"
# Set format type, allowed: csv, tsv, json, json.v2, dot
format_type = 'csv'
# Set default file name
default_file_name = f"{interaction}_{source_taxa}_{format_type}.bin"
# Make the API call
search_by_interaction_request = requests.get(root_endpoint,
                                             params={'sourceTaxon': source_taxa,
                                                     'interactionType': interaction,
                                                     'type': format_type})

print(search_by_interaction_request.status_code)

open('test_search_by_interaction_request.csv', 'wb').write(search_by_interaction_request.content)

gbi_interaction = GBIInteraction()

search_by_interaction_file = gbi_interaction.get_bin_data(source_taxa,
                                                          interaction,
                                                          format_type,
                                                          force_download=False)

# Check
print(f"New request results match? {search_by_interaction_file == search_by_interaction_request.content}")

with open(default_file_name, 'rb') as saved_request_file:
    return_file = saved_request_file.read()

    print(f"Read file results match? {search_by_interaction_file == return_file}")
