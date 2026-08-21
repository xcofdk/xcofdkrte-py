# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : xmpdefs.py
#
# Copyright(c) 2023-2026 Farzad Safa (farzad.safa@xcofdk.com)
#
# This file is distributed under the same license provided through the SOFTWARE it is part of.
# A copy of the license file can also be obtained following the link below:
#     https://github.com/xcofdk/xcofdkrte-py/blob/master/LICENSE.txt
# -----------------------------------------------------------------------------------------------


"""
Module 'xmpdefs' is part of framework's multiprocessing subsystem, i.e. 'xmp'.

It mainly provides commonly used type definitions below:
    >>> EXmpPredefinedID
    >>> EProcessStartMethodID
"""


# ------------------------------------------------------------------------------
# Import libs / modules
# ------------------------------------------------------------------------------
from enum import auto
from enum import unique
from enum import IntEnum


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
@unique
class EProcessStartMethodID(IntEnum):
    """
    Enum class providing symbolic IDs for process start methods recommended to
    use in connection with framework's subsystem of multiprocessing.

    Python's multiprocessing package defines three possible start methods:
        - spawn
        - fork
        - forkserver

    Note:
    ------
        - For details of process start methods refer to the official
          documentation following link below:
              https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods
    """

    SystemDefault = 0
    Spawn         = auto()
    Fork          = auto()
    ForkServer    = auto()
#END class EProcessStartMethodID


@unique
class EXmpPredefinedID(IntEnum):
    """
    Enum class providing pre-defined IDs used in the context of framework's
    multiprocessing interface.

    The IDs currently defined are as follows:
        - MinSuppliedDataSize
          min. size of a byte stream representing the value or object (including
          None), also referred to as supplied data, returned by the target
          callback fucntion of a child process,

        - MaxSuppliedDataSize
          max. size of a byte stream representing the above-mentioned supplied
          data, (= 2146435072 or ca. 2GB)

        - DefaultSuppliedDataMaxSize:
          default value used for a child process as maximum length of a byte
          stream representing the above-mentioned supplied data.

          Current value of 10240 (i.e. 10 KB) is large enough for a byte stream
          occupying a list of up to 1022 integer values each equal to the
          built-in constant 'sys.maxsize'.

    Note:
    ------
        - This enum class and its members must not be changed or extended by
          additional enum members.

    See:
    -----
        - class XProcess
    """

    MinSuppliedDataSize        = 4
    MaxSuppliedDataSize        = 2146435072
    DefaultSuppliedDataMaxSize = 10240
#END class EXmpPredefinedID
