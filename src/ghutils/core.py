"""
GitHub Utilities - Core logic library/framework containing classes for each utilities
"""
import os
import sys
from subprocess import PIPE, Popen

class GitHubClone():
    def __init__(self, GIT_REPO_AUTHOR="",
                 GIT_REMOTE_REPO_SERVER_PROTOCOL="https", GIT_REMOTE_REPO_SERVER_DOMAIN="github.com",
                 REPO_NAMES_DB_FILE_PATH="docs/records", REPO_NAMES_DB_FILE_NAME="all-repos.txt",
                 REPO_DIR="repos",
                 REPO_EXPORT_LOGS_FILE_PATH="docs/exports", REPO_EXPORT_LOGS_FILE_NAME="exports.log"
                 ):
        """
        Class Constructor
        """
        # Initialize Variables
        # Get Environment Variables
        ## Security
        self.GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

        ## Remote Git Repository Server
        self.GIT_REMOTE_REPO_SERVER_PROTOCOL = os.getenv("GIT_REMOTE_REPO_SERVER_PROTOCOL", GIT_REMOTE_REPO_SERVER_PROTOCOL)
        self.GIT_REMOTE_REPO_SERVER_DOMAIN = os.getenv("GIT_REMOTE_REPO_SERVER_DOMAIN", GIT_REMOTE_REPO_SERVER_DOMAIN)

        ## Repository records
        self.REPO_NAMES_DB_FILE_PATH = os.getenv("REPO_NAMES_DB_FILE_PATH", REPO_NAMES_DB_FILE_PATH)
        self.REPO_NAMES_DB_FILE_NAME = os.getenv("REPO_NAMES_DB_FILE_NAME", REPO_NAMES_DB_FILE_NAME)

        ## Local Repository directory
        self.REPO_DIR = os.getenv("REPO_DIR", REPO_DIR) # Repository storage directory
        self.REPO_EXPORT_LOGS_FILE_PATH = os.getenv("REPO_EXPORT_LOGS_FILE_PATH", REPO_EXPORT_LOGS_FILE_PATH) # Export logs filepath
        self.REPO_EXPORT_LOGS_FILE_NAME = os.getenv("REPO_EXPORT_LOGS_FILE_NAME", REPO_EXPORT_LOGS_FILE_NAME)  # Export logs filename

        ## Format strings
        self.GIT_REMOTE_REPO_SERVER_URL="{}://{}".format(GIT_REMOTE_REPO_SERVER_PROTOCOL, GIT_REMOTE_REPO_SERVER_DOMAIN)
        self.REPO_NAMES_DB_FILE="{}/{}".format(REPO_NAMES_DB_FILE_PATH, REPO_NAMES_DB_FILE_NAME)
        self.PUBLIC_REPO_DIR="{}/Public".format(self.REPO_DIR)
        self.PRIVATE_REPO_DIR="{}/Private".format(self.REPO_DIR)
        self.REPO_EXPORT_LOGS_FILE="{}/{}".format(REPO_EXPORT_LOGS_FILE_PATH, REPO_EXPORT_LOGS_FILE_NAME)

        # Read the repository names file into an array
        self.repositories=[]
        self.file_contents = {
            "public" : "",
            "private" : "",
            "forks" : ""
        }
        self.cloned = {
            # List of repositories cloned
            # [author-name] : [ repositories, ... ]
        }

    def set_new_git_remote_repo_server_protocol(self, new_protocol="https"):
        """
        Set a new Git Remote Repository Server Protocol

        :: Params
        - new_protocol : Specify the new protocol
            + Type: String
            + Default: https
        """
        self.GIT_REMOTE_REPO_SERVER_PROTOCOL = new_protocol
        self.GIT_REMOTE_REPO_SERVER_URL="{}://{}".format(self.GIT_REMOTE_REPO_SERVER_PROTOCOL, self.GIT_REMOTE_REPO_SERVER_DOMAIN)

    def set_new_git_remote_repo_server_domain(self, new_domain="github.com"):
        """
        Set a new Git Remote Repository Server IP address/domain name

        :: Params
        - new_domain : Specify the new git server IP address/domain name
            + Type: String
            + Default: 'github.com'
        """
        self.GIT_REMOTE_REPO_SERVER_DOMAIN = new_domain
        self.GIT_REMOTE_REPO_SERVER_URL="{}://{}".format(self.GIT_REMOTE_REPO_SERVER_PROTOCOL, self.GIT_REMOTE_REPO_SERVER_DOMAIN)

    def set_new_git_repository_author(self, new_author):
        """
        Set a new repository author

        :: Params
        - new_author : Specify the new default target git repository author
            + Type: String
        """
        self.REPO_AUTHOR = new_author
        self.GIT_REMOTE_REPO_URL="{}/{}".format(self.GIT_REMOTE_REPO_SERVER_URL, self.REPO_AUTHOR)

    def reset_git_remote_repository_url(self):
        """
        Re-set the git remote repository URL with new changes
        """
        self.GIT_REMOTE_REPO_URL="{}/{}".format(self.GIT_REMOTE_REPO_SERVER_URL, self.REPO_AUTHOR)

    def set_new_repository_db_file_path(self, new_db_filepath="docs/records"):
        """
        Set a new repository database file path

        :: Params
        - new_db_filepath : Set new database file path
            + Type: String
            + Default: docs/records
        """
        self.REPO_NAMES_DB_FILE_PATH = new_db_filepath

    def set_new_repository_db_file_name(self, new_db_filename="all-repos.txt"):
        """
        Set a new repository database file name

        :: Params
        - new_db_filename : Set new database file name
            + Type: String
            + Default: all-repos.txt
        """
        self.REPO_NAMES_DB_FILE_PATH = new_db_filename

    def set_new_repository_db_file(self, new_db_file):
        """
        Set a new repository database file

        :: Params
        - new_db_file : Set new database file
            + Type: String
        """
        self.REPO_NAMES_DB_FILE = new_db_file

    def set_repository_public_dir_path(self, repo_dir_base="repos", custom_public_dir_name="Public"):
        """
        Append 'Public' in front of the specified repository base/root directory path

        :: Params
        - repo_dir_base : Specify the repository base/root directory path
            + Type: String
            + Default: repos

        - custom_public_dir_name: Specify a custom 'Public' directory name to replace the default ('Public')
            + Type: String
            + Default: Public
        """
        self.PUBLIC_REPO_DIR="{}/{}".format(repo_dir_base, custom_public_dir_name)

    def set_repository_private_dir_path(self, repo_dir_base="repos", custom_public_dir_name="Private"):
        """
        Append 'Private' in front of the specified repository base/root directory path

        :: Params
        - repo_dir_base : Specify the repository base/root directory path
            + Type: String
            + Default: repos

        - custom_private_dir_name: Specify a custom 'Private' directory name to replace the default ('Private')
            + Type: String
            + Default: Private
        """
        self.PRIVATE_REPO_DIR="{}/{}".format(repo_dir_base, custom_public_dir_name)

    def set_export_logs_file_path(self, new_filepath="docs/exports"):
        """
        Set a new export logs output file path

        :: Params
        - new_filepath : Specify new file path
            + Type: String
            + Default: docs/exports
        """
        self.REPO_EXPORT_LOGS_FILE_PATH = new_filepath
        self.REPO_EXPORT_LOGS_FILE="{}/{}".format(self.REPO_EXPORT_LOGS_FILE_PATH, self.REPO_EXPORT_LOGS_FILE_NAME)

    def set_export_logs_file_name(self, new_filename="exports.log"):
        """
        Set a new export logs output file name

        :: Params
        - new_filename : Specify new file name
            + Type: String
            + Default: exports.log
        """
        self.REPO_EXPORT_LOGS_FILE_NAME = new_filename
        self.REPO_EXPORT_LOGS_FILE="{}/{}".format(self.REPO_EXPORT_LOGS_FILE_PATH, self.REPO_EXPORT_LOGS_FILE_NAME)

    def open_repository_db(self):
        """
        Open and read the initialized repository file into the repositories list
        """
        with open(self.REPO_NAMES_DB_FILE, "r+") as read_file:
            # Read content into list
            self.repositories = read_file.readlines()

            # Close file after usage
            read_file.close()

        # Output
        return self.repositories

    def cleanup_and_sanitization(self, repositories:list):
        """
        Cleanup and sanitize repositories list

        :: Params
        - repositories : List of repositories to be cleaned up before cloning
            + Type: List
        """
        # Initialize Variables
        tmp_list = []

        # Iterate through repositories list and sanitize elements
        for i in range(len(repositories)):
            # Get current entry
            curr_entry = repositories[i]

            # Strip all special characters from the sides
            sanitized_entry = curr_entry.strip()

            # Check if is newline
            if len(curr_entry) > 0:
                tmp_list.append(sanitized_entry)

        return tmp_list

    def create_project_structure(self, project_struct_layout=None):
        """
        Create the defined project structure layout

        :: Params
        - project_struct_layout : Specify the project structure layout list you wish to create; if not specified, the layout will be defaulted to '[ REPO_DIR, REPO_NAMES_DB_FILE_PATH, REPO_EXPORT_LOGS_FILE_PATH ]'
            + Type: List
            + Default: None
        """
        # Initialize Variables
        if project_struct_layout == None:
            project_structure = [ self.REPO_DIR, self.REPO_NAMES_DB_FILE_PATH, self.REPO_EXPORT_LOGS_FILE_PATH ]
        else:
            project_structure = project_struct_layout

        # Create project structure
        for curr_dir in project_structure:
            # Check if current project structure exists
            if not (os.path.isdir(curr_dir)):
                # Directory does not exist
                os.makedirs(curr_dir)

    def clone(self, repositories:list):
        """
        Begin cloning repositories list

        :: Params
        - repositories : List of repositories to be cleaned up before cloning
            + Type: List
        """
        # Initialize Variables

        # Open export logs file to write to during the cloning process
        with open(self.REPO_EXPORT_LOGS_FILE, "a+") as export_logs:
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
                        if not (curr_repo_author in self.cloned):
                            # Not in dictionary
                            # Initialize entry in clone list
                            self.cloned[curr_repo_author] = []

                        # Append entry to author list
                        self.cloned[curr_repo_author].append(curr_repo_pkg)

                        # Append the current author to the root/base directory
                        self.REPO_DIR += "/{}".format(curr_repo_author)

                        # Format repository URL
                        curr_repo_url="{}/{}".format(self.GIT_REMOTE_REPO_SERVER_URL, curr_repo_name)

                        # Check repository type
                        match curr_repo_type:
                            case "Public":
                                self.REPO_DIR += "/Public"
                            case "Private":
                                self.REPO_DIR += "/Private"
                                # Set API Token
                                # Check if API Token is set
                                if self.GITHUB_API_TOKEN == None:
                                    # Not set
                                    error_env_not_set("GitHub API Token/Key", "GITHUB_API_TOKEN")
                                curr_repo_url="{}://{}@{}/{}".format(self.GIT_REMOTE_REPO_SERVER_PROTOCOL, self.GITHUB_API_TOKEN, self.GIT_REMOTE_REPO_SERVER_DOMAIN, curr_repo_name)
                            case "Fork":
                                self.REPO_DIR += "/Forks"

                        # Check if current author folder exists
                        if not (os.path.isdir(self.REPO_DIR)):
                            # Directory does not exist
                            # Create directory for the current author
                            os.makedirs(self.REPO_DIR)

                        # Clone the github repo
                        print("Cloning current repository: {}".format(curr_repo_url))
                        cmd_str = "git -C {} clone {}".format(self.REPO_DIR, curr_repo_url)
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
                self.REPO_DIR = "repos"

                # Newline
                print("")

            # Close file after usage
            export_logs.close()

    def start_clone(self):
        # Create project structure layout
        self.create_project_structure()

        # Check if repository list exists
        if os.path.isfile(self.REPO_NAMES_DB_FILE):
            # Read repositories list file into list
            repositories = self.open_repository_db()

            # Cleanup and sanitize repositories list
            self.repositories = self.cleanup_and_sanitization(repositories)

            # Open up export logs, and begin cloning
            self.clone(self.repositories)
        else:
            print("Repository List {} does not exist, please create one before proceeding".format(self.REPO_NAMES_DB_FILE))

