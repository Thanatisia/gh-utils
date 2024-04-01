"""
GitHub: Mass repository clone
"""
import os
import sys
from subprocess import PIPE, Popen

def error_env_not_set(error_topic, env_var_str):
    """
    Error message: Environment Variable not set
    """
    err_msg = "{} is not set in the Environment Variable '{}', please set before proceeeding.".format(error_topic, env_var_str)
    print(err_msg)
    exit(1)

def main():
    # Initialize Variables

    ## Get Environment Variables
    if os.getenv("REPO_AUTHOR") != None:
        REPO_AUTHOR = os.getenv("REPO_AUTHOR")
    else:
        error_env_not_set("Main repository author", "REPO_AUTHOR")

    ## Security
    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

    ## Remote Git Repository Server
    GIT_REMOTE_REPO_SERVER_PROTOCOL="https"
    GIT_REMOTE_REPO_SERVER_DOMAIN="github.com"
    GIT_REMOTE_REPO_SERVER_URL="{}://{}".format(GIT_REMOTE_REPO_SERVER_PROTOCOL, GIT_REMOTE_REPO_SERVER_DOMAIN)

    ## Repository records
    REPO_NAMES_DB_FILE_PATH="docs/records"
    REPO_NAMES_DB_FILE_NAME="all-repos.txt"
    REPO_NAMES_DB_FILE="{}/{}".format(REPO_NAMES_DB_FILE_PATH, REPO_NAMES_DB_FILE_NAME)

    ## Local Repository directory
    REPO_DIR="repos/{}".format(REPO_AUTHOR) # Repository storage directory
    PUBLIC_REPO_DIR="{}/Public".format(REPO_DIR)
    PRIVATE_REPO_DIR="{}/Private".format(REPO_DIR)
    REPO_EXPORT_LOGS_FILE_PATH="docs/exports"
    REPO_EXPORT_LOGS_FILE_NAME="exports.log"
    REPO_EXPORT_LOGS_FILE="{}/{}".format(REPO_EXPORT_LOGS_FILE_PATH, REPO_EXPORT_LOGS_FILE_NAME)

    # Read the repository names file into an array
    repositories=[]
    file_contents = {
        "public" : "",
        "private" : "",
        "forks" : ""
    }
    line = ""
    with open(REPO_NAMES_DB_FILE, "r+") as read_file:
        # Read content into list
        repositories = read_file.readlines()

        # Close file after usage
        read_file.close()

    # Cleanup and sanitize repositories list
    tmp_list = []
    for i in range(len(repositories)):
        # Get current entry
        curr_entry = repositories[i]

        # Strip all special characters from the sides
        sanitized_entry = curr_entry.strip()

        # Check if is newline
        if len(curr_entry) > 0:
            tmp_list.append(sanitized_entry)
    repositories = tmp_list

    # Open export logs file to write to during the cloning process
    with open(REPO_EXPORT_LOGS_FILE, "a+") as export_logs:
        # Initialize Variables
        curr_repo_type = "Public"

        # Iterate through repositories list
        for i in range(len(repositories)):
            # Get current repository
            curr_repo_name = repositories[i]

            # Check if is comment
            if '#' in curr_repo_name:
                # Is a comment
                print("[{}] is a comment".format(curr_repo_name))

                header = curr_repo_name.split('#')[1].strip()
                print("Header: {}".format(header))

                # Check if header contains 'Public', 'Private' or 'Fork'
                if 'Public' in header:
                    # Public Repositories
                    curr_repo_type = "Public"
                elif 'Private' in header:
                    # Private Repositories
                    curr_repo_type = "Private"
                elif 'Fork' in header:
                    # Forked Repositories
                    curr_repo_type = "Fork"
            else:
                # Not a comment
                # Check if there are any repositories
                if len(curr_repo_name) > 0:
                    # Repository found

                    # Format repository URL
                    curr_repo_url="{}/{}".format(GIT_REMOTE_REPO_SERVER_URL, curr_repo_name)

                    # Check repository type
                    match curr_repo_type:
                        case "Public":
                            REPO_DIR += "/Public"
                        case "Private":
                            REPO_DIR += "/Private"
                            # Set API Token
                            # Check if API Token is set
                            if GITHUB_API_TOKEN == None:
                                # Not set
                                error_env_not_set("GitHub API Token/Key", "GITHUB_API_TOKEN")
                            curr_repo_url="{}://{}@{}/{}".format(GIT_REMOTE_REPO_SERVER_PROTOCOL, GITHUB_API_TOKEN, GIT_REMOTE_REPO_SERVER_DOMAIN, curr_repo_name)
                        case "Fork":
                            REPO_DIR += "/Forks"

                    # Check if current author folder exists
                    if not (os.path.isdir(REPO_DIR)):
                        # Directory does not exist
                        # Create directory for the current author
                        os.makedirs(REPO_DIR)

                    # Clone the github repo
                    print("Cloning current repository: {}".format(curr_repo_url))
                    cmd_str = "git -C {} clone {}".format(REPO_DIR, curr_repo_url)
                    print("Command: {}".format(cmd_str.split()))
                    proc = Popen(cmd_str.split(), stdout=PIPE)
                    stdout = proc.communicate()[0].decode("utf-8")
                    res_code = proc.stdout
                    print("Standard Output: {}".format(stdout))

                    # Write repository URL to logs
                    export_logs.write("{} : {}".format(i, curr_repo_url))

            # Reset
            REPO_DIR = "repos/{}".format(REPO_AUTHOR)

            # Newline
            print("")

        # Close file after usage
        export_logs.close()


