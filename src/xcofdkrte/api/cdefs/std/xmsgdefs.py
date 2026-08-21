# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : xmsgdefs.py
#
# Copyright(c) 2023-2026 Farzad Safa (farzad.safa@xcofdk.com)
#
# This file is distributed under the same license provided through the SOFTWARE it is part of.
# A copy of the license file can also be obtained following the link below:
#     https://github.com/xcofdk/xcofdkrte-py/blob/master/LICENSE.txt
# -----------------------------------------------------------------------------------------------


"""
Module 'xmsgdefs' is part of framework's messaging subsystem, i.e. 'xmsg'.

It mainly provides commonly used type definition below:
    >>> EXmsgPredefinedID
"""

# ------------------------------------------------------------------------------
# Import libs / modules
# ------------------------------------------------------------------------------
from enum import unique
from enum import IntEnum


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
@unique
class EXmsgPredefinedID(IntEnum):
    """
    Enum class providing pre-defined IDs specified for use in the context of
    task comminication via messaging.

    The IDs currently defined are as follows:
        - DontCare:
          usable wherever wildcard specification of a communication or messaging
          endpoint is applicable. When specified by this ID any possible
          receiver/sender endpoint is intended.

        - MainTask:
          unique ID referring to application's main task, i.e. the singleton
          instance of the interface class IRCTask, whenever anonymous (or alias)
          addressing is applicable.

        - Broadcast:
          unique ID referring to the wildcard specification of any possible
          receiver endpoint available. This ID is part of the anonymous (or
          alias) addressing, too.

        - MinUserDefinedID:
          unique ID supposed to be used by applications as starting point to
          define their own, custom IDs. In other words, (the integer value of)
          any application-specific ID must not be less than this ID.

    Note:
    ------
        - Applications are recommended to always introduce their own enum
          classes (if any) as this enum class must not be changed or extended
          by additional enum members.
    """

    DontCare         = 0
    MainTask         = 1
    Broadcast        = 2
    MinUserDefinedID = 5001
#END class EXmsgPredefinedID
