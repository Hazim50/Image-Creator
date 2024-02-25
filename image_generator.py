import cv2
import numpy as np
import os

COLOR_DICT = {
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

MATERIAL_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"{folder_path} folder created.")


def create_background(color, size=(400, 400)):
    return np.zeros(shape=[size[0], size[1], 3], dtype=np.uint8) + color


def place_text(img, text, position, color):
    if text == "I":
        cv2.putText(img, text, position, 2, 11, color, 11, cv2.LINE_AA)
    else:
        cv2.putText(img, text, position, 2, 11, color, 11, cv2.LINE_AA)
    return img


def save_images(background_dict, color_dict, material_list, save_location):
    for bg_color, bg_image in background_dict.items():
        for text_color, text_color_value in color_dict.items():
            if bg_color == text_color:
                continue
            for material in material_list:
                pos=(92, 300)
                if material == "I":
                    pos=(150, 300)
                img = place_text(bg_image.copy(), material, pos, text_color_value)
                img_path = f"{save_location}{bg_color}-{text_color}-{material}.png"
                print(f"{img_path} has created")
                cv2.imwrite(img_path, img)

def main():
    background_dict = {}
    for color_name, color_value in COLOR_DICT.items():
        background_dict[color_name] = create_background(color_value)

    save_location = "C:\\Users\\Hazim\\Desktop\\Materials\\"
    create_folder_if_not_exists(save_location)
    save_images(background_dict, COLOR_DICT, MATERIAL_LIST, save_location)


if __name__ == "__main__":
    main()
