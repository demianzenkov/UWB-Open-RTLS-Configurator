# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0eSettings.proto\"\xec\x03\n\x08Settings\x12\x10\n\x08\x44\x65viceID\x18\x01 \x01(\r\x12\x10\n\x08\x44\x65viceIp\x18\x02 \x01(\r\x12\x12\n\nSubnetMask\x18\x03 \x01(\r\x12\x11\n\tGatewayIp\x18\x04 \x01(\r\x12\x10\n\x08ServerIp\x18\x05 \x01(\r\x12\x16\n\x0e\x43onnectionPort\x18\x06 \x01(\r\x12\x0e\n\x06NodeID\x18\x07 \x01(\r\x12%\n\x08NodeType\x18\x08 \x01(\x0e\x32\x13.Settings.node_type\x12%\n\x08RTLSMode\x18\t \x01(\x0e\x32\x13.Settings.rtls_mode\x12\x11\n\tPositionX\x18\n \x01(\x02\x12\x11\n\tPositionY\x18\x0b \x01(\x02\x12\x11\n\tPositionZ\x18\x0c \x01(\x02\x12\x18\n\x10TwrAnchorsForTag\x18\r \x03(\r\x12\x14\n\x0cTwrTagPeriod\x18\x0e \x01(\r\"]\n\tnode_type\x12\r\n\tTYPE_NONE\x10\x00\x12\x0e\n\nTYPE_UNDEF\x10\x01\x12\x0f\n\x0bTYPE_ANCHOR\x10\x02\x12\x12\n\x0eTYPE_SYNC_NODE\x10\x03\x12\x0c\n\x08TYPE_TAG\x10\x04\"E\n\trtls_mode\x12\r\n\tMODE_NONE\x10\x00\x12\x0c\n\x08MODE_OFF\x10\x01\x12\x0c\n\x08MODE_TWR\x10\x02\x12\r\n\tMODE_TDOA\x10\x03\x62\x06proto3'
)



_SETTINGS_NODE_TYPE = _descriptor.EnumDescriptor(
  name='node_type',
  full_name='Settings.node_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNDEF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_ANCHOR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SYNC_NODE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_TAG', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=347,
  serialized_end=440,
)
_sym_db.RegisterEnumDescriptor(_SETTINGS_NODE_TYPE)

_SETTINGS_RTLS_MODE = _descriptor.EnumDescriptor(
  name='rtls_mode',
  full_name='Settings.rtls_mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODE_OFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODE_TWR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODE_TDOA', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=442,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_SETTINGS_RTLS_MODE)


_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DeviceID', full_name='Settings.DeviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DeviceIp', full_name='Settings.DeviceIp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SubnetMask', full_name='Settings.SubnetMask', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GatewayIp', full_name='Settings.GatewayIp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ServerIp', full_name='Settings.ServerIp', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ConnectionPort', full_name='Settings.ConnectionPort', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NodeID', full_name='Settings.NodeID', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NodeType', full_name='Settings.NodeType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RTLSMode', full_name='Settings.RTLSMode', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PositionX', full_name='Settings.PositionX', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PositionY', full_name='Settings.PositionY', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PositionZ', full_name='Settings.PositionZ', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TwrAnchorsForTag', full_name='Settings.TwrAnchorsForTag', index=12,
      number=13, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TwrTagPeriod', full_name='Settings.TwrTagPeriod', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETTINGS_NODE_TYPE,
    _SETTINGS_RTLS_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=511,
)

_SETTINGS.fields_by_name['NodeType'].enum_type = _SETTINGS_NODE_TYPE
_SETTINGS.fields_by_name['RTLSMode'].enum_type = _SETTINGS_RTLS_MODE
_SETTINGS_NODE_TYPE.containing_type = _SETTINGS
_SETTINGS_RTLS_MODE.containing_type = _SETTINGS
DESCRIPTOR.message_types_by_name['Settings'] = _SETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGS,
  '__module__' : 'Settings_pb2'
  # @@protoc_insertion_point(class_scope:Settings)
  })
_sym_db.RegisterMessage(Settings)


# @@protoc_insertion_point(module_scope)
