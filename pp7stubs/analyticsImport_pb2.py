# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analyticsImport.proto
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
    'analyticsImport.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import analyticsMultiTracks_pb2 as analyticsMultiTracks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61nalyticsImport.proto\x12\x0crv.analytics\x1a\x1a\x61nalyticsMultiTracks.proto\"\xcf\x03\n\x06Import\x12\x36\n\x0bsong_select\x18\x01 \x01(\x0b\x32\x1f.rv.analytics.Import.SongSelectH\x00\x12\x37\n\x0bmultitracks\x18\x02 \x01(\x0b\x32 .rv.analytics.MultiTracks.ImportH\x00\x1a\xc6\x02\n\nSongSelect\x12)\n!template_slide_text_element_count\x18\x01 \x01(\x05\x12\x1c\n\x14import_into_playlist\x18\x02 \x01(\x08\x12\x45\n\x0eline_delimiter\x18\x03 \x01(\x0e\x32-.rv.analytics.Import.SongSelect.LineDelimiter\x12\x1c\n\x14line_delimiter_count\x18\x04 \x01(\x05\x12\x1a\n\x12\x64id_open_edit_view\x18\x05 \x01(\x08\"n\n\rLineDelimiter\x12\x1a\n\x16LINE_DELIMITER_UNKNOWN\x10\x00\x12\x1d\n\x19LINE_DELIMITER_LINE_BREAK\x10\x01\x12\"\n\x1eLINE_DELIMITER_PARAGRAPH_BREAK\x10\x02\x42\x0b\n\tComponentBA\xf8\x01\x01\xaa\x02.Pro.SerializationInterop.RVProtoData.Analytics\xba\x02\nAnalytics_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analyticsImport_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002.Pro.SerializationInterop.RVProtoData.Analytics\272\002\nAnalytics_'
  _globals['_IMPORT']._serialized_start=68
  _globals['_IMPORT']._serialized_end=531
  _globals['_IMPORT_SONGSELECT']._serialized_start=192
  _globals['_IMPORT_SONGSELECT']._serialized_end=518
  _globals['_IMPORT_SONGSELECT_LINEDELIMITER']._serialized_start=408
  _globals['_IMPORT_SONGSELECT_LINEDELIMITER']._serialized_end=518
# @@protoc_insertion_point(module_scope)
