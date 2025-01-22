from enum import Enum


class ManageImagesRequest(str, Enum):
    add = "add"
    replace = "replace"
