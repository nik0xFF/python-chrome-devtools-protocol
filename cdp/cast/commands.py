'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: cast
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


def enable(presentation_url: str) -> typing.Generator[dict,dict,None]:
    '''
    Starts observing for sinks that can be used for tab mirroring, and if set,
    sinks compatible with |presentationUrl| as well. When sinks are found, a
    |sinksUpdated| event is fired.
    Also starts observing for issue messages. When an issue is added or removed,
    an |issueUpdated| event is fired.
    
    :param presentation_url: 
    '''

    cmd_dict = {
        'method': 'Cast.enable',
        'params': {
            'presentationUrl': presentation_url,
        }
    }
    response = yield cmd_dict


def disable() -> typing.Generator[dict,dict,None]:
    '''
    Stops observing for sinks and issues.
    '''

    cmd_dict = {
        'method': 'Cast.disable',
    }
    response = yield cmd_dict


def set_sink_to_use(sink_name: str) -> typing.Generator[dict,dict,None]:
    '''
    Sets a sink to be used when the web page requests the browser to choose a
    sink via Presentation API, Remote Playback API, or Cast SDK.
    
    :param sink_name: 
    '''

    cmd_dict = {
        'method': 'Cast.setSinkToUse',
        'params': {
            'sinkName': sink_name,
        }
    }
    response = yield cmd_dict


def start_tab_mirroring(sink_name: str) -> typing.Generator[dict,dict,None]:
    '''
    Starts mirroring the tab to the sink.
    
    :param sink_name: 
    '''

    cmd_dict = {
        'method': 'Cast.startTabMirroring',
        'params': {
            'sinkName': sink_name,
        }
    }
    response = yield cmd_dict


def stop_casting(sink_name: str) -> typing.Generator[dict,dict,None]:
    '''
    Stops the active Cast session on the sink.
    
    :param sink_name: 
    '''

    cmd_dict = {
        'method': 'Cast.stopCasting',
        'params': {
            'sinkName': sink_name,
        }
    }
    response = yield cmd_dict


