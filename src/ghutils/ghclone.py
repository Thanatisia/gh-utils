"""
GitHub: Mass repository clone
"""
import os
import sys
from subprocess import PIPE, Popen

def error_env_not_set(error_topic, env_var_str, exit_flag=False):
    """
    Error message: Environment Variable not set

    :: Params
    - error_topic : The topic header and reason for error
        + Type: String

    - env_var_str : The target Environment Variable that was not set
        + Type: String

    - exit_flag: Flag to enable/disable automatic exit if function is called
        + Type: Boolean
        + Default: False
    """
    err_msg = "[-] {} is not set in the Environment Variable '{}', please set before proceeeding.".format(error_topic, env_var_str)
    print(err_msg)

    if exit_flag:
        exit(1)

def get_env_var():
    """
    Get Environment Variables
    """
    env_var = {
        # [Environment Variable] = { "description" : "summary", "value" : value }
        "REPO_AUTHOR" : { "description" : "Main Repository Author", "value" : None },
        "GIT_REMOTE_REPO_SERVER_PROTOCOL" : { "description" : "The Git Remote Repository Server domain protocol", "value" : None },
    }
    for env_var_name, env_var_mapping in env_var.items():
        # Get value of environment variable
        env_var_value = os.getenv(env_var_name)

        # Get header description of environment variable
        env_var_desc = env_var_mapping["description"]

        # Check if environment variable is found
        if env_var_value != None:
            env_var[env_var_name]["value"] = env_var_value
        else:
            error_env_not_set(env_var_desc, env_var_name)
    print("")

def main():
    # Initialize Variables

    # Get Environment Variables
    ## Security
    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

    ## Remote Git Repository Server
    GIT_REMOTE_REPO_SERVER_PROTOCOL = os.getenv("GIT_REMOTE_REPO_SERVER_PROTOCOL", "https")
    GIT_REMOTE_REPO_SERVER_DOMAIN = os.getenv("GIT_REMOTE_REPO_SERVER_DOMAIN", "github.com")

    ## Repository records
    REPO_NAMES_DB_FILE_PATH = os.getenv("REPO_NAMES_DB_FILE_PATH", "docs/records")
    REPO_NAMES_DB_FILE_NAME = os.getenv("REPO_NAMES_DB_FILE_NAME", "all-repos.txt")

    ## Local Repository directory
    REPO_DIR = os.getenv("REPO_DIR", "repos") # Repository storage directory
    REPO_EXPORT_LOGS_FILE_PATH = os.getenv("REPO_EXPORT_LOGS_FILE_PATH", "docs/exports") # Export logs filepath
    REPO_EXPORT_LOGS_FILE_NAME = os.getenv("REPO_EXPORT_LOGS_FILE_NAME", "exports.log")  # Export logs filename

    ## Format strings
    GIT_REMOTE_REPO_SERVER_URL="{}://{}".format(GIT_REMOTE_REPO_SERVER_PROTOCOL, GIT_REMOTE_REPO_SERVER_DOMAIN)
    REPO_NAMES_DB_FILE="{}/{}".format(REPO_NAMES_DB_FILE_PATH, REPO_NAMES_DB_FILE_NAME)
    PUBLIC_REPO_DIR="{}/Public".format(REPO_DIR)
    PRIVATE_REPO_DIR="{}/Private".format(REPO_DIR)
    REPO_EXPORT_LOGS_FILE="{}/{}".format(REPO_EXPORT_LOGS_FILE_PATH, REPO_EXPORT_LOGS_FILE_NAME)

    # Read the repository names file into an array
    repositories=[]
    file_contents = {
        "public" : "",
        "private" : "",
        "forks" : ""
    }
    cloned = {
        # List of repositories cloned
        # [author-name] : [ repositories, ... ]
    }

    # Check if current project structure exists
    project_structure = [ REPO_DIR, REPO_NAMES_DB_FILE_PATH, REPO_EXPORT_LOGS_FILE_PATH ]
    # Create project structure
    for curr_dir in project_structure:
        if not (os.path.isdir(curr_dir)):
            # Directory does not exist
            os.makedirs(curr_dir)

    # Check if repository list exists
    line = ""
    if os.path.isfile(REPO_NAMES_DB_FILE):
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

                        # Split current repository name into author and repository
                        curr_repo = curr_repo_name.split("/")
                        curr_repo_author = curr_repo[0]
                        curr_repo_pkg = curr_repo[1]

                        # Check if current author is in the dictionary
                        if not (curr_repo_author in cloned):
                            # Not in dictionary
                            # Initialize entry in clone list
                            cloned[curr_repo_author] = []

                        # Append entry to author list
                        cloned[curr_repo_author].append(curr_repo_pkg)

                        # Append the current author to the root/base directory
                        REPO_DIR += "/{}".format(curr_repo_author)

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
                        export_logs.write("{} : {}".format(i+1, curr_repo_url))

                        # Write a newline
                        export_logs.write("\n")

                # Reset
                REPO_DIR = "repos"

                # Newline
                print("")

            # Close file after usage
            export_logs.close()
    else:
        print("Repository List {} does not exist, please create one before proceeding".format(REPO_NAMES_DB_FILE))

