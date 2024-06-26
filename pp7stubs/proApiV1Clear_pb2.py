# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Clear.proto
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
    'proApiV1Clear.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import proApiV1Color_pb2 as proApiV1Color__pb2
from . import proApiV1Identifier_pb2 as proApiV1Identifier__pb2
from . import proApiV1LayerType_pb2 as proApiV1LayerType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proApiV1Clear.proto\x12\x07rv.data\x1a\x13proApiV1Color.proto\x1a\x18proApiV1Identifier.proto\x1a\x17proApiV1LayerType.proto\"\xc3\x03\n\x11\x41PI_v1_ClearGroup\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12#\n\x04tint\x18\x03 \x01(\x0b\x32\x15.rv.data.API_v1_Color\x12\x45\n\x06layers\x18\x04 \x03(\x0e\x32\x35.rv.data.API_v1_ClearGroup.API_v1_ClearGroupLayerType\x12#\n\x1bstop_timeline_announcements\x18\x05 \x01(\x08\x12\"\n\x1astop_timeline_presentation\x18\x06 \x01(\x08\x12\x1f\n\x17\x63lear_next_presentation\x18\x07 \x01(\x08\"\xa1\x01\n\x1a\x41PI_v1_ClearGroupLayerType\x12\t\n\x05music\x10\x00\x12\x11\n\raudio_effects\x10\x01\x12\t\n\x05props\x10\x02\x12\x0c\n\x08messages\x10\x03\x12\x11\n\rannouncements\x10\x04\x12\x10\n\x0cpresentation\x10\x05\x12\x16\n\x12presentation_media\x10\x06\x12\x0f\n\x0bvideo_input\x10\x07\"\xdf\x07\n\x14\x41PI_v1_Clear_Request\x12?\n\x0b\x63lear_layer\x18\x01 \x01(\x0b\x32(.rv.data.API_v1_Clear_Request.ClearLayerH\x00\x12\x41\n\x0c\x63reate_group\x18\x02 \x01(\x0b\x32).rv.data.API_v1_Clear_Request.CreateGroupH\x00\x12;\n\tget_group\x18\x03 \x01(\x0b\x32&.rv.data.API_v1_Clear_Request.GetGroupH\x00\x12;\n\tput_group\x18\x04 \x01(\x0b\x32&.rv.data.API_v1_Clear_Request.PutGroupH\x00\x12\x44\n\x0eget_group_icon\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Clear_Request.GetGroupIconH\x00\x12\x44\n\x0eput_group_icon\x18\x06 \x01(\x0b\x32*.rv.data.API_v1_Clear_Request.PutGroupIconH\x00\x12\x41\n\x0c\x64\x65lete_group\x18\x07 \x01(\x0b\x32).rv.data.API_v1_Clear_Request.DeleteGroupH\x00\x12\x43\n\rtrigger_group\x18\x08 \x01(\x0b\x32*.rv.data.API_v1_Clear_Request.TriggerGroupH\x00\x12=\n\nget_groups\x18\t \x01(\x0b\x32\'.rv.data.API_v1_Clear_Request.GetGroupsH\x00\x1a\x36\n\nClearLayer\x12(\n\x05layer\x18\x01 \x01(\x0e\x32\x19.rv.data.API_v1_LayerType\x1a\x38\n\x0b\x43reateGroup\x12)\n\x05group\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\x16\n\x08GetGroup\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x41\n\x08PutGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x05group\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\x1a\n\x0cGetGroupIcon\x12\n\n\x02id\x18\x01 \x01(\t\x1a>\n\x0cPutGroupIcon\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\x0c\x1a\x19\n\x0b\x44\x65leteGroup\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x0cTriggerGroup\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x0b\n\tGetGroupsB\t\n\x07Request\"\xcf\x07\n\x15\x41PI_v1_Clear_Response\x12@\n\x0b\x63lear_layer\x18\x01 \x01(\x0b\x32).rv.data.API_v1_Clear_Response.ClearLayerH\x00\x12\x42\n\x0c\x63reate_group\x18\x02 \x01(\x0b\x32*.rv.data.API_v1_Clear_Response.CreateGroupH\x00\x12<\n\tget_group\x18\x03 \x01(\x0b\x32\'.rv.data.API_v1_Clear_Response.GetGroupH\x00\x12<\n\tput_group\x18\x04 \x01(\x0b\x32\'.rv.data.API_v1_Clear_Response.PutGroupH\x00\x12\x42\n\x0c\x64\x65lete_group\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Clear_Response.DeleteGroupH\x00\x12\x44\n\rtrigger_group\x18\x06 \x01(\x0b\x32+.rv.data.API_v1_Clear_Response.TriggerGroupH\x00\x12>\n\nget_groups\x18\x07 \x01(\x0b\x32(.rv.data.API_v1_Clear_Response.GetGroupsH\x00\x12\x45\n\x0eget_group_icon\x18\x08 \x01(\x0b\x32+.rv.data.API_v1_Clear_Response.GetGroupIconH\x00\x12\x45\n\x0eput_group_icon\x18\t \x01(\x0b\x32+.rv.data.API_v1_Clear_Response.PutGroupIconH\x00\x1a\x0c\n\nClearLayer\x1a\x35\n\x08PutGroup\x12)\n\x05group\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\r\n\x0b\x44\x65leteGroup\x1a\x0e\n\x0cTriggerGroup\x1a\x38\n\x0b\x43reateGroup\x12)\n\x05group\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\x35\n\x08GetGroup\x12)\n\x05group\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\x37\n\tGetGroups\x12*\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.rv.data.API_v1_ClearGroup\x1a\x32\n\x0cGetGroupIcon\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\x0c\x1a\x0e\n\x0cPutGroupIconB\n\n\x08ResponseB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Clear_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_CLEARGROUP']._serialized_start=105
  _globals['_API_V1_CLEARGROUP']._serialized_end=556
  _globals['_API_V1_CLEARGROUP_API_V1_CLEARGROUPLAYERTYPE']._serialized_start=395
  _globals['_API_V1_CLEARGROUP_API_V1_CLEARGROUPLAYERTYPE']._serialized_end=556
  _globals['_API_V1_CLEAR_REQUEST']._serialized_start=559
  _globals['_API_V1_CLEAR_REQUEST']._serialized_end=1550
  _globals['_API_V1_CLEAR_REQUEST_CLEARLAYER']._serialized_start=1176
  _globals['_API_V1_CLEAR_REQUEST_CLEARLAYER']._serialized_end=1230
  _globals['_API_V1_CLEAR_REQUEST_CREATEGROUP']._serialized_start=1232
  _globals['_API_V1_CLEAR_REQUEST_CREATEGROUP']._serialized_end=1288
  _globals['_API_V1_CLEAR_REQUEST_GETGROUP']._serialized_start=1290
  _globals['_API_V1_CLEAR_REQUEST_GETGROUP']._serialized_end=1312
  _globals['_API_V1_CLEAR_REQUEST_PUTGROUP']._serialized_start=1314
  _globals['_API_V1_CLEAR_REQUEST_PUTGROUP']._serialized_end=1379
  _globals['_API_V1_CLEAR_REQUEST_GETGROUPICON']._serialized_start=1381
  _globals['_API_V1_CLEAR_REQUEST_GETGROUPICON']._serialized_end=1407
  _globals['_API_V1_CLEAR_REQUEST_PUTGROUPICON']._serialized_start=1409
  _globals['_API_V1_CLEAR_REQUEST_PUTGROUPICON']._serialized_end=1471
  _globals['_API_V1_CLEAR_REQUEST_DELETEGROUP']._serialized_start=1473
  _globals['_API_V1_CLEAR_REQUEST_DELETEGROUP']._serialized_end=1498
  _globals['_API_V1_CLEAR_REQUEST_TRIGGERGROUP']._serialized_start=1500
  _globals['_API_V1_CLEAR_REQUEST_TRIGGERGROUP']._serialized_end=1526
  _globals['_API_V1_CLEAR_REQUEST_GETGROUPS']._serialized_start=1528
  _globals['_API_V1_CLEAR_REQUEST_GETGROUPS']._serialized_end=1539
  _globals['_API_V1_CLEAR_RESPONSE']._serialized_start=1553
  _globals['_API_V1_CLEAR_RESPONSE']._serialized_end=2528
  _globals['_API_V1_CLEAR_RESPONSE_CLEARLAYER']._serialized_start=1176
  _globals['_API_V1_CLEAR_RESPONSE_CLEARLAYER']._serialized_end=1188
  _globals['_API_V1_CLEAR_RESPONSE_PUTGROUP']._serialized_start=2194
  _globals['_API_V1_CLEAR_RESPONSE_PUTGROUP']._serialized_end=2247
  _globals['_API_V1_CLEAR_RESPONSE_DELETEGROUP']._serialized_start=1473
  _globals['_API_V1_CLEAR_RESPONSE_DELETEGROUP']._serialized_end=1486
  _globals['_API_V1_CLEAR_RESPONSE_TRIGGERGROUP']._serialized_start=1500
  _globals['_API_V1_CLEAR_RESPONSE_TRIGGERGROUP']._serialized_end=1514
  _globals['_API_V1_CLEAR_RESPONSE_CREATEGROUP']._serialized_start=1232
  _globals['_API_V1_CLEAR_RESPONSE_CREATEGROUP']._serialized_end=1288
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUP']._serialized_start=2338
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUP']._serialized_end=2391
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUPS']._serialized_start=2393
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUPS']._serialized_end=2448
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUPICON']._serialized_start=2450
  _globals['_API_V1_CLEAR_RESPONSE_GETGROUPICON']._serialized_end=2500
  _globals['_API_V1_CLEAR_RESPONSE_PUTGROUPICON']._serialized_start=1409
  _globals['_API_V1_CLEAR_RESPONSE_PUTGROUPICON']._serialized_end=1423
# @@protoc_insertion_point(module_scope)
