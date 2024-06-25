# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Announcement.proto
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
    'proApiV1Announcement.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Presentation_pb2 as proApiV1Presentation__pb2
import proApiV1TimelineOperation_pb2 as proApiV1TimelineOperation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aproApiV1Announcement.proto\x12\x07rv.data\x1a\x1aproApiV1Presentation.proto\x1a\x1fproApiV1TimelineOperation.proto\"\x98\x08\n\x1b\x41PI_v1_Announcement_Request\x12\x61\n\x19\x61\x63tive_timeline_operation\x18\x01 \x01(\x0b\x32<.rv.data.API_v1_Announcement_Request.ActiveTimelineOperationH\x00\x12[\n\x16\x61\x63tive_timeline_status\x18\x02 \x01(\x0b\x32\x39.rv.data.API_v1_Announcement_Request.ActiveTimelineStatusH\x00\x12=\n\x06\x61\x63tive\x18\x03 \x01(\x0b\x32+.rv.data.API_v1_Announcement_Request.ActiveH\x00\x12M\n\x0bslide_index\x18\x04 \x01(\x0b\x32\x36.rv.data.API_v1_Announcement_Request.AnnouncementIndexH\x00\x12H\n\x0c\x61\x63tive_focus\x18\x05 \x01(\x0b\x32\x30.rv.data.API_v1_Announcement_Request.ActiveFocusH\x00\x12L\n\x0e\x61\x63tive_trigger\x18\x06 \x01(\x0b\x32\x32.rv.data.API_v1_Announcement_Request.ActiveTriggerH\x00\x12U\n\x13\x61\x63tive_next_trigger\x18\x07 \x01(\x0b\x32\x36.rv.data.API_v1_Announcement_Request.ActiveNextTriggerH\x00\x12]\n\x17\x61\x63tive_previous_trigger\x18\x08 \x01(\x0b\x32:.rv.data.API_v1_Announcement_Request.ActivePreviousTriggerH\x00\x12W\n\x14\x61\x63tive_index_trigger\x18\t \x01(\x0b\x32\x37.rv.data.API_v1_Announcement_Request.ActiveIndexTriggerH\x00\x1aO\n\x17\x41\x63tiveTimelineOperation\x12\x34\n\toperation\x18\x01 \x01(\x0e\x32!.rv.data.API_v1_TimelineOperation\x1a\x16\n\x14\x41\x63tiveTimelineStatus\x1a\x08\n\x06\x41\x63tive\x1a\x13\n\x11\x41nnouncementIndex\x1a\r\n\x0b\x41\x63tiveFocus\x1a\x0f\n\rActiveTrigger\x1a\x13\n\x11\x41\x63tiveNextTrigger\x1a\x17\n\x15\x41\x63tivePreviousTrigger\x1a#\n\x12\x41\x63tiveIndexTrigger\x12\r\n\x05index\x18\x01 \x01(\rB\t\n\x07Request\"\xe5\x08\n\x1c\x41PI_v1_Announcement_Response\x12\x62\n\x19\x61\x63tive_timeline_operation\x18\x01 \x01(\x0b\x32=.rv.data.API_v1_Announcement_Response.ActiveTimelineOperationH\x00\x12\\\n\x16\x61\x63tive_timeline_status\x18\x02 \x01(\x0b\x32:.rv.data.API_v1_Announcement_Response.ActiveTimelineStatusH\x00\x12>\n\x06\x61\x63tive\x18\x03 \x01(\x0b\x32,.rv.data.API_v1_Announcement_Response.ActiveH\x00\x12G\n\x0bslide_index\x18\x04 \x01(\x0b\x32\x30.rv.data.API_v1_Announcement_Response.SlideIndexH\x00\x12I\n\x0c\x61\x63tive_focus\x18\x05 \x01(\x0b\x32\x31.rv.data.API_v1_Announcement_Response.ActiveFocusH\x00\x12M\n\x0e\x61\x63tive_trigger\x18\x06 \x01(\x0b\x32\x33.rv.data.API_v1_Announcement_Response.ActiveTriggerH\x00\x12V\n\x13\x61\x63tive_next_trigger\x18\x07 \x01(\x0b\x32\x37.rv.data.API_v1_Announcement_Response.ActiveNextTriggerH\x00\x12^\n\x17\x61\x63tive_previous_trigger\x18\x08 \x01(\x0b\x32;.rv.data.API_v1_Announcement_Response.ActivePreviousTriggerH\x00\x12X\n\x14\x61\x63tive_index_trigger\x18\t \x01(\x0b\x32\x38.rv.data.API_v1_Announcement_Response.ActiveIndexTriggerH\x00\x1a\x19\n\x17\x41\x63tiveTimelineOperation\x1a@\n\x14\x41\x63tiveTimelineStatus\x12\x12\n\nis_running\x18\x01 \x01(\x08\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x01\x1a<\n\x06\x41\x63tive\x12\x32\n\x0c\x61nnouncement\x18\x01 \x01(\x0b\x32\x1c.rv.data.API_v1_Presentation\x1a\x44\n\nSlideIndex\x12\x36\n\x12\x61nnouncement_index\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_SlideIndex\x1a\r\n\x0b\x41\x63tiveFocus\x1a\x0f\n\rActiveTrigger\x1a\x13\n\x11\x41\x63tiveNextTrigger\x1a\x17\n\x15\x41\x63tivePreviousTrigger\x1a\x14\n\x12\x41\x63tiveIndexTriggerB\t\n\x07RequestB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Announcement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_ANNOUNCEMENT_REQUEST']._serialized_start=101
  _globals['_API_V1_ANNOUNCEMENT_REQUEST']._serialized_end=1149
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETIMELINEOPERATION']._serialized_start=889
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETIMELINEOPERATION']._serialized_end=968
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETIMELINESTATUS']._serialized_start=970
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETIMELINESTATUS']._serialized_end=992
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVE']._serialized_start=994
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVE']._serialized_end=1002
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ANNOUNCEMENTINDEX']._serialized_start=1004
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ANNOUNCEMENTINDEX']._serialized_end=1023
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEFOCUS']._serialized_start=1025
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEFOCUS']._serialized_end=1038
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETRIGGER']._serialized_start=1040
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVETRIGGER']._serialized_end=1055
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVENEXTTRIGGER']._serialized_start=1057
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVENEXTTRIGGER']._serialized_end=1076
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEPREVIOUSTRIGGER']._serialized_start=1078
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEPREVIOUSTRIGGER']._serialized_end=1101
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEINDEXTRIGGER']._serialized_start=1103
  _globals['_API_V1_ANNOUNCEMENT_REQUEST_ACTIVEINDEXTRIGGER']._serialized_end=1138
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE']._serialized_start=1152
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE']._serialized_end=2277
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETIMELINEOPERATION']._serialized_start=889
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETIMELINEOPERATION']._serialized_end=914
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETIMELINESTATUS']._serialized_start=1970
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETIMELINESTATUS']._serialized_end=2034
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVE']._serialized_start=2036
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVE']._serialized_end=2096
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_SLIDEINDEX']._serialized_start=2098
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_SLIDEINDEX']._serialized_end=2166
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEFOCUS']._serialized_start=1025
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEFOCUS']._serialized_end=1038
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETRIGGER']._serialized_start=1040
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVETRIGGER']._serialized_end=1055
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVENEXTTRIGGER']._serialized_start=1057
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVENEXTTRIGGER']._serialized_end=1076
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEPREVIOUSTRIGGER']._serialized_start=1078
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEPREVIOUSTRIGGER']._serialized_end=1101
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEINDEXTRIGGER']._serialized_start=1103
  _globals['_API_V1_ANNOUNCEMENT_RESPONSE_ACTIVEINDEXTRIGGER']._serialized_end=1123
# @@protoc_insertion_point(module_scope)
