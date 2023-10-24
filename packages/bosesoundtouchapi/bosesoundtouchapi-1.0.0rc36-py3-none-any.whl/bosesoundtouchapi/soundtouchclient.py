# external package imports.
from functools import reduce
from io import BytesIO
import re
import time
from tinytag import TinyTag 
import urllib.parse
from urllib3 import PoolManager, request
from xml.etree.ElementTree import fromstring, Element

# our package imports.
from .bstappmessages import BSTAppMessages
from .bstutils import export
from .models import *
import bosesoundtouchapi.models
from .soundtouchdevice import SoundTouchDevice
from .soundtoucherror import SoundTouchError
from .soundtouchexception import SoundTouchException
from .soundtouchkeys import SoundTouchKeys
from .soundtouchmessage import SoundTouchMessage
from .soundtouchmodelrequest import SoundTouchModelRequest
from .soundtouchsources import SoundTouchSources
from .soundtouchwarning import SoundTouchWarning
from bosesoundtouchapi.uri import *

from .bstconst import (
    MSG_TRACE_ACTION_KEY,
    MSG_TRACE_DELAY_DEVICE,
    MSG_TRACE_FAVORITE_NOT_ENABLED,
    MSG_TRACE_GET_CONFIG_OBJECT,
    MSG_TRACE_SET_PROPERTY_VALUE_SIMPLE
)

# get smartinspect logger reference; create a new session for this module name.
from smartinspectpython.siauto import SIAuto, SILevel, SISession
import logging
_logsi:SISession = SIAuto.Si.GetSession(__name__)
if (_logsi == None):
    _logsi = SIAuto.Si.AddSession(__name__, True)
_logsi.SystemLogger = logging.getLogger(__name__)

@export
class SoundTouchClient:
    """
    The SoundTouchClient uses the underlying Bose Web Socket api to communicate 
    with a specified Bose SoundTouch device. 
    
    This client communicates with a Bose device on port 8090 by default (the
    standard WebAPI port), but the port number can be changed.

    The client uses an urllib3.PoolManager instance to delegate the HTTP-requests.
    Set a custom manager with the manage_traffic() method.

    Like the BoseWebSocket, this client can be used in two ways: 1. create a
    client manually or 2. use the client within a _with_ statement. Additionally,
    this class implements a dict-like functionality. So, the loaded configuration
    can be accessed by typing: `config = client[<config_name>]`
    """

    def __init__(self, device:SoundTouchDevice, raiseErrors:bool=True, manager:PoolManager=None) -> None:
        """
        Initializes a new instance of the class.
        
        Args:
            device (SoundTouchDevice):
                The device to interace with. Some configuration data stored here will be
                updated if specific methods were called in this client.
            raiseErrors (bool):
                Specifies if the client should raise exceptions returned by the SoundTouch
                device. Use `ignore` to ignore the errors (they will be given as the
                response object in a SoundTouchMessage).
                Default = 'raise'.
            manager (urllib3.PoolManager):
                The manager for HTTP requests to the device.
        """
        self._ConfigurationCache:dict = {}
        self._Device:SoundTouchDevice = device
        self._Manager:PoolManager = PoolManager(num_pools=5, headers={'User-Agent': 'BoseSoundTouchApi/1.0.0'})
        self._RaiseErrors:bool = bool(raiseErrors)
        self._SnapshotSettings:dict = {}
        

    def __enter__(self) -> 'SoundTouchClient':
        return self


    def __exit__(self, etype, value, traceback) -> None:
        """No need to do anything"""


    def __getitem__(self, key):
        if repr(key) in self._ConfigurationCache:
            return self._ConfigurationCache[repr(key)]


    def __setitem__(self, key, value):
        if not isinstance(key, str):
            key = repr(key)
        self._ConfigurationCache[key] = value


    def __iter__(self):
        return iter(self._ConfigurationCache)


    def __str__(self) -> str:
        return self.ToString()


    @property
    def ConfigurationCache(self) -> dict:
        """ 
        A dictionary of cached configuration objects that have been obtained from
        the SoundTouch device.  Use the objects in this cache whenever it is
        too expensive or time consuming to make a real-time request from the device.

        The configuration cache is updated for any "Get...()" methods that return
        device information.  All of the "Get...()" methods have a `refresh:bool`
        argument that controls where information is obtained from; if refresh=True,
        then the device is queried for real-time configuration information. If
        refresh=False, then the configuration information is pulled from the configuration
        cache dictionary; if the cache does not contain the object, then the device
        is queried for real-time configuration information.
        
        It is obviously MUCH faster to retrieve device configuration objects from the 
        cache than from real-time device queries.  This works very well for configuration
        objects that do not change very often (e.g. Capabilities, Language, SourceList,
        etc).  You will still want to make real-time queries for configuration objects
        that change frequently (e.g. Volume, NowPlayingStatus, Presets, etc).
        
        This property is read-only, and is set when the class is instantiated.  The
        dictionary entries can be changed, but not the dictionary itself.

        Returns:
            The `_ConfigurationCache` property value.
            
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/ConfigurationCache.py
        ```
        </details>
        """
        return self._ConfigurationCache
    

    @property
    def Device(self) -> SoundTouchDevice:
        """
        The SoundTouchDevice object used to connect to the SoundTouch device.
        
        This property is read-only, and is set when the class is instantiated.
        """
        return self._Device


    @property
    def Manager(self) -> PoolManager:
        """ 
        Sets the request PoolManager object to use for http requests
        to the device.
        
        Returns:
            The `_Manager' property value.
        """
        return self._Manager
    
    @Manager.setter
    def Manager(self, value:PoolManager):
        """ 
        Sets the Manager property value.
        """
        if value != None:
            if isinstance(value, PoolManager):
                self._Manager = value


    @property
    def SnapshotSettings(self) -> dict:
        """
        A dictionary of configuration objects that are used by the Snapshot
        processing methods.
        
        This property is read-only.
        """
        return self._SnapshotSettings


    def _CheckResponseForErrors(self, element:Element):
        """
        Checks a device response for errors.  If found, a `SoundTouchError`
        is raised to inform the user of the error.
        
        Args:
            element (xml.etree.ElementTree.Element): 
                The response element to inspect.
                
        Raises:
            SoundTouchError: 
                If the element argument represents an error element.
        """
        # if we are ignoring errors then we are done.
        if (not self._RaiseErrors):
            return

        # if it's an error response then process it.
        if (element.tag in ['errors', 'error', 'Error']):

            # find the error portion of the message and raise a SoundTouchError.
            error = element.find('error')
            if error != None:
                errValue:int = int(error.get('value', -1))
                errName:str =  error.get('name', 'NONE')
                errSeverity:str =  error.get('severity', 'NONE')
                errMessage:str = error.text
                raise SoundTouchError(errMessage, errName, errSeverity, errValue, _logsi)
            
            # sometimes an error is not returned in an <errors> collection:
            # status=200 - <Error value="401" name="HTTP_STATUS_UNAUTHORIZED" severity="Unknown">app_key not authorized</Error>
            # status=200 - <Error value="415" name="HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE" severity="Unknown">media referenced by url is not supported by speaker</Error>
            if element.tag == 'Error':
                error = element
                errValue:int = int(error.get('value', -1))
                errName:str =  error.get('name', 'NONE')
                errSeverity:str =  error.get('severity', 'NONE')
                errMessage:str = error.text
                raise SoundTouchError(errMessage, errName, errSeverity, errValue, _logsi)
        return


    def _GetMetadataFromUrl_nBytes(self, url, size):

        headers={'Range': 'bytes=%s-%s' % (0, size-1)}
        response = self._Manager.request("GET", url, headers=headers)

        # req = request.Request(url)
        # req.headers['Range'] = 'bytes=%s-%s' % (0, size-1)
        # response = request.urlopen(req)
        #return response.read()
        return response.data


    def _GetMetadataFromUrl(self, url:str) -> TinyTag:
        """
        Args:
            url (str):
                The url to play, which also contains ID3V2 header data.

        Returns:                                
            A `TinyTag` object with the retrieved metadata if found; otherwise, None.
        """
        try:
            
            # download the first 10 bytes of the mp3 file
            # if no ID3 header present then we are done.
            data = self._GetMetadataFromUrl_nBytes(url, 10)
            if data[0:3] != b'ID3':
                return None

            # extract the ID3v2 header and compute the size of the id3v2 header.
            size_encoded = bytearray(data[-4:])
            size = reduce(lambda a,b: a*128+b, size_encoded, 0)

            # download the ID3v2 header into memory; we will also include one full
            # frame in order to function. Add max frame size
            header = BytesIO()
            data = self._GetMetadataFromUrl_nBytes(url, size+2881)  # 2881 = max frame size
            header.write(data)
            header.seek(0)

            # use TinyTag package to retrieve metadata from ID3v2 header, including image if present
            metadata = TinyTag.get(file_obj=header, image=True)

            # return metadata to caller.
            return metadata
        
        except SoundTouchException: raise  # pass handled exceptions on thru
        except Exception as ex:
        
            # format unhandled exception.
            raise SoundTouchException(BSTAppMessages.UNHANDLED_EXCEPTION.format("_GetMetadataFromUrl", str(ex)), ex, _logsi)
        

    def _ValidateDelay(self, delay:int, default:int=5, maxDelay:int=10) -> int:
        """
        Validates a delay value
        
        Args:
            delay (int):
                The delay value to validate.
            default (int):
                The default delay value to set if the user-input delay is not valid.
            maxDelay (int):
                The maximum delay value allowed.  
                Default is 10.
        """
        if (not isinstance(delay,int)) or (delay < 0): 
            result = default
        elif (delay > maxDelay): 
            result = maxDelay
        else:
            result = delay
        return result


    def Action(self, keyName:SoundTouchKeys) -> None:
        """
        Tries to imitate a pressed key.

        Args:
            keyName (SoundTouchKeys): 
                The specified key to press.
                A string is also accepted for this argument.

        This method can be used to invoke different actions by using the different
        keys defined in `bosesoundtouchapi.soundtouchkeys.SoundTouchKeys`.
        """
        key:str = str(keyName)
        if isinstance(keyName, SoundTouchKeys):
            key = keyName.value
            
        _logsi.LogVerbose(MSG_TRACE_ACTION_KEY % (key, self._Device.DeviceName))
        
        temp = f'<key state="%s" sender="Gabbo">{key}</key>'
        self.Put(SoundTouchNodes.key, temp % 'press')
        self.Put(SoundTouchNodes.key, temp % 'release')


    def AddFavorite(self) -> None:
        """ 
        Adds the currently playing media to the device favorites.

        This will first make a call to `GetNowPlayingStatus()` method to ensure
        favorites are enabled for the now playing media.  If not enabled, then
        the request is ignored and no exception is raised.
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/AddFavorite.py
        ```
        </details>
        """
        # get current nowPlaying status.
        nowPlaying:NowPlayingStatus = self.GetNowPlayingStatus(True)

        # can the nowPlaying item be a favorite?
        if nowPlaying.IsFavoriteEnabled:
            self.Action(SoundTouchKeys.ADD_FAVORITE)
        else:
            _logsi.LogVerbose(MSG_TRACE_FAVORITE_NOT_ENABLED % nowPlaying.ToString())


    def AddZoneMembers(self, members:list[ZoneMember], delay:int=3) -> SoundTouchMessage:
        """
        Adds the given zone members to the device's zone.
        
        Args:
            members (list):
                A list of `ZoneMember` objects to add to the master zone.
            delay (int):
                Time delay (in seconds) to wait AFTER adding zone members.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.
                
        Raises:
            SoundTouchException:
                Master zone status could not be retrieved.  
            SoundTouchWarning:
                Master zone does not exist; zone members cannot be added.  
                Members argument was not supplied, or has no members.  
                Members argument contained a list item that is not of type `ZoneMember`.  
        
        The SoundTouch master device cannot find zone members without their device id.  
        
        The SoundTouch device does not return errors if a zone member device id does not
        exist; it simply ignores the invalid member entry and moves on to the next.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/AddZoneMembers.py
        ```
        </details>
        """
        # validations.
        if not members or len(members) == 0:
            raise SoundTouchWarning('Members argument was not supplied, or has no members', logsi=_logsi)
        delay = self._ValidateDelay(delay, 3, 10)
        
        # get master zone status.
        # we do this to retrieve the master zone device id.
        masterZone:Zone = self.GetZoneStatus(refresh=True)
        if masterZone is None:
            raise SoundTouchException('Master zone status could not be retrieved', logsi=_logsi)
        if len(masterZone.Members) == 0:
            raise SoundTouchWarning('Master zone does not exist; zone members cannot be added', logsi=_logsi)
        
        # create a temporary Zone object (used to add zone members)
        # and add the zone members that we want to add.
        tempZone:Zone = Zone(masterZone.MasterDeviceId)
        for member in members:
            tempZone.AddMember(member, _logsi)

        _logsi.LogVerbose("Adding zone members from SoundTouch device: '%s' - %s" % (
            self._Device.DeviceName, tempZone.ToStringMemberSummary()))
        
        # add the member zones from the device.
        result = self.Put(SoundTouchNodes.addZoneSlave, tempZone.ToXmlString())
    
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)

        return result


    # def Bookmark(self) -> None:
    #     """ 
    #     Not sure what this does ... similar to favorites maybe?

    #     <details>
    #       <summary>Sample Code</summary>
    #     ```python
    #     .. include:: ../docs/include/samplecode/SoundTouchClient/Bookmark.py
    #     ```
    #     </details>
    #     """
    #     self.Action(SoundTouchKeys.BOOKMARK)


    def CreateZone(self, zone:Zone, delay:int=3) -> SoundTouchMessage:
        """
        Creates a multiroom zone from a Zone object.
        
        Args:
            zone (Zone):
                Multiroom configuration (zone) object that will control the zone
                (e.g. the master).  This object also contains a list of all zone
                members that will be under its control (e.g. Members property).
            delay (int):
                Time delay (in seconds) to wait AFTER creating the zone.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.
                
        Raises:
            SoundTouchWarning:
                Zone argument was not supplied.  
                Zone argument is not of type Zone.  
                Zone argument did not contain any members.  The zone must have at least 
                one zone member in order to create a zone.  
                
        The master SoundTouch device cannot find zone members without their device id.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/CreateZone.py
        ```
        </details>
        """
        # validations.
        if zone is None:
            raise SoundTouchWarning('Zone argument was not supplied', logsi=_logsi)
        if not isinstance(zone, Zone):
            raise SoundTouchWarning('Zone argument is not of type Zone', logsi=_logsi)
        if len(zone.Members) == 0:
            raise SoundTouchWarning('Zone argument object did not contain any members; the zone must have at least one zone member', logsi=_logsi)
        delay = self._ValidateDelay(delay, 3, 10)
        
        # if first zone member is not the master, then insert the master in list position one.
        # this emulates the SoundTouch App behavior, in that it creates the zone member list
        # with the master device listed as the first member, followed by the other zone members:

        # <zone master="9070658C9D4A">
        #     <member ipaddress="192.168.1.131">9070658C9D4A</member>   <- master
        #     <member ipaddress="192.168.1.130">E8EB11B9B723</member>   <- member #1
        #     ... more zone members
        # </zone>
        if zone.Members[0].DeviceId != zone.MasterDeviceId:
            zone.Members.insert(0, ZoneMember(zone.MasterIpAddress, zone.MasterDeviceId))

        # create the zone.
        result = self.Put(SoundTouchNodes.setZone, zone.ToXmlString())
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)

        return result


    def CreateZoneFromDevices(self, master:SoundTouchDevice, members:list) -> Zone:
        """ 
        Creates a new multiroom zone with the given member devices. 

        Args:
            master (SoundTouchDevice):
                The device object that will control the zone (e.g. the master).
            members (list):
                A list of SoundTouchDevice objects that will be controlled by the
                master zone (e.g. the zone members).
                
        Raises:
            SoundTouchWarning:  
                Master argument was not supplied.  
                Master argument is not of type SoundTouchDevice.  
                Members argument is not of type list.  
                Members argument was not supplied, or has no members.  
                Members argument contained a list item that is not of type SoundTouchDevice.  

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/CreateZoneFromDevices.py
        ```
        </details>
        """
        if master is None:
            raise SoundTouchWarning('Master argument was not supplied', logsi=_logsi)
        if not isinstance(master, SoundTouchDevice):
            raise SoundTouchWarning('Master argument is not of type SoundTouchDevice', logsi=_logsi)
        if not isinstance(members, list):
            raise SoundTouchWarning('Members argument is not of type list', logsi=_logsi)
        if (members is None) or (len(members) == 0):
            raise SoundTouchWarning('Members argument was not supplied, or has no members', logsi=_logsi)

        # create new Zone master object.
        zone = Zone(master.DeviceId, master.Host, True)
        
        # validate members, and add zone members.
        member:SoundTouchDevice
        for member in members:
            if not isinstance(member, SoundTouchDevice):
                raise SoundTouchWarning('Member argument contained an entry in the list that is not of type SoundTouchDevice: %s' % str(member), logsi=_logsi)
            zone.AddMember(ZoneMember(member.Host, member.DeviceId), _logsi)

        # create the zone.
        self.CreateZone(zone)
        return zone


    def Get(self, uri:SoundTouchUri) -> SoundTouchMessage:
        """
        Makes a GET request to retrieve a stored value.

        Use this method when querying for specific nodes. All standard nodes
        are implemented by this class.

        Args:
            uri (SoundTouchUri):
                The node where the requested value is stored. DANGER: This request can also have
                a massive effect on your Bose device, for instance when calling
                `client.get(SoundTouchNodes.resetDefaults)`, it will wipe all data on the device and
                perform a factory reset.

        Returns:
            An object storing the request uri, optional a payload that has been sent and 
            the response as an `xml.etree.ElementTree.Element`.

        Raises:
            SoundTouchError:
                When errors should not be ignored on this client, they will raise a SoundTouchError
                exception with all information related to that error.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/Get.py
        ```
        </details>
        """
        message = SoundTouchMessage(uri)
        if uri and uri.UriType == SoundTouchUriTypes.OP_TYPE_EVENT:
            return message

        self.MakeRequest('GET', message)
        return message


    def GetBalance(self, refresh=True) -> Balance:
        """
        Gets the current balance configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `Balance` object that contains balance configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetBalance.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Balance", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.balance, Balance, refresh)


    def GetBass(self, refresh=True) -> Bass:
        """
        Gets the current bass configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `Bass` object that contains bass configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetBass.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Bass", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.bass, Bass, refresh)


    def GetBassCapabilities(self, refresh=True) -> BassCapabilities:
        """
        Gets the current bass capability configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `BassCapabilities` object that contains bass capabilities configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetBassCapabilities.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("BassCapabilities", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.bassCapabilities, BassCapabilities, refresh)


    def GetCapabilities(self, refresh=True) -> Capabilities:
        """
        Gets the current bass capability configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `Capabilities` object that contains capabilities configuration of the device.

        The returned object has a dict-like implementation; individual capabilities
        can be accessed by typing: `GetCapabilities_results['capability_name']`.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetCapabilities.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Capabilities", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.capabilities, Capabilities, refresh)


    def GetClockConfig(self, refresh=True) -> ClockConfig:
        """
        Gets the current clock configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `ClockConfig` object that contains clock configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetClockConfig.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("ClockConfig", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.clockDisplay, ClockConfig, refresh)


    def GetClockTime(self, refresh=True) -> ClockTime:
        """
        Gets the current clock time configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `ClockTime` object that contains clock time configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetClockTime.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("ClockTime", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.clockTime, ClockTime, refresh)


    def GetDspMono(self, refresh=True) -> DSPMonoStereoItem:
        """
        Gets the current digital signal processor configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `DSPMonoStereoItem` object that contains DSP configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetDspMono.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("DSPMonoStereo", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.DSPMonoStereo, DSPMonoStereoItem, refresh)


    def GetLanguage(self, refresh=True) -> SimpleConfig:
        """
        Gets the current language configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `SimpleConfig` object that contains language configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetLanguage.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Language", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.language, SimpleConfig, refresh)


    def GetMediaServerList(self, refresh=True) -> MediaServerList:
        """
        Gets the list of UPnP Media servers found by the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `MediaServerList` object that contains media server configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetMediaServerList.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("MediaServerList", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.listMediaServers, MediaServerList, refresh)


    def GetName(self, refresh=True) -> SimpleConfig:
        """
        Gets the current name configuration of the device, and updates the SoundTouchDevice 
        class device name if possible.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `SimpleConfig` object that contains name configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetName.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Name", self._Device.DeviceName))
        name = self.GetProperty(SoundTouchNodes.name, SimpleConfig, refresh)
        
        if name.Value != self._Device.DeviceName:
            self._Device.DeviceName = name.Value
            
        return name


    def GetNetworkInfo(self, refresh=True) -> NetworkInfo:
        """
        Gets the current network information configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `NetworkInfo` object that contains network information configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python 
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetNetworkInfo.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("NetworkInfo", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.networkInfo, NetworkInfo, refresh)


    def GetNetworkStatus(self, refresh=True) -> NetworkStatus:
        """
        Gets the current network status configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `NetworkStatus` object that contains network status configuration of the device.
            
        This method can be used to retrieve the network status of the device for each
        network interface that has established a connection.  This includes details like
        the interface name (e.g. 'eth0'), the network SSID, MAC Address, and more.

        <details>
          <summary>Sample Code</summary>
        ```python 
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetNetworkStatus.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("NetworkStatus", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.netStats, NetworkStatus, refresh)


    def GetNowPlayingStatus(self, refresh=True) -> NowPlayingStatus:
        """
        Gets the now playing status configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `NowPlayingStatus` object that contains now playing status configuration of the device.
            
            
        This method can be used to retrieve the status of media that is currently playing
        on the device.  This includes the media source, ContentItem, track, artist,
        album, preview image, duration, position, play status, shuffle and repeat setting,
        stream type, track ID, station description and the location of the station.

        <details>
          <summary>Sample Code</summary>
        ```python 
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetNowPlayingStatus.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("NowPlayingStatus", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.nowPlaying, NowPlayingStatus, refresh)


    def GetOptions(self, uri:SoundTouchUri) -> list:
        """
        Makes an OPTIONS request and returns the list of available HTTP-Methods.

        Use this method when testing whether a node can be accessed.

        Args:
            uri (SoundTouchUri):
                The node where the requested value is stored.

        Returns:
            A list of strings storing all available HTTP-Methods.

        Raises:
            SoundTouchError:
                When errors should not be ignored on this client, they will raise a SoundTouchError
                exception with all information related to that error.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetOptions.py
        ```
        </details>
        """
        message = SoundTouchMessage(uri)
        headers = self.MakeRequest('OPTIONS', message)
        if isinstance(headers, int):
            return []
        return headers['Allow'].split(', ')


    def GetPowerManagement(self, refresh=True) -> PowerManagement:
        """
        Gets the current power management status configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `PowerManagement` object that contains power management configuration of the device.
            
        <details>
          <summary>Sample Code</summary>
        ```python 
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetPowerManagement.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("PowerManagement", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.powerManagement, PowerManagement, refresh)


    def GetPresetList(self, refresh=True) -> PresetList:
        """
        Gets the current preset list configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `PresetList` object that contains preset list configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetPresetList.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("PresetList", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.presets, PresetList, refresh)
        

    def GetProperty(self, uri:SoundTouchUri, classType, refresh=True):
        """
        Returns a cached property mapped to the given URI.
        
        Args:
            uri (SoundTouchUri):
                The property key (e.g. 'balance', 'volume', etc).
            classType (type):
                The configuration class type (e.g. Balance, Volume, etc).
            refresh (bool):
                True to refresh the property with real-time information from the device;
                otherwise, False to just return the cached value.
                
        Returns:
            A configuration instance of the provided classType argument.

        This method will refresh the property from the device if the property
        does not exist in the cache, regardless of the refresh argument value.
        """
        if repr(uri) not in self or refresh:
            self.RefreshConfiguration(uri, classType)

        if _logsi.IsOn(SILevel.Verbose):
            _logsi.LogVerbose("SoundTouchClient configuration object: '%s'" % (str(self[uri])))

        return self[uri]


    def GetRecentList(self, refresh=True) -> RecentList:
        """
        Gets the current recent list configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `RecentList` object that contains recent list configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetRecentList.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("RecentList", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.recents, RecentList, refresh)
        

    def GetRequestToken(self, refresh=True) -> SimpleConfig:
        """
        Gets a new request token generated by the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `SimpleConfig` object that contains the request token in the Attribute property.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetRequestToken.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("RequestToken", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.requestToken, SimpleConfig, refresh)


    def GetSourceList(self, refresh=True) -> SourceList:
        """
        Gets the current source list configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `SourceList` object that contains source list configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetSourceList.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("SourceList", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.sources, SourceList, refresh)


    def GetSystemTimeout(self, refresh=True) -> SystemTimeout:
        """
        Gets the current system timeout configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `SystemTimeout` object that contains system timeout configuration of the device.

        Use this method to determine whether power saving is enabled or not.
            
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetSystemTimeout.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("SystemTimeout", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.systemtimeout, SystemTimeout, refresh)


    def GetVolume(self, refresh=True) -> Volume:
        """
        Gets the current volume configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `Volume` object that contains volume configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetVolume.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Volume", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.volume, Volume, refresh)


    def GetWirelessProfile(self, refresh=True) -> WirelessProfile:
        """
        Gets the current wireless profile configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `WirelessProfile` object that contains wireless profile configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetWirelessProfile.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("WirelessProfile", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.getActiveWirelessProfile, WirelessProfile, refresh)


    def GetZoneStatus(self, refresh=True) -> Zone:
        """
        Gets the current wireless zone status configuration of the device.

        Args:
            refresh (bool):
                True to query the device for realtime information and refresh the cache;
                otherwise, False to just return the cached information.

        Returns:
            A `Zone` object that contains zone configuration of the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/GetZoneStatus.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("Zone", self._Device.DeviceName))
        return self.GetProperty(SoundTouchNodes.getZone, Zone, refresh)


    def MakeRequest(self, method:str, msg:SoundTouchMessage) -> int:
        """
        Performs a generic request by converting the response into the message object.
        
        Args:
            method (str): 
                The preferred HTTP method (e.g. "GET", "POST", etc).
            msg (SoundTouchMessage): 
                The altered message object.
                
        Returns:
            The status code (integer) or allowed methods (list).

        Raises:
            InterruptedError: 
                If an error occurs while requesting content.
                
        A 400 status code is immediately returned for the following scenarios:  
        - The method argument is not supplied.  
        - The msg argument is not supplied.  
        - The msg.Uri is not in the device list of supported URI's.  

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MakeRequest.py
        ```
        </details>
        """
        if not method or not msg:
            return 400 # bad request

        if msg.Uri not in self._Device.SupportedUris:
            return 400

        url = f'http://{self._Device.Host}:{self._Device.Port}/{msg.Uri}'
        
        try:
            if msg.HasXmlMessage:
                reqbody = msg.XmlMessage
                reqbodyencoded = reqbody.encode('utf-8')
                _logsi.LogXml(SILevel.Verbose, "SoundTouchClient http request: '%s' (with body)" % (url), reqbody)
                response = self._Manager.request(method, url, body=reqbodyencoded)
            else:
                _logsi.LogVerbose("SoundTouchClient http request: '%s'" % (url))
                response = self._Manager.request(method, url)

            if _logsi.IsOn(SILevel.Verbose):
                _logsi.LogXml(SILevel.Verbose, "SoundTouchClient http response: (%s) %s" % (response.status, url), response.data.decode("utf-8"))
            if _logsi.IsOn(SILevel.Debug):
                if (response.headers):
                    _logsi.LogCollection(SILevel.Debug, "SoundTouchClient http response headers", response.headers.items())

            if response.status == 200:
                if response.data:
                    msg.Response = fromstring(response.data)
                    self._CheckResponseForErrors(msg.Response)
            else:
                # soundtouch server can also issue errors response for http status codes other than 200 (e.g. 500, etc)
                # example - select AUX source with no sourceAccount specified.
                # request: <ContentItem source="AUX" />
                # result:  <errors deviceID="9070658C9D4A"><error value="1005" name="UNKNOWN_SOURCE_ERROR" severity="Unknown">1005</error></errors>
                if response.data:
                    msg.Response = fromstring(response.data)
                    self._CheckResponseForErrors(msg.Response)

            response.close()
            return response.headers
        
        except Exception as ex:
            
            raise InterruptedError(ex) from ex


    def MediaNextTrack(self) -> None:
        """ 
        Move to the next track in the current media playlist.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaNextTrack.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.NEXT_TRACK)


    def MediaPause(self) -> None:
        """ 
        Pause the current media playing.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaPause.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.PAUSE)


    def MediaPlay(self) -> None:
        """ 
        Play the currently paused media.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaPlay.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.PLAY)


    def MediaPlayPause(self) -> None:
        """ 
        Toggle the Play / Pause state of the current media playing.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaPlayPause.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.PLAY_PAUSE)


    def MediaPreviousTrack(self) -> None:
        """ 
        Move to the previous track in the current media playlist.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaPreviousTrack.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.PREV_TRACK)


    def MediaRepeatAll(self) -> None:
        """ 
        Enables repeat all processing for the current media playlist.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaRepeatAll.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.REPEAT_ALL)


    def MediaRepeatOff(self) -> None:
        """ 
        Turns off repeat (all / one) processing for the current media playlist.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaRepeatOff.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.REPEAT_OFF)


    def MediaRepeatOne(self) -> None:
        """ 
        Enables repeat single track processing for the current media playlist.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaRepeatOne.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.REPEAT_ONE)


    def MediaResume(self) -> None:
        """ 
        Resume the current media playing. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaResume.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.PLAY)


    def MediaShuffleOff(self) -> None:
        """ 
        Disables shuffling of the current media playlist. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaShuffleOff.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.SHUFFLE_OFF)


    def MediaShuffleOn(self) -> None:
        """ 
        Enables shuffling of the current media playlist. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaShuffleOn.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.SHUFFLE_ON)


    def MediaStop(self) -> None:
        """ 
        Stop the current media playing. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MediaStop.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.STOP)


    def Mute(self) -> None:
        """
        Toggle mute / unmute.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/Mute.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.MUTE)


    def MuteOff(self, refresh: bool=True) -> None:
        """
        Unmutes the device, if the device is currently muted.
        
        Args:
            refresh (bool):
                True to check the real-time status of the device; otherwise, False
                to check the cached status of the device.  
                Default = True.
            
        This will first issue a `GetVolume()` method call to query the current volume of the
        device.  If the refresh argument is True, then the volume status is refreshed with real-time
        data; otherwise the cached volume status is used.
        
        If the volume IsMuted property is true, then the MUTE key will be sent to unmute the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MuteOff.py
        ```
        </details>
        """
        volume:Volume = self.GetVolume(refresh)
        if (volume):
            if (volume.IsMuted):
                self.Action(SoundTouchKeys.MUTE)


    def MuteOn(self, refresh: bool=True) -> None:
        """
        Mutes the device, if the device is currently not muted.
        
        Args:
            refresh (bool):
                True to check the real-time status of the device; otherwise, False
                to check the cached status of the device.  
                Default = True.
            
        This will first issue a `GetVolume()` method call to query the current volume of the
        device.  If the refresh argument is True, then the volume status is refreshed with real-time
        data; otherwise the cached volume status is used.
        
        If the volume IsMuted property is false, then the MUTE key will be sent to mute the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/MuteOn.py
        ```
        </details>
        """
        volume:Volume = self.GetVolume(refresh)
        if (volume):
            if (not volume.IsMuted):
                self.Action(SoundTouchKeys.MUTE)
                

    def PlayContentItem(self, item:ContentItem, delay:int=5) -> SoundTouchMessage:
        """
        Plays the given ContentItem.

        Args:
            item (ContentItem):
                content item to play.
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the content item.  
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 5; value range is 0 - 10.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PlayContentItem.py
        ```
        </details>
        """
        return self.SelectContentItem(item, delay)


    def PlayNotificationTTS(self, sayText:str, ttsUrl:str=None, 
                            artist:str=None, album:str=None, track:str=None,  
                            volumeLevel:int=0, appKey:str=None
                            ) -> SoundTouchMessage:
        """
        Plays a notification message via Google TTS (Text-To-Speech) processing.
        
        Args:
            sayText (str):
                The message that will be converted from text to speech and played
                on the device.
            ttsUrl (str):
                The Text-To-Speech url used to translate the message.  
                The value should contain a "{saytext}" format parameter, that will be used
                to insert the encoded sayText value.
                Default value is:  
                "http://translate.google.com/translate_tts?ie=UTF-8&tl=EN&client=tw-ob&q={saytext}"
            artist (str):
                The message text that will appear in the NowPlaying Artist node.  
                Default is "TTS Notification"
            album (str):
                The message text that will appear in the NowPlaying Album node.  
                Default is "Google TTS"
            track (str):
                The message text that will appear in the NowPlaying Track node.  
                Default is the sayText argument value.
            volumeLevel (int):
                The temporary volume level that will be used when the message is played.  
                Specify a value of zero to play at the current volume.  
                Per Bose limitations, max level cannot be more than 70.
                Default is zero.
            appKey (str):
                Bose Developer API application key.
        
        Note that SoundTouch devices do not support playing content from HTTPS (secure 
        socket layer) url's.  A `SoundTouchException` will be raised if a non `http://` url 
        is supplied for the ttsUrl argument.

        The notification message is played at the level specified by the volumeLevel argument.
        Specify a volumeLevel of zero to play the notification at the current volume level.
        The volume level is restored to the level it was before the notification message was 
        played after the notification is complete; e.g. if you made changes to the volume while
        the notification is playing then they are changed back to the volume level that was in
        effect prior to playing the notification.  The SoundTouch device automatically takes 
        care of the volume level switching; there are no calls in the method to change the 
        volume or currently playing content status.  The SoundTouch device also limits the
        volume range between 10 (min) and 70 (max); this is a Bose limitation, and is not
        imposed by this API.
        
        The currently playing content (if any) is paused while the notification message
        content is played, and then resumed once the notification ends.
        
        If the device is the master controller of a zone, then the notification message will 
        be played on all devices that are members of the zone.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PlayNotificationTTS.py
        ```
        </details>
        """
        if sayText is None or len(sayText) == 0:
            _logsi.LogWarning("sayText argument was not supplied to PlayNotificationTTS method; ignoring request")
            return
        
        if ttsUrl is None:
            ttsUrl:str = "http://translate.google.com/translate_tts?ie=UTF-8&tl=EN&client=tw-ob&q={saytext}"
        if not isinstance(ttsUrl, str):
            _logsi.LogWarning("ttsUrl argument was not a string; ignoring PlayNotificationTTS request")
            return
        ttsUrl = ttsUrl.lstrip()
        if not re.match(r'http://', ttsUrl):
            raise SoundTouchException("ttsUrl argument value does not start with 'http://'; https url's are not supported by SoundTouch devices", logsi=_logsi)

        if artist is None:
            artist = "TTS Notification"
        if album is None:
            album = "Google TTS"
        if track is None:
            track = sayText
        if volumeLevel is None or volumeLevel < 0 or volumeLevel > 100:
            volumeLevel = 30
            
        if volumeLevel > 0 and volumeLevel < 10:
            volumeLevel = 10  # SoundTouch will fail the request if volume level is less than 10.
        if volumeLevel > 70:
            volumeLevel = 70  # SoundTouch will fail the request if volume level is greater than 70.
        
        # replace sayText in the TTS url.
        ttsUrl = ttsUrl.format(saytext=urllib.parse.quote(sayText))
        
        # build playinfo configuration and the message to send.
        playInfo:PlayInfo = PlayInfo(ttsUrl, artist, album, track, volumeLevel, appKey)
        message = SoundTouchMessage(SoundTouchNodes.speaker, playInfo.ToXmlRequestBody())
        
        self.MakeRequest('POST', message)
        return message


    def PlayUrl(self, url:str, artist:str=None, album:str=None, track:str=None, 
                volumeLevel:int=0, appKey:str=None, getMetaDataFromUrlFile:bool=False
                ) -> SoundTouchMessage:
        """
        Plays media from the given URL.

        Args:
            url (str):
                The url to play.
            artist (str):
                The message text that will appear in the NowPlaying Artist node.  
                Default is "Unknown Artist"
            album (str):
                The message text that will appear in the NowPlaying Album node.  
                Default is "Unknown Album"
            track (str):
                The message text that will appear in the NowPlaying Track node.  
                Default is "Unknown Track"
            volumeLevel (int):
                The temporary volume level that will be used when the message is played.  
                Specify a value of zero to play at the current volume.  
                Default is zero.
            appKey (str):
                Bose Developer API application key.
            getMetaDataFromUrlFile (bool):
                If true, the artist, album, and song title metadata details will be retrieved
                from the ID3 header of the url content (if available); otherwise, False to
                use the artist, album, and song title arguments specified.

        Returns:                                
            A `SoundTouchMessage` object storing the request uri, a payload that has been 
            sent (optional), and the response as an `xml.etree.ElementTree.Element`.
            
        Raises:
            SoundTouchException:
                Url argument value does not start with 'http://' or 'https://'.
            SoundTouchError:
                If the SoundTouch device encounters an error while trying to play the url
                media content.
                
        The given url content is played at the level specified by the volumeLevel argument.
        Specify a volumeLevel of zero to play the given url content at the current volume level.
        The volume level is restored to the level it was before the given url content was 
        played after play is complete; e.g. if you made changes to the volume while
        the given url content is playing then they are changed back to the volume level that was in
        effect prior to playing the given url content.  The SoundTouch device automatically takes 
        care of the volume level switching; there are no calls in the method to change the 
        volume or currently playing content status.
        
        The currently playing content (if any) is paused while the given url content
        is played, and then resumed once the given url content ends.  If the currently
        playing content is a url (or other "notification" source type), then the `MediaNextTrack`
        method will be called to stop the current play and the new source will be played.
        
        If the device is the master controller of a zone, then the given url content will 
        be played on all devices that are members of the zone.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PlayUrl.py
        ```
        </details>
        """
        if (url is None) or (not isinstance(url, str)):
            _logsi.LogVerbose("A string url argument was not supplied; ignoring PlayUrl request")
            return
        url = url.lstrip()
        
        # only support http or https url's at this time.
        if not re.match(r'http[s]?://', url):
           raise SoundTouchException("url argument value does not start with 'http://' or 'https://'", logsi=_logsi)
       
        if artist is None:
            artist = "Unknown Artist"
        if album is None:
            album = "Unknown Album"
        if track is None:
            track = "Unknown Track"
        if volumeLevel is None or volumeLevel < 0 or volumeLevel > 100:
            volumeLevel = 30
            
        # retrieve nowPlaying status; if source is notification, then we must first
        # call MediaNextTrack command before trying to play the specified url; failure to
        # do so will result in the following error:
        # id=409, name="HTTP_STATUS_CONFLICT", cause="request not supported while speaker resource is in use"
        nowPlaying:NowPlayingStatus = self.GetNowPlayingStatus(True)
        if nowPlaying is not None:
            if nowPlaying.Source == SoundTouchSources.NOTIFICATION.value:
                self.MediaNextTrack()

        # do we need to retrieve metadata from the url file itself?
        if getMetaDataFromUrlFile == True:
            # try to retrieve the metadata; if found, then use it.
            metadata:TinyTag = self._GetMetadataFromUrl(url)
            if metadata is not None:
                artist = metadata.artist
                album = metadata.album
                track = metadata.title
                
                # retrieve cover art (if embedded).
                #coverArt = metadata.get_image()

        # build playinfo configuration and the message to send.
        playInfo:PlayInfo = PlayInfo(url, artist, album, track, volumeLevel, appKey)
        message = SoundTouchMessage(SoundTouchNodes.speaker, playInfo.ToXmlRequestBody())
        
        # make the request.
        self.MakeRequest('POST', message)
        return message
    
    
    def Power(self) -> None:
        """
        Toggle power on / off.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/Power.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.POWER)


    def PowerOff(self, refresh: bool=True) -> None:
        """
        Set power off, if the device is currently powered on and not in standby mode.
        
        Args:
            refresh (bool):
                True to check the real-time status of the device; otherwise, False
                to check the cached status of the device.  
                Default = True.
            
        This will first issue a `GetNowPlayingStatus()` method call to query the current status of the
        device.  If the refresh argument is True, then the status is refreshed with real-time
        data; otherwise the cached status is used.
        
        If the nowPlaying source is not "STANDBY", then the POWER key will be sent to power off
        the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PowerOff.py
        ```
        </details>
        """
        stat:NowPlayingStatus = self.GetNowPlayingStatus(refresh)
        if (stat):
            if (stat.Source not in ["STANDBY", None]):
                self.Action(SoundTouchKeys.POWER)


    def PowerOn(self, refresh: bool=True) -> None:
        """
        Set power on, if the device is currently in standby mode.
        
        Args:
            refresh (bool):
                True to check the real-time status of the device; otherwise, False
                to check the cached status of the device.  
                Default = True.
            
        This will first issue a `GetNowPlayingStatus()` method call to query the current status of the
        device.  If the refresh argument is True, then the status is refreshed with real-time
        data; otherwise the cached status is used.
        
        If the nowPlaying source is "STANDBY", then the POWER key will be sent to power on the device.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PowerOn.py
        ```
        </details>
        """
        stat:NowPlayingStatus = self.GetNowPlayingStatus(refresh)
        if (stat):
            if (stat.Source in ["STANDBY", None]):
                self.Action(SoundTouchKeys.POWER)


    def PowerStandby(self) -> None:
        """
        Set power to standby, if the device is currently powered on.
        
        This method does not update a configuration, as there is no object to
        configure - it simply places the device in STANDBY mode.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/PowerStandby.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_GET_CONFIG_OBJECT % ("StandBy", self._Device.DeviceName))
        msg = self.Get(SoundTouchNodes.standby)
        return
        

    def Put(self, uri:SoundTouchUri, body:str) -> SoundTouchMessage:
        """
        Makes a POST request to apply a new value for the given node.

        Use this method when setting some configuration related data. All standard operations
        where a POST request is necessary are implemented by this class.

        Args:
            uri (SoundTouchUri):
                The node where the requested value is stored.
            body (str | SoundTouchModelRequest):
                The request body xml, or a class that inherits from `SoundTouchModelRequest`
                that implements the `ToXmlRequestBody` method.

        Returns: 
            A `SoundTouchMessage` object storing the request uri, a payload that has been 
            sent (optional), and the response as an `xml.etree.ElementTree.Element`.

        Raises:
            SoundTouchError:
                When errors should not be ignored on this client, they will raise a SoundTouchError
                exception with all information related to that error.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/Put.py
        ```
        </details>
        """
        # if body implements SoundTouchModelRequest then call it's ToXmlRequestBody()
        # method to get the request body; otherwise, just assume it's xml already.
        reqBody:str = body
        if isinstance(body, SoundTouchModelRequest):
            reqBody = body.ToXmlRequestBody()
            
        message = SoundTouchMessage(uri, reqBody)
        
        self.MakeRequest('POST', message)
        return message


    def RefreshConfiguration(self, uri:SoundTouchUri, classType) -> object:
        """        
        Refreshes the cached configuration for the given URI.
        
        Args:
            uri (SoundTouchUri):
                The configuration uri key.
            classType (type):
                The configuration class type (e.g. Balance, Volume, etc).
            refresh (bool):
                True to refresh the property with real-time information from the device;
                otherwise, False to just return the cached value.
                
        Returns:
            A configuration instance of the provided classType argument.

        This method will call the `Get()` method to refresh the configuration with
        real-time information from the device, and store the results in the cache.
        """
        if _logsi.IsOn(SILevel.Verbose):
            _logsi.LogVerbose("Refreshing '%s' configuration from the SoundTouch device" % (str(uri)))
        
        msg = self.Get(uri)
        if msg.Response is not None:
            self[uri] = classType(root=msg.Response)
            
        return self[uri]


    def RemoveAllPresets(self) -> SoundTouchMessage:
        """
        Removes all presets from the device's list of presets.
        
        Returns:
            A message object that may contain more information about the result.
            
        Raises:
            Exception:
                If the command fails for any reason.
        
        A `GetPresetList()` method call is made to retrieve the current list of presets.
        The returned list of presets are deleted one by one.  
        The message returned is the message returned from the final preset removal.  
        If there were no presets to remove, then the returned result is None.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/RemoveAllPresets.py
        ```
        </details>
        """
        _logsi.LogVerbose("Removing all presets from SoundTouch device: '%s'" % self._Device.DeviceName)

        # get current list of presets.
        presets:PresetList = self.GetPresetList(True)
        
        # remove them all.
        msg:SoundTouchMessage = None
        preset:Preset
        for preset in presets:
            msg = self.Put(SoundTouchNodes.removePreset, preset.ToXmlString())
        return msg


    def RemovePreset(self, presetId: int) -> SoundTouchMessage:
        """
        Removes the specified Preset id from the device's list of presets.
        
        Args:
            presetId (int):
                The preset id to remove; valid values are 1 thru 6.
                
        Returns:
            A message object that may contain more information about the result.
            
        Raises:
            Exception:
                If the command fails for any reason.
        
        The preset with the specified id is removed.  
        No exception is raised if the preset id does not exist.
        
        Presets and favorites in the SoundTouch app are not reordered once the
        preset is removed; it simply creates an open / empty slot in the list.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/RemovePreset.py
        ```
        </details>
        """
        _logsi.LogVerbose("Removing preset from SoundTouch device: '%s'" % self._Device.DeviceName)
        item:Preset = Preset(presetId)
        return self.Put(SoundTouchNodes.removePreset, item.ToXmlString())


    def RemoveFavorite(self) -> None:
        """ 
        Removes the currently playing media from the device favorites.
        
        This will first make a call to `GetNowPlayingStatus()` method to ensure
        favorites are enabled for the now playing media.  If not enabled, then
        the request is ignored and no exception is raised.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/RemoveFavorite.py
        ```
        </details>
        """
        # get current nowPlaying status.
        nowPlaying:NowPlayingStatus = self.GetNowPlayingStatus(True)

        # can the nowPlaying item be a favorite?
        if nowPlaying.IsFavoriteEnabled:
            self.Action(SoundTouchKeys.REMOVE_FAVORITE)
        else:
            _logsi.LogVerbose(MSG_TRACE_FAVORITE_NOT_ENABLED % nowPlaying.ToString())


    def RemoveZone(self, delay:int=1) -> SoundTouchMessage:
        """
        Removes the given zone.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER removing zone members.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 1; value range is 0 - 10.
                
        Raises:
            SoundTouchException:
                Master zone status could not be retrieved.  
            SoundTouchWarning:
                Master zone does not exist; zone members cannot be removed.  
        
        This method retrieves the current master zone status, and issues a call to
        `RemoveZoneMembers` to remove all members from the zone.  
        
        Note that the master zone itself is also removed; you will need to 
        reissue a call to the `CreateZone()` method to re-create the master zone.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/RemoveZone.py
        ```
        </details>
        """
        # validations.
        delay = self._ValidateDelay(delay, 1, 10)
        
        # get master zone status.
        # we do this to retrieve the master zone device id and its zone members.
        masterZone:Zone = self.GetZoneStatus(refresh=True)
        if masterZone is None:
            raise SoundTouchException('Master zone status could not be retrieved', logsi=_logsi)
        if len(masterZone.Members) == 0:
            raise SoundTouchWarning('Master zone does not exist; zone members cannot be removed', logsi=_logsi)
        
        _logsi.LogVerbose("Removing zone members from SoundTouch device: '%s' - %s" % (
            self._Device.DeviceName, masterZone.ToStringMemberSummary()))
        
        # remove the member zones from the device.
        result = self.Put(SoundTouchNodes.removeZoneSlave, masterZone.ToXmlString())

        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)

        return result


    def RemoveZoneMembers(self, members:list, delay:int=3) -> SoundTouchMessage:
        """
        Removes the given zone members from the device's zone.
        
        Args:
            members (list):
                A list of `ZoneMember` objects to remove from the master zone.
            delay (int):
                Time delay (in seconds) to wait AFTER removing zone members.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.
                
        Raises:
            SoundTouchException:
                Master zone status could not be retrieved.  
            SoundTouchWarning:
                Master zone does not exist; zone members cannot be removed.  
                Members argument was not supplied, or has no members.  
                Members argument contained a list item that is not of type `ZoneMember`.  
        
        Note that the master zone itself is also removed if there are no zone members
        left after the remove request is complete.  In this case, you will need to 
        reissue a call to the `CreateZone()` method to re-create the master zone.
        
        The SoundTouch device does not return errors if a zone member device id does not
        exist; it simply ignores the invalid member entry and moves on to the next.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/RemoveZoneMembers.py
        ```
        </details>
        """
        # validations.
        if not members or len(members) == 0:
            raise SoundTouchWarning('Members argument contained no zone members to remove', logsi=_logsi)
        delay = self._ValidateDelay(delay, 5, 10)
        
        # get master zone status.
        # we do this to retrieve the master zone device id.
        masterZone:Zone = self.GetZoneStatus(refresh=True)
        if masterZone is None:
            raise SoundTouchException('Master zone status could not be retrieved', logsi=_logsi)
        if len(masterZone.Members) == 0:
            raise SoundTouchWarning('Master zone does not exist; zone members cannot be removed', logsi=_logsi)
        
        # create a temporary Zone object (used to remove zone members)
        # and add the zone members that we want to remove.
        tempZone:Zone = Zone(masterZone.MasterDeviceId)
        for member in members:
            tempZone.AddMember(member, _logsi)

        _logsi.LogVerbose("Removing zone members from SoundTouch device: '%s' - %s" % (
            self._Device.DeviceName, tempZone.ToStringMemberSummary()))

        # remove the member zones from the device.
        result = self.Put(SoundTouchNodes.removeZoneSlave, tempZone.ToXmlString())

        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)

        return result


    def RestoreSnapshot(self, delay:int = 5) -> None:
        """
        Restores selected portions of the configuration from a snapshot that was
        previously taken with the `StoreSnapshot` method.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait for the playing content to change.  
                Default is 5 seconds.
        
        The following settings will be restored from the snapshot dictionary by default:
        - `SoundTouchNodes.nowPlaying.Path` - playing content.  
        - `SoundTouchNodes.volume.Path` - volume level and mute status.
        
        No restore actions will be taken if snapshot settings do not exist.
        
        You can restore your own custom settings from the snapshot dictionary; note
        that these custom settings are NOT restored by default.
        
        You may remove default items from the snapshot dictionary prior to calling
        the `RestoreSnapshot` method.  Let's say you did not want to restore the
        volume level - simply remove the volume item from the snapshot dictionary.
        See the sample code below for an example.
        
        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/StoreSnapshot.py
        ```
        </details>
        """
        if len(self._SnapshotSettings) == 0:
            _logsi.LogMessage("No snapshot has been taken yet; nothing to do")
            return
        
        if SoundTouchNodes.nowPlaying.Path in self._SnapshotSettings.keys():
            currentStatus:NowPlayingStatus = self.GetNowPlayingStatus(True)
            status:NowPlayingStatus = self._SnapshotSettings[SoundTouchNodes.nowPlaying.Path]
            # switch the input source if need be, waiting 2 seconds for the change to process.
            if currentStatus.Source != status.Source:
                self.SelectSource(status.Source, status.ContentItem.SourceAccount, 2)
            self.SelectContentItem(status.ContentItem, delay)
        
        if SoundTouchNodes.volume.Path in self._SnapshotSettings.keys():
            # set volume level also restores mute / unmute status.
            volume:Volume = self._SnapshotSettings[SoundTouchNodes.volume.Path]
            self.SetVolumeLevel(volume.Actual)
            
        return


    def SelectContentItem(self, item:ContentItem, delay:int=5) -> SoundTouchMessage:
        """
        Selects the given ContentItem.

        Args:
            item (ContentItem):
                Content item to select.
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the content item.  
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 5; value range is 0 - 10.
                
        Note that playing of "https://" content is not supported by SoundTouch devices.
                
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectContentItem.py
        ```
        </details>
        """
        _logsi.LogObject(SILevel.Verbose, "Select content item", item)
        delay = self._ValidateDelay(delay, 5, 10)
            
        result = self.Put(SoundTouchNodes.select, item.ToXmlString())
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)
            
        return result


    def SelectPreset(self, preset:Preset, delay:int=5) -> SoundTouchMessage:
        """
        Selects the given preset.

        Args:
            item (Preset):
                Preset item to select.
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 5; value range is 0 - 10.

        Raises:
            SoundTouchWarning:
                Preset argument was not supplied.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset.py
        ```
        </details>
        """
        _logsi.LogVerbose("Selecting preset on SoundTouch device: '%s'" % self._Device.DeviceName)
        
        if not preset:
            raise SoundTouchWarning('Preset argument was not supplied', logsi=_logsi)
        delay = self._ValidateDelay(delay, 5, 10)
        
        result = self.Put(SoundTouchNodes.select, preset.ContentItem_ToXmlString())
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)
            
        return result


    def SelectPreset1(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET1 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset1.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_1)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectPreset2(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET2 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset2.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_2)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectPreset3(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET3 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset3.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_3)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectPreset4(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET4 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset4.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_4)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectPreset5(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET5 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset5.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_5)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectPreset6(self, delay:int=3) -> None:
        """ 
        Mirrors the press and release of the PRESET6 key on the SoundTouch remote.
        
        Args:
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the preset.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 3; value range is 0 - 10.

        This method does nothing if there is no preset at the specified preset index.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectPreset6.py
        ```
        </details>
        """
        delay = self._ValidateDelay(delay, 3, 10)
        self.Action(SoundTouchKeys.PRESET_6)
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)


    def SelectRecent(self, recent:Recent, delay:int=5) -> SoundTouchMessage:
        """
        Selects the given recent.

        Args:
            item (Recent):
                Recent item to select.
            delay (int):
                Time delay (in seconds) to wait AFTER selecting the recent.
                This delay will give the device time to process the change before another 
                command is accepted.  
                Default is 5; value range is 0 - 10.

        Raises:
            SoundTouchWarning:
                Recent argument was not supplied.

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectRecent.py
        ```
        </details>
        """
        _logsi.LogVerbose("Selecting recent on SoundTouch device: '%s'" % self._Device.DeviceName)
        
        if not recent:
            raise SoundTouchWarning('Recent argument was not supplied', logsi=_logsi)
        delay = self._ValidateDelay(delay, 5, 10)
        
        result = self.Put(SoundTouchNodes.select, recent.ContentItem_ToXmlString())
        
        if delay > 0:
            _logsi.LogVerbose(MSG_TRACE_DELAY_DEVICE % (delay, self._Device.DeviceName))
            time.sleep(delay)
            
        return result


    def SelectSource(self, source:SoundTouchSources, sourceAccount:str=None, delay:int=3) -> SoundTouchMessage:
        """
        Selects a new input source.
        
        Args:
            source (SoundTouchSources | str):
                Input source value; this can either be a `SoundTouchSources` enum value or a string.
                If specifying a string value, then it should be in upper-case.
            sourceAccount (str):
                Source account value; some sources require one when changing the input 
                source (e.g. "AUX").
            delay (int):
                time delay (in seconds) to wait AFTER selecting the source.  This delay
                will give the SoundTouch device time to process the change before another 
                command is accepted.
                default is 3 seconds, and value range is 0 - 10.
                
        Returns:
            A SoundTouchMessage response that indicates success or failure of the command.
            
        Raises:
            SoundTouchWarning:
                Source argument was not supplied.  

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SelectSource.py
        ```
        </details>
        """
        if not source:
            raise SoundTouchWarning('Source argument was not supplied', logsi=_logsi)
        if isinstance(source, SoundTouchSources):
            source = source.value
        return self.SelectContentItem(ContentItem(source=source, sourceAccount=sourceAccount), delay)


    def SetBassLevel(self, level: int) -> SoundTouchMessage:
        """
        Sets the device bass level to the given level.
        
        Args:
            level (int):
                Bass level to set, in the range of -9 (no bass) to 0 (full bass).
                The range can vary by device; use `GetBassCapabilities()` method to
                retrieve the allowable range for your device.
        """
        _logsi.LogVerbose(MSG_TRACE_SET_PROPERTY_VALUE_SIMPLE % ("bass level", str(level), self._Device.DeviceName))
        request:Bass = Bass(level)
        return self.Put(SoundTouchNodes.bass, request)


    def SetName(self, name:str) -> SoundTouchMessage:
        """
        Sets a new device name.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SetName.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_SET_PROPERTY_VALUE_SIMPLE % ("device name", name, self._Device.DeviceName))
        
        # update the device configuration.
        request:SimpleConfig = SimpleConfig('name', name)
        result:SoundTouchMessage = self.Put(SoundTouchNodes.name, request)
    
        # update the SoundTouchDevice object device name to match.
        self._Device._DeviceName = name
        return result


    def SetVolumeLevel(self, level:int) -> SoundTouchMessage:
        """
        Sets the device volume level to the given level.
        
        Args:
            level (int):
                Volume level to set, in the range of 0 (mute) to 100 (full volume).

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/SetVolumeLevel.py
        ```
        </details>
        """
        _logsi.LogVerbose(MSG_TRACE_SET_PROPERTY_VALUE_SIMPLE % ("volume level", str(level), self._Device.DeviceName))
        request:Volume = Volume(level, level)
        return self.Put(SoundTouchNodes.volume, request)


    def StorePreset(self, item:Preset) -> SoundTouchMessage:
        """
        Stores the given Preset to the device's list of presets.
        
        Args:
            item (Preset):
                The Preset object to store.
                
        Returns:
            A message object that may contain more information about the result.
            
        Raises:
            Exception:
                If the command fails for any reason.
                
        Most SoundTouch devices can only store 6 presets in their internal memory.
        The Preset.preset_id property controls what slot the stored preset gets
        placed in.  If a preset already exists in a slot, then it is over-written
        with the newly stored preset.  If a preset with the same details exists in
        another slot, then the duplicate preset is removed and its slot is emptied.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/StorePreset.py
        ```
        </details>
        """
        _logsi.LogVerbose("Storing preset to SoundTouch device: '%s'" % self._Device.DeviceName)
        return self.Put(SoundTouchNodes.storePreset, item.ToXmlString())


    def StoreSnapshot(self) -> None:
        """
        Stores selected portions of the configuration so that they can be easily
        restored with the `RestoreSnapshot` method.
        
        The following settings will be stored to the snapshot dictionary by default:
        - `SoundTouchNodes.nowPlaying.Path` - playing content.  
        - `SoundTouchNodes.volume.Path` - volume level and mute status.
        
        The `SnapshotSettings` dictionary is cleared prior to storing any settings.
        
        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/StoreSnapshot.py
        ```
        </details>
        """
        self._SnapshotSettings.clear()
               
        status:NowPlayingStatus = self.GetNowPlayingStatus(True)
        self._SnapshotSettings[SoundTouchNodes.nowPlaying.Path] = status
        
        volume:Volume = self.GetVolume(True)
        self._SnapshotSettings[SoundTouchNodes.volume.Path] = volume
        return


    def ThumbsDown(self) -> None:
        """ 
        Removes the currently playing media from the device favorites.
        
        This will first make a call to `GetNowPlayingStatus()` method to ensure
        favorites are enabled for the now playing media.  If not enabled, then
        the request is ignored and no exception is raised.
        
        The THUMBS_DOWN key appears to do the same thing as the REMOVE_FAVORITE
        key, but it's included here for completeness.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/ThumbsDown.py
        ```
        </details>
        """
        # get current nowPlaying status.
        nowPlaying:NowPlayingStatus = self.GetNowPlayingStatus(True)

        # can the nowPlaying item be a favorite?
        if nowPlaying.IsFavoriteEnabled:
            self.Action(SoundTouchKeys.THUMBS_DOWN)
        else:
            _logsi.LogVerbose(MSG_TRACE_FAVORITE_NOT_ENABLED % nowPlaying.ToString())


    def ThumbsUp(self) -> None:
        """ 
        Adds the currently playing media to the device favorites.

        This will first make a call to `GetNowPlayingStatus()` method to ensure
        favorites are enabled for the now playing media.  If not enabled, then
        the request is ignored and no exception is raised.
        
        The THUMBS_UP key appears to do the same thing as the ADD_FAVORITE
        key, but it's included here for completeness.
        
        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/ThumbsUp.py
        ```
        </details>
        """
        # get current nowPlaying status.
        nowPlaying:NowPlayingStatus = self.GetNowPlayingStatus(True)

        # can the nowPlaying item be a favorite?
        if nowPlaying.IsFavoriteEnabled:
            self.Action(SoundTouchKeys.THUMBS_UP)
        else:
            _logsi.LogVerbose(MSG_TRACE_FAVORITE_NOT_ENABLED % nowPlaying.ToString())


    def ToString(self) -> str:
        """
        Returns a displayable string representation of the class.
        """
        msg:str = 'SoundTouchClient:'
        if self._Device is not None:
            msg = "%s DeviceName='%s'" % (msg, self._Device.DeviceName)
            msg = "%s DeviceId='%s'" % (msg, self._Device._DeviceId)
            msg = "%s Host='%s'" % (msg, self._Device.Host)
            msg = "%s Port='%s'" % (msg, self._Device.Port)
        return msg


    def VolumeDown(self) -> None:
        """ 
        Decrease the volume of the device by one. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/VolumeDown.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.VOLUME_DOWN)


    def VolumeUp(self) -> None:
        """ 
        Increase the volume of the device by one. 

        <details>
          <summary>Sample Code</summary>
        ```python
        .. include:: ../docs/include/samplecode/SoundTouchClient/VolumeUp.py
        ```
        </details>
        """
        self.Action(SoundTouchKeys.VOLUME_UP)



###################################################################################################
# ideas:

# /bluetoothInfo - bt MAC address info.

# play https urls:
# Well, i own a soundtouch device and am happy with its sound quality. But the the actual component does not play media from https:// urls only from http://.
# But the soundtouch boxes are capable to play these urls by the notification api. You only need an appkey from the bose developer program. With the appkey, you can get one free for 100 calls a day, it is easy. Just post an XML string and you are done.
# val String PostData = '<play_info><app_key>' + AppKey + '</app_key><url>' + TTSUrl + '</url><service>OpenHAB</service><volume>' + Volume +'</volume></play_info>';
# sendHttpPostRequest("http://192.168.178.xx:8090/speaker","",PostData)
# Perhaps it is possible to add an appkey value to the configuration data and if it is present use the notification api to play the url instead of using the libsoundtouch play_url method.

  # val String AppKey = "Ml7YGAI9JWjFhU7D348e86JPXtisddBa"   <- not sure if this is a temporary key?
  # val String BoseIP = "172.17.100.21"
  # val String BoseMsg = "Hallo dies ist ein Test"  // BoseTTSText.state
  # val String TranslateUrl = "http://translate.google.com/translate_tts?ie=UTF-8&amp;tl=DE&amp;client=tw-ob&amp;q=" + URLEncoder.encode(BoseMsg,"UTF-8")
  # val String PostData = '<play_info><app_key>' + AppKey + '</app_key><url>' + TranslateUrl + '</url><service>OpenHAB</service><volume>20</volume></play_info>';
  # sendHttpPostRequest("http://" + BoseIP + ":8090/speaker","",PostData)
