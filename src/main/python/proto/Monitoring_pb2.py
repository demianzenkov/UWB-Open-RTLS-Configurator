# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Monitoring.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Monitoring.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10Monitoring.proto\"\x81\x03\n\nMonitoring\x12$\n\x03TWR\x18\x01 \x01(\x0b\x32\x17.Monitoring.TWR_message\x12&\n\x04TDOA\x18\x02 \x01(\x0b\x32\x18.Monitoring.TDOA_message\x1a\x8c\x01\n\x0bTWR_message\x12\x0e\n\x06NodeID\x18\x01 \x01(\r\x12\x13\n\x0bInitiatorID\x18\x02 \x01(\r\x12\x10\n\x08\x44istance\x18\x03 \x01(\x02\x12\x11\n\tNodeTicks\x18\x04 \x01(\r\x12\x0e\n\x06PollNN\x18\x05 \x01(\r\x12\x12\n\nResponseNN\x18\x07 \x01(\r\x12\x0f\n\x07\x46inalNN\x18\x06 \x01(\r\x1a\x95\x01\n\x0cTDOA_message\x12\x0e\n\x06NodeID\x18\x01 \x01(\r\x12\x0f\n\x07\x42linkID\x18\x02 \x01(\r\x12\x0f\n\x07\x42linkTS\x18\x03 \x01(\x04\x12\x0f\n\x07\x42linkNN\x18\x04 \x01(\r\x12\x0e\n\x06SyncID\x18\x05 \x01(\r\x12\x10\n\x08SyncTxTS\x18\x06 \x01(\x04\x12\x10\n\x08SyncRxTS\x18\x07 \x01(\x04\x12\x0e\n\x06SyncNN\x18\x08 \x01(\rb\x06proto3'
)




_MONITORING_TWR_MESSAGE = _descriptor.Descriptor(
  name='TWR_message',
  full_name='Monitoring.TWR_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NodeID', full_name='Monitoring.TWR_message.NodeID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='InitiatorID', full_name='Monitoring.TWR_message.InitiatorID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Distance', full_name='Monitoring.TWR_message.Distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NodeTicks', full_name='Monitoring.TWR_message.NodeTicks', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PollNN', full_name='Monitoring.TWR_message.PollNN', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ResponseNN', full_name='Monitoring.TWR_message.ResponseNN', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FinalNN', full_name='Monitoring.TWR_message.FinalNN', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=254,
)

_MONITORING_TDOA_MESSAGE = _descriptor.Descriptor(
  name='TDOA_message',
  full_name='Monitoring.TDOA_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NodeID', full_name='Monitoring.TDOA_message.NodeID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BlinkID', full_name='Monitoring.TDOA_message.BlinkID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BlinkTS', full_name='Monitoring.TDOA_message.BlinkTS', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BlinkNN', full_name='Monitoring.TDOA_message.BlinkNN', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SyncID', full_name='Monitoring.TDOA_message.SyncID', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SyncTxTS', full_name='Monitoring.TDOA_message.SyncTxTS', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SyncRxTS', full_name='Monitoring.TDOA_message.SyncRxTS', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SyncNN', full_name='Monitoring.TDOA_message.SyncNN', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=406,
)

_MONITORING = _descriptor.Descriptor(
  name='Monitoring',
  full_name='Monitoring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TWR', full_name='Monitoring.TWR', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TDOA', full_name='Monitoring.TDOA', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MONITORING_TWR_MESSAGE, _MONITORING_TDOA_MESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=406,
)

_MONITORING_TWR_MESSAGE.containing_type = _MONITORING
_MONITORING_TDOA_MESSAGE.containing_type = _MONITORING
_MONITORING.fields_by_name['TWR'].message_type = _MONITORING_TWR_MESSAGE
_MONITORING.fields_by_name['TDOA'].message_type = _MONITORING_TDOA_MESSAGE
DESCRIPTOR.message_types_by_name['Monitoring'] = _MONITORING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), {

  'TWR_message' : _reflection.GeneratedProtocolMessageType('TWR_message', (_message.Message,), {
    'DESCRIPTOR' : _MONITORING_TWR_MESSAGE,
    '__module__' : 'Monitoring_pb2'
    # @@protoc_insertion_point(class_scope:Monitoring.TWR_message)
    })
  ,

  'TDOA_message' : _reflection.GeneratedProtocolMessageType('TDOA_message', (_message.Message,), {
    'DESCRIPTOR' : _MONITORING_TDOA_MESSAGE,
    '__module__' : 'Monitoring_pb2'
    # @@protoc_insertion_point(class_scope:Monitoring.TDOA_message)
    })
  ,
  'DESCRIPTOR' : _MONITORING,
  '__module__' : 'Monitoring_pb2'
  # @@protoc_insertion_point(class_scope:Monitoring)
  })
_sym_db.RegisterMessage(Monitoring)
_sym_db.RegisterMessage(Monitoring.TWR_message)
_sym_db.RegisterMessage(Monitoring.TDOA_message)


# @@protoc_insertion_point(module_scope)
