# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------
# File   : ifxpayload.py
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
from .ifpayload import IPayload


# ------------------------------------------------------------------------------
# Interface
# ------------------------------------------------------------------------------
class IXPayload(IPayload):
    """
    Subclassing the generic payload interface, this interface class represents
    payload instances created by the framework by default whenever needed.

    That is, it represents the usual funtionality expected from a typical
    container type. In addition, it provides a few supplementary API functions
    commonly expected from a collection-like payload object.

    See:
    -----
        >>> IPayload
    """


    __slots__ = []


    def __init__(self):
        """
        Constructor of this instance used by the derived class instantiating
        new instances of this class.
        """
        super().__init__()


    # --------------------------------------------------------------------------
    # Interface inherited from IPayload
    # --------------------------------------------------------------------------
    @staticmethod
    def CustomSerializePayload(payload_) -> bytes:
        """
        Custom serialization is not supported by this class.

        See:
        -----
            - IPayload.SerializePayload()
        """
        return None


    @staticmethod
    def CustomDeserializePayload(dump_: bytes):
        """
        Custom de-serialization is not supported by this class.

        See:
        -----
            - IPayload.DeserializePayload()
        """
        return None
    # --------------------------------------------------------------------------
    #END Interface inherited from IPayload
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # supplementary API
    # --------------------------------------------------------------------------
    @property
    def payloadContainer(self) -> dict:
        """
        Getter property to get access to the underlying container.

        This property is provided for convenient as it enables direct
        manipulation of the underlying container right after instantiation.

        Returns:
        ----------
            the underlying container object of this instance if valid, None
            otherwise.

        See:
        -----
            >>> IPayload.isValidPayload
            >>> IXPayload.UpdatePayloadContainer()
        """
        pass


    def SetParameter(self, paramKey_, paramValue_) -> bool:
        """
        Add or update a parameter.

        Managed data items are stored by the usual key-value principle of
        collection types.

        Parameters:
        -------------
            - paramKey_ :
              key of the parameter to be added (or updated).
            - paramValue_ :
              value of (or reference to) the parameter to be added or updated.

        Returns:
        ----------
            True if the operation succeeds, False otherwise.

        See:
        -----
            >>> IPayload.isValidPayload
            >>> IPayload.GetParameter()
            >>> IPayload.IsIncludingParameter()
            >>> IXPayload.UpdatePayloadContainer()
        """
        pass


    def UpdatePayloadContainer(self, dictParams_: dict, bShallowCopy_ =True) -> bool:
        """
        Add or update a bunch of parameters.

        Managed data items are stored by the usual key-value principle of
        collection types.

        Parameters:
        -------------
            - dictParams_ :
              collection object containing parameters to be added (or updated).
            - bShallowCopy_ :
              if True then the built-in 'copy' operation of mutable collection
              types will be applied to the passed in collection object before
              actual update of the underlying container object takes place.

        Returns:
        ----------
            True if the operation succeeds, False otherwise.

        See:
        -----
            >>> IPayload.isValidPayload
            >>> IPayload.IsIncludingParameter()
            >>> IXPayload.GetParameter()
            >>> IXPayload.SetParameter()
        """
        pass
    # --------------------------------------------------------------------------
    # supplementary API
    # --------------------------------------------------------------------------
#END class IXPayload
