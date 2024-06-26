# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1.proto
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
    'proApiV1.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import proApiV1Announcement_pb2 as proApiV1Announcement__pb2
from . import proApiV1Audio_pb2 as proApiV1Audio__pb2
from . import proApiV1Capture_pb2 as proApiV1Capture__pb2
from . import proApiV1Clear_pb2 as proApiV1Clear__pb2
from . import proApiV1ErrorResponse_pb2 as proApiV1ErrorResponse__pb2
from . import proApiV1Groups_pb2 as proApiV1Groups__pb2
from . import proApiV1Link_pb2 as proApiV1Link__pb2
from . import proApiV1Library_pb2 as proApiV1Library__pb2
from . import proApiV1Looks_pb2 as proApiV1Looks__pb2
from . import proApiV1Macro_pb2 as proApiV1Macro__pb2
from . import proApiV1Masks_pb2 as proApiV1Masks__pb2
from . import proApiV1Media_pb2 as proApiV1Media__pb2
from . import proApiV1Message_pb2 as proApiV1Message__pb2
from . import proApiV1Miscellaneous_pb2 as proApiV1Miscellaneous__pb2
from . import proApiV1Playlist_pb2 as proApiV1Playlist__pb2
from . import proApiV1Preroll_pb2 as proApiV1Preroll__pb2
from . import proApiV1Presentation_pb2 as proApiV1Presentation__pb2
from . import proApiV1Prop_pb2 as proApiV1Prop__pb2
from . import proApiV1Stage_pb2 as proApiV1Stage__pb2
from . import proApiV1Status_pb2 as proApiV1Status__pb2
from . import proApiV1Theme_pb2 as proApiV1Theme__pb2
from . import proApiV1Timer_pb2 as proApiV1Timer__pb2
from . import proApiV1Transport_pb2 as proApiV1Transport__pb2
from . import proApiV1Trigger_pb2 as proApiV1Trigger__pb2
from . import proApiV1VideoInputs_pb2 as proApiV1VideoInputs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproApiV1.proto\x12\x07rv.data\x1a\x1aproApiV1Announcement.proto\x1a\x13proApiV1Audio.proto\x1a\x15proApiV1Capture.proto\x1a\x13proApiV1Clear.proto\x1a\x1bproApiV1ErrorResponse.proto\x1a\x14proApiV1Groups.proto\x1a\x12proApiV1Link.proto\x1a\x15proApiV1Library.proto\x1a\x13proApiV1Looks.proto\x1a\x13proApiV1Macro.proto\x1a\x13proApiV1Masks.proto\x1a\x13proApiV1Media.proto\x1a\x15proApiV1Message.proto\x1a\x1bproApiV1Miscellaneous.proto\x1a\x16proApiV1Playlist.proto\x1a\x15proApiV1Preroll.proto\x1a\x1aproApiV1Presentation.proto\x1a\x12proApiV1Prop.proto\x1a\x13proApiV1Stage.proto\x1a\x14proApiV1Status.proto\x1a\x13proApiV1Theme.proto\x1a\x13proApiV1Timer.proto\x1a\x17proApiV1Transport.proto\x1a\x15proApiV1Trigger.proto\x1a\x19proApiV1VideoInputs.proto\"\xd1\x18\n\rNetworkAPI_v1\x12/\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x1d.rv.data.NetworkAPI_v1.ActionH\x00\x1a\x83\x18\n\x06\x41\x63tion\x12\x36\n\raudio_request\x18\x01 \x01(\x0b\x32\x1d.rv.data.API_v1_Audio_RequestH\x00\x12:\n\x0f\x63\x61pture_request\x18\x02 \x01(\x0b\x32\x1f.rv.data.API_v1_Capture_RequestH\x00\x12\x39\n\x10\x63learing_request\x18\x03 \x01(\x0b\x32\x1d.rv.data.API_v1_Clear_RequestH\x00\x12\x38\n\x0egroups_request\x18\x04 \x01(\x0b\x32\x1e.rv.data.API_v1_Groups_RequestH\x00\x12\x34\n\x0clink_request\x18\x05 \x01(\x0b\x32\x1c.rv.data.API_v1_Link_RequestH\x00\x12:\n\x0flibrary_request\x18\x06 \x01(\x0b\x32\x1f.rv.data.API_v1_Library_RequestH\x00\x12\x36\n\rlooks_request\x18\x07 \x01(\x0b\x32\x1d.rv.data.API_v1_Looks_RequestH\x00\x12\x36\n\rmacro_request\x18\x08 \x01(\x0b\x32\x1d.rv.data.API_v1_Macro_RequestH\x00\x12\x36\n\rmasks_request\x18\t \x01(\x0b\x32\x1d.rv.data.API_v1_Masks_RequestH\x00\x12\x36\n\rmedia_request\x18\n \x01(\x0b\x32\x1d.rv.data.API_v1_Media_RequestH\x00\x12:\n\x0fmessage_request\x18\x0b \x01(\x0b\x32\x1f.rv.data.API_v1_Message_RequestH\x00\x12\x46\n\x15miscellaneous_request\x18\x0c \x01(\x0b\x32%.rv.data.API_v1_Miscellaneous_RequestH\x00\x12<\n\x10playlist_request\x18\r \x01(\x0b\x32 .rv.data.API_v1_Playlist_RequestH\x00\x12:\n\x0fpreroll_request\x18\x0e \x01(\x0b\x32\x1f.rv.data.API_v1_Preroll_RequestH\x00\x12\x44\n\x14presentation_request\x18\x0f \x01(\x0b\x32$.rv.data.API_v1_Presentation_RequestH\x00\x12\x34\n\x0cprop_request\x18\x10 \x01(\x0b\x32\x1c.rv.data.API_v1_Prop_RequestH\x00\x12\x36\n\rstage_request\x18\x11 \x01(\x0b\x32\x1d.rv.data.API_v1_Stage_RequestH\x00\x12\x38\n\x0estatus_request\x18\x12 \x01(\x0b\x32\x1e.rv.data.API_v1_Status_RequestH\x00\x12\x36\n\rtheme_request\x18\x13 \x01(\x0b\x32\x1d.rv.data.API_v1_Theme_RequestH\x00\x12\x36\n\rtimer_request\x18\x14 \x01(\x0b\x32\x1d.rv.data.API_v1_Timer_RequestH\x00\x12>\n\x11transport_request\x18\x15 \x01(\x0b\x32!.rv.data.API_v1_Transport_RequestH\x00\x12:\n\x0ftrigger_request\x18\x16 \x01(\x0b\x32\x1f.rv.data.API_v1_Trigger_RequestH\x00\x12\x44\n\x14video_inputs_request\x18\x17 \x01(\x0b\x32$.rv.data.API_v1_Video_Inputs_RequestH\x00\x12\x44\n\x14\x61nnouncement_request\x18\x18 \x01(\x0b\x32$.rv.data.API_v1_Announcement_RequestH\x00\x12\x38\n\x0e\x61udio_response\x18\x65 \x01(\x0b\x32\x1e.rv.data.API_v1_Audio_ResponseH\x01\x12<\n\x10\x63\x61pture_response\x18\x66 \x01(\x0b\x32 .rv.data.API_v1_Capture_ResponseH\x01\x12;\n\x11\x63learing_response\x18g \x01(\x0b\x32\x1e.rv.data.API_v1_Clear_ResponseH\x01\x12:\n\x0fgroups_response\x18h \x01(\x0b\x32\x1f.rv.data.API_v1_Groups_ResponseH\x01\x12\x36\n\rlink_response\x18i \x01(\x0b\x32\x1d.rv.data.API_v1_Link_ResponseH\x01\x12<\n\x10library_response\x18j \x01(\x0b\x32 .rv.data.API_v1_Library_ResponseH\x01\x12\x38\n\x0elooks_response\x18k \x01(\x0b\x32\x1e.rv.data.API_v1_Looks_ResponseH\x01\x12\x38\n\x0emacro_response\x18l \x01(\x0b\x32\x1e.rv.data.API_v1_Macro_ResponseH\x01\x12\x38\n\x0emasks_response\x18m \x01(\x0b\x32\x1e.rv.data.API_v1_Masks_ResponseH\x01\x12\x38\n\x0emedia_response\x18n \x01(\x0b\x32\x1e.rv.data.API_v1_Media_ResponseH\x01\x12<\n\x10message_response\x18o \x01(\x0b\x32 .rv.data.API_v1_Message_ResponseH\x01\x12H\n\x16miscellaneous_response\x18p \x01(\x0b\x32&.rv.data.API_v1_Miscellaneous_ResponseH\x01\x12>\n\x11playlist_response\x18q \x01(\x0b\x32!.rv.data.API_v1_Playlist_ResponseH\x01\x12<\n\x10preroll_response\x18r \x01(\x0b\x32 .rv.data.API_v1_Preroll_ResponseH\x01\x12\x46\n\x15presentation_response\x18s \x01(\x0b\x32%.rv.data.API_v1_Presentation_ResponseH\x01\x12\x36\n\rprop_response\x18t \x01(\x0b\x32\x1d.rv.data.API_v1_Prop_ResponseH\x01\x12\x38\n\x0estage_response\x18u \x01(\x0b\x32\x1e.rv.data.API_v1_Stage_ResponseH\x01\x12:\n\x0fstatus_response\x18v \x01(\x0b\x32\x1f.rv.data.API_v1_Status_ResponseH\x01\x12\x38\n\x0etheme_response\x18w \x01(\x0b\x32\x1e.rv.data.API_v1_Theme_ResponseH\x01\x12\x38\n\x0etimer_response\x18x \x01(\x0b\x32\x1e.rv.data.API_v1_Timer_ResponseH\x01\x12@\n\x12transport_response\x18y \x01(\x0b\x32\".rv.data.API_v1_Transport_ResponseH\x01\x12<\n\x10trigger_response\x18z \x01(\x0b\x32 .rv.data.API_v1_Trigger_ResponseH\x01\x12\x46\n\x15video_inputs_response\x18{ \x01(\x0b\x32%.rv.data.API_v1_Video_Inputs_ResponseH\x01\x12\x46\n\x15\x61nnouncement_response\x18| \x01(\x0b\x32%.rv.data.API_v1_Announcement_ResponseH\x01\x12\x39\n\x0e\x65rror_response\x18\xc8\x01 \x01(\x0b\x32\x1e.rv.data.API_v1_Error_ResponseH\x01\x12\x1c\n\x11update_identifier\x18\xc9\x01 \x01(\tH\x02\x42\t\n\x07RequestB\n\n\x08ResponseB\x1b\n\x19StreamingUpdateIdentifierB\t\n\x07\x43ommandB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_NETWORKAPI_V1']._serialized_start=606
  _globals['_NETWORKAPI_V1']._serialized_end=3759
  _globals['_NETWORKAPI_V1_ACTION']._serialized_start=673
  _globals['_NETWORKAPI_V1_ACTION']._serialized_end=3748
# @@protoc_insertion_point(module_scope)
