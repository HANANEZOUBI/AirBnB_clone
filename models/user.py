#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel




class User(BaseModel):
    """Managing user objects
       Attributes :
            email (str)
            password (str)
            first_name (str)
            last_name (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""


