# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:54:30 2023

@author: Mario
"""
from werkzeug.security import generate_password_hash, check_password_hash

hash_pwd = generate_password_hash("12345");

print(hash_pwd)