# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : ifprocessxcp.py
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
from typing  import Union

from xcofdkrte.api import ERtePolicyID


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class IPTException(Exception):
    """
    Instances of this class are exceptions raised during execution of the target
    callback function of a child process, i.e. of an instance of interface class
    IProcess.

    Whenever such an exception is raised on target side, the framework will
    provide a reference to the transferred copy of that exception via respective
    property of the affected instance of class IProcess.

    An exception using an instance of this class may appear in two ways:
        - as an abnormal condition encountered on target side and described by a
          (short) message and an error code, or
        - caused by another exception raised on target side.

    Note:
    ------
        - This feature of child processes is available only if the related RTE
          policy for exception tracking of child processes is not disabled.
        - Also, if the byte stream size of an instance of this class exceeds the
          max. size of supplied data specified for the affected child process,
          then a so-called 'wrapped' (and compact) version (which is small
          enough to be transferred) will be used instead.

    See:
    -----
        - class IProcess
        >>> IPTWrappedException
        >>> ERtePolicyID.eDisableExceptionTrackingOfChildProcesses
    """


    # --------------------------------------------------------------------------
    # c-tor / built-in
    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.
        """
        super().__init__(type(self).__name__)


    def __str__(self):
        """
        Returns:
        ----------
            A nicely printable string representation of this instance.
        """
        pass
    # --------------------------------------------------------------------------
    #END c-tor / built-in
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # API
    # --------------------------------------------------------------------------
    @property
    def isWrappedException(self) -> bool:
        """
        Returns:
        ----------
            True if this instance represents the wrapped version of another
            non-wrapped instance of this class, False otherwise.

        Note:
        ------
            - A wrapped exception is always an instance of class
              IPTWrappedException derived from this interface class.

        See:
        -----
            >>> IPTException.__init__()
            >>> IPTWrappedException
        """
        pass


    @property
    def message(self) -> str:
        """
        Returns:
        ----------
            Short description of this instance.

        See:
        -----
            >>> IPTException.code
            >>> IPTException.reason
        """
        pass


    @property
    def code(self) -> int:
        """
        Returns:
        ----------
            A positive integer value as the error code of this instance.

        See:
        -----
            >>> IPTException.message
            >>> IPTException.reason
        """
        pass


    @property
    def reason(self) -> Union[BaseException, None]:
        """
        Returns:
        ----------
            - None if this instance was not created because of an exception
              raised on target side, but rather interally constructed by the
              framework,
            - an exception object representing the root cause otherwise.

        See:
        -----
            >>> IPTException.message
            >>> IPTException.code
        """
        pass
    # --------------------------------------------------------------------------
    #END API
    # --------------------------------------------------------------------------
#END class IPTException


class IPTWrappedException(IPTException):
    """
    Derived from class IPTException, instances of this class represent exceptions
    raised on target side, too.

    A wrapped exception always represent the compact version of a non-wrapped
    instance of class IPTException.

    Note:
    ------
        - This feature of child processes is available only if the related RTE
          policy for exception tracking of child processes is not disabled.

    See:
    -----
        - class IProcess
        >>> IPTException
        >>> ERtePolicyID.eDisableExceptionTrackingOfChildProcesses
    """


    # --------------------------------------------------------------------------
    # c-tor / built-in
    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.
        """
        super().__init__()


    def __str__(self):
        """
        Returns:
        ----------
            A nicely printable string representation of this instance.
        """
        pass
    # --------------------------------------------------------------------------
    #END c-tor / built-in
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # API
    # --------------------------------------------------------------------------
    @IPTException.message.getter
    def message(self) -> str:
        """
        Returns:
        ----------
            Short description of this instance.

        See:
        -----
            >>> IPTWrappedException.code
            >>> IPTWrappedException.reason
        """
        pass


    @IPTException.code.getter
    def code(self) -> int:
        """
        Returns:
        ----------
            A positive integer value as the error code of this instance.

        See:
        -----
            >>> IPTWrappedException.message
            >>> IPTWrappedException.reason
        """
        pass


    @IPTException.reason.getter
    def reason(self) -> str:
        """
        Returns:
        ----------
            - A compact string representation of a non-wrapped instance of class
              IPTException this instance is wrapping it.

              It may or may not include callstack and/or traceback of the root
              cause of the exception raised on target side.

        See:
        -----
            >>> IPTException.reason
            >>> IPTWrappedException.message
            >>> IPTWrappedException.code
            >>> IPTWrappedException.reasonType
            >>> IPTWrappedException.IsReasonType()
        """
        pass


    @property
    def reasonType(self) -> type:
        """
        Returns:
        ----------
            Type information of the root cause of the exception raised on
            target side.

        See:
        -----
            >>> IPTWrappedException.IsReasonType()
        """
        pass


    def IsReasonType(self, cls_ : type) -> bool:
        """
        Returns:
        ----------
            True if the type argument passed to passes a check for the exact
            matching to the reason type of this instance, False otherwise.

        See:
        -----
            >>> IPTWrappedException.reasonType
        """
        pass
    # --------------------------------------------------------------------------
    #END API
    # --------------------------------------------------------------------------
#END class IPTWrappedException
