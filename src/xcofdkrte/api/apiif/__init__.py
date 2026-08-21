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
Subpackage 'xcofdkrte.api.apiif' provides a collection of basic interface
classes supported by RTE.
"""


# ------------------------------------------------------------------------------
# Import libs / modules
# ------------------------------------------------------------------------------
from .std.ifpayload       import IPayload
from .std.ifxpayload      import IXPayload
from .std.ifmsgheader     import IMessageHeader
from .std.ifmessage       import IMessage
from .std.iftaskerror     import ITaskError
from .std.iftaskprofile   import ITaskProfile
from .std.iftask          import ITask
from .std.ifrctask        import IRCTask
from .std.ifrctask        import IRCCommTask
from .std.ifrteconfig     import IRteConfig
from .std.iftaskerror     import ITaskError
from .std.iftaskexception import ITaskException
from .std.ifprocessxcp    import IPTException
from .std.ifprocessxcp    import IPTWrappedException
from .std.ifprocess       import IProcess
