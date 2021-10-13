#!/usr/bin/python3
"""A file containing a function that 
returns an object represented by a json string
"""
import json



def from_json_string(my_str):
    """Returns object represented by a json string
    """
    return json.loads(my_str)
