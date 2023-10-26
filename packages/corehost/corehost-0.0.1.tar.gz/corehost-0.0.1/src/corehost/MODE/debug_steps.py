# -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2022 NEW ENTITY OPERATIONS INC. ALL RIGHTS RESERVED
CREATED: 2022/02/13
INSTANCE: MODE-> debug_steps
MODIFIED: 2022/11/05
OVERVIEW: Debug various steps
HISTORY: VERSION 0.0.3
-> 2022/08/24 (VERSION 0.0.2)
-> 2022/02/13 (VERSION 0.0.1)
"""
__version__ = "0.0.3"
__author__ = "Ryan McKenna"
__copyright__ = "Copyright (C) 2022 CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations Inc.", "New Entity Operations, LLC"]
__email__ = "Operator@NewEntityOperations.com"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Production"

## MODE-> debug_core
from src.corehost.MODE.debug_core import Debugging

## Local scope
dEbSt = Debugging

class DEBUG_STEPS:
 """
 Provide step related debugging types
 """
 def step_establish_runtime_seed(MODE):
  def output():
   if MODE=="START":
    print("---- START: STEP PRE CONFIGURATION - ESTABLISH-> RUNTIME SEED -----")
   elif MODE=="STOP":
    print("---- STOP: STEP PRE CONFIGURATION - ESTABLISH-> RUNTIME SEED  -----")
   else:
    print("The valid modes for step_establish_runtime_seed are"+\
     " 'START' and 'STOP'")
  if dEbSt.lab == 1 or dEbSt.complete == 1 or dEbSt.steps == 1:
   output()
  else:
   pass
