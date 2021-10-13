#!/usr/bin/python3
"""Ceates an object from json file"""

import json



def load_from_json_file(filename):
    """
    function that creates obj from json file
    """
    with open(filename) as Myfile:
        return json.loads(Myfile.read())
