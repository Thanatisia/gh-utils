# CHANGELOGS

## Table of Contents
+ [2024-04-01](#2024-04-01)
+ [2024-04-02](#2024-04-02)
+ [2024-04-03](#2024-04-03)

## Entry Logs
### 2024-04-01
#### 1303H
+ Initial Commit

+ Version: 0.1.0

- New
    + Added new document 'README.md'
    + Added new document 'CHANGELOGS.md'
    + Added new document 'USAGE.md'
    - Added new package 'gh-utils'
        + Added new module 'gh-clone.py' : Clones git repositories from GitHub based on a list of your GitHub repositories (presumable obtained via the GitHub API)


#### 1340H
- New
    + Added new python packaging script 'setup.py' for setuptools
    + Added '.gitignore'

#### 1445H
- Goals
    + Make gh-clone.py into a standalone utility that is customizable

- Add
    + Added python package dependencies file 'requirements.txt'

- Updates
    - Updated document 'USAGE.md'
        + Cleaned up and changed some usage documentations
        + Fixed formatting
    - Updated source file 'gh-clone.py' in 'src/gh-utils'
        + Added directories creation if does not exist
        + Updated variables default values

#### 1821H
- Updates
    - Updated document 'USAGE.md'
        + Added more context to setup
        + Added installation steps
    - Updated python packaging script 'setup.py'
        + Renamed package
        + Fixed entry point for console scripts
    - Migrated package 'src/gh-utils' to 'src/ghutils'
        + Renamed 'gh-clone.py' to 'ghclone.py'
    - Updated source file 'ghclone.py' in 'src/gh-utils'
        + Moved current body of code into 'main()' function for entry point

#### 1831H
- Updates
    - Updated document 'USAGE.md'
        + Removed 'python' from gh-clone usage after pip installation

#### 1842H
- Updates
    - Updated source file 'ghclone.py' in 'src/gh-utils'
        + Created function 'error_env_not_set()' to display a custom error message and exit if an environment variable is not set
        + Performed some refactoring

#### 2059H
- Updates
    - Updated document 'USAGE.md'
        + Added Environment Variables for 'gh-clone'
    - Updated source file 'ghclone.py' in 'src/gh-utils'
        + Added function 'get_env_var()' as an implementation test for getting environment variables
        + Added documentations to 'error_env_not_set()'
        + Refactored variable initialization to object as an environment variable for some customization (for the time being) with the original default values set
        + Added a 'cloned' dictionary to store all results for future use
        + Split the current repository in the repository iteration by the '/' delimiter to obtain the project author and project name
        + Removed necessity on 'REPO_AUTHOR' and making use of the repository list's author, allowing for dynamic author detection

#### 2145H
- Updates
    - Updated source file 'ghclone.py' in 'src/gh-utils'
        + Added directory and file checking

#### 2200H
+ Version: 0.2.0

- Version Changes
    - gh-clone
        - Added python packaging for easy installation and debugging
            + Installable as a standalone executable/binary via pip install
        - Added environment variables for working customization
            + TODO: Implement CLI argument parsing to simplify setting of parameters
            + Place gh-clone's logic into a class for GitHub-related usage as a library/module
            + Verification and validation of data

- New
    + Added new python packaging script 'setup.py' for setuptools
    + Added '.gitignore'
    + Added python package dependencies file 'requirements.txt'

- Updates
    - Updated document 'USAGE.md'
        + Cleaned up and changed some usage documentations
        + Fixed formatting
        + Added more context to setup
        + Added installation steps
        + Removed 'python' from gh-clone usage after pip installation
        + Added Environment Variables for 'gh-clone'
    - Updated python packaging script 'setup.py'
        + Renamed package
        + Fixed entry point for console scripts
    - Updated source file 'gh-clone.py' in 'src/gh-utils'
        + Added directories creation if does not exist
        + Updated variables default values
    - Migrated package 'src/gh-utils' to 'src/ghutils'
        + Renamed 'gh-clone.py' to 'ghclone.py'
    - Updated source file 'ghclone.py' in 'src/gh-utils'
        + Moved current body of code into 'main()' function for entry point
        + Created function 'error_env_not_set()' to display a custom error message and exit if an environment variable is not set
        + Performed some refactoring
        + Added function 'get_env_var()' as an implementation test for getting environment variables
        + Added documentations to 'error_env_not_set()'
        + Refactored variable initialization to object as an environment variable for some customization (for the time being) with the original default values set
        + Added a 'cloned' dictionary to store all results for future use
        + Split the current repository in the repository iteration by the '/' delimiter to obtain the project author and project name
        + Removed necessity on 'REPO_AUTHOR' and making use of the repository list's author, allowing for dynamic author detection

#### 2209H
- Updates
    - Updated document 'README.md'
        + Updated version to v0.2.0
    - Updated python packaging script 'setup.py'
        + Updated version to v0.2.0

#### 2247H
- Updates
    - Updated source file 'ghclone.py'
        + Added new class 'GitHubClone' as an attempt to start creating a library/framework of GitHub-related utilities

#### 2258H
- New
    - Added new directory 'tests/' for all unit tests
        + Added new unit test source file 'ghclone-unittest.py' for testing 'gh-clone'

#### 2308H
- New
    - Added new module/library 'core.py' in 'src/ghutils': Contains the Core logic library/framework containing classes for each utilities
        + Added class 'GitHubClone': Functions pertaining to cloning from GitHub through a list of defined repositories in the format of 'author/project-name'
    - Updated unit test 'ghclone-unittest.py'
        + Renamed module import 'ghclone.py' => 'core.py'

#### 2312H
- Updates
    + Fixed changelogs header

### 2024-04-02
#### 1048H
+ Version: 0.3.0

- Version Changes
    - gh-clone
        + (Temporary) Added new class 'GitHubClone' as an attempt to start creating a library/framework of GitHub-related utilities
    - Added new module/library 'core.py' : Contains the Core logic library/framework containing classes for each utilities
        + Added class 'GitHubClone': Functions pertaining to cloning from GitHub through a list of defined repositories in the format of 'author/project-name'

- New
    - Added new directory 'tests/' for all unit tests
        - Added new unit test source file 'ghclone-unittest.py' for testing 'gh-clone'
            - Updated unit test 'ghclone-unittest.py'
                + Renamed module import 'ghclone.py' => 'core.py'
    - Added new module/library 'core.py' in 'src/ghutils': Contains the Core logic library/framework containing classes for each utilities
        + Added class 'GitHubClone': Functions pertaining to cloning from GitHub through a list of defined repositories in the format of 'author/project-name'

- Updates
    - Updated source file 'ghclone.py'
        + Added new class 'GitHubClone' as an attempt to start creating a library/framework of GitHub-related utilities
    + Fixed changelogs header

#### 1105H
- Updates
    - Updated source file 'ghclone.py'
        + Replaced embedded class 'GitHubClone' with library/module 'from ghutils.core import GitHubCore'
        + Moved the cloning logical statements from main() to function ghclone()

#### 1200H
- Updates
    - Updated document 'USAGE.md'
        + Added complete write-up for implementations in library/module 'core.py'
        + Added usage examples to embed/implement the library/module
    - Updated module 'core.py' in 'src/ghutils'
        + Added docstring comments to class 'GitHubClone'

#### 1317H
- Updates
    - Updated document 'USAGE.md'
        + Added complete write-up for implementations in library/module 'core.py'
        + Added usage examples to embed/implement the library/module
    - Updated source file 'ghclone.py'
        + Replaced embedded class 'GitHubClone' with library/module 'from ghutils.core import GitHubCore'
        + Moved the cloning logical statements from main() to function ghclone()
    - Updated module 'core.py' in 'src/ghutils'
        + Added docstring comments to class 'GitHubClone'

#### 2244H
- New
    + Added new module 'ghretrieve.py' in 'src/ghutils' : Backup/Archive your full list of your Public/Private repositories using the GitHub API

- Updates
    - Updated document 'README.md'
        + Updated version to v0.4.0
        + Added 'gh-retrieve' to the list
    - Updated document 'requirements.txt'
        + Added new dependencies
    - Updated python packaging script 'setup.py'
        + Updated version to v0.4.0
        + Added new dependencies
    - Updated document 'USAGE.md'
        + Added usage documentation and examples for new GitHub CLI support utility - ghretrieve

#### 1102H
+ Version: 0.4.0

- Version Changes
    + Added new CLI support utility to the GitHub utilities package: ghretrieve
    + Added new dependencies

- Updates
    - Updated document 'README.md'
        + Updated version to v0.4.0
        + Added 'gh-retrieve' to the list
    - Updated document 'requirements.txt'
        + Added new dependencies
    - Updated python packaging script 'setup.py'
        + Updated version to v0.4.0
        + Added new dependencies
    - Updated document 'USAGE.md'
        + Added complete write-up for implementations in library/module 'core.py'
        + Added usage examples to embed/implement the library/module
        + Added usage documentation and examples for new GitHub CLI support utility - ghretrieve
    - Updated source file 'ghclone.py'
        + Replaced embedded class 'GitHubClone' with library/module 'from ghutils.core import GitHubCore'
        + Moved the cloning logical statements from main() to function ghclone()
    - Updated module 'core.py' in 'src/ghutils'
        + Added docstring comments to class 'GitHubClone'

#### 2305H
+ Version: 0.4.1

- Version Changes
    + Removed 'json' from dependencies
    + Added new console_script entry point for 'gh-retrieve'

- Updates
    - Updated document 'README.md'
        + Updated version to v0.4.1
    - Updated document 'USAGE.md'
        + Added new usage for 'gh-retrieve': To debug and check if the repositories are correct
    - Updated document 'requirements.txt'
        + Removed dependencies - 'json': Built-in; not found in pip
    - Updated python packaging script 'setup.py'
        + Updated version to v0.4.1
        + Removed dependencies - 'json': Built-in; not found in pip
        + Added new console_script entry point for 'gh-retrieve'

### 2024-04-03
#### 1258H
- Updates
    - Updated module 'ghretrieve.py'
        + Added new function 'gh_search_by_token()': Search and return a list of all repositories according to a provided GitHub API Token
        + Added file existence check if the JSON files are found
        + Fixed lines to import the JSON file contents into dictionary properly
        + Added lines to process the JSON dictionary contents for both Public and Private repositories, and extract the filenames

#### 2209H
- Updates
    - Updated module 'ghretrieve.py'
        - Function 'send_get_request()'
            + Added docstring documentation comments to function 'send_get_request()'
            + Added new parameter 'other_parameters' for holding other parameters to parse into the GET request
        - obtain_repo_json()
            + Replaced 'send_get_request()' to 'gh_search_by_token()' to make it more modular

#### 2214H
+ Version: 0.4.2

- Version Changes
    - gh-retrieve
        - New Features
            + Added lines to process the JSON dictionary contents for both Public and Private repositories, and extract the filenames
            - Able to properly
                + Obtain the Public repositories of your GITHUB_API_KEY via sending a GET request and return the results to a JSON file containing the information of all repositories found that is Public
                + Obtain the Private repositories of your GITHUB_API_KEY via sending a GET request and return the results to a JSON file containing the information of all repositories found that is Private
                + Go through the output JSON files, import into the system to filter and obtain the file names of every project repository
                + Write the repository list into an output 'repositories list' file for cloning with 'gh-clone'
        - New Functions
            + Added new function 'gh_search_by_token()': Search and return a list of all repositories according to a provided GitHub API Token
        - Modifications and Changes
            - Function 'send_get_request()'
                + Added new parameter 'other_parameters' for holding other parameters to parse into the GET request
        - Bug Fixes
            + Added file existence check if the JSON files are found
            + Fixed lines to import the JSON file contents into dictionary properly

- Updates
    - Updated document 'README.md'
        + Updated version to v0.4.2
    - Updated python packaging script 'setup.py'
        + Updated version to v0.4.2
    - Updated module 'ghretrieve.py'
        + Added new function 'gh_search_by_token()': Search and return a list of all repositories according to a provided GitHub API Token
        + Added file existence check if the JSON files are found
        + Fixed lines to import the JSON file contents into dictionary properly
        + Added lines to process the JSON dictionary contents for both Public and Private repositories, and extract the filenames
        - Function 'send_get_request()'
            + Added docstring documentation comments to function 'send_get_request()'
            + Added new parameter 'other_parameters' for holding other parameters to parse into the GET request
        - obtain_repo_json()
            + Replaced 'send_get_request()' to 'gh_search_by_token()' to make it more modular

