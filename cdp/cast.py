'''
DO NOT EDIT THIS FILE

This file is generated from the CDP specification. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: Cast
Experimental: True
'''

from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing


@dataclass
class Sink:
    name: str

    id: str

    #: Text describing the current session. Present only if there is an active
    #: session on the sink.
    session: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['id'] = self.id
        if self.session is not None:
            json['session'] = self.session
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'Sink':
        return cls(
            name=str(json['name']),
            id=str(json['id']),
            session=str(json['session']) if 'session' in json else None,
        )


def enable(
        presentation_url: typing.Optional[str] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Starts observing for sinks that can be used for tab mirroring, and if set,
    sinks compatible with |presentationUrl| as well. When sinks are found, a
    |sinksUpdated| event is fired.
    Also starts observing for issue messages. When an issue is added or removed,
    an |issueUpdated| event is fired.

    :param presentation_url:
    '''
    params: T_JSON_DICT = dict()
    if presentation_url is not None:
        params['presentationUrl'] = presentation_url
    cmd_dict: T_JSON_DICT = {
        'method': 'Cast.enable',
        'params': params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Stops observing for sinks and issues.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Cast.disable',
    }
    json = yield cmd_dict


def set_sink_to_use(
        sink_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Sets a sink to be used when the web page requests the browser to choose a
    sink via Presentation API, Remote Playback API, or Cast SDK.

    :param sink_name:
    '''
    params: T_JSON_DICT = dict()
    params['sinkName'] = sink_name
    cmd_dict: T_JSON_DICT = {
        'method': 'Cast.setSinkToUse',
        'params': params,
    }
    json = yield cmd_dict


def start_tab_mirroring(
        sink_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Starts mirroring the tab to the sink.

    :param sink_name:
    '''
    params: T_JSON_DICT = dict()
    params['sinkName'] = sink_name
    cmd_dict: T_JSON_DICT = {
        'method': 'Cast.startTabMirroring',
        'params': params,
    }
    json = yield cmd_dict


def stop_casting(
        sink_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Stops the active Cast session on the sink.

    :param sink_name:
    '''
    params: T_JSON_DICT = dict()
    params['sinkName'] = sink_name
    cmd_dict: T_JSON_DICT = {
        'method': 'Cast.stopCasting',
        'params': params,
    }
    json = yield cmd_dict


@event_class('Cast.sinksUpdated')
@dataclass
class SinksUpdated:
    '''
    This is fired whenever the list of available sinks changes. A sink is a
    device or a software surface that you can cast to.
    '''
    sinks: typing.List['Sink']

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'SinksUpdated':
        return cls(
            sinks=[Sink.from_json(i) for i in json['sinks']]
        )


@event_class('Cast.issueUpdated')
@dataclass
class IssueUpdated:
    '''
    This is fired whenever the outstanding issue/error message changes.
    |issueMessage| is empty if there is no issue.
    '''
    issue_message: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'IssueUpdated':
        return cls(
            issue_message=str(json['issueMessage'])
        )