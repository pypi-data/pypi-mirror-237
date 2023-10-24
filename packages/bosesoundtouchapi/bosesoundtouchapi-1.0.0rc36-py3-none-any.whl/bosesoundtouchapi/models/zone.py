# external package imports.
from typing import Iterator
from xml.etree.ElementTree import Element, tostring

# our package imports.
from bosesoundtouchapi.bstutils import export
from bosesoundtouchapi.soundtouchwarning import SoundTouchWarning
from .zonemember import ZoneMember

@export
class Zone:
    """
    SoundTouch device Zone configuration object.
       
    This class contains the attributes and sub-items that represent a
    multiroom zone configuration of the device.
    """

    def __init__(self, masterDeviceId:str=None, masterIpAddress:str=None, isZoneMaster:bool=None, members:list=None,
                 root:Element=None
                 ) -> None:
        """
        Initializes a new instance of the class.
        
        Args:
            masterDeviceId (str):
                Master device identifier for this zone.
            masterIpAddress (str):
                Master device ipv4 address.
            isZoneMaster (bool):
                True if this zone object is a zone master; otherwise, False.
            members (list):
                List of `ZoneMember` objects that are under the control of this zone.
            root (Element):
                xmltree Element item to load arguments from.  
                If specified, then other passed arguments are ignored.
                
        Raises:
            SoundTouchWarning:
                If any zone member specified by the members argument is not a `ZoneMember`
                object, or if a device id was not supplied for each member.
        """
        self._Members = []
        
        if (root is None):
            
            self._MasterDeviceId:str = masterDeviceId
            self._MasterIpAddress:str = masterIpAddress
            self._IsZoneMaster:bool = isZoneMaster
            
            if masterIpAddress is None:
                self._IsZoneMaster = False
        
            if members != None:
                if isinstance(members, list):
                    member:ZoneMember    
                    for member in members:
                        if isinstance(member, ZoneMember):
                            self._Members.append(ZoneMember(root=member))

        else:
            
            self._MasterDeviceId:str = root.get('master')
            self._MasterIpAddress:str = root.get('senderIPAddress')
            self._IsZoneMaster:bool = bool(root.get('senderIsMaster', default='false') == 'true')
            
            for member in root.findall('member'):
                self._Members.append(ZoneMember(root=member))
        

    def __repr__(self) -> str:
        return self.ToString()


    def __iter__(self) -> Iterator:
        return iter(self._Members)


    def __len__(self) -> int:
        return len(self._Members)


    def __getitem__(self, key) -> ZoneMember:
        if isinstance(key, int) and 0 <= key < len(self):
            return self._Members[key]


    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self):
            self._Members[key] = value


    @property
    def IsZoneMaster(self) -> bool:
        """ Returns true if this zone object is a zone master; otherwise, false. """
        return self._IsZoneMaster


    @property
    def MasterDeviceId(self) -> str:
        """ Master device identifier for this zone. """
        return self._MasterDeviceId


    @property
    def MasterIpAddress(self) -> str:
        """ Master device IPV4 address. """
        return self._MasterIpAddress


    @property
    def Members(self) -> list:
        """ The list of `ZoneMember` objects that are members of this Zone. """
        return self._Members


    def AddMember(self, member:ZoneMember, logsi=None):
        """ 
        Add a new member to the list of members for this zone.
        
        Args:
            value:
                The `ZoneMember` object to append.
            logsi:
                A SmartInspect logging session, used to log exception messages.
                
        Raises:
            SoundTouchWarning:
                Zone member to be added is not a ZoneMember object.
                Zone member to be added did not specify a DeviceId.
                Zone member DeviceId to be added or removed cannot be the master DeviceId.
                
        The master SoundTouch device cannot find zone members without their device
        id.  This method will validate each zone member in the list to ensure that
        a device id was supplied.
        """
        if member: 
            if not isinstance(member, ZoneMember):
                raise SoundTouchWarning('Zone member to be added is not a ZoneMember object: %s' % str(member), logsi=logsi)
            if member.DeviceId is None:
                raise SoundTouchWarning('Zone member to be added did not specify a DeviceId: %s' % member.ToString(), logsi=logsi)
            if member.DeviceId == self.MasterDeviceId:
                raise SoundTouchWarning('Zone member DeviceId to be added or removed cannot be the master DeviceId: %s' % member.DeviceId, logsi=logsi)
            self._Members.append(member)


    def ToElement(self) -> Element:
        """ 
        Returns an xmltree Element node representation of the class. 
        """
        elm = Element('zone')
        if self._MasterDeviceId: elm.set('master', str(self._MasterDeviceId))
        if self._MasterIpAddress: elm.set('senderIPAddress', str(self._MasterIpAddress))
        if self._IsZoneMaster: elm.set('senderIsMaster', str(self._IsZoneMaster).lower())
               
        member:ZoneMember
        for member in self._Members:
            elm.append(member.ToElement())
        return elm


    def ToString(self, includeItems:bool=False) -> str:
        """
        Returns a displayable string representation of the class.
        
        Args:
            includeItems (bool):
                True to include all items in the list; otherwise False to only
                include the base list.
        """
        msg:str = 'Zone:'
        if self._MasterDeviceId and len(self._MasterDeviceId) > 0: msg = '%s masterDeviceId="%s"' % (msg, str(self._MasterDeviceId))
        if self._MasterIpAddress and len(self._MasterIpAddress) > 0: msg = '%s masterIpAddress="%s"' % (msg, str(self._MasterIpAddress))
        if self._IsZoneMaster: msg = '%s isZoneMaster=%s' % (msg, str(self._IsZoneMaster).lower())
        msg = "%s (%d items)" % (msg, self.__len__())
        
        if includeItems == True:
            item:ZoneMember
            for item in self:
                msg = "%s\n- %s" % (msg, item.ToString())
            
        return msg


    def ToStringMemberSummary(self) -> str:
        """
        Returns a displayable string representation of the Members list.
        """
        msg:str = "(%d items): " % (self.__len__())
        item:ZoneMember
        for item in self:
            msg = "%s '%s (%s)'," % (msg, item.DeviceId, item.IpAddress)
            
        return msg[0:len(msg)-1]


    def ToXmlString(self, encoding:str='utf-8') -> str:
        """ 
        Returns an xml string representation of the class. 
        
        Args:
            encoding (str):
                encode type (e.g. 'utf-8', 'unicode', etc).  
                Default is 'utf-8'.
        """
        if encoding is None:
            encoding = 'utf-8'
        elm = self.ToElement()
        xml = tostring(elm, encoding=encoding).decode(encoding)
        return xml
