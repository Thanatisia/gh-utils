USAGE
=====

## Tools
+ gh-clone.py : GitHub repositories cloning CLI utility

## Documentations

> gh-clone.py

### Setup

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

- Install package dependencies
    ```bash
    python -m pip install -Ur requirements.txt
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
        + Please comment out all repositories you do not wish to clone by prepending the repository URL with the '#' delimiter
        + Please note that for the repositories under the 'Forks' header, please prepend your GitHub API Token the same way as you would when cloning a Private Repository (i.e. https://[GITHUB_API_TOKEN]@github.com/author-name/repo-name)
    ```
    # Public
    https://github.com/author/repo-name-1
    https://github.com/author/repo-name-2
    https://github.com/author/repo-name-3
    https://github.com/author/repo-name-4
    ...
    https://github.com/author/repo-name-N

    # Private
    https://github.com/author/repo-name-1
    https://github.com/author/repo-name-2
    https://github.com/author/repo-name-3
    https://github.com/author/repo-name-4
    https://github.com/author/repo-name-N

    # Forks
    https://github.com/author/repo-name-N
    ```

- (Optional) If you are cloning private repositories
    - Set your GitHub API Token/Secret Key as an Environment Variable
        ```bash
        export GITHUB_API_TOKEN=[GITHUB_API_TOKEN]
        ```

*Usage*
-------
- Cloning Public Repositories
    ```bash
    python gh-clone.py
    ```

- Cloning Private (and Public) Repositories
    ```bash
    GITHUB_API_TOKEN=[GITHUB_API_TOKEN] python gh-clone.py
    ```

## Wiki

## Resources

## References

## Remarks

