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


"""
Subpackage 'xcofdkrte.api.cdefs' provides the API of commonly used definitions and
data types available through below modules:
   - fwdefs
   - xmpdefs
   - xmsgdefs
"""


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
from .std.fwdefs   import CompoundTUID
from .std.fwdefs   import EExecutionCmdID
from .std.fwdefs   import override
from .std.fwdefs   import ILcFailure
from .std.fwdefs   import ELineEnding
from .std.fwdefs   import ERtePolicyID
from .std.xmpdefs  import EProcessStartMethodID
from .std.xmpdefs  import EXmpPredefinedID
from .std.xmsgdefs import EXmsgPredefinedID
