#!/usr/bin/python3
"""Contains the City model"""
from models.base_model import BaseModel

class City(BaseModel):
    """Implements the City class"""
    state_id = ""
    name = ""


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
