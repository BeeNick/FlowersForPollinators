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

# Test level
# INFO -> informative print
# DEBUG -> detailed print info

test_level = "INFO"

###All species's search
# Set base endpoint
root_endpoint = "http://www.usanpn.org/npn_portal/species/getSpecies"
# Set format type
format_type = 'json'
# Set default file name
default_file_name = f"All_species_{format_type}.bin"


species_request = requests.get(f"{root_endpoint}.{format_type}")

print(species_request.status_code)

open('test_species_request.json', 'wb').write(species_request.content)

usa_npn_data = USANPNData()

species_npn_data = usa_npn_data.get_bin_species_data(format_type,
                                                     force_download=False,
                                                     save=False)

#Check
print('results match? ' , species_npn_data == species_request.content )

# Check
print(f"New request results match possibily old saved? {species_npn_data == species_request.content}")

if test_level == "DEBUG":
    print(f"species_npn_data \n {species_npn_data} \n")
    print(f"species_request.content \n {species_request.content} \n")


species_npn_data = usa_npn_data.get_bin_species_data(format_type,
                                                          force_download=True,
                                                          save=False)


print(f"New request results match new not saved? {species_npn_data == species_request.content}")

if test_level == "DEBUG":
    print(f"species_npn_data \n {species_npn_data} \n")
    print(f"species_request.content \n {species_request.content} \n")

species_npn_data = usa_npn_data.get_bin_species_data(format_type,
                                                          force_download=True,
                                                          save=True)

print(f"New request results match new saved? {species_npn_data == species_request.content}")

if test_level == "DEBUG":
    print(f"species_npn_data \n {species_npn_data} \n")
    print(f"species_request.content \n {species_request.content} \n")

species_npn_data = usa_npn_data.get_bin_species_data(format_type,
                                                          force_download=False,
                                                          save=True)

print(f"New request results match saved? {species_npn_data == species_request.content}")

if test_level == "DEBUG":
    print(f"species_npn_data \n {species_npn_data} \n")
    print(f"species_request.content \n {species_request.content} \n")

with open(default_file_name, 'rb') as saved_request_file:
    return_file = saved_request_file.read()

    print(f"Read file results match? {species_npn_data == return_file}")

    if test_level == "DEBUG":
        print(f"species_npn_data \n {species_npn_data} \n")
        print(f"return_file \n {return_file} \n")
