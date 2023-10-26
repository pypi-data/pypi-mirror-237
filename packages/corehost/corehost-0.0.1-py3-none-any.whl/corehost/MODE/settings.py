## -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2023 CORE.HOST, LLC. ALL RIGHTS RESERVED
INSTANCE: MODE-> settings
CREATED: 2023/10/25
OVERVIEW: Express settings instances that alter the program MODE

settings is the default configurations reader and read/write slug_maker
for the instance

The settings module has a few purposes and one goal.

The goal is to give you one easy format to import built-in modules while
 also allowing for branching primary settings depending on what user
 is accessing them.

A complex-middlelayer format is used to call this information at runtime
 and extend branched sub-program states into static variables.

The purpose behind this is for seperation and modular functionality both
 before and during runtime
"""
__version__ =  "0.0.1"
__author__ = "Ryan McKenna"
__copyright__ = "CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations, LLC", "New Entity Operations Inc."]
__email__ = "Operator@CORE.HOST"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Preview"

## define the path of the instance. Defaults the the cwd
PATH_INSTANCE = "."

## base extension formats
## allow datascript sources
ext_ds = ".ds"
## allow entityscript sources
ext_entity = ".entity"

## import: built-in packages
from datetime import (date, datetime)
from os import path
from random import randint
from sys import path as SysPath

