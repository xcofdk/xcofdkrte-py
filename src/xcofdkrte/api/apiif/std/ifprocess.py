# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : ifprocess.py
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
from typing import Any
from typing import Union

from xcofdkrte.api import ERtePolicyID
from .ifprocessxcp import IPTException
from .ifprocessxcp import IPTWrappedException


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class IProcess:
    """
    This class represents the heavy-weight counterpart of the interface class
    ITask for concurrancy or multitasking.

    Instances of this class are child processes, basically constructed by
    passing a callable object. Later, they can be started for parallel execution
    with the launching task continues its own exection as usual.

    For quick orientation and guidance on by when to use which one, the
    interface is arranged in subsets each of them labeled in accordance to the
    given logical context by a comment block of the form:
        >>> # --------------------------------------------------------------
        >>> # SecNo) title of interface subset
        >>> # --------------------------------------------------------------

    Currently available interface subsets of this class are as follows:
        1) c-tor / built-in
        2) API basic process properties
        3) API start, stop etc.
        4) API process state

    Note:
    ------
        Any request to the API of this class will be (noiselessly) discarded,
        if the subsystem of multiprocessing, i.e. 'xmp', is disabled via
        framework's RTE configuration.

    See:
    -----
        >>> ERtePolicyID.eDisableSubSystemMultiProcessing
    """


    # --------------------------------------------------------------------------
    # 1) c-tor / built-in
    # --------------------------------------------------------------------------
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
    # --------------------------------------------------------------------------
    #END 1) c-tor / built-in
    # --------------------------------------------------------------------------


    # ------------------------------------------------------------------------------
    # 2) API basic process properties
    # ------------------------------------------------------------------------------
    @property
    def isAttachedToFW(self):
        """
        Returns:
        ----------
            True if this instance is (still) attached to the framework,
            False otherwise.

        Note:
        ------
            - An instance of this class correctly constructed is always attached
              to the framework until it is requested to be detached from the
              framework.

        See:
        -----
            >>> IProcess.isDetachedFromFW
            >>> IProcess.DetachFromFW()
        """
        pass


    @property
    def isDetachedFromFW(self):
        """
        Returns:
        ----------
            True if this instance is (no longer) attached to the framework,
            False otherwise.

        Note:
        ------
            - An instance of this class correctly constructed is always attached
              to the framework until it is requested to be detached from the
              framework.

        See:
        -----
            >>> IProcess.isAttachedToFW
            >>> IProcess.DetachFromFW()
        """
        pass


    @property
    def aliasName(self) -> str:
        """
        Returns:
        ----------
            (Auto-generted) alias name of this instance.
        """
        pass


    @property
    def processPID(self) -> int:
        """
        Returns:
        ----------
            PID of the associated host process of this instance if started,
            None otherwise.

        See:
        -----
            >>> IProcess.Start()
        """
        pass


    @property
    def processName(self) -> str:
        """
        Returns:
        ----------
            (Auto-generted) name of this instance.
        """
        pass


    @property
    def processExitCode(self) -> int:
        """
        Getter property for exit code of this instance.

        Returns:
        ----------
            - None if not started or not terminated yet,
            - 0 upon successful termination,
            - an integer value otherwise.

        Note:
        ------
            The exit code value of a failed child process indicates an error
            code:
                - Unless terminated due to the 'SystemExit' exception caught
                  by the child process (or otherwise issued termination
                  signal), the exit code is always a positive integer value.
                - Otherwise, it is the negation of the integer value of a
                  signal, e.g. 'SIGTERM', which caused the termination.

        See:
        -----
            >>> IProcess.isDone
            >>> IProcess.isFailed
            >>> IProcess.isTerminated
            >>> IProcess.processException
            >>> IProcess.processExitCodeAsStr
            >>> IProcess.Start()
            >>> IProcess.Terminate()
        """
        pass


    @property
    def processExitCodeAsStr(self) -> Union[str, None]:
        """
        Returns:
        ----------
            The exit code (if available) of this child process as a string object,
            None otherwise.

        See:
        -----
            >>> IProcess.processExitCode
        """
        pass


    @property
    def processSuppliedData(self) -> Any:
        """
        Getter property for the application-specific result of execution.

        Returns:
        ----------
            The (application-specific) data (if any) supplied by the child
            process through the returned value of the target callback function
            passed to the constructor of the derived class instantiating child
            processes.

        Note:
        ------
            - Child processes may supply a byte stream as the result of their
              execution, too.
            - If so, this property will return that byte stream as is.

        See:
        -----
            >>> IProcess.Start()
        """
        pass


    @property
    def processException(self) -> Union[IPTException, IPTWrappedException, None]:
        """
        Returns:
        ----------
            - None if exception tracking of child processes is disabled via
              RTE configuration,
            - None if this instance is not started,
            - None if this instance is terminated upon successful termination,
            - None if no exception was raised while execution of the target
              callback function passed to the constructor of the derived class
              instantiating child processes,
            - that raised exception otherwise.

        See:
        -----
            >>> IPTException
            >>> IPTWrappedException
            >>> IProcess.isDone
            >>> IProcess.isFailed
            >>> IProcess.isTerminated
            >>> IProcess.Start()
            >>> ERtePolicyID.eDisableExceptionTrackingOfChildProcesses
        """
        pass
    # ------------------------------------------------------------------------------
    #END 2) API basic process properties
    # ------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------
    # 3) API start, stop etc.
    # ------------------------------------------------------------------------------
    def Start(self, *args_, **kwargs_) -> bool:
        """
        Request to start this instance.

        It starts the host process associated to this instance making the
        associated callable target is called.

        Parameters:
        -------------
            - args_ :
              positional arguments (if any) to be passed to the callable target
              when started.
            - kwargs_ :
              keyword arguments (if any) to be passed to the callable target
              when started.

        Returns:
        ----------
            False if this instance is detached from the framework, or if it has
            been started already, or if the start of the associated host process
            failed, True otherwise.

        Note:
        ------
            - This operation is not available to applications in limited RTE
              modes.

        See:
        -----
            >>> IProcess.isAttachedToFW
            >>> IProcess.isStarted
            >>> IProcess.isTerminated
            >>> IProcess.DetachFromFW()
        """
        pass


    def Join(self, maxWaitTime_: Union[int, float, None] =None) -> bool:
        """
        Request to join this innstance, thus synchronously waiting for its
        termination.

        Parameters:
        -------------
            - maxWaitTime_ :
              if None it will wait forever. Otherwise, it will wait for the
              specified amount of time (milliseconds for integer values or
              seconds for floating-point values) before the operation returns.

        Returns:
        ----------
            True if the operation succeeds, False otherwise.

        Note:
        ------
            - This operation is not available to applications in limited RTE
              modes.
            - Requests to join a child process which is detached from the
              framework or not started yet or terminated already will be ignored.

        See:
        -----
            >>> IProcess.isAttachedToFW
            >>> IProcess.isStarted
            >>> IProcess.isTerminated
        """
        pass


    def Terminate(self):
        """
        Request to terminate this innstance.

        The framework will ask the associated host process to terminate.
        Also, it will wait for a short, pre-defined max. amount of time as long
        as the host process is not terminated.

        Finally, this instance is detached from the framwork with its process
        state is updated to the last available one before return.

        Note:
        ------
            - This operation is available to applications even in limited RTE
              modes.
            - Unless requested to do so, the framework never terminates child
              processes on its own.
            - Requests to terminate a child process which is detached from the
              framework or not started yet or terminated already will be
              ignored.

        See:
        -----
            >>> IProcess.isAttachedToFW
            >>> IProcess.isStarted
            >>> IProcess.isTerminated
            >>> IProcess.isTerminatedByCmd
            >>> IProcess.DetachFromFW()
        """
        pass


    def DetachFromFW(self):
        """
        Request to detach this instance from the framework.

        Note:
        ------
            - This operation is available to applications even in limited RTE
              modes.
            - Main purpose of detaching child processes from the framework is
              releasing application or system resources used for them.
            - Detaching is always done automatically by the framework upon
              termination of child processes.
            - Detaching a child process from the framework by intention and
              before its termination, is much like immediately releasing all
              resources used for it.
            - As soon as a child process is detached from the framework, it
              won't be able to use all of its reqular API anymore. Its execution
              state will be set in accordance to the state right after internal
              handling of the request, e.g. 'done' or 'running', and not updated
              anymore.

        See:
        -----
            >>> IProcess.isAttachedToFW
        """
        pass
    # ------------------------------------------------------------------------------
    #END 3) API start, stop etc.
    # ------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------
    # 4) API process state
    # ------------------------------------------------------------------------------
    @property
    def isStarted(self) -> bool:
        """
        Returns:
        ----------
            True if this instance has been started, False otherwise.

        Note:
        ------
            - A child process is considered 'started', as soon as a request to
              start it is succeeded.
            - However, the fact of being 'started' does not necessarily imply
              any specific, subsequent state during the lifecycle of that child
              process, e.g. 'running'.
            - But, for all subsequent process states, it is always considered
              'started'.

        See:
        -----
            >>> IProcess.isRunning
            >>> IProcess.Start()
        """
        pass


    @property
    def isRunning(self) -> bool:
        """
        Returns:
        ----------
            - False if this instance is not started yet,
            - False if the associated host process is not alive anymore or
              terminated already by providing an exit code,
            - False if this instance has been requested to terminate,
            - True otherwise.

        Note:
        ------
            - A child process is considered 'running', as soon as a request to
              start it is succeeded.

        See:
        -----
            >>> IProcess.isTerminated
            >>> IProcess.isTerminatedByCmd
            >>> IProcess.Start()
            >>> IProcess.Terminate()
        """
        pass


    @property
    def isDone(self) -> bool:
        """
        Returns:
        ----------
            True if this instance has finished its execution upon normal
            termination indicated by an exit code of 0, False otherwise.

        See:
        -----
            >>> IProcess.isFailed
            >>> IProcess.isTerminated
            >>> IProcess.processExitCode
        """
        pass


    @property
    def isFailed(self) -> bool:
        """
        Returns:
        ----------
            True if this instance has finished its execution upon abnormal
            termination indicated by an exit code other than 0, False otherwise.

        See:
        -----
            >>> IProcess.isDone
            >>> IProcess.isTerminated
            >>> IProcess.processExitCode
        """
        pass


    @property
    def isTerminated(self) -> bool:
        """
        As long as a child process is in stste 'running', this property will
        resolve to False.

        Returns:
        ----------
            - False if this instance is not started yet,
            - False as long as this instance is in state 'running',
            - True otherwise.

        See:
        -----
            >>> IProcess.isStarted
            >>> IProcess.isDone
            >>> IProcess.isFailed
            >>> IProcess.isRunning
            >>> IProcess.isTerminatedByCmd
            >>> IProcess.processExitCode
            >>> IProcess.Terminate()
        """
        pass


    @property
    def isTerminatedByCmd(self) -> bool:
        """
        Returns:
        ----------
            - False if this instance is not started yet,
            - False as long as this instance is in state 'running',
            - False if this instance is terminated already with or without
              having a request to terminate it by intention,
            - True after a request to terminate this instance by intention with
              the framework was not able to establish the exit code and/or the
              aliveness of the associated host process.

        See:
        -----
            >>> IProcess.isStarted
            >>> IProcess.isRunning
            >>> IProcess.isTerminated
            >>> IProcess.processExitCode
            >>> IProcess.Terminate()
        """
        pass
    # ------------------------------------------------------------------------------
    #END 4) API process state
    # ------------------------------------------------------------------------------
#END class IProcess
