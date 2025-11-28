class ImageMetadata:

    _applied_transformation: dict

    def __init__(self, label_id: int, name: str, location: str):
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