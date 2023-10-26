## -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2023 CORE.HOST, LLC. ALL RIGHTS RESERVED
INSTANCE: MODE-> facilities
CREATED: 2023/10/25
OVERVIEW: Establish default facility instances
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

## import; required system settings interfaces
from src.corehost.MODE.settings import *

## import: dynamic attributes
from src.corehost.INSTANCE.state import (FIRSTRUN,
 HAS_ALREADY_STATED, Instance)

## File Instances
SLUG_BUILD_LIST = "build_list.op"
SLUG_LICENSE = "LICENSE"
SLUG_README = "README.md"
SLUG_RUNTIME = "runtime.txt"
SLUG_SETUP = "setup.cfg"

