## -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2023 CORE.HOST, LLC. ALL RIGHTS RESERVED
INSTANCE: INSTANCE-> state
CREATED: 2023/10/25
OVERVIEW: Establish a default program STATE and related stateful values
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

## FIRSTRUN
class FIRSTRUN:
 """
 Keep track of single instandce methods that run on startup
 """
 count = 0

## HAS_ALREADY_*
class HAS_ALREADY_STATED:
 """
 Mute available output with a branched state
 """
 count = 0

## Instance
class Instance:
 """
 Group X number of outputs together
 """
 ticket = 1
 output = 0

