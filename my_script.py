import os
import logging
import cv2

def change_to_project_path(main_script_path: str):
    """
    Change the current working directory to the directory where the script is located.
    """
    try:
        script_path = os.path.dirname(os.path.abspath(main_script_path))
        current_path = os.getcwd()

        logging.info(f"Current path: {current_path}")

        if current_path != script_path:
            os.chdir(script_path)
            print(f"current path: {os.getcwd()}")
            logging.info(f"Changed current path to script path: {script_path}")
        else:
            logging.info("Current path is already the script path.")
    except Exception as e:
        logging.error(f"Error changing to script path: {e}")

def check_loaded_image(image: cv2.typing.MatLike):
    assert image is not None, "MyDebug: imread error"

def is_path_exists(file_path: str) -> bool:
    return os.path.exists(file_path)

def check_path_exists(file_path: str) -> None:
    assert is_path_exists(file_path), f"MyDebug: {file_path} - image not found"

def check_path_compatibility(folder_path: str):
    if not is_path_exists(folder_path):
        os.makedirs(folder_path)

def get_filename_without_extension(file_path: str) -> str:
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    return file_name
