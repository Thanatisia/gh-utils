# CHANGELOGS

## Table of Contents
+ [2024-04-01](#2024-04-01)

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
    + Added module '__init__.py' in 'src/gh-utils' to initialize the package and modules to be imported
    + Added '.gitignore'

- Updates
    - Updated module/library file 'gh-clone.py' in 'src/gh-utils'
        + Added class 'GitHubClone' for GitHub cloning-related functionalities
        + Moving functions into class (to be tested)


