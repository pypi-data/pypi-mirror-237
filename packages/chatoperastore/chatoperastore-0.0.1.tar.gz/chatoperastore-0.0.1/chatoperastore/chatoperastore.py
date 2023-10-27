#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/store/sdk/python/chatoperastore/chatoperastore.py
# Author: Hai Liang Wang
# Date: 2023-10-27:09:27:26
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2023-10-27:09:27:26"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

# Get ENV
ENVIRON = os.environ.copy()

def download_licensedfile(licenseId, serverinst_id = None, service_name = None):
    '''
    Download Licensed file
    '''
    print('licenseId ', licenseId)