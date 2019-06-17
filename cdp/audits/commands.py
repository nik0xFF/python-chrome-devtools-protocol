'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: audits
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..network import types as network



def get_encoded_response(request_id: network.RequestId, encoding: str, quality: float, size_only: bool) -> typing.Generator[dict,dict,dict]:
    '''
    Returns the response body and size if it were re-encoded with the specified settings. Only
    applies to images.
    
    :param request_id: Identifier of the network request to get content for.
    :param encoding: The encoding to use.
    :param quality: The quality of the encoding (0-1). (defaults to 1)
    :param size_only: Whether to only return the size information (defaults to false).
    :returns: a dict with the following keys:
        * body: The encoded body as a base64 string. Omitted if sizeOnly is true.
        * originalSize: Size before re-encoding.
        * encodedSize: Size after re-encoding.
    '''

    cmd_dict = {
        'method': 'Audits.getEncodedResponse',
        'params': {
            'requestId': request_id,
            'encoding': encoding,
            'quality': quality,
            'sizeOnly': size_only,
        }
    }
    response = yield cmd_dict
    return {
        'body': str(response['body']),
        'originalSize': int(response['originalSize']),
        'encodedSize': int(response['encodedSize']),
    }


