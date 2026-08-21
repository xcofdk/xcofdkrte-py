# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : __init__.py
#
# Copyright(c) 2023-2026 Farzad Safa (farzad.safa@xcofdk.com)
#
# This file is distributed under the same license provided through the SOFTWARE it is part of.
# A copy of the license file can also be obtained following the link below:
#     https://github.com/xcofdk/xcofdkrte-py/blob/master/LICENSE.txt
# -----------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# PYTHONPATH extension
# ------------------------------------------------------------------------------
import os
import sys
sys.path.extend(((_rteFW  := os.path.normpath(os.path.join(str(os.path.dirname(__file__)), '_xrte'))) not in sys.path) * [_rteFW])
sys.path.extend(((_rteFWA := os.path.normpath(os.path.join(str(os.path.dirname(__file__)), '_xrtea'))) not in sys.path) * [_rteFWA])
sys.path.extend(((_rteFWG := os.path.normpath(os.path.join(str(os.path.dirname(__file__)), '_xrteg'))) not in sys.path) * [_rteFWG])


# ------------------------------------------------------------------------------
# Import libs / modules
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
"""
The top-level package 'xcofdkrte' is an implementation of the runtime
environment, also referred to as RTE, of XCOFDK for the programming language
Python. 

The RTE, also referred to as the framework backend (or backend for short), is
designed to be used by Python programs via framework frontends. Such a frontend,
e.g. the top-lvel package 'xcofdk', represents the interaction layer of the
framework which user applications can use to run their task model utilized by
the features and services provided by the RTE.

Accordingly, the public API of the backend is used in two ways:
    - by the frontends to implement and provide their own public API,
    - transparently forwarded by the frontends, so backend's public API is
      made available to user applications, too.

In other words, the public API of the frontend at hand represents the API of
the framework of XCOFDK as a whole made available to user applications.


Public API of the RTE:
------------------------
Throughout this source documentation the term 'public API' is also reffered to
as 'API' for short. 

In general, the RTE provides its default API via corresponding subpackags called
'std'. They are always available regardless of the underlying licensing.

The default API of the RTE is composed of and explained in more detail by the
subpackages below:
    - xcofdkrte.api.apiif.std:
      providing basic interface classes supported by RTE.
    - xcofdkrte.api.cdefs.std:
      providing commonly used definitions and types.


Documentation:
----------------
The source code documentation, also referred to as 'this documentation', of the
API of the RTE frequently refers to the terms and basic concepts explained
in the documentation of framework frontends. For better readability this
documentation has chosen to not repeat those explanations, their knowledge will
be assumed throughout this documentation.

Also, note that this documentation intensively uses 'doctest' lines with a
leading '>>>'. They are not meant for any kind of testing purposes, but rather
for both:
    a) (highlighting of) embedded code snippet inside docstrings.
       Modern IDE editors, e.g. PyCharm (Community Edition), are able to
       display them as expected,
    b) cross referencing to existing documentation provided at some other place,
       e.g. to the respective API documentation of the parent class.
       Again, modern IDE editors are able to generate and display the 
       corresponding hyperlink, too.

Note:
------
    - Unless otherwise stated, the term 'RTE' and a given implementation of
      its architecture, e.g. the top-level package 'xcofdkrte', are often used
      interchangeably,

    - also, the terms 'XCOFDK', 'frameowrk', 'runtime environment' and 'RTE'
      are used interchangeably, too, throughout this documentation,

    - applications shall interface with the framework only using the public API
      provided by a frontend package of XCOFDK,

    - be aware that all subpackages named with a leading underscore (if any)
      compose the interal implementation (or private library) of the framework
      which is not designed to be imported by user applications.
"""


__version__ = '1.0'
__all__     = [ '__version__' ]
