# -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2022 NEW ENTITY OPERATIONS INC. ALL RIGHTS RESERVED
CREATED: 2022/02/13
INSTANCE: KEYS-> seed
MODIFIED: 2022/11/05
OVERVIEW: Utilize CORE.HOST compliant seeds to generate server access points
HISTORY: VERSION 0.0.3
-> 2022/08/24 (VERSION 0.0.2)
-> 2022/02/13 (VERSION 0.0.1)
"""
__version__ = "0.0.3"
__author__ = "Ryan McKenna"
__copyright__ = "Copyright (C) 2023 CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations Inc.", "New Entity Operations, LLC"]
__email__ = "Operator@NewEntityOperations.com"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Production"

## from MODE-> *
from src.corehost.MODE.debug_keys import (DEBUG_KEYS)
from src.corehost.MODE.debug_steps import (DEBUG_STEPS)

## import dependent modules from a designated facility
from src.corehost.MODE.facilities import randint

## Pull in verification nodes-> Pull from custom pools of blocks that meet your
## needs. Dependency instances can pull from KEYS.seed when they need the
## seed data: This could be network routines, or image parsing in binary/hex
## form

## imports: dependent
import src.corehost.KEYS.pool.block as block

## Bucket for storing used-system SEED values
BUCKET_SEED = ["XHNH-HYOP-NAHL"]
## Bucket for storing the current SEED
BUCKET_SEED_NOW = ["No seed created"]
## Bucket for storing the current SEED
BUCKET_SEED_POOL = ["No seed created"]
## Change the POOL based on what is available
POOL = block.POOL_STANDARD_CHARACTER
## Subtract 1 to account for the index, avoiding an IndexError
SEED_VALUE = len(POOL)-1
def SEED_UPDATER():
 """
 Function to update the SEED pool based on the desired POOL
 Start with 0 because we're dealing with an index
 """
 L = POOL[randint(0, SEED_VALUE)]
 BUCKET_SEED_POOL.clear()
 BUCKET_SEED_POOL.append(L)
 return(BUCKET_SEED_POOL[0])
def SEED_NOW():
 """
 Construct the Seed value
 """
 SEED = \
 SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()+"-"+\
 SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()+"-"+\
 SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()+SEED_UPDATER()
 ## Provide a conflict overload checker
 # SEED = "XHNH-HYOP-NAHL"
 BUCKET_SEED_NOW.clear()
 BUCKET_SEED_NOW.append(SEED)
class SECURE_CRYPTO_SLUG:
 ## Finally, make the SECURE_SEED AVAILABLE
 SECURE_SEED = BUCKET_SEED_NOW[0]
 def assemble_SEED():
  SEED_NOW()
 def determine_slug_integrity():
  ## Run the SEED_NOW populator
  ## Check for conflicts based on your bucket
  DEBUG_STEPS.step_establish_runtime_seed(MODE="START")
  if BUCKET_SEED_NOW[0] in BUCKET_SEED[:]:
   DEBUG_KEYS.secure_seed_failure()
   ## Provide a seed now overloader
   #SEED_NOW()
  else:
   DEBUG_KEYS.secure_seed_made(
    SECURE_SEED=BUCKET_SEED_NOW[0])
  DEBUG_STEPS.step_establish_runtime_seed(MODE="STOP")

## Both should run to build the SEED from the POOL
SECURE_CRYPTO_SLUG.assemble_SEED()
SECURE_CRYPTO_SLUG.determine_slug_integrity()
## The slug can then be accessed at
## SECURE_CRYPTO_SLUG.SECURE_SEED

