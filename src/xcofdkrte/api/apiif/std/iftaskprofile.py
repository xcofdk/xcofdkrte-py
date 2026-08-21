# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : iftaskprofile.py
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
from xcofdkrte.api.cdefs import EExecutionCmdID


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class ITaskProfile:
    """
    This interface class represents the read-only collection of all
    pre-instantiation properties which were needed to be laid out for the
    runtime configuration of a task instance to be created.

    For quick orientation and guidance on by when to use which API property,
    the interface is arranged in subsets each of them labeled in accordance to
    the given logical context by a comment block of the form:
        >>> # --------------------------------------------------------------
        >>> # SecNo) title of interface subset
        >>> # --------------------------------------------------------------

    Currently available interface subsets of this class are as follows:
        1) c-tor / built-in
        2) API basic (read-only) configuration
        3) API 3-PhXF configuration
        4) API queue configuration
        5) API timing configuration
    """

    __slots__ = []


    # --------------------------------------------------------------------------
    # 1) c-tor / built-in
    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.
        """
        pass


    def __str__(self) -> str:
        """
        Returns:
        ----------
            A nicely printable string representation of this instance.
        """
        pass
    # --------------------------------------------------------------------------
    #END 1) c-tor / built-in
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # 2) API basic (read-only) configuration
    # --------------------------------------------------------------------------
    @property
    def isMainTask(self) -> bool:
        """
        Returns:
        ----------
            True if this instance is the configuration of application's main
            task, False otherwise.

        Note:
        ------
            - The property defaults to False.
            - It is set to True when creating application's main task.
        """
        pass


    @property
    def isPrivilegedTask(self) -> bool:
        """
        Returns:
        ----------
            True if task(s) to be created using this instance shall be
            considered priviledged, False otherwise.

        Note:
        ------
            - The property defaults to False.
            - Privileged task instances are granted particular rights or
              permissions.
        """
        pass


    @property
    def isSyncTask(self) -> bool:
        """
        Returns:
        ----------
            True for configuration of synchronous execution type, False
            otherwise.

        Note:
        ------
            - The property defaults to False.
        """
        pass


    @property
    def aliasName(self) -> str:
        """
        Returns:
        ----------
            If configured the alias name (to be) used for a task instance,
            None otherwise.

        Note:
        ------
            - The property defaults to None.
            - If not configured, then the framework will later auto-generate
              one based on the type of the task instance to be created:
                Tsk_<INST_NO>   : for instances of class IRCTask without
                                  external queue support
                CTsk_<INST_NO>  : for instances of class IRCTask with
                                  external queue support
              with:
                - 'INST_NO' is the unique instance number of the task instance.
                - 'C' stands for 'capable of full Communication',
                  something available to a task only if created with
                  support for external queue requested for.
            - Also, for a configured alias name with a trailing '_' the
              above-mentioned 'INST_NO' will be appended to.

        See:
        -----
            >>> ITaskProfile.isExternalQueueEnabled
        """
        pass
    # --------------------------------------------------------------------------
    #END 2) API basic (read-only) configuration
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # 3) API 3-PhXF configuration
    # --------------------------------------------------------------------------
    @property
    def isRunPhaseEnabled(self) -> bool:
        """
        Returns:
        ----------
            True if the run phase of task's 3-PhXF is enabled, False otherwise.

        Note:
        ------
            - The property defaults to True.
            - It resolves to False, if and only if the instacne is configured
              to support blocking external queue.

        See:
        -----
            >>> ITaskProfile.isExternalQueueBlocking
        """
        pass


    @property
    def isSetupPhaseEnabled(self) -> bool:
        """
        Returns:
        ----------
            True if the setup phase of task's 3-PhXF is enabled, False
            otherwise.

        Note:
        ------
            - The property defaults to False.
        """
        pass


    @property
    def isTeardownPhaseEnabled(self) -> bool:
        """
        Returns:
        ----------
            True if the teardown phase of task's 3-PhXF is enabled, False
            otherwise.

        Note:
        ------
            - The property defaults to False.
        """
        pass
    # --------------------------------------------------------------------------
    #END 3) API 3-PhXF configuration
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # 4) API queue configuration
    # --------------------------------------------------------------------------
    @property
    def isInternalQueueEnabled(self) -> bool:
        """
        Returns:
        ----------
            True if a task is enabled to have support for internal queue, False
            otherwise.

        Note:
        ------
            - The property defaults to False.
        """
        pass


    @property
    def isExternalQueueEnabled(self) -> bool:
        """
        Returns:
        ----------
            True if a task is enabled to have support for external queue, False
            otherwise.

        Note:
        ------
            - The property defaults to False.

        See:
        -----
            >>> ITaskProfile.isExternalQueueBlocking
        """
        pass


    @property
    def isExternalQueueBlocking(self) -> bool:
        """
        Returns:
        ----------
            True if a task is enabled to have support for blocking external
            queue, False otherwise.

        Note:
        ------
            - The property defaults to False.
            - If enabled, then support for external queue is enabled (if not
              done yet), too, while the configuration of the run phase of such
              a taks become disabled.

        See:
        -----
            >>> ITaskProfile.isRunPhaseEnabled
            >>> ITaskProfile.isExternalQueueEnabled
        """
        pass
    # --------------------------------------------------------------------------
    #END 4) API queue configuration
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # 5) API timing configuration
    # --------------------------------------------------------------------------
    @property
    def isCyclicRunPhase(self) -> bool:
        """
        Returns:
        ----------
            True if the configured run phase frequency is larger than 0 (i.e.
            meant as an instruction to the framework to execute the run phase
            repeatedly), False otherwise.

        Note:
        ------
            - Whether the run phase of a task is cyclically executed by the
              framework is basically controlled by the return value of the
              respective 3-PhXF callback method.
            - However, if this property resolves to True, then the framework
              will execute the above-mentioned callback at the specified
              frequency, as long as it returns with an indication to continue
              the execution by the next iteration, i.e. 'EExecutionCmdID'.
            - Also, the application code may use it as a supplementary property
              to control the return value of the run phase callback
              programmatically for advanced use cases.

        See:
        -----
            >>> ITaskProfile.isSingleCycleRunPhase
            >>> ITaskProfile.isRunPhaseEnabled
            >>> ITaskProfile.isExternalQueueEnabled
            >>> ITaskProfile.runPhaseFrequencyMS
            >>> EExecutionCmdID.CONTINUE
        """
        pass


    @property
    def isSingleCycleRunPhase(self) -> bool:
        """
        Returns:
        ----------
            True if the configured run phase frequency is set to 0 (i.e. meant
            as an instruction to the framework to execute the runphase only
            once), False otherwise.

        Note:
        ------
            - Whether the run phase of a task is cyclically executed by the
              framework is basically controlled by the return value of the
              respective 3-PhXF callback method.
            - However, if this property resolves to True, then the framework will
              execute the above-mentioned callback only once, even if it returned
              with an indication to continue the execution by the next iteration,
              i.e. 'EExecutionCmdID'.
            - Also, the application code may use it as a supplementary property
              to control the return value of the run phase callback
              programmatically for advanced use cases.

        See:
        -----
            >>> ITaskProfile.isCyclicRunPhase
            >>> ITaskProfile.isRunPhaseEnabled
            >>> ITaskProfile.isExternalQueueEnabled
            >>> ITaskProfile.runPhaseFrequencyMS
            >>> EExecutionCmdID.CONTINUE
        """
        pass


    @property
    def runPhaseFrequencyMS(self) -> int:
        """
        Returns:
        ----------
            A non-negatve integer value as amount of time (in milliseconds) used
            to configure a task's run phase frequency.

        Note:
        ------
            - It defaults to a pre-defined value of:
                    0 : for synchronous tasks (that is non-cyclic)
                  100 : for asynchronous tasks (that is cyclic)
            - Tasks, however, may also have been configured to run
              (non-)cyclically regardless of their execution type.

        See:
        -----
            >>> ITaskProfile.isCyclicRunPhase
            >>> ITaskProfile.isSingleCycleRunPhase
        """
        pass


    @property
    def runPhaseMaxProcessingTimeMS(self) -> int:
        """
        Returns:
        ----------
            A non-negatve integer value as amount of time (in milliseconds)
            used to configure the estimated max. processing time of each
            iteration of the run phase.

        Note:
        ------
            - It defaults to a pre-defined value of 50 [ms].
        """
        pass
    # --------------------------------------------------------------------------
    #END 5) API timing configuration
    # --------------------------------------------------------------------------
#END class ITaskProfile
