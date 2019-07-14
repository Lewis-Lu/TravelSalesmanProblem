'''Global config of map
'''

def _init():
    global _global_dict
    _global_dict = {}

def _set_global_value(k, v):
    '''_set_global_value
    k: key
    v: value
    '''
    _global_dict[k] = v

def _get_global_value(k, default=None):
    '''_get_global_value
    k: key
    '''
    try:
        return _global_dict[k]
    except KeyError:
        return default