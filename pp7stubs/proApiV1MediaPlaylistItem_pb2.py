# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1MediaPlaylistItem.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'proApiV1MediaPlaylistItem.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import proApiV1Identifier_pb2 as proApiV1Identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fproApiV1MediaPlaylistItem.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\"\xf3\x01\n\x18\x41PI_v1_MediaPlaylistItem\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12L\n\x04type\x18\x02 \x01(\x0e\x32>.rv.data.API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType\x12\x0e\n\x06\x61rtist\x18\x03 \x01(\t\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\"?\n\x1c\x41PI_v1_MediaPlaylistItemType\x12\t\n\x05\x61udio\x10\x00\x12\t\n\x05image\x10\x01\x12\t\n\x05video\x10\x02\x42\x34\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1MediaPlaylistItem_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_MEDIAPLAYLISTITEM']._serialized_start=71
  _globals['_API_V1_MEDIAPLAYLISTITEM']._serialized_end=314
  _globals['_API_V1_MEDIAPLAYLISTITEM_API_V1_MEDIAPLAYLISTITEMTYPE']._serialized_start=251
  _globals['_API_V1_MEDIAPLAYLISTITEM_API_V1_MEDIAPLAYLISTITEMTYPE']._serialized_end=314
# @@protoc_insertion_point(module_scope)
