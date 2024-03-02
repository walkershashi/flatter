from pandas import json_normalize 

def flatter(dictionary_obj):
    return json_normalize(dictionary_obj)