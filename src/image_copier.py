import os
import traceback

from PIL import Image

class ImageCopier:
    """
    Main entry point for image copier.
    """
    output_direction: str
    rotation_name: str
    _angle: int
    def __init__(self, output_direction: str) -> None:
        self.output_direction = output_direction
        self.rotation_name = "{file}=rot-{rotation}.jpg"
        self._angle = 0
    def basic_perform(self, directory, file_list: list[str], copies: int):
        """
        This is the basic class that looks up images and makes a copy of them like image_1|rot-5.jpg
        """
        succes = 0
        failed = 0
        for names in file_list:
            self._create_directory_if_not_exists(names)

        for file_name in file_list:
            image = Image.open(f"{directory}/{file_name}")
            for i in range(0, copies):
                new_angle = self._apply_rotation(copies)
                format_out = self._format_output_file(file_name, new_angle)
                output_file_name = f"{file_name}/{format_out}"
                processed_image = image.rotate(new_angle)
                if self._copy_image(processed_image, output_file_name):
                    succes += 1
                else:
                    failed += 1
        print(f"{succes} Files have been copied, {failed} Files have not been copied")
    def _copy_image(self, image: Image, output_name: str) -> None:
        print(f"Copying image initiated")
        try:
            # output
            image.save(f"{self.output_direction}{output_name}")
            print(f"Image successfully copied")
            return True
        except:
            traceback.print_exc()
            return False
    def _format_output_file(self, file_name: str, angle: int) -> str:
        return self.rotation_name.format(file=file_name, rotation=angle)
    def _apply_rotation(self, number: int) -> int:
        angle = 360 / (number + 1)
        self._angle += angle
        if self._angle > 360:
            self._reset()
        return self._angle

    def _create_directory_if_not_exists(self, directory: str) -> str:
        if not os.path.exists(directory):
            print(f"Created directory: {directory}")
            os.makedirs(f"{self.output_direction}{directory}")
            return directory
        return directory
    def _reset(self):
        self._angle = 0
