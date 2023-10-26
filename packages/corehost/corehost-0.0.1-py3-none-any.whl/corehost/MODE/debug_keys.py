# -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2022 NEW ENTITY OPERATIONS INC. ALL RIGHTS RESERVED
CREATED: 2022/02/13
INSTANCE: MODE-> debug_keys
MODIFIED: 2022/11/05
OVERVIEW: Debug a specific key routine
HISTORY: VERSION 0.0.3
-> 2022/08/24 (VERSION 0.0.2)
-> 2022/02/13 (VERSION 0.0.1)
"""
__version__ = "0.0.1"
__author__ = "Ryan McKenna"
__copyright__ = "Copyright (C) 2023 CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations Inc.", "New Entity Operations, LLC"]
__email__ = "Operator@NewEntityOperations.com"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Preview"

## MODE-> facilities_core
from src.corehost.MODE.debug_core import Debugging

## Local scope
dEbk = Debugging

class DEBUG_KEYS:
 """
 Provide key-based debugging instances
 """
 def secure_seed_failure():
  """
  Confirm that a secure seed conflict has occured and the instance
  needs to be reseeded in order to maintain seed integrity
  """
  def output():
   print("Conflict-> SEED INTEGRITY: Reseeding from SEED POOL now")
  if dEbk.lab == 1 or dEbk.complete == 1 or dEbk.backend == 1:
   output()
  else:
   pass

 def secure_seed_made(SECURE_SEED):
  """
  Confirm a secure SEED has been produced according to your desired
  POOL
  """
  def output():
   print("Your Secured Seed is: "+str(SECURE_SEED))
  if dEbk.lab == 1 or dEbk.complete == 1 or dEbk.backend == 1:
   output()
  else:
   pass

