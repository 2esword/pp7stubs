# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stage.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import applicationInfo_pb2 as applicationInfo__pb2
from . import collectionElementType_pb2 as collectionElementType__pb2
from . import uuid_pb2 as uuid__pb2
from . import slide_pb2 as slide__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstage.proto\x12\x07rv.data\x1a\x15\x61pplicationInfo.proto\x1a\x1b\x63ollectionElementType.proto\x1a\nuuid.proto\x1a\x0bslide.proto\"\xb7\x02\n\x05Stage\x1aR\n\x06Layout\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05slide\x18\x03 \x01(\x0b\x32\x0e.rv.data.Slide\x1a\x66\n\x08\x44ocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12&\n\x07layouts\x18\x02 \x03(\x0b\x32\x15.rv.data.Stage.Layout\x1ar\n\x10ScreenAssignment\x12.\n\x06screen\x18\x01 \x01(\x0b\x32\x1e.rv.data.CollectionElementType\x12.\n\x06layout\x18\x02 \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STAGE']._serialized_start=102
  _globals['_STAGE']._serialized_end=413
  _globals['_STAGE_LAYOUT']._serialized_start=111
  _globals['_STAGE_LAYOUT']._serialized_end=193
  _globals['_STAGE_DOCUMENT']._serialized_start=195
  _globals['_STAGE_DOCUMENT']._serialized_end=297
  _globals['_STAGE_SCREENASSIGNMENT']._serialized_start=299
  _globals['_STAGE_SCREENASSIGNMENT']._serialized_end=413
# @@protoc_insertion_point(module_scope)
