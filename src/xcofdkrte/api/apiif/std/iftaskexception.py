# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : iftaskexception.py
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


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class ITaskException(Exception):
    """
    Instances of this class are exceptions raised by the framework.

    The purpose of this class is to inform currently running application task,
    i.e. an instance of the interface class IRCTask, about submitted fatal errors
    which need to be qualified or aproved.

    For more detail refer to the respective wiki page discussing error handling.
    """


    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.

        Note:
        ------
            - Instances of this class are created by the framework only.
            - They are raised during the qualificaiton procedure of submitted
              fatal errors.
        """
        super().__init__()


    def __str__(self):
        """
        Returns:
        ----------
            A nicely printable string object as representation of this instance.
        """
        return super().__str__()



    @property
    def uniqueID(self) -> int:
        """
        Returns:
        ----------
            An integer value as unique ID of this instance.
        """
        pass


    @property
    def message(self) -> str:
        """
        Returns:
        ----------
            A string object giving (short) description of the exception cause
            as the respective fatal error was submitted.
        """
        pass


    @property
    def errorCode(self) -> int:
        """
        Returns:
        ----------
            None if not available, otherwise an integer value as the error code
            assigned when the respective fatal error was submitted.

        Note:
        ------
            The error code (if any) of fatal error messages submitted are always
            positive integer values, unless they were submitted by the framework.
        """
        pass


    @property
    def callstack(self) -> str | None:
        """
        Returns:
        ----------
            None if not available, otherwise the callstack retrieved at the time
            of detection of the respective fatal error.
        """
        pass


    @property
    def traceback(self) -> str | None:
        """
        Returns:
        ----------
            None if not available, otherwise the traceback retrieved at the time
            of detection of the respective fatal error.
        """
        pass
#END class ITaskException
