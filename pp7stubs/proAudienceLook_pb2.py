# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proAudienceLook.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proAudienceLook.proto\x12\x07rv.data\x1a\turl.proto\x1a\nuuid.proto\"\xde\x04\n\x0fProAudienceLook\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x0cscreen_looks\x18\x03 \x03(\x0b\x32&.rv.data.ProAudienceLook.ProScreenLook\x12)\n\x12original_look_uuid\x18\x04 \x01(\x0b\x32\r.rv.data.UUID\x12\x1b\n\x13transition_duration\x18\x05 \x01(\x01\x1a\x99\x03\n\rProScreenLook\x12&\n\x0fpro_screen_uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x15\n\rprops_enabled\x18\x02 \x01(\x08\x12\x1a\n\x12live_video_enabled\x18\x03 \x01(\x08\x12\'\n\x1fpresentation_background_enabled\x18\x04 \x01(\x08\x12\x31\n\x1btemplate_document_file_path\x18\x05 \x01(\x0b\x32\x0c.rv.data.URL\x12*\n\x13template_slide_uuid\x18\x06 \x01(\x0b\x32\r.rv.data.UUID\x12\'\n\x1fpresentation_foreground_enabled\x18\x07 \x01(\x08\x12 \n\tmask_uuid\x18\x08 \x01(\x0b\x32\r.rv.data.UUID\x12\x1d\n\x15\x61nnouncements_enabled\x18\t \x01(\x08\x12\x1b\n\x13props_layer_enabled\x18\n \x01(\x08\x12\x1e\n\x16messages_layer_enabled\x18\x0b \x01(\x08\"F\n\x16\x41udienceLookCollection\x12,\n\ncollection\x18\x01 \x03(\x0b\x32\x18.rv.data.ProAudienceLookb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proAudienceLook_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PROAUDIENCELOOK']._serialized_start=58
  _globals['_PROAUDIENCELOOK']._serialized_end=664
  _globals['_PROAUDIENCELOOK_PROSCREENLOOK']._serialized_start=255
  _globals['_PROAUDIENCELOOK_PROSCREENLOOK']._serialized_end=664
  _globals['_AUDIENCELOOKCOLLECTION']._serialized_start=666
  _globals['_AUDIENCELOOKCOLLECTION']._serialized_end=736
# @@protoc_insertion_point(module_scope)