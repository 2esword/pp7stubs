# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timecode.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etimecode.proto\x12\x07rv.data\x1a\nuuid.proto\"\x98\x02\n\x10TimecodeSettings\x12\x19\n\x11\x64\x65vice_identifier\x18\x01 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\x05\x12\x30\n\x06\x66ormat\x18\x03 \x01(\x0e\x32 .rv.data.TimecodeSettings.Format\x12\x0e\n\x06offset\x18\x04 \x01(\x01\x12*\n\x13playlist_identifier\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\x12\x11\n\tis_active\x18\x06 \x01(\x08\"W\n\x06\x46ormat\x12\x11\n\rFORMAT_24_FPS\x10\x00\x12\x11\n\rFORMAT_25_FPS\x10\x01\x12\x14\n\x10\x46ORMAT_29_97_FPS\x10\x02\x12\x11\n\rFORMAT_30_FPS\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'timecode_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMECODESETTINGS']._serialized_start=40
  _globals['_TIMECODESETTINGS']._serialized_end=320
  _globals['_TIMECODESETTINGS_FORMAT']._serialized_start=233
  _globals['_TIMECODESETTINGS_FORMAT']._serialized_end=320
# @@protoc_insertion_point(module_scope)
