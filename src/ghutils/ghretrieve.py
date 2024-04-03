"""
Backup/Archive your full list of your Public/Private repositories using the GitHub API

:: Dependencies
- json
- requests
- subprocess
"""
import os
import sys
import json
import requests
from subprocess import Popen, PIPE

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

def send_get_request(url, headers, other_parameters={}):
    """
    Send a HTTP REST API GET request to the specified URL and return the results as a response

    :: Params
    - url: Specify the server URL you wish to send the GET request to
        + Type: String

    - headers: Specify the header to parse into the GET request
        + Type: Dictionary
        + Format: `headers={"header-name" : "header-value"}`
        - Examples
            + "Authorization: Bearer [API KEY]" : `headers={"Authorization" : "Bearer [API-KEY]"}`

    - other_parameters : Specify a dictionary object containing other parameters you wish to parse into the GET request
        + Type: Dictionary
        + Default: {} (Empty Dictionary)
    """
    # Send a HTTP REST API GET request and return the results as a response
    response = requests.get(url, headers=headers, **other_parameters)

    # Obtain GET request response text
    response_text = response.text
    response_json = response.json()

    # Close response after usage
    response.close()

    # Output
    return [response_text, response_json]

def gh_search_by_token(gh_api_token="", curr_page_number=1, maximum_repo=100, repository_type="public"):
    """
    Search and return a list of all repositories according to a provided GitHub API Token

    :: Params
    - gh_api_token : Specify the target GitHub API Token to search with
        + Type: String
        + Default: ""

    - curr_page_number: Specify the current page number of the repository search results to download
        + Type: Integer
        + Default: 1

    - maximum_repo: Specify the maximum number of repositories to display per page
        + Type: Integer
        + Default: 100

    - repository_type: Specify the target repository type you wish to search for (public|private)
        + Type: String
        + Default: public
        - Possible Values
            + public
            + private

    :: Return
    - returned_repositories : List of repositories returned that corresponds/belongs to the provided Github API Token
        + Type: List
    """
    # Initialize Variables
    returned_repositories = [] # List of repositories returned that corresponds/belongs to the provided Github API Token

    # Curl the repositories list and output to a JSON file
    if gh_api_token != "":
        # Send a HTTP REST API GET request to GitHub API and return the results as a response
        response_text, response_json = send_get_request(
            "https://api.github.com/user/repos?type={}&per_page={}&page={}".format(repository_type, maximum_repo, curr_page_number),
            headers={"Authorization" : "Bearer {}".format(gh_api_token)}
        )

        # Substitute
        returned_repositories = response_json

    # Output
    return returned_repositories

def obtain_repo_json(output_json_file="output.json", curr_page_number=1, maximum_repo=100, repository_type="public"):
    """
    Curl and obtain your public repositories in the form of a JSON data serizalition object file

    :: Params
    - output_json_file: Specify the name of the output JSON file containing the repository contents returned from GitHub API
        + Type: String
        + Default: output.json

    - curr_page_number: Specify the current page number of the repository search results to download
        + Type: Integer
        + Default: 1

    - maximum_repo: Specify the maximum number of repositories to display per page
        + Type: Integer
        + Default: 100

    - repository_type: Specify the target repository type you wish to search for (public|private)
        + Type: String
        + Default: public
        - Possible Values
            + public
            + private
    """
    # Initialize Variables

    # Curl the repositories list and output to a JSON file
    if GITHUB_API_TOKEN != None:
        # Check if JSON file exists
        if not (os.path.isfile(output_json_file)):
            # Send a HTTP REST API GET request to GitHub API and return the results as a response
            response_json = gh_search_by_token(GITHUB_API_TOKEN, curr_page_number, maximum_repo, repository_type)

            # Write to output file
            with open(output_json_file, "w+") as export_output_JSON_file:
                # Write JSON
                json.dump(response_json, export_output_JSON_file)

                # Close file after usage
                export_output_JSON_file.close()
        else:
            print("JSON File {} exists".format(output_json_file))
    else:
        print("Your GitHub API Token/Secret Key is not set in the Environment Variable 'GITHUB_API_TOKEN', please set before proceeding.")
        exit(1)

def obtain_public_repo_json(output_json_file="output-public.json", curr_page_number=1, maximum_pages=100):
    """
    Curl and obtain your public repositories in the form of a JSON data serizalition object file
    """
    # Initialize Variables

    # Curl the repositories list and output to a JSON file
    if GITHUB_API_TOKEN != None:
        # Check if JSON file exists
        if not (os.path.isfile(output_json_file)):
            # Send a HTTP REST API GET request to GitHub API and return the results as a response
            response = requests.get("https://api.github.com/user/repos?type=public&per_page={}&page={}".format(maximum_pages, curr_page_number), headers={"Authorization" : "Bearer {}".format(GITHUB_API_TOKEN)})

            # Obtain GET request response text
            response_text = response.text

            # Close response after usage
            response.close()

            # Write to output file
            with open(output_json_file, "w+") as export_output_JSON_file:
                # Write JSON
                export_output_JSON_file.write(response_text)

                # Close file after usage
                export_output_JSON_file.close()
        else:
            print("JSON File {} exists".format(output_json_file))
    else:
        print("Your GitHub API Token/Secret Key is not set in the Environment Variable 'GITHUB_API_TOKEN', please set before proceeding.")
        exit(1)

def obtain_private_repo_json(output_json_file="output-private.json", curr_page_number=1, maximum_pages=100):
    """
    Curl and obtain your public repositories in the form of a JSON data serizalition object file
    """
    # Check if GitHub API token is provided
    if GITHUB_API_TOKEN != None:
        # Check if JSON file exists
        if not (os.path.isfile(output_json_file)):
            # Send a HTTP REST API GET request to GitHub API and return the results as a response
            response = requests.get("https://api.github.com/user/repos?type=private&per_page={}&page={}".format(maximum_pages, curr_page_number), headers={"Authorization" : "Bearer {}".format(GITHUB_API_TOKEN)})

            # Obtain GET request response text
            response_text = response.text

            # Close response after usage
            response.close()

            # Write to output file
            with open(output_json_file, "a+") as export_output_JSON_file:
                # Write JSON
                export_output_JSON_file.write(response_text)

                # Close file after usage
                export_output_JSON_file.close()
        else:
            print("JSON File {} exists".format(output_json_file))
    else:
        print("Your GitHub API Token/Secret Key is not set in the Environment Variable 'GITHUB_API_TOKEN', please set before proceeding.")
        exit(1)

def export_repo_filenames(output_filename="repositories.txt", output_repositories_json_Public="output-public.json", output_repositories_json_Private="output-private.json"):
    """
    Parse JSON log files into jq and export the filenames without string quotes
    """
    # Initialize Variables
    public_json_Contents = {}
    private_json_Contents = {}

    # Open the repository list file
    with open(output_filename, "w+") as repository_list:
        # cat output-public.json | jq -r '.[].full_name' >> ${output_filenames}

        # Check if the public repositories JSON list exists
        if os.path.isfile(output_repositories_json_Public):
            # Initialize Variables

            # Open the Public repository JSON file and import into dictionary
            with open(output_repositories_json_Public, "r+") as read_public_json:
                # Load the JSON contents of the Public repository list into the dictionary object; Each entry of the list is 1 project information in a dictionary
                public_json_Contents = json.load(read_public_json)

                # Close file after usage
                read_public_json.close()
        else:
            print("Public repositories JSON file [{}] does not exist.".format(output_repositories_json_Public))

        # Check if the private repositories JSON list exists
        if os.path.isfile(output_repositories_json_Private):
            # Initialize Variables

            # Open the Public repository JSON file and import into dictionary
            with open(output_repositories_json_Private, "r+") as read_private_json:
                # Load the JSON contents of the Public repository list into the dictionary object; Each entry of the list is 1 project information in a dictionary
                private_json_Contents = json.load(read_private_json)

                # Close file after usage
                read_private_json.close()
        else:
            print("Private repositories JSON file [{}] does not exist.".format(output_repositories_json_Private))

        # Write repository type header
        repository_list.write("# Public")

        # Write a newline between repository type header and repository
        repository_list.write("\n")

        # Obtain Public repository filenames from dictionary
        print("Public JSON Contents: {}".format(public_json_Contents))

        # Output Public repositories to the list
        for i in range(len(public_json_Contents)):
            # Get current project information
            curr_project = public_json_Contents[i]

            # DEBUG: Iterate through project information
            for k,v in curr_project.items():
                print("{} = {}".format(k,v))

            # Obtain full name
            repo_full_name = curr_project["full_name"]

            # Write repository full name to repository list
            repository_list.write(repo_full_name)
            repository_list.write("\n")

            print("")

        print("")

        # Write a newline between repository type header
        repository_list.write("\n")

        # Write a new repository type headeer
        repository_list.write("# Private")

        # Write a newline between repository type header and repository
        repository_list.write("\n")

        # Obtain Private repository filenames from dictionary
        print("Private JSON Contents: {}".format(private_json_Contents))

        # Output Private repositories to the list
        for i in range(len(private_json_Contents)):
            # Get current project information
            curr_project = private_json_Contents[i]

            # DEBUG: Iterate through project information
            for k,v in curr_project.items():
                print("{} = {}".format(k,v))

            # Obtain full name
            repo_full_name = curr_project["full_name"]

            # Write repository full name to repository list
            repository_list.write(repo_full_name)
            repository_list.write("\n")

            print("")

        # Close file after usage
        repository_list.close()


def main():
    obtain_repo_json(output_json_file="output-public.json", repository_type="public")
    obtain_repo_json(output_json_file="output-private.json", repository_type="private")
    export_repo_filenames()

if __name__ == "__main__":
    main()

