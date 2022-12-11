"""
Author BeeNick
2022

USA NPN APIs's calls tests

USA National Phenology Network
Website https://usanpn.org/data/overview
Github https://github.com/usa-npn/

Advanced Phenology Information System (APIS)
NASA Repo https://git.earthdata.nasa.gov/projects/APIS

"""

from USA_NPN_API import *

species_request = requests.get("http://www.usanpn.org/npn_portal/species/getSpecies.json")

print(species_request.status_code)

open('species_request.json', 'wb').write(species_request.content)

species_request_list = download_USA_NPN_species()

#Status
print(species_request_list[0])

#Check
print('results match? ' , species_request_list[1] == species_request.content )