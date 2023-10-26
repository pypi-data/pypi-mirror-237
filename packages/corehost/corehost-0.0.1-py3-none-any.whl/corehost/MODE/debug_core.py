# -*- coding: utf-8 -*-
"""
COPYRIGHT (C) 2022 NEW ENTITY OPERATIONS INC. ALL RIGHTS RESERVED
CREATED: 2022/02/13
INSTANCE: MODE-> debug_core
MODIFIED: 2022/12/01
OVERVIEW: Provide an instance wide debugging instance:
 Debug specific essential processes such as the environment and users in the
 system.
HISTORY: VERSION 0.0.3
-> 2022/08/24 (VERSION 0.0.2)
-> 2022/02/13 (VERSION 0.0.1)
"""
__version__ = "0.0.1"
__author__ = "Ryan McKenna"
__copyright__ = "Copyright (C) 2022 CORE.HOST, LLC."
__credits__ = [
 "Ryan McKenna",
 "New Entity Operations Inc.", "New Entity Operations, LLC"]
__email__ = "Operator@NewEntityOperations.com"
__license__ = "New Entity License"
__maintainer__ = "Ryan McKenna"
__status__ = "Preview"

## Debugging
class Debugging:
 """
 Activate program debugging on either a partial basis, or in a complete manner
 The following settings are available.

 backend = 1 will enable backend debugging instances, primarily those that deal
  with interfacing with system data
 complete = 1 enables all the debugging protocols except those explicitly left
  out of the standard convention - requiring at least dEb.complete == 1
 lab = 1 with both complete and warn being 0 activiates the lab build, which
  will provide more robust terminal outputs
 server = 1 will enable server related debugging
 state = 1 will enable state debugging, primarily functions having to do with
  on/off functionality
 steps = 1 will enable step related outputs, such as copyright, system,
  and step 1->N
 time = 1 will enable time-based outputs, such as the date, current time,
  and various timers based on either real, system, or simulated time series
 url = 1 will enable url specific debugging
 warn = 1 with complete being 0 activates the warn protocols

 """
 backend = 0
 complete = 1
 lab = 0
 server = 0
 state = 0
 steps = 1
 time = 0
 url = 0
 warn = 0

