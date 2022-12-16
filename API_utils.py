"""
Author BeeNick
2022

Common functions for Flowers For Pollinators external databases's APIs

"""

import requests


def web_request_get_data(endpoint_url: str, parameters: dict, timeout: int = 5) -> list:
    """
    Request data from an url in a standard way for Flowers For Pollintators
    :param endpoint_url: endpoint for the request
    :param parameters: parameters for the request
    :return: return a list of status and content of the API request
    """

    if len(parameters.items()) > 0 :
        print(len(parameters.items()))
        print(f"Start new request to {endpoint_url}{parameters}")
        request = requests.get(endpoint_url,
                               params = parameters, timeout = timeout)
    else:
        print(f"Start new request to {endpoint_url}")
        request = requests.get(endpoint_url, timeout=timeout)

    print(f"End request")
    print(f"Status {request.status_code}")

    return([request.status_code, request.content])

def save_bin_data(binary_data: bytes, file_name: str):
    """
    Save binary data in a file
    """

    with open(file_name, 'wb') as file:
        file.write(binary_data)

    return

def get_external_db_data(file_name:str, endpoint_url: str, parameters: dict,
                         timeout: int = 5, force_download: bool=False,
                         save: bool=True) -> bytes:
    """
    Retrive data from external database, by default search the file, if not present make a new request and save it
    :param **parameters:
    :param file_name: name of the saved or to save file
    :param endpoint_url: endpoint for the request
    :param timeout: timeout for the API call
    :param force_download: by default the function search for the latest downloaded data, this parameter allow
            to force a new download of the data
    :param save: save the possibly downloaded data in a file
    :param parameters: parameters for the request
    :return: a binary with the requested information from the external db
    """

    return_binary = b''

    # By default the function make a new web request only if the default file do not exist

    if force_download:
        web_request_list = web_request_get_data(endpoint_url,
                                                parameters,
                                                timeout)
        if web_request_list[0] == 200:
            request_data = web_request_list[1]
            if save:
                save_bin_data(request_data, file_name)

    try:
        with open(file_name, 'rb') as saved_request_file:
            return_binary = saved_request_file.read()
    except:
        web_request_list = web_request_get_data(endpoint_url,
                                                parameters,
                                                timeout)

        if web_request_list[0] == 200:
            request_data = web_request_list[1]
            if save:
                save_bin_data(request_data, file_name)
            else:
                return request_data
        else:
            return return_binary
    finally:
        try:
            with open(file_name, 'rb') as saved_request_file:
                return_binary = saved_request_file.read()
        except:
            return b''

    return return_binary

