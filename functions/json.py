#!/usr/bin/env python
#
# functions.py : 
#             useful functions for the python modules in this folder
#
# Copyright © Noé Perard-Gayot 2020.                                                                                        #
# Licensed under the MIT License. You may obtain a copy of the License at https://opensource.org/licenses/mit-license.php   #
#

def JsonConfig(path = './', override_globals = False) ->dict :
    '''
    importJsonConfig() :
    import our json file as a dict, into the global()[]
    '''
    from os.path import isfile
    if not isfile(path) :
        path = findFiles(path, "config.json")
    json_dict = dict()
    try:
        f = open(path, "r")
        s = str(f.read())
        import json
        json_dict = json.loads(s)
        if override_globals : 
            for k, v in json_dict.items() :
                globals()[k] = v
    except:
        pass
    finally:
        f.close()
    return json_dict