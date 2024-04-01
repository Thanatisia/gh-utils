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

