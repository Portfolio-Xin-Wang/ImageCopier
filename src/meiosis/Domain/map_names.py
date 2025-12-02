MAP = {
    "frikandel_brood": 1,
    "koffie_brood": 2
}


def map_name_to_id(name: str) -> int:
    """
    Based on the name of the image file, it should return a label id.
    If name does not exist in the map, return 0 as it represents 'Others'
    """
    keys = MAP.keys()
    for key in keys:
        if key in name:
            return MAP.get(key)
    return 0
