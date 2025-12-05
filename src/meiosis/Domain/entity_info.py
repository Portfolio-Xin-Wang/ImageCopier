class EntityInfo:
    """
    Class to hold metadata for an image, including label ID, name & directory location.
    This is used as a data structured to store information about PIL-images and the unique ID. 
    This is used within this software to assign new ID and track transformations applied to images.
    """

    _applied_transformation: dict

    def __init__(self, name: str, location: str, label_id: int = None):
        self.label_id = label_id
        self.name = name
        self.location = location
        self._applied_transformation = {}

    def add_transformation(self, key, value):
        self._applied_transformation[key] = value

    def return_name(self):
        transformation_string = ""
        for key, value in self._applied_transformation.items():
            transformation_string += f"{value};{key}&"
        
        return f"{self.label_id}&{transformation_string}{self.name}"
    
    def __dict__(self):
        return {
            "label_id": self.label_id,
            "name": self.name,
            "location": self.location
        }