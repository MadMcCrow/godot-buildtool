#!/usr/bin/env python
#
# git.py : 
#             useful git related functions for the python modules in this folder
#
# Copyright © Noé Perard-Gayot 2020.                                                                                        #
# Licensed under the MIT License. You may obtain a copy of the License at https://opensource.org/licenses/mit-license.php   #
#

#get git Rep out of a path
def getGitRepo(path : str):
    import os.path
    path = os.path.realpath(path)
    repo = None
    try:
        from git import Repo
        from .platform import getFolders
        try :
            repo = Repo(path)
        except:
            parent_path = None
            is_git = False
            while not is_git : 
                parent_path = os.path.abspath(os.path.join(path, os.pardir))
                is_git = ".git" in getFolders(parent_path)
            if not is_git : 
                raise Exception
            repo = Repo(parent_path)
    except:
        return None
    finally:
        return repo


# look for path in tree
def _gitRecursiveLookForPath(path, trees, found = None) :
    if  not isinstance(found, list) :
        found = []
    import os.path
    try:
        for tree in trees :
            try :
                if str(os.path.basename(path)) in str(os.path.basename(tree.path))  :
                    found = [str(p.path) for p in tree.trees]
                else:
                    _gitRecursiveLookForPath(path, tree.trees, found)
            except:
                continue
    except:
        pass
    return found
    


# get names of git tracked folders in path
def getGitFolders(path : str) -> list :
    dirs = []
    try:
        import os.path 
        repo = getGitRepo(path)
        dirs = _gitRecursiveLookForPath(path, repo.tree())
    except:
        raise
    finally:
        return dirs
