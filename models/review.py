#!/usr/bin/python3
"""Contains the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review model"""
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
