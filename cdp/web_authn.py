# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: WebAuthn (experimental)

from __future__ import annotations
from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing


class AuthenticatorId(str):
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> AuthenticatorId:
        return cls(json)

    def __repr__(self):
        return 'AuthenticatorId({})'.format(super().__repr__())


class AuthenticatorProtocol(enum.Enum):
    U2F = "u2f"
    CTAP2 = "ctap2"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AuthenticatorProtocol:
        return cls(json)


class Ctap2Version(enum.Enum):
    CTAP2_0 = "ctap2_0"
    CTAP2_1 = "ctap2_1"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> Ctap2Version:
        return cls(json)


class AuthenticatorTransport(enum.Enum):
    USB = "usb"
    NFC = "nfc"
    BLE = "ble"
    CABLE = "cable"
    INTERNAL = "internal"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AuthenticatorTransport:
        return cls(json)


@dataclass
class VirtualAuthenticatorOptions:
    protocol: AuthenticatorProtocol

    transport: AuthenticatorTransport

    #: Defaults to ctap2_0. Ignored if ``protocol`` == u2f.
    ctap2_version: typing.Optional[Ctap2Version] = None

    #: Defaults to false.
    has_resident_key: typing.Optional[bool] = None

    #: Defaults to false.
    has_user_verification: typing.Optional[bool] = None

    #: If set to true, the authenticator will support the largeBlob extension.
    #: https://w3c.github.io/webauthn#largeBlob
    #: Defaults to false.
    has_large_blob: typing.Optional[bool] = None

    #: If set to true, the authenticator will support the credBlob extension.
    #: https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension
    #: Defaults to false.
    has_cred_blob: typing.Optional[bool] = None

    #: If set to true, the authenticator will support the minPinLength extension.
    #: https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extension
    #: Defaults to false.
    has_min_pin_length: typing.Optional[bool] = None

    #: If set to true, the authenticator will support the prf extension.
    #: https://w3c.github.io/webauthn/#prf-extension
    #: Defaults to false.
    has_prf: typing.Optional[bool] = None

    #: If set to true, tests of user presence will succeed immediately.
    #: Otherwise, they will not be resolved. Defaults to true.
    automatic_presence_simulation: typing.Optional[bool] = None

    #: Sets whether User Verification succeeds or fails for an authenticator.
    #: Defaults to false.
    is_user_verified: typing.Optional[bool] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['protocol'] = self.protocol.to_json()
        json['transport'] = self.transport.to_json()
        if self.ctap2_version is not None:
            json['ctap2Version'] = self.ctap2_version.to_json()
        if self.has_resident_key is not None:
            json['hasResidentKey'] = self.has_resident_key
        if self.has_user_verification is not None:
            json['hasUserVerification'] = self.has_user_verification
        if self.has_large_blob is not None:
            json['hasLargeBlob'] = self.has_large_blob
        if self.has_cred_blob is not None:
            json['hasCredBlob'] = self.has_cred_blob
        if self.has_min_pin_length is not None:
            json['hasMinPinLength'] = self.has_min_pin_length
        if self.has_prf is not None:
            json['hasPrf'] = self.has_prf
        if self.automatic_presence_simulation is not None:
            json['automaticPresenceSimulation'] = self.automatic_presence_simulation
        if self.is_user_verified is not None:
            json['isUserVerified'] = self.is_user_verified
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> VirtualAuthenticatorOptions:
        return cls(
            protocol=AuthenticatorProtocol.from_json(json['protocol']),
            transport=AuthenticatorTransport.from_json(json['transport']),
            ctap2_version=Ctap2Version.from_json(json['ctap2Version']) if 'ctap2Version' in json else None,
            has_resident_key=bool(json['hasResidentKey']) if 'hasResidentKey' in json else None,
            has_user_verification=bool(json['hasUserVerification']) if 'hasUserVerification' in json else None,
            has_large_blob=bool(json['hasLargeBlob']) if 'hasLargeBlob' in json else None,
            has_cred_blob=bool(json['hasCredBlob']) if 'hasCredBlob' in json else None,
            has_min_pin_length=bool(json['hasMinPinLength']) if 'hasMinPinLength' in json else None,
            has_prf=bool(json['hasPrf']) if 'hasPrf' in json else None,
            automatic_presence_simulation=bool(json['automaticPresenceSimulation']) if 'automaticPresenceSimulation' in json else None,
            is_user_verified=bool(json['isUserVerified']) if 'isUserVerified' in json else None,
        )


@dataclass
class Credential:
    credential_id: str

    is_resident_credential: bool

    #: The ECDSA P-256 private key in PKCS#8 format. (Encoded as a base64 string when passed over JSON)
    private_key: str

    #: Signature counter. This is incremented by one for each successful
    #: assertion.
    #: See https://w3c.github.io/webauthn/#signature-counter
    sign_count: int

    #: Relying Party ID the credential is scoped to. Must be set when adding a
    #: credential.
    rp_id: typing.Optional[str] = None

    #: An opaque byte sequence with a maximum size of 64 bytes mapping the
    #: credential to a specific user. (Encoded as a base64 string when passed over JSON)
    user_handle: typing.Optional[str] = None

    #: The large blob associated with the credential.
    #: See https://w3c.github.io/webauthn/#sctn-large-blob-extension (Encoded as a base64 string when passed over JSON)
    large_blob: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['credentialId'] = self.credential_id
        json['isResidentCredential'] = self.is_resident_credential
        json['privateKey'] = self.private_key
        json['signCount'] = self.sign_count
        if self.rp_id is not None:
            json['rpId'] = self.rp_id
        if self.user_handle is not None:
            json['userHandle'] = self.user_handle
        if self.large_blob is not None:
            json['largeBlob'] = self.large_blob
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Credential:
        return cls(
            credential_id=str(json['credentialId']),
            is_resident_credential=bool(json['isResidentCredential']),
            private_key=str(json['privateKey']),
            sign_count=int(json['signCount']),
            rp_id=str(json['rpId']) if 'rpId' in json else None,
            user_handle=str(json['userHandle']) if 'userHandle' in json else None,
            large_blob=str(json['largeBlob']) if 'largeBlob' in json else None,
        )


def enable(
        enable_ui: typing.Optional[bool] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enable the WebAuthn domain and start intercepting credential storage and
    retrieval with a virtual authenticator.

    :param enable_ui: *(Optional)* Whether to enable the WebAuthn user interface. Enabling the UI is recommended for debugging and demo purposes, as it is closer to the real experience. Disabling the UI is recommended for automated testing. Supported at the embedder's discretion if UI is available. Defaults to false.
    '''
    params: T_JSON_DICT = dict()
    if enable_ui is not None:
        params['enableUI'] = enable_ui
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.enable',
        'params': params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disable the WebAuthn domain.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.disable',
    }
    json = yield cmd_dict


def add_virtual_authenticator(
        options: VirtualAuthenticatorOptions
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,AuthenticatorId]:
    '''
    Creates and adds a virtual authenticator.

    :param options:
    :returns: 
    '''
    params: T_JSON_DICT = dict()
    params['options'] = options.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.addVirtualAuthenticator',
        'params': params,
    }
    json = yield cmd_dict
    return AuthenticatorId.from_json(json['authenticatorId'])


def set_response_override_bits(
        authenticator_id: AuthenticatorId,
        is_bogus_signature: typing.Optional[bool] = None,
        is_bad_uv: typing.Optional[bool] = None,
        is_bad_up: typing.Optional[bool] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.

    :param authenticator_id:
    :param is_bogus_signature: *(Optional)* If isBogusSignature is set, overrides the signature in the authenticator response to be zero. Defaults to false.
    :param is_bad_uv: *(Optional)* If isBadUV is set, overrides the UV bit in the flags in the authenticator response to be zero. Defaults to false.
    :param is_bad_up: *(Optional)* If isBadUP is set, overrides the UP bit in the flags in the authenticator response to be zero. Defaults to false.
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    if is_bogus_signature is not None:
        params['isBogusSignature'] = is_bogus_signature
    if is_bad_uv is not None:
        params['isBadUV'] = is_bad_uv
    if is_bad_up is not None:
        params['isBadUP'] = is_bad_up
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.setResponseOverrideBits',
        'params': params,
    }
    json = yield cmd_dict


def remove_virtual_authenticator(
        authenticator_id: AuthenticatorId
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Removes the given authenticator.

    :param authenticator_id:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.removeVirtualAuthenticator',
        'params': params,
    }
    json = yield cmd_dict


def add_credential(
        authenticator_id: AuthenticatorId,
        credential: Credential
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Adds the credential to the specified authenticator.

    :param authenticator_id:
    :param credential:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    params['credential'] = credential.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.addCredential',
        'params': params,
    }
    json = yield cmd_dict


def get_credential(
        authenticator_id: AuthenticatorId,
        credential_id: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,Credential]:
    '''
    Returns a single credential stored in the given virtual authenticator that
    matches the credential ID.

    :param authenticator_id:
    :param credential_id:
    :returns: 
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    params['credentialId'] = credential_id
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.getCredential',
        'params': params,
    }
    json = yield cmd_dict
    return Credential.from_json(json['credential'])


def get_credentials(
        authenticator_id: AuthenticatorId
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List[Credential]]:
    '''
    Returns all the credentials stored in the given virtual authenticator.

    :param authenticator_id:
    :returns: 
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.getCredentials',
        'params': params,
    }
    json = yield cmd_dict
    return [Credential.from_json(i) for i in json['credentials']]


def remove_credential(
        authenticator_id: AuthenticatorId,
        credential_id: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Removes a credential from the authenticator.

    :param authenticator_id:
    :param credential_id:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    params['credentialId'] = credential_id
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.removeCredential',
        'params': params,
    }
    json = yield cmd_dict


def clear_credentials(
        authenticator_id: AuthenticatorId
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Clears all the credentials from the specified device.

    :param authenticator_id:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.clearCredentials',
        'params': params,
    }
    json = yield cmd_dict


def set_user_verified(
        authenticator_id: AuthenticatorId,
        is_user_verified: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Sets whether User Verification succeeds or fails for an authenticator.
    The default is true.

    :param authenticator_id:
    :param is_user_verified:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    params['isUserVerified'] = is_user_verified
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.setUserVerified',
        'params': params,
    }
    json = yield cmd_dict


def set_automatic_presence_simulation(
        authenticator_id: AuthenticatorId,
        enabled: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator.
    The default is true.

    :param authenticator_id:
    :param enabled:
    '''
    params: T_JSON_DICT = dict()
    params['authenticatorId'] = authenticator_id.to_json()
    params['enabled'] = enabled
    cmd_dict: T_JSON_DICT = {
        'method': 'WebAuthn.setAutomaticPresenceSimulation',
        'params': params,
    }
    json = yield cmd_dict


@event_class('WebAuthn.credentialAdded')
@dataclass
class CredentialAdded:
    '''
    Triggered when a credential is added to an authenticator.
    '''
    authenticator_id: AuthenticatorId
    credential: Credential

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CredentialAdded:
        return cls(
            authenticator_id=AuthenticatorId.from_json(json['authenticatorId']),
            credential=Credential.from_json(json['credential'])
        )


@event_class('WebAuthn.credentialAsserted')
@dataclass
class CredentialAsserted:
    '''
    Triggered when a credential is used in a webauthn assertion.
    '''
    authenticator_id: AuthenticatorId
    credential: Credential

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CredentialAsserted:
        return cls(
            authenticator_id=AuthenticatorId.from_json(json['authenticatorId']),
            credential=Credential.from_json(json['credential'])
        )
