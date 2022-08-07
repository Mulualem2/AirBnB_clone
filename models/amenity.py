#!/usr/bin/python3
"""Contains the Amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Implements the Amenity model"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

