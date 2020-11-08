# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protodb.proto

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
  name='protodb.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rprotodb.proto\"O\n\x07ProtoDB\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ProtoDBHeader\x12$\n\tdirectory\x18\x02 \x01(\x0b\x32\x11.ProtoDBDirectory\"1\n\rProtoDBHeader\x12\r\n\x05magic\x18\x01 \x01(\x0c\x12\x11\n\tdbversion\x18\x02 \x01(\x0c\"4\n\x17ProtoDBDocumentMetadata\x12\x19\n\x11\x63reationTimestamp\x18\x01 \x01(\x03\"Y\n\x0fProtoDBDocument\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.ProtoDBDocumentMetadata\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"5\n\x18ProtoDBDirectoryMetadata\x12\x19\n\x11\x63reationTimestamp\x18\x01 \x01(\x03\"\x97\x01\n\x10ProtoDBDirectory\x12+\n\x08metadata\x18\x01 \x01(\x0b\x32\x19.ProtoDBDirectoryMetadata\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\tdirectory\x18\x03 \x03(\x0b\x32\x11.ProtoDBDirectory\x12\"\n\x08\x64ocument\x18\x04 \x03(\x0b\x32\x10.ProtoDBDocumentb\x06proto3')
)




_PROTODB = _descriptor.Descriptor(
  name='ProtoDB',
  full_name='ProtoDB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ProtoDB.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directory', full_name='ProtoDB.directory', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=17,
  serialized_end=96,
)


_PROTODBHEADER = _descriptor.Descriptor(
  name='ProtoDBHeader',
  full_name='ProtoDBHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='magic', full_name='ProtoDBHeader.magic', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbversion', full_name='ProtoDBHeader.dbversion', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=98,
  serialized_end=147,
)


_PROTODBDOCUMENTMETADATA = _descriptor.Descriptor(
  name='ProtoDBDocumentMetadata',
  full_name='ProtoDBDocumentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creationTimestamp', full_name='ProtoDBDocumentMetadata.creationTimestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=149,
  serialized_end=201,
)


_PROTODBDOCUMENT = _descriptor.Descriptor(
  name='ProtoDBDocument',
  full_name='ProtoDBDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProtoDBDocument.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ProtoDBDocument.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ProtoDBDocument.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=203,
  serialized_end=292,
)


_PROTODBDIRECTORYMETADATA = _descriptor.Descriptor(
  name='ProtoDBDirectoryMetadata',
  full_name='ProtoDBDirectoryMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creationTimestamp', full_name='ProtoDBDirectoryMetadata.creationTimestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=294,
  serialized_end=347,
)


_PROTODBDIRECTORY = _descriptor.Descriptor(
  name='ProtoDBDirectory',
  full_name='ProtoDBDirectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProtoDBDirectory.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ProtoDBDirectory.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directory', full_name='ProtoDBDirectory.directory', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document', full_name='ProtoDBDirectory.document', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=350,
  serialized_end=501,
)

_PROTODB.fields_by_name['header'].message_type = _PROTODBHEADER
_PROTODB.fields_by_name['directory'].message_type = _PROTODBDIRECTORY
_PROTODBDOCUMENT.fields_by_name['metadata'].message_type = _PROTODBDOCUMENTMETADATA
_PROTODBDIRECTORY.fields_by_name['metadata'].message_type = _PROTODBDIRECTORYMETADATA
_PROTODBDIRECTORY.fields_by_name['directory'].message_type = _PROTODBDIRECTORY
_PROTODBDIRECTORY.fields_by_name['document'].message_type = _PROTODBDOCUMENT
DESCRIPTOR.message_types_by_name['ProtoDB'] = _PROTODB
DESCRIPTOR.message_types_by_name['ProtoDBHeader'] = _PROTODBHEADER
DESCRIPTOR.message_types_by_name['ProtoDBDocumentMetadata'] = _PROTODBDOCUMENTMETADATA
DESCRIPTOR.message_types_by_name['ProtoDBDocument'] = _PROTODBDOCUMENT
DESCRIPTOR.message_types_by_name['ProtoDBDirectoryMetadata'] = _PROTODBDIRECTORYMETADATA
DESCRIPTOR.message_types_by_name['ProtoDBDirectory'] = _PROTODBDIRECTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoDB = _reflection.GeneratedProtocolMessageType('ProtoDB', (_message.Message,), dict(
  DESCRIPTOR = _PROTODB,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDB)
  ))
_sym_db.RegisterMessage(ProtoDB)

ProtoDBHeader = _reflection.GeneratedProtocolMessageType('ProtoDBHeader', (_message.Message,), dict(
  DESCRIPTOR = _PROTODBHEADER,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDBHeader)
  ))
_sym_db.RegisterMessage(ProtoDBHeader)

ProtoDBDocumentMetadata = _reflection.GeneratedProtocolMessageType('ProtoDBDocumentMetadata', (_message.Message,), dict(
  DESCRIPTOR = _PROTODBDOCUMENTMETADATA,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDBDocumentMetadata)
  ))
_sym_db.RegisterMessage(ProtoDBDocumentMetadata)

ProtoDBDocument = _reflection.GeneratedProtocolMessageType('ProtoDBDocument', (_message.Message,), dict(
  DESCRIPTOR = _PROTODBDOCUMENT,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDBDocument)
  ))
_sym_db.RegisterMessage(ProtoDBDocument)

ProtoDBDirectoryMetadata = _reflection.GeneratedProtocolMessageType('ProtoDBDirectoryMetadata', (_message.Message,), dict(
  DESCRIPTOR = _PROTODBDIRECTORYMETADATA,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDBDirectoryMetadata)
  ))
_sym_db.RegisterMessage(ProtoDBDirectoryMetadata)

ProtoDBDirectory = _reflection.GeneratedProtocolMessageType('ProtoDBDirectory', (_message.Message,), dict(
  DESCRIPTOR = _PROTODBDIRECTORY,
  __module__ = 'protodb_pb2'
  # @@protoc_insertion_point(class_scope:ProtoDBDirectory)
  ))
_sym_db.RegisterMessage(ProtoDBDirectory)


# @@protoc_insertion_point(module_scope)
