# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proMask.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import slide_pb2 as slide__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproMask.proto\x12\x07rv.data\x1a\x0bslide.proto\";\n\x07ProMask\x12\"\n\nbase_slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12\x0c\n\x04name\x18\x02 \x01(\t\"6\n\x0eMaskCollection\x12$\n\ncollection\x18\x01 \x03(\x0b\x32\x10.rv.data.ProMaskb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proMask_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PROMASK']._serialized_start=39
  _globals['_PROMASK']._serialized_end=98
  _globals['_MASKCOLLECTION']._serialized_start=100
  _globals['_MASKCOLLECTION']._serialized_end=154
# @@protoc_insertion_point(module_scope)
