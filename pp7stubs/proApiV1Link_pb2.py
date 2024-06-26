# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Link.proto
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
    'proApiV1Link.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import rvtimestamp_pb2 as rvtimestamp__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proApiV1Link.proto\x12\x07rv.data\x1a\x11rvtimestamp.proto\x1a\nuuid.proto\".\n\x12\x41PI_v1_GroupMember\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\xcb\x04\n\x18\x41PI_v1_GroupMemberStatus\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12U\n\x08platform\x18\x04 \x01(\x0e\x32\x43.rv.data.API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x18\n\x10host_description\x18\x06 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x07 \x01(\t\x12\x66\n\x11\x63onnection_status\x18\x08 \x01(\x0e\x32K.rv.data.API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus\"\x8f\x01\n)API_v1_GroupMemberStatus_ConnectionStatus\x12\x1d\n\x19\x43ONNECTION_STATUS_UNKNOWN\x10\x00\x12\x1f\n\x1b\x43ONNECTION_STATUS_CONNECTED\x10\x01\x12\"\n\x1e\x43ONNECTION_STATUS_DISCONNECTED\x10\x02\"s\n!API_v1_GroupMemberStatus_Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x12\n\x0ePLATFORM_WIN32\x10\x02\x12\x10\n\x0cPLATFORM_WEB\x10\x03\"\xb4\x01\n\x16\x41PI_v1_GroupDefinition\x12%\n\ttimestamp\x18\x01 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12,\n\x07members\x18\x04 \x03(\x0b\x32\x1b.rv.data.API_v1_GroupMember\x12\'\n\x10group_identifier\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\"\xa8\x04\n\x13\x41PI_v1_Link_Request\x12;\n\theartbeat\x18\x01 \x01(\x0b\x32&.rv.data.API_v1_Link_Request.HeartbeatH\x00\x12\x35\n\x06status\x18\x02 \x01(\x0b\x32#.rv.data.API_v1_Link_Request.StatusH\x00\x12<\n\nadd_member\x18\x03 \x01(\x0b\x32&.rv.data.API_v1_Link_Request.AddMemberH\x00\x12\x42\n\rremove_member\x18\x04 \x01(\x0b\x32).rv.data.API_v1_Link_Request.RemoveMemberH\x00\x1a\x34\n\tHeartbeat\x12\x0c\n\x04port\x18\x01 \x01(\r\x12\x19\n\x11if_modified_since\x18\x02 \x01(\t\x1a\x08\n\x06Status\x1a\x8a\x01\n\tAddMember\x12;\n\x10group_definition\x18\x01 \x01(\x0b\x32\x1f.rv.data.API_v1_GroupDefinitionH\x00\x12\x35\n\x0emember_details\x18\x02 \x01(\x0b\x32\x1b.rv.data.API_v1_GroupMemberH\x00\x42\t\n\x07\x41\x64\x64Type\x1a\x43\n\x0cRemoveMember\x12\x33\n\x0emember_details\x18\x01 \x01(\x0b\x32\x1b.rv.data.API_v1_GroupMemberB\t\n\x07Request\"\xbe\x07\n\x14\x41PI_v1_Link_Response\x12<\n\theartbeat\x18\x01 \x01(\x0b\x32\'.rv.data.API_v1_Link_Response.HeartbeatH\x00\x12\x36\n\x06status\x18\x02 \x01(\x0b\x32$.rv.data.API_v1_Link_Response.StatusH\x00\x12=\n\nadd_member\x18\x03 \x01(\x0b\x32\'.rv.data.API_v1_Link_Response.AddMemberH\x00\x12\x43\n\rremove_member\x18\x04 \x01(\x0b\x32*.rv.data.API_v1_Link_Response.RemoveMemberH\x00\x1ay\n\tHeartbeat\x12\x39\n\x10group_definition\x18\x01 \x01(\x0b\x32\x1f.rv.data.API_v1_GroupDefinition\x12\x31\n\x06status\x18\x02 \x01(\x0b\x32!.rv.data.API_v1_GroupMemberStatus\x1aX\n\x06Status\x12\x39\n\x10group_definition\x18\x01 \x01(\x0b\x32\x1f.rv.data.API_v1_GroupDefinition\x12\x13\n\x0bmember_name\x18\x02 \x01(\t\x1a\xba\x03\n\tAddMember\x12;\n\x10group_definition\x18\x01 \x01(\x0b\x32\x1f.rv.data.API_v1_GroupDefinitionH\x00\x12N\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x0b\x32<.rv.data.API_v1_Link_Response.AddMember.RemoteMachineAcceptsH\x00\x12O\n\x07\x64\x65\x63line\x18\x03 \x01(\x0b\x32<.rv.data.API_v1_Link_Response.AddMember.RemoteMachineDeclineH\x00\x1a\x16\n\x14RemoteMachineAccepts\x1a\xac\x01\n\x14RemoteMachineDecline\x12Z\n\x06reason\x18\x01 \x01(\x0e\x32J.rv.data.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason\"8\n\rDeclineReason\x12\x14\n\x10\x41LREADY_IN_GROUP\x10\x00\x12\x11\n\rUSER_DECLINED\x10\x01\x42\x08\n\x06Result\x1a\x0e\n\x0cRemoveMemberB\n\n\x08ResponseB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_GROUPMEMBER']._serialized_start=62
  _globals['_API_V1_GROUPMEMBER']._serialized_end=108
  _globals['_API_V1_GROUPMEMBERSTATUS']._serialized_start=111
  _globals['_API_V1_GROUPMEMBERSTATUS']._serialized_end=698
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_CONNECTIONSTATUS']._serialized_start=438
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_CONNECTIONSTATUS']._serialized_end=581
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_PLATFORM']._serialized_start=583
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_PLATFORM']._serialized_end=698
  _globals['_API_V1_GROUPDEFINITION']._serialized_start=701
  _globals['_API_V1_GROUPDEFINITION']._serialized_end=881
  _globals['_API_V1_LINK_REQUEST']._serialized_start=884
  _globals['_API_V1_LINK_REQUEST']._serialized_end=1436
  _globals['_API_V1_LINK_REQUEST_HEARTBEAT']._serialized_start=1153
  _globals['_API_V1_LINK_REQUEST_HEARTBEAT']._serialized_end=1205
  _globals['_API_V1_LINK_REQUEST_STATUS']._serialized_start=1207
  _globals['_API_V1_LINK_REQUEST_STATUS']._serialized_end=1215
  _globals['_API_V1_LINK_REQUEST_ADDMEMBER']._serialized_start=1218
  _globals['_API_V1_LINK_REQUEST_ADDMEMBER']._serialized_end=1356
  _globals['_API_V1_LINK_REQUEST_REMOVEMEMBER']._serialized_start=1358
  _globals['_API_V1_LINK_REQUEST_REMOVEMEMBER']._serialized_end=1425
  _globals['_API_V1_LINK_RESPONSE']._serialized_start=1439
  _globals['_API_V1_LINK_RESPONSE']._serialized_end=2397
  _globals['_API_V1_LINK_RESPONSE_HEARTBEAT']._serialized_start=1713
  _globals['_API_V1_LINK_RESPONSE_HEARTBEAT']._serialized_end=1834
  _globals['_API_V1_LINK_RESPONSE_STATUS']._serialized_start=1836
  _globals['_API_V1_LINK_RESPONSE_STATUS']._serialized_end=1924
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER']._serialized_start=1927
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER']._serialized_end=2369
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEACCEPTS']._serialized_start=2162
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEACCEPTS']._serialized_end=2184
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEDECLINE']._serialized_start=2187
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEDECLINE']._serialized_end=2359
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEDECLINE_DECLINEREASON']._serialized_start=2303
  _globals['_API_V1_LINK_RESPONSE_ADDMEMBER_REMOTEMACHINEDECLINE_DECLINEREASON']._serialized_end=2359
  _globals['_API_V1_LINK_RESPONSE_REMOVEMEMBER']._serialized_start=1358
  _globals['_API_V1_LINK_RESPONSE_REMOVEMEMBER']._serialized_end=1372
# @@protoc_insertion_point(module_scope)
