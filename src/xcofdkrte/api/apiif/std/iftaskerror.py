# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : iftaskerror.py
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
from typing import Union


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class ITaskError:
    """
    Instances of this interface class represent common API of qualified task
    error instances submitted by either the application or the framework.

    Such an instance is associated to the affected task instance managed and
    monitored by the framework.

    See:
    -----
        >>> ITaskError.isFatalError
        >>> ITaskError.uniqueID
        >>> ITaskError.message
        >>> ITaskError.errorCode
    """

    __slots__ = []


    # ------------------------------------------------------------------------------
    # c-tor / built-in
    # ------------------------------------------------------------------------------
    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.
        """
        pass

    def __str__(self):
        """
        Returns:
        ----------
            A nicely printable string representation of this instance.
        """
        pass
    # ------------------------------------------------------------------------------
    #END c-tor / built-in
    # ------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------
    # API
    # ------------------------------------------------------------------------------
    @property
    def isFatalError(self) -> bool:
        """
        Returns:
        ----------
            True if this instance is a fatal error, False otherwise
            (i.e. a non-fatal error, also referred to as user error).

        Note:
        ------
            - A fatal error at this level of abstraction is always a
              qualified one.
        """
        pass


    @property
    def uniqueID(self) -> int:
        """
        Returns:
        ----------
            A positive integer value as unique ID of this instance.
        """
        pass


    @property
    def message(self) -> str:
        """
        Returns:
        ----------
            A string object giving (short) description of the error cause when
            the respective, underlying error object was submitted.
        """
        pass


    @property
    def errorCode(self) -> Union[int, None]:
        """
        Returns:
        ----------
            None if not available, otherwise an integer value as the error code
            assigned when the respective, underlying error object was submitted.

        Note:
        ------
            The error code (if any) of submitted task errors are always
            positive integer values, unless they were submitted by the
            framework.
        """
        pass
    # ------------------------------------------------------------------------------
    #END API
    # ------------------------------------------------------------------------------
#END class ITaskError
