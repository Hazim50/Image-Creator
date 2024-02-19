import cv2
import numpy as np
import os

class ColorGenerator:
    def __init__(self):
        self.color_dict = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (128, 128, 128),
            "red": (0, 0, 255),
            "blue": (255, 0, 0),
            "green": (0, 255, 0),
            "yellow": (0, 255, 255),
            "purple": (173, 13, 106),
            "brown": (0, 75, 150),
            "orange": (39, 127, 255)
        }

    def get_color(self, color_name):
        return self.color_dict.get(color_name)

class ImageGenerator:
    def __init__(self, color_generator):
        self.color_generator = color_generator

    def generate_image(self, background_color, text_color, material, location):
        backgr = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
        background_frame = np.copy(backgr)
        text_color_value = self.color_generator.get_color(text_color)

        if material == "I":
            text_location = (150, 300)
        else:
            text_location = (92, 300)

        cv2.putText(background_frame, material, text_location, fontFace, fontScale, text_color_value, thickness, lineType)
        image_name = f"{location}{background_color}-{text_color}-{material}.png"
        cv2.imwrite(image_name, background_frame)
        print(f"{image_name} file has created")

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"{folder_path} folder created.")

if __name__ == "__main__":
    fontFace = 2
    fontScale = 11
    thickness = 11
    lineType = cv2.FONT_HERSHEY_SIMPLEX
    location = "C:\\Users\\Hazim\\Desktop\\folder\\Materials\\" # WARNING Don't write desktop location
                                                                # Also, last 2 slash is important

    color_generator = ColorGenerator()
    image_generator = ImageGenerator(color_generator)

    create_folder_if_not_exists(location)

    material_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for background_color in color_generator.color_dict:
        for text_color in color_generator.color_dict:
            if background_color == text_color:
                continue
            for material in material_list:
                image_generator.generate_image(background_color, text_color, material, location)

    cv2.destroyAllWindows()
