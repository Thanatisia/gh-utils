"""
Unit Test for gh-clone
"""
import os
import sys
from ghutils.core import GitHubClone

def init():
    """
    Initialize Global Variables
    """
    global gh_clone
    gh_clone = GitHubClone()

def test_start_clone():
    """
    Test function: start_clone()
    """
    # Initialize Variables
    result_status_code = -1
    try:
        gh_clone.start_clone()
        result_status_code = 0
    except Exception as ex:
        print("Exception: {}".format(ex))
        result_status_code = -1
    return result_status_code

def main():
    """
    Unit Test workflow here
    """
    assert test_start_clone() == 0, "[-] Function start_clone: Error"
    print("[+] Function start_clone: Success")

if __name__ == "__main__":
    init()
    main()

