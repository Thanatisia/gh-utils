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

