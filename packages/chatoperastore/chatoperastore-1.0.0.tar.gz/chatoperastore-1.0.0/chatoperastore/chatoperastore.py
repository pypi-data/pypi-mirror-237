#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/store/sdk/python/chatoperastore/chatoperastore.py
# Author: Hai Liang Wang
# Date: 2023-10-27:09:27:26
#
# ===============================================================================

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

from .wget import download
from .logger import Logger, LN
from .exceptions import LicensedfileDownloadException

# Get ENV
ENVIRON = os.environ.copy()
logger = Logger(LN(__file__))

LICENSE_STORE_PROVIDER = os.getenv("LICENSE_STORE_PROVIDER", "https://store.chatopera.com")
ERROR_CODES = dict({
    404: "License not found",
    406: "Licensed file metadata error",  # bad file extenstion of Licensedfile of productModel
    400: "Bad Request",  # File download interrupt
    402: "Need purchase valid license from license store",  # need purchase valid license from license store
    424: "Licensedfile not exist of productModel",
    501: "Product not exist or peer product model does not contain licensed file",
    500: "Product model not found",
})


def download_licensedfile(license_id, save_to_filepath, serverinst_id=None, service_name=None):
    '''
    Download Licensed file
    '''
    if not license_id:
        raise ValueError("licenseId is required for download licensed file")

    if not (isinstance(license_id, str) and license_id.strip()):
        raise ValueError("licenseId should be a string and not blank.")

    dl_url = "%s/dl/%s.gz" % (LICENSE_STORE_PROVIDER, license_id)

    if serverinst_id or service_name:
        dl_url += "?"

    if serverinst_id:
        dl_url += "serverId=%s" % serverinst_id

    if service_name:
        if not dl_url.endswith("?"):
            dl_url += "&"
        dl_url += "servicename=%s" % service_name

    try:
        logger.info("dl_url %s" % dl_url)
        download(dl_url, save_to_filepath)
    except BaseException as e:
        if isinstance(e, LicensedfileDownloadException):
            if e.errcode in ERROR_CODES:
                logger.error("Error %s %s" % (e.errcode, ERROR_CODES[e.errcode]))
            else:
                print("[download_licensedfile] error")
                print(e)
        else:
            print(e)

        if save_to_filepath and os.path.exists(save_to_filepath) and save_to_filepath.endswith(".gz"):
            os.remove(save_to_filepath)

        raise e
