import os
from enum import Enum
import subprocess

# Uses Linux Kernel GPU driver registers, should be supported by most Linux platforms
# https://docs.kernel.org/gpu/backlight.html
# Doesn't work on OLED screen because of no backlight

default_backlight_dir = "/sys/class/backlight/"
brightness_file = "brightness"


# Error codes
class ErrorCode(Enum):
    PATH_NOT_FOUND = 1
    INT_OUT_OF_RANGE = 2
    UPDATE_FAILED = 3
    TOO_MANY_DEVICES = 4
    FILE_DOESNT_EXIST = 5


def find_backlight_path(custom_backlight_dir=None):
    # Check if /sys/class/backlight/ exists
    backlight_dir = custom_backlight_dir or default_backlight_dir

    if not os.path.exists(backlight_dir) or not os.path.isdir(backlight_dir):
        return ErrorCode.PATH_NOT_FOUND

    # Get list of subdirectories in /sys/class/backlight/
    backlight_subdirs = [d for d in os.listdir(backlight_dir) if os.path.isdir(os.path.join(backlight_dir, d))]

    # Check if there is exactly one child directory
    # Will only change backlight if only 1 attached screen is detected
    if len(backlight_subdirs) == 1:
        # Construct the full path of the child directory
        brightness_file_path = os.path.join(backlight_dir, backlight_subdirs[0], brightness_file)
        if os.path.isfile(brightness_file_path):
            return brightness_file_path
        else:
            return ErrorCode.FILE_DOESNT_EXIST
    else:
        return ErrorCode.TOO_MANY_DEVICES


# Change 0-100% to 0-255 for GPU register
def translate_percentage_brightness(brightness):
    brightness = int((int(brightness) / 100) * 255)
    return brightness


def update_brightness(brightness, brightness_file_path=None):
    # Validate user input
    if 0 <= int(brightness) <= 100:
        brightness = translate_percentage_brightness(brightness)
    else:
        return ErrorCode.INT_OUT_OF_RANGE

    # Check if path and file exists
    backlight_path = find_backlight_path(brightness_file_path)

    # If path is not a path
    if isinstance(backlight_path, ErrorCode):
        return backlight_path

    # TODO: Better way of doing this?
    command = f"echo {brightness} | sudo tee {backlight_path}"
    exit_code = subprocess.call(command, shell=True)

    if exit_code == 0:
        return 0
    else:
        return ErrorCode.UPDATE_FAILED
