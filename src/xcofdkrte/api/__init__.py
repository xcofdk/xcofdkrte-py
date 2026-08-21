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
# Import libs / modules
# ------------------------------------------------------------------------------
from .cdefs import override
from .cdefs import EExecutionCmdID
from .cdefs import CompoundTUID
from .cdefs import ILcFailure
from .cdefs import ELineEnding
from .cdefs import ERtePolicyID
from .cdefs import EProcessStartMethodID
from .cdefs import EXmpPredefinedID
from .cdefs import EXmsgPredefinedID

from .apiif import IRteConfig
from .apiif import IPayload
from .apiif import IXPayload
from .apiif import IMessageHeader
from .apiif import IMessage
from .apiif import ITaskProfile
from .apiif import ITask
from .apiif import IRCTask
from .apiif import IRCCommTask
from .apiif import ITaskError
from .apiif import ITaskException
from .apiif import IProcess
from .apiif import IPTException
from .apiif import IPTWrappedException

from _rfwg.gimpl import _HCAAFH


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
def XRteApiXtor(apir_):
    return _HCAAFH._HMAI()(apir_)
