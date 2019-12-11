# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: innpv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='innpv.proto',
  package='innpv.protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0binnpv.proto\x12\x0einnpv.protocol\"\x85\x01\n\nFromClient\x12\x37\n\ninitialize\x18\x01 \x01(\x0b\x32!.innpv.protocol.InitializeRequestH\x00\x12\x33\n\x08\x61nalysis\x18\x02 \x01(\x0b\x32\x1f.innpv.protocol.AnalysisRequestH\x00\x42\t\n\x07payload\"-\n\x11InitializeRequest\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\"*\n\x0f\x41nalysisRequest\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\"\xf7\x01\n\nFromServer\x12.\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.innpv.protocol.ProtocolErrorH\x00\x12\x38\n\ninitialize\x18\x02 \x01(\x0b\x32\".innpv.protocol.InitializeResponseH\x00\x12;\n\x0cmemory_usage\x18\x03 \x01(\x0b\x32#.innpv.protocol.MemoryUsageResponseH\x00\x12\x37\n\x0e\x61nalysis_error\x18\x04 \x01(\x0b\x32\x1d.innpv.protocol.AnalysisErrorH\x00\x42\t\n\x07payload\"\\\n\x12InitializeResponse\x12\x1b\n\x13server_project_root\x18\x01 \x01(\t\x12)\n\x0b\x65ntry_point\x18\x02 \x01(\x0b\x32\x14.innpv.protocol.Path\"\xd9\x01\n\x13MemoryUsageResponse\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\x12\x18\n\x10peak_usage_bytes\x18\x02 \x01(\x04\x12\x1d\n\x15memory_capacity_bytes\x18\x03 \x01(\x04\x12\x33\n\x0eweight_entries\x18\x04 \x03(\x0b\x32\x1b.innpv.protocol.WeightEntry\x12;\n\x12\x61\x63tivation_entries\x18\x05 \x03(\x0b\x32\x1f.innpv.protocol.ActivationEntry\"?\n\rAnalysisError\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\x12\x15\n\rerror_message\x18\x02 \x01(\t\"#\n\rProtocolError\x12\x12\n\nerror_code\x18\x01 \x01(\r\"\x1a\n\x04Path\x12\x12\n\ncomponents\x18\x01 \x03(\t\"H\n\rFileReference\x12\"\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x14.innpv.protocol.Path\x12\x13\n\x0bline_number\x18\x02 \x01(\r\"m\n\x0f\x41\x63tivationEntry\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x04\x12.\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x1d.innpv.protocol.FileReference\"\x7f\n\x0bWeightEntry\x12\x13\n\x0bweight_name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x04\x12\x17\n\x0fgrad_size_bytes\x18\x03 \x01(\x04\x12.\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x1d.innpv.protocol.FileReferenceb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FROMCLIENT = _descriptor.Descriptor(
  name='FromClient',
  full_name='innpv.protocol.FromClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initialize', full_name='innpv.protocol.FromClient.initialize', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis', full_name='innpv.protocol.FromClient.analysis', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='innpv.protocol.FromClient.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=32,
  serialized_end=165,
)


_INITIALIZEREQUEST = _descriptor.Descriptor(
  name='InitializeRequest',
  full_name='innpv.protocol.InitializeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='innpv.protocol.InitializeRequest.protocol_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=212,
)


_ANALYSISREQUEST = _descriptor.Descriptor(
  name='AnalysisRequest',
  full_name='innpv.protocol.AnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='innpv.protocol.AnalysisRequest.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=256,
)


_FROMSERVER = _descriptor.Descriptor(
  name='FromServer',
  full_name='innpv.protocol.FromServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='innpv.protocol.FromServer.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initialize', full_name='innpv.protocol.FromServer.initialize', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_usage', full_name='innpv.protocol.FromServer.memory_usage', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis_error', full_name='innpv.protocol.FromServer.analysis_error', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='innpv.protocol.FromServer.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=259,
  serialized_end=506,
)


_INITIALIZERESPONSE = _descriptor.Descriptor(
  name='InitializeResponse',
  full_name='innpv.protocol.InitializeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_project_root', full_name='innpv.protocol.InitializeResponse.server_project_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entry_point', full_name='innpv.protocol.InitializeResponse.entry_point', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=600,
)


_MEMORYUSAGERESPONSE = _descriptor.Descriptor(
  name='MemoryUsageResponse',
  full_name='innpv.protocol.MemoryUsageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='innpv.protocol.MemoryUsageResponse.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peak_usage_bytes', full_name='innpv.protocol.MemoryUsageResponse.peak_usage_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_capacity_bytes', full_name='innpv.protocol.MemoryUsageResponse.memory_capacity_bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_entries', full_name='innpv.protocol.MemoryUsageResponse.weight_entries', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activation_entries', full_name='innpv.protocol.MemoryUsageResponse.activation_entries', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=820,
)


_ANALYSISERROR = _descriptor.Descriptor(
  name='AnalysisError',
  full_name='innpv.protocol.AnalysisError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='innpv.protocol.AnalysisError.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='innpv.protocol.AnalysisError.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=885,
)


_PROTOCOLERROR = _descriptor.Descriptor(
  name='ProtocolError',
  full_name='innpv.protocol.ProtocolError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='innpv.protocol.ProtocolError.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=922,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='innpv.protocol.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='components', full_name='innpv.protocol.Path.components', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=950,
)


_FILEREFERENCE = _descriptor.Descriptor(
  name='FileReference',
  full_name='innpv.protocol.FileReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='innpv.protocol.FileReference.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_number', full_name='innpv.protocol.FileReference.line_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=952,
  serialized_end=1024,
)


_ACTIVATIONENTRY = _descriptor.Descriptor(
  name='ActivationEntry',
  full_name='innpv.protocol.ActivationEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_name', full_name='innpv.protocol.ActivationEntry.operation_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='innpv.protocol.ActivationEntry.size_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='innpv.protocol.ActivationEntry.context', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1026,
  serialized_end=1135,
)


_WEIGHTENTRY = _descriptor.Descriptor(
  name='WeightEntry',
  full_name='innpv.protocol.WeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight_name', full_name='innpv.protocol.WeightEntry.weight_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='innpv.protocol.WeightEntry.size_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grad_size_bytes', full_name='innpv.protocol.WeightEntry.grad_size_bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='innpv.protocol.WeightEntry.context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1264,
)

_FROMCLIENT.fields_by_name['initialize'].message_type = _INITIALIZEREQUEST
_FROMCLIENT.fields_by_name['analysis'].message_type = _ANALYSISREQUEST
_FROMCLIENT.oneofs_by_name['payload'].fields.append(
  _FROMCLIENT.fields_by_name['initialize'])
_FROMCLIENT.fields_by_name['initialize'].containing_oneof = _FROMCLIENT.oneofs_by_name['payload']
_FROMCLIENT.oneofs_by_name['payload'].fields.append(
  _FROMCLIENT.fields_by_name['analysis'])
_FROMCLIENT.fields_by_name['analysis'].containing_oneof = _FROMCLIENT.oneofs_by_name['payload']
_FROMSERVER.fields_by_name['error'].message_type = _PROTOCOLERROR
_FROMSERVER.fields_by_name['initialize'].message_type = _INITIALIZERESPONSE
_FROMSERVER.fields_by_name['memory_usage'].message_type = _MEMORYUSAGERESPONSE
_FROMSERVER.fields_by_name['analysis_error'].message_type = _ANALYSISERROR
_FROMSERVER.oneofs_by_name['payload'].fields.append(
  _FROMSERVER.fields_by_name['error'])
_FROMSERVER.fields_by_name['error'].containing_oneof = _FROMSERVER.oneofs_by_name['payload']
_FROMSERVER.oneofs_by_name['payload'].fields.append(
  _FROMSERVER.fields_by_name['initialize'])
_FROMSERVER.fields_by_name['initialize'].containing_oneof = _FROMSERVER.oneofs_by_name['payload']
_FROMSERVER.oneofs_by_name['payload'].fields.append(
  _FROMSERVER.fields_by_name['memory_usage'])
_FROMSERVER.fields_by_name['memory_usage'].containing_oneof = _FROMSERVER.oneofs_by_name['payload']
_FROMSERVER.oneofs_by_name['payload'].fields.append(
  _FROMSERVER.fields_by_name['analysis_error'])
_FROMSERVER.fields_by_name['analysis_error'].containing_oneof = _FROMSERVER.oneofs_by_name['payload']
_INITIALIZERESPONSE.fields_by_name['entry_point'].message_type = _PATH
_MEMORYUSAGERESPONSE.fields_by_name['weight_entries'].message_type = _WEIGHTENTRY
_MEMORYUSAGERESPONSE.fields_by_name['activation_entries'].message_type = _ACTIVATIONENTRY
_FILEREFERENCE.fields_by_name['file'].message_type = _PATH
_ACTIVATIONENTRY.fields_by_name['context'].message_type = _FILEREFERENCE
_WEIGHTENTRY.fields_by_name['context'].message_type = _FILEREFERENCE
DESCRIPTOR.message_types_by_name['FromClient'] = _FROMCLIENT
DESCRIPTOR.message_types_by_name['InitializeRequest'] = _INITIALIZEREQUEST
DESCRIPTOR.message_types_by_name['AnalysisRequest'] = _ANALYSISREQUEST
DESCRIPTOR.message_types_by_name['FromServer'] = _FROMSERVER
DESCRIPTOR.message_types_by_name['InitializeResponse'] = _INITIALIZERESPONSE
DESCRIPTOR.message_types_by_name['MemoryUsageResponse'] = _MEMORYUSAGERESPONSE
DESCRIPTOR.message_types_by_name['AnalysisError'] = _ANALYSISERROR
DESCRIPTOR.message_types_by_name['ProtocolError'] = _PROTOCOLERROR
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['FileReference'] = _FILEREFERENCE
DESCRIPTOR.message_types_by_name['ActivationEntry'] = _ACTIVATIONENTRY
DESCRIPTOR.message_types_by_name['WeightEntry'] = _WEIGHTENTRY

FromClient = _reflection.GeneratedProtocolMessageType('FromClient', (_message.Message,), dict(
  DESCRIPTOR = _FROMCLIENT,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.FromClient)
  ))
_sym_db.RegisterMessage(FromClient)

InitializeRequest = _reflection.GeneratedProtocolMessageType('InitializeRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZEREQUEST,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.InitializeRequest)
  ))
_sym_db.RegisterMessage(InitializeRequest)

AnalysisRequest = _reflection.GeneratedProtocolMessageType('AnalysisRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISREQUEST,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.AnalysisRequest)
  ))
_sym_db.RegisterMessage(AnalysisRequest)

FromServer = _reflection.GeneratedProtocolMessageType('FromServer', (_message.Message,), dict(
  DESCRIPTOR = _FROMSERVER,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.FromServer)
  ))
_sym_db.RegisterMessage(FromServer)

InitializeResponse = _reflection.GeneratedProtocolMessageType('InitializeResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZERESPONSE,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.InitializeResponse)
  ))
_sym_db.RegisterMessage(InitializeResponse)

MemoryUsageResponse = _reflection.GeneratedProtocolMessageType('MemoryUsageResponse', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYUSAGERESPONSE,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.MemoryUsageResponse)
  ))
_sym_db.RegisterMessage(MemoryUsageResponse)

AnalysisError = _reflection.GeneratedProtocolMessageType('AnalysisError', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISERROR,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.AnalysisError)
  ))
_sym_db.RegisterMessage(AnalysisError)

ProtocolError = _reflection.GeneratedProtocolMessageType('ProtocolError', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCOLERROR,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.ProtocolError)
  ))
_sym_db.RegisterMessage(ProtocolError)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.Path)
  ))
_sym_db.RegisterMessage(Path)

FileReference = _reflection.GeneratedProtocolMessageType('FileReference', (_message.Message,), dict(
  DESCRIPTOR = _FILEREFERENCE,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.FileReference)
  ))
_sym_db.RegisterMessage(FileReference)

ActivationEntry = _reflection.GeneratedProtocolMessageType('ActivationEntry', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVATIONENTRY,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.ActivationEntry)
  ))
_sym_db.RegisterMessage(ActivationEntry)

WeightEntry = _reflection.GeneratedProtocolMessageType('WeightEntry', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTENTRY,
  __module__ = 'innpv_pb2'
  # @@protoc_insertion_point(class_scope:innpv.protocol.WeightEntry)
  ))
_sym_db.RegisterMessage(WeightEntry)


# @@protoc_insertion_point(module_scope)
