"""
Modify response before validation
"""
def StrToListFunc(value):
    '''If value is a string instead of list return a list'''
    refString = []
    if isinstance(value, list):
        return value
    else: 
        refString.append(value)
        return refString
    

def ReplaceStrToList(data):

    for k, v in data.items():
        if k in ['pricing', 'topic_selection', 'platform']:
            data[k] = StrToListFunc(v)
    return data



