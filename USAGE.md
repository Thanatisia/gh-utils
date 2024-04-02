USAGE
=====

## Documentations

*Tools*
-------
+ gh-clone : GitHub repositories cloning CLI utility
+ gh-retrieve : Backup/Archive your full list of your Public/Private repositories using the GitHub API

## CLI utilities

> gh-clone

#### Setup

*Dependencies*
--------------
+ python
+ python-pip
+ python-venv
- Python packages

*Pre-Requisites*
----------------
- Create a Python Virtual Environment
    - Generate Virtual Environment
        ```bash
        python -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Install locally
    - Install package dependencies
        ```bash
        python -m pip install -Ur requirements.txt
        ```
    - (Optional) Uninstall current package
        ```bash
        pip uninstall ghutils
        ```
    - Install locally as development mode 
        ```bash 
        pip install .
        ```

- Install using pip
    ```bash
    pip install git+https://github.com/Thanatisia/gh-utils
    ```

- Obtain your GitHub repositories as a JSON data serialization file using the GitHub API
    - Using Curl
        - Obtaining Public Repositories
            ```bash
            curl -H "Authorization: Bearer [GITHUB_API_TOKEN]" "https://api.github.com/user/repos?type=public&per_page=[maximum-page-numbers]?page=[page-number]" > output-repos.json
            ```

        - Obtaining Private Repositories
            ```bash
            curl -H "Authorization: Bearer [GITHUB_API_TOKEN]" "https://api.github.com/user/repos?type=private&per_page=[maximum-page-numbers]?page=[page-number]" > output-repos.json
            ```

- To format and obtain JSON key-values using 'jq'
    - Obtain full name of repositories without string wrap
        ```bash
        cat output-repos.json | jq ".[].full_name" -r > [public|private].repos.txt
        ```

    - Obtain number of repositories in list
        ```bash
        cat output-repos.json | jq ".[].full_name" -r | wc -l
        ```

- Prepare your GitHub repositories list in the following format
    - Notes
        - Please place your repositories ('author/repo-name') under the appropriate headers
            + Headers are identified by '# Public|Private|Forks'
            + By default (Header is not specified): The cloned repositories are public
        + Please comment out all repositories you do not wish to clone by prepending the repository URL with the '#' delimiter
        - Please note that for the repositories under the 'Forks' header, 
            - Assuming your repository is a private repository, please follow the same rules when cloning a Private Repository
                - i.e.
                    + Ensure that the Environment Variable 'GITHUB_API_TOKEN' is set
    ```
    # Public
    author/repo-name-1
    author/repo-name-2
    author/repo-name-3
    author/repo-name-4
    ...
    author/repo-name-N

    # Private
    author/repo-name-1
    author/repo-name-2
    author/repo-name-3
    author/repo-name-4
    author/repo-name-N

    # Forks
    author/repo-name-N
    ```

- (Optional) If you are cloning private repositories
    - Set your GitHub API Token/Secret Key as an Environment Variable
        ```bash
        export GITHUB_API_TOKEN=[GITHUB_API_TOKEN]
        ```

*Environment Variables*
-----------------------
- Security
    - GITHUB_API_TOKEN : Set your GitHub API Token (aka 'Secret Key') if you wish to clone Private Repositories
        + Type: String

- Remote Git Repository Server
    - GIT_REMOTE_REPO_SERVER_PROTOCOL : Set the protocol (i.e. http|https) used by the target git remote repository server's domain (i.e. http|https://github.com)
        + Type: String
        + Default: https
    - GIT_REMOTE_REPO_SERVER_DOMAIN : Set the Server IP/domain of your target git remote repository server
        + Type: String
        + Default: "github.com"

- Repository lists
    - REPO_NAMES_DB_FILE_PATH : Set the file path to the repository list
        + Default: "docs/records"
    - REPO_NAMES_DB_FILE_NAME : Set the file name of the repository list
        + Default: "all-repos.txt"

- Local Repository directory
    - REPO_DIR : Set the git repository base/root directory
        + Default: "repos"
    - REPO_EXPORT_LOGS_FILE_PATH : Set the output filepath to the Export logs
        + Default: "docs/exports"
    - REPO_EXPORT_LOGS_FILE_NAME : Set the Export logs filename
        + Default: "exports.log"

*Usage*
-------
- Cloning Public Repositories
    ```bash
    gh-clone
    ```

- Cloning Private (and Public) Repositories
    ```bash
    GITHUB_API_TOKEN=[GITHUB_API_TOKEN] gh-clone
    ```

> gh-retrieve

#### Setup

*Dependencies*
--------------
+ python
+ python-pip
+ python-venv
- Python packages
    - json
    - requests
    - subprocess

*Pre-Requisites*
----------------
- Create a Python Virtual Environment
    - Generate Virtual Environment
        ```bash
        python -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Set your GitHub API Token/Secret Key as an Environment Variable
    ```bash
    export GITHUB_API_TOKEN=[GITHUB_API_TOKEN]
    ```

*Environment Variables*
-----------------------
- Security
    - GITHUB_API_TOKEN : Set your GitHub API Token (aka 'Secret Key') if you wish to clone Private Repositories
        + Type: String

*Usage*
-------
- Cloning Public Repositories
    ```bash
    gh-retrieve
    ```

- Cloning Private (and Public) Repositories
    ```bash
    GITHUB_API_TOKEN=[GITHUB_API_TOKEN] gh-retrieve
    ```

- To debug and check if the repositories are correct
    - using 'jq'
        - Get repository full names (Format: author/project-name)
            ```bash 
            cat output-[public|private].json | jq -r '.[].full_name'
            ```
        - Check number of entries
            ```bash 
            cat output-[public|private].json | jq -r '.[].full_name' | wc -l
            ```

## Importing/Embedding as a library/module

*Library*
---------

### Package
- ghutils : Collection of GitHub Utilities, library/frameworks and executables

### Modules
- ghutils
    - core : Core logic library/framework containing classes for each utilities
    - ghcore : The GitHub mass cloning CLI utility/executable source code; importable as a module/library

### Classes
- ghutils.core
    - `.GitHubClone(GIT_REPO_AUTHOR, GIT_REMOTE_REPO_SERVER_PROTOCOL, GIT_REMOTE_REPO_SERVER_DOMAIN, REPO_NAMES_DB_FILE_PATH, REPO_NAMES_DB_FILE_NAME, REPO_DIR, REPO_EXPORT_LOGS_FILE_PATH, REPO_EXPORT_LOGS_FILE_NAME)` : Class containing implementations and logic for customizing specifications when cloning git repositories from GitHub en-mass
        - Class Constructor Parameters
            - GIT_REPO_AUTHOR : The primary/default git repository author of choice (currently unused)
                + Type: String
                + Default: ""
            - GIT_REMOTE_REPO_SERVER_PROTOCOL : Set the default protocol used by the git remote repository server (i.e. http|https)
                + Type: String
                - Acceptable Values:
                    + http
                    + https
                + Default: https
            - GIT_REMOTE_REPO_SERVER_DOMAIN : Set the default Server IP/domain of the git remote repository server
                + Type: String
                + Default: github.com
            - REPO_NAMES_DB_FILE_PATH : Set the default filepath of the repositories list containing the repositories to be cloned
                + Type: String
                + Default: "docs/records"
            - REPO_NAMES_DB_FILE_NAME : Set the default filename of the repositories list containing the repositories to be cloned
                + Type: String
                + Default: "all-repos.txt"
            - REPO_DIR : Set the default base/root output path to clone the repositories into
                + Type: String
                + Default: "repos"
            - REPO_EXPORT_LOGS_FILE_PATH : Set the output filepath to store the exported log file
                + Type: String
                + Default: "docs/exports"
            - REPO_EXPORT_LOGS_FILE_NAME : Set the output filename of the exported log file
                + Type: String
                + Default: "exports.log"

### Functions
- ghutils.core.GitHubClone()
    - `.set_new_git_remote_repo_server_protocol(new_protocol="https")`: Set a new Git Remote Repository Server Protocol
        - Parameter/Argument Signatures
            - new_protocol : Specify the new protocol
                + Type: String
                + Default: https

    - `.set_new_git_remote_repo_server_domain(new_domain="github.com")`: Set a new Git Remote Repository Server IP address/domain name
        - Parameter/Argument Signatures
            - new_domain : Specify the new git server IP address/domain name
                + Type: String
                + Default: 'github.com'

    - `.set_new_git_repository_author(new_author)`: Set a new repository author
        - Parameter/Argument Signatures
            - new_author : Specify the new default target git repository author
                + Type: String

    + `.reset_git_remote_repository_url()`: Re-set the git remote repository URL with new changes

    - `.set_new_repository_db_file_path(new_db_filepath="docs/records")`: Set a new repository database file path
        - Parameter/Argument Signatures
            - new_db_filepath : Set new database file path
                + Type: String
                + Default: docs/records

    - `.set_new_repository_db_file_name(new_db_filename="all-repos.txt")`: Set a new repository database file name
        - Parameter/Argument Signatures
            - new_db_filename : Set new database file name
                + Type: String
                + Default: all-repos.txt

    - `.set_new_repository_db_file(new_db_file)`: Set a new repository database file
        - Parameter/Argument Signatures
            - new_db_file : Set new database file
                + Type: String

    - `.set_repository_public_dir_path(repo_dir_base="repos", custom_public_dir_name="Public")`: Append 'Public' in front of the specified repository base/root directory path
        - Parameter/Argument Signatures
            - repo_dir_base : Specify the repository base/root directory path
                + Type: String
                + Default: repos

            - custom_public_dir_name: Specify a custom 'Public' directory name to replace the default ('Public')
                + Type: String
                + Default: Public

    - `.set_repository_private_dir_path(repo_dir_base="repos", custom_public_dir_name="Private")`: Append 'Private' in front of the specified repository base/root directory path
        - Parameter/Argument Signatures
            - repo_dir_base : Specify the repository base/root directory path
                + Type: String
                + Default: repos

            - custom_private_dir_name: Specify a custom 'Private' directory name to replace the default ('Private')
                + Type: String
                + Default: Private

    - `.set_export_logs_file_path(new_filepath="docs/exports")`: Set a new export logs output file path
        - Parameter/Argument Signatures
            - new_filepath : Specify new file path
                + Type: String
                + Default: docs/exports

    - `.set_export_logs_file_name(new_filename="exports.log")`: Set a new export logs output file name
        - Parameter/Argument Signatures
            - new_filename : Specify new file name
                + Type: String
                + Default: exports.log

    - `.open_repository_db()`: Open and read the initialized repository file into the repositories list
        - Return
            - self.repositories
                + Type: Dictionary (Key-Value Mapping (aka Associative Array))

    - `.cleanup_and_sanitization(repositories:list)`: Cleanup and sanitize repositories list
        - Parameter/Argument Signatures
            - repositories : List of repositories to be cleaned up before cloning
                + Type: List
        - Return
            - tmp_list : Resulting repositories list after cleaning and sanitizing the list (i.e. removing/trimming the special characters etc etc)
                + Type: List

    - `.create_project_structure(project_struct_layout=None)`: Create the defined project structure layout
        - Parameter/Argument Signatures
            - project_struct_layout : Specify the project structure layout list you wish to create; if not specified, the layout will be defaulted to '[ REPO_DIR, REPO_NAMES_DB_FILE_PATH, REPO_EXPORT_LOGS_FILE_PATH ]'
                + Type: List
                + Default: None

    - `.clone(repositories:list)`: Begin cloning repositories list
        - Parameter/Argument Signatures
            - repositories : List of repositories to be cleaned up before cloning
                + Type: List

    + `.start_clone()`: Begin the complete cloning workflow; use this if you do not wish to customize anything


### Data Classes/Types

### Attributes/Variables Objects
- core.GitHubClone
    - Environment Variables
        - `.GITHUB_API_TOKEN` : Set your GitHub API Token (aka Secret Key); required if you are cloning a Private Repository (or a Fork that is a Private Repository)
            + Type: String
            - Default
                + Environment Variable: `os.getenv("GITHUB_API_TOKEN")`
        - `.GIT_REMOTE_REPO_SERVER_PROTOCOL` : Set the default protocol used by the git remote repository server (i.e. http|https)
            + Type: String
            - Default
                + Environment Variable: `os.getenv("GIT_REMOTE_REPO_SERVER_PROTOCOL", https)`
        - `.GIT_REMOTE_REPO_SERVER_DOMAIN` : Set the default Server IP/domain of the git remote repository server
            + Type: String
            - Default
                + Environment Variable: `os.getenv("GIT_REMOTE_REPO_SERVER_DOMAIN", github.com)`
        - `.REPO_NAMES_DB_FILE_PATH` : Set the default filepath of the repositories list containing the repositories to be cloned
            + Type: String
            - Default
                + Environment Variable: `os.getenv("REPO_NAMES_DB_FILE_PATH", "docs/records")`
        - `.REPO_NAMES_DB_FILE_NAME` : Set the default filename of the repositories list containing the repositories to be cloned
            + Type: String
            - Default
                + Environment Variable: `os.getenv("REPO_NAMES_DB_FILE_NAME", "all-repos.txt")`
        - `.REPO_DIR` : Set the default base/root output path to clone the repositories into
            + Type: String
            - Default
                + Environment Variable: `os.getenv("REPO_DIR", "repos")`
        - `.REPO_EXPORT_LOGS_FILE_PATH` : Set the output filepath to store the exported log file
            + Type: String
            - Default
                + Environment Variable: `os.getenv("REPO_EXPORT_LOGS_FILE_PATH", "docs/exports")`
        - `.REPO_EXPORT_LOGS_FILE_NAME` : Set the output filename of the exported log file
            + Type: String
            - Default
                + Environment Variable: `os.getenv("REPO_EXPORT_LOGS_FILE_NAME", "exports.log")`
    - Formatted Variables
        - `.GIT_REMOTE_REPO_SERVER_URL` : Contains the complete combination of the git remote repository server's URL by combining the protocol and domain (i.e. https://github.com)
            + Type: String
            + Default Value: `"{}://{}".format(GIT_REMOTE_REPO_SERVER_PROTOCOL, GIT_REMOTE_REPO_SERVER_DOMAIN)`
        - `.REPO_NAMES_DB_FILE` : Contains the default formatted repositories list filename
            + Type: String
            + Default Value: `"{}/{}".format(REPO_NAMES_DB_FILE_PATH, REPO_NAMES_DB_FILE_NAME)`
        - `.PUBLIC_REPO_DIR` : Contains the default formatted 'Public' directory to clone Public projects repositories to
            + Type: String
            + Default Value: `"{}/Public".format(self.REPO_DIR)`
        - `.PRIVATE_REPO_DIR` : Contains the default formatted 'Private' directory to clone Private project repositories to
            + Type: String
            + Default Value: `"{}/Private".format(self.REPO_DIR)`
        - `.REPO_EXPORT_LOGS_FILE` : Contains the formatted default full filepath of the export logs
            + Type: String
            + Default Value: `"{}/{}".format(REPO_EXPORT_LOGS_FILE_PATH, REPO_EXPORT_LOGS_FILE_NAME)`
    - Local Variables
        - `.repositories` : To contain/store all the repositories to be cloned after reading the repositories list file
            + Type: List
            + Default: '[]' (Empty List)
        - `.file_contents` : Contains a mapping of the various repository type (i.e. Public, Private, Forks) to the current repository
            + Type: Dictionary (Key-Value Mapping (i.e. Associative Array))
            + Default: `{ "public" : "", "private" : "", "forks" : "" }`
        - `.cloned` : Contains the List of repositories cloned
            + Type: Dictionary (Key-Value Mapping (i.e. Associative Array))
            + Default: '{}' (Empty Dictionary)
            + Format: `[author-name] : [ repositories, ... ]`

*Usage*
-------
- Import python package
    ```python
    from ghutils.core import GitHubClone
    ```

- Initialize Variables
    ```python
    # Initialize Variables
    ```

- Initialize Module Classes
    - GitHubClone : Class containing implementations and logic for customizing specifications when cloning git repositories from GitHub en-mass
        ```python
        gh_clone = GitHubClone()
        ```

- Start the general cloning operational flow
    ```python
    gh_clone.start_clone()
    ```

## Wiki

## Resources

## References

## Remarks

