# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1VideoInputs.proto
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
    'proApiV1VideoInputs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Identifier_pb2 as proApiV1Identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proApiV1VideoInputs.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\"\xca\x01\n\x1b\x41PI_v1_Video_Inputs_Request\x12>\n\x07get_all\x18\x01 \x01(\x0b\x32+.rv.data.API_v1_Video_Inputs_Request.GetAllH\x00\x12?\n\x07trigger\x18\x02 \x01(\x0b\x32,.rv.data.API_v1_Video_Inputs_Request.TriggerH\x00\x1a\x08\n\x06GetAll\x1a\x15\n\x07Trigger\x12\n\n\x02id\x18\x01 \x01(\tB\t\n\x07Request\"\xed\x01\n\x1c\x41PI_v1_Video_Inputs_Response\x12?\n\x07get_all\x18\x01 \x01(\x0b\x32,.rv.data.API_v1_Video_Inputs_Response.GetAllH\x00\x12@\n\x07trigger\x18\x02 \x01(\x0b\x32-.rv.data.API_v1_Video_Inputs_Response.TriggerH\x00\x1a\x34\n\x06GetAll\x12*\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\t\n\x07TriggerB\t\n\x07RequestB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1VideoInputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_VIDEO_INPUTS_REQUEST']._serialized_start=65
  _globals['_API_V1_VIDEO_INPUTS_REQUEST']._serialized_end=267
  _globals['_API_V1_VIDEO_INPUTS_REQUEST_GETALL']._serialized_start=225
  _globals['_API_V1_VIDEO_INPUTS_REQUEST_GETALL']._serialized_end=233
  _globals['_API_V1_VIDEO_INPUTS_REQUEST_TRIGGER']._serialized_start=235
  _globals['_API_V1_VIDEO_INPUTS_REQUEST_TRIGGER']._serialized_end=256
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE']._serialized_start=270
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE']._serialized_end=507
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE_GETALL']._serialized_start=433
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE_GETALL']._serialized_end=485
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE_TRIGGER']._serialized_start=235
  _globals['_API_V1_VIDEO_INPUTS_RESPONSE_TRIGGER']._serialized_end=244
# @@protoc_insertion_point(module_scope)
