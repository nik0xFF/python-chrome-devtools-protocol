'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: emulation
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..dom import types as dom
from ..network import types as network
from ..page import types as page



def can_emulate() -> typing.Generator[dict,dict,bool]:
    '''
    Tells whether emulation is supported.
    :returns: True if emulation is supported.
    '''

    cmd_dict = {
        'method': 'Emulation.canEmulate',
    }
    response = yield cmd_dict
    return bool(response['result'])


def clear_device_metrics_override() -> typing.Generator[dict,dict,None]:
    '''
    Clears the overriden device metrics.
    '''

    cmd_dict = {
        'method': 'Emulation.clearDeviceMetricsOverride',
    }
    response = yield cmd_dict


def clear_geolocation_override() -> typing.Generator[dict,dict,None]:
    '''
    Clears the overriden Geolocation Position and Error.
    '''

    cmd_dict = {
        'method': 'Emulation.clearGeolocationOverride',
    }
    response = yield cmd_dict


def reset_page_scale_factor() -> typing.Generator[dict,dict,None]:
    '''
    Requests that page scale factor is reset to initial values.
    '''

    cmd_dict = {
        'method': 'Emulation.resetPageScaleFactor',
    }
    response = yield cmd_dict


def set_focus_emulation_enabled(enabled: bool) -> typing.Generator[dict,dict,None]:
    '''
    Enables or disables simulating a focused and active page.
    
    :param enabled: Whether to enable to disable focus emulation.
    '''

    cmd_dict = {
        'method': 'Emulation.setFocusEmulationEnabled',
        'params': {
            'enabled': enabled,
        }
    }
    response = yield cmd_dict


def set_cpu_throttling_rate(rate: float) -> typing.Generator[dict,dict,None]:
    '''
    Enables CPU throttling to emulate slow CPUs.
    
    :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
    '''

    cmd_dict = {
        'method': 'Emulation.setCPUThrottlingRate',
        'params': {
            'rate': rate,
        }
    }
    response = yield cmd_dict


def set_default_background_color_override(color: dom.RGBA) -> typing.Generator[dict,dict,None]:
    '''
    Sets or clears an override of the default background color of the frame. This override is used
    if the content does not specify one.
    
    :param color: RGBA of the default background color. If not specified, any existing override will be
    cleared.
    '''

    cmd_dict = {
        'method': 'Emulation.setDefaultBackgroundColorOverride',
        'params': {
            'color': color,
        }
    }
    response = yield cmd_dict


def set_device_metrics_override(width: int, height: int, device_scale_factor: float, mobile: bool, scale: float, screen_width: int, screen_height: int, position_x: int, position_y: int, dont_set_visible_size: bool, screen_orientation: ScreenOrientation, viewport: page.Viewport) -> typing.Generator[dict,dict,None]:
    '''
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
    window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
    query results).
    
    :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
    :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
    autosizing and more.
    :param scale: Scale to apply to resulting view image.
    :param screen_width: Overriding screen width value in pixels (minimum 0, maximum 10000000).
    :param screen_height: Overriding screen height value in pixels (minimum 0, maximum 10000000).
    :param position_x: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
    :param position_y: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
    :param dont_set_visible_size: Do not set visible view size, rely upon explicit setVisibleSize call.
    :param screen_orientation: Screen orientation override.
    :param viewport: If set, the visible area of the page will be overridden to this viewport. This viewport
    change is not observed by the page, e.g. viewport-relative elements do not change positions.
    '''

    cmd_dict = {
        'method': 'Emulation.setDeviceMetricsOverride',
        'params': {
            'width': width,
            'height': height,
            'deviceScaleFactor': device_scale_factor,
            'mobile': mobile,
            'scale': scale,
            'screenWidth': screen_width,
            'screenHeight': screen_height,
            'positionX': position_x,
            'positionY': position_y,
            'dontSetVisibleSize': dont_set_visible_size,
            'screenOrientation': screen_orientation,
            'viewport': viewport,
        }
    }
    response = yield cmd_dict


def set_scrollbars_hidden(hidden: bool) -> typing.Generator[dict,dict,None]:
    '''
    
    
    :param hidden: Whether scrollbars should be always hidden.
    '''

    cmd_dict = {
        'method': 'Emulation.setScrollbarsHidden',
        'params': {
            'hidden': hidden,
        }
    }
    response = yield cmd_dict


def set_document_cookie_disabled(disabled: bool) -> typing.Generator[dict,dict,None]:
    '''
    
    
    :param disabled: Whether document.coookie API should be disabled.
    '''

    cmd_dict = {
        'method': 'Emulation.setDocumentCookieDisabled',
        'params': {
            'disabled': disabled,
        }
    }
    response = yield cmd_dict


def set_emit_touch_events_for_mouse(enabled: bool, configuration: str) -> typing.Generator[dict,dict,None]:
    '''
    
    
    :param enabled: Whether touch emulation based on mouse input should be enabled.
    :param configuration: Touch/gesture events configuration. Default: current platform.
    '''

    cmd_dict = {
        'method': 'Emulation.setEmitTouchEventsForMouse',
        'params': {
            'enabled': enabled,
            'configuration': configuration,
        }
    }
    response = yield cmd_dict


def set_emulated_media(media: str) -> typing.Generator[dict,dict,None]:
    '''
    Emulates the given media for CSS media queries.
    
    :param media: Media type to emulate. Empty string disables the override.
    '''

    cmd_dict = {
        'method': 'Emulation.setEmulatedMedia',
        'params': {
            'media': media,
        }
    }
    response = yield cmd_dict


def set_geolocation_override(latitude: float, longitude: float, accuracy: float) -> typing.Generator[dict,dict,None]:
    '''
    Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
    unavailable.
    
    :param latitude: Mock latitude
    :param longitude: Mock longitude
    :param accuracy: Mock accuracy
    '''

    cmd_dict = {
        'method': 'Emulation.setGeolocationOverride',
        'params': {
            'latitude': latitude,
            'longitude': longitude,
            'accuracy': accuracy,
        }
    }
    response = yield cmd_dict


def set_navigator_overrides(platform: str) -> typing.Generator[dict,dict,None]:
    '''
    Overrides value returned by the javascript navigator object.
    
    :param platform: The platform navigator.platform should return.
    '''

    cmd_dict = {
        'method': 'Emulation.setNavigatorOverrides',
        'params': {
            'platform': platform,
        }
    }
    response = yield cmd_dict


def set_page_scale_factor(page_scale_factor: float) -> typing.Generator[dict,dict,None]:
    '''
    Sets a specified page scale factor.
    
    :param page_scale_factor: Page scale factor.
    '''

    cmd_dict = {
        'method': 'Emulation.setPageScaleFactor',
        'params': {
            'pageScaleFactor': page_scale_factor,
        }
    }
    response = yield cmd_dict


def set_script_execution_disabled(value: bool) -> typing.Generator[dict,dict,None]:
    '''
    Switches script execution in the page.
    
    :param value: Whether script execution should be disabled in the page.
    '''

    cmd_dict = {
        'method': 'Emulation.setScriptExecutionDisabled',
        'params': {
            'value': value,
        }
    }
    response = yield cmd_dict


def set_touch_emulation_enabled(enabled: bool, max_touch_points: int) -> typing.Generator[dict,dict,None]:
    '''
    Enables touch on platforms which do not support them.
    
    :param enabled: Whether the touch event emulation should be enabled.
    :param max_touch_points: Maximum touch points supported. Defaults to one.
    '''

    cmd_dict = {
        'method': 'Emulation.setTouchEmulationEnabled',
        'params': {
            'enabled': enabled,
            'maxTouchPoints': max_touch_points,
        }
    }
    response = yield cmd_dict


def set_virtual_time_policy(policy: VirtualTimePolicy, budget: float, max_virtual_time_task_starvation_count: int, wait_for_navigation: bool, initial_virtual_time: network.TimeSinceEpoch) -> typing.Generator[dict,dict,float]:
    '''
    Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
    the current virtual time policy.  Note this supersedes any previous time budget.
    
    :param policy: 
    :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
    virtualTimeBudgetExpired event is sent.
    :param max_virtual_time_task_starvation_count: If set this specifies the maximum number of tasks that can be run before virtual is forced
    forwards to prevent deadlock.
    :param wait_for_navigation: If set the virtual time policy change should be deferred until any frame starts navigating.
    Note any previous deferred policy change is superseded.
    :param initial_virtual_time: If set, base::Time::Now will be overriden to initially return this value.
    :returns: Absolute timestamp at which virtual time was first enabled (up time in milliseconds).
    '''

    cmd_dict = {
        'method': 'Emulation.setVirtualTimePolicy',
        'params': {
            'policy': policy,
            'budget': budget,
            'maxVirtualTimeTaskStarvationCount': max_virtual_time_task_starvation_count,
            'waitForNavigation': wait_for_navigation,
            'initialVirtualTime': initial_virtual_time,
        }
    }
    response = yield cmd_dict
    return float(response['virtualTimeTicksBase'])


def set_timezone_override(timezone_id: str) -> typing.Generator[dict,dict,None]:
    '''
    Overrides default host system timezone with the specified one.
    
    :param timezone_id: The timezone identifier. If empty, disables the override and
    restores default host system timezone.
    '''

    cmd_dict = {
        'method': 'Emulation.setTimezoneOverride',
        'params': {
            'timezoneId': timezone_id,
        }
    }
    response = yield cmd_dict


def set_visible_size(width: int, height: int) -> typing.Generator[dict,dict,None]:
    '''
    Resizes the frame/viewport of the page. Note that this does not affect the frame's container
    (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
    on Android.
    
    :param width: Frame width (DIP).
    :param height: Frame height (DIP).
    '''

    cmd_dict = {
        'method': 'Emulation.setVisibleSize',
        'params': {
            'width': width,
            'height': height,
        }
    }
    response = yield cmd_dict


def set_user_agent_override(user_agent: str, accept_language: str, platform: str) -> typing.Generator[dict,dict,None]:
    '''
    Allows overriding user agent with the given string.
    
    :param user_agent: User agent to use.
    :param accept_language: Browser langugage to emulate.
    :param platform: The platform navigator.platform should return.
    '''

    cmd_dict = {
        'method': 'Emulation.setUserAgentOverride',
        'params': {
            'userAgent': user_agent,
            'acceptLanguage': accept_language,
            'platform': platform,
        }
    }
    response = yield cmd_dict


