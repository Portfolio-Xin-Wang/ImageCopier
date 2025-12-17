class EntityInfo:
    """
    Class to hold metadata for an image, including label ID, name & directory location.
    This is used as a data structured to store information about PIL-images and the unique ID. 
    This is used within this software to assign new ID and track transformations applied to images.
    """

    _applied_transformation: dict

    def __init__(self, name: str, location: str, target_director: str):
        self.target_director = target_director
        self.name = name
        self.location = location
        self._applied_transformation = {}

    def add_transformation(self, key, value):
        self._applied_transformation[key] = value

    def return_name(self):
        transformation_string = ""
        for key, value in self._applied_transformation.items():
            transformation_string += f"{value};{key}&"
        
        return f"{transformation_string}{self.name}"
    
    def __dict__(self):
        standard_dict = {
            "name": self.name,
            "location": self.location
        }
        for key, value in self._applied_transformation.items():
            standard_dict[key] = value
        return standard_dict