# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Trigger.proto
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
    'proApiV1Trigger.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proApiV1Trigger.proto\x12\x07rv.data\"\xe5\x07\n\x16\x41PI_v1_Trigger_Request\x12\x32\n\x03\x63ue\x18\x01 \x01(\x0b\x32#.rv.data.API_v1_Trigger_Request.CueH\x00\x12<\n\x08playlist\x18\x02 \x01(\x0b\x32(.rv.data.API_v1_Trigger_Request.PlaylistH\x00\x12\x36\n\x05media\x18\x03 \x01(\x0b\x32%.rv.data.API_v1_Trigger_Request.MediaH\x00\x12\x36\n\x05\x61udio\x18\x04 \x01(\x0b\x32%.rv.data.API_v1_Trigger_Request.AudioH\x00\x12\x41\n\x0bvideo_input\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Trigger_Request.VideoInputH\x00\x12:\n\x07library\x18\x06 \x01(\x0b\x32\'.rv.data.API_v1_Trigger_Request.LibraryH\x00\x12\x34\n\x04next\x18\x07 \x01(\x0b\x32$.rv.data.API_v1_Trigger_Request.NextH\x00\x12<\n\x08previous\x18\x08 \x01(\x0b\x32(.rv.data.API_v1_Trigger_Request.PreviousH\x00\x12?\n\nmedia_next\x18\t \x01(\x0b\x32).rv.data.API_v1_Trigger_Request.MediaNextH\x00\x12G\n\x0emedia_previous\x18\n \x01(\x0b\x32-.rv.data.API_v1_Trigger_Request.MediaPreviousH\x00\x12?\n\naudio_next\x18\x0b \x01(\x0b\x32).rv.data.API_v1_Trigger_Request.AudioNextH\x00\x12G\n\x0e\x61udio_previous\x18\x0c \x01(\x0b\x32-.rv.data.API_v1_Trigger_Request.AudioPreviousH\x00\x1a\x14\n\x03\x43ue\x12\r\n\x05index\x18\x01 \x01(\r\x1a\x16\n\x08Playlist\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x13\n\x05Media\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x0b\n\tMediaNext\x1a\x0f\n\rMediaPrevious\x1a\x13\n\x05\x41udio\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x0b\n\tAudioNext\x1a\x0f\n\rAudioPrevious\x1a\x18\n\nVideoInput\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x15\n\x07Library\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x06\n\x04Next\x1a\n\n\x08PreviousB\t\n\x07Request\"\xa8\x07\n\x17\x41PI_v1_Trigger_Response\x12\x33\n\x03\x63ue\x18\x01 \x01(\x0b\x32$.rv.data.API_v1_Trigger_Response.CueH\x00\x12=\n\x08playlist\x18\x02 \x01(\x0b\x32).rv.data.API_v1_Trigger_Response.PlaylistH\x00\x12\x37\n\x05media\x18\x03 \x01(\x0b\x32&.rv.data.API_v1_Trigger_Response.MediaH\x00\x12\x37\n\x05\x61udio\x18\x04 \x01(\x0b\x32&.rv.data.API_v1_Trigger_Response.AudioH\x00\x12\x42\n\x0bvideo_input\x18\x05 \x01(\x0b\x32+.rv.data.API_v1_Trigger_Response.VideoInputH\x00\x12;\n\x07library\x18\x06 \x01(\x0b\x32(.rv.data.API_v1_Trigger_Response.LibraryH\x00\x12\x35\n\x04next\x18\x07 \x01(\x0b\x32%.rv.data.API_v1_Trigger_Response.NextH\x00\x12=\n\x08previous\x18\x08 \x01(\x0b\x32).rv.data.API_v1_Trigger_Response.PreviousH\x00\x12@\n\nmedia_next\x18\t \x01(\x0b\x32*.rv.data.API_v1_Trigger_Response.MediaNextH\x00\x12H\n\x0emedia_previous\x18\n \x01(\x0b\x32..rv.data.API_v1_Trigger_Response.MediaPreviousH\x00\x12@\n\naudio_next\x18\x0b \x01(\x0b\x32*.rv.data.API_v1_Trigger_Response.AudioNextH\x00\x12H\n\x0e\x61udio_previous\x18\x0c \x01(\x0b\x32..rv.data.API_v1_Trigger_Response.AudioPreviousH\x00\x1a\x05\n\x03\x43ue\x1a\n\n\x08Playlist\x1a\x07\n\x05Media\x1a\x0b\n\tMediaNext\x1a\x0f\n\rMediaPrevious\x1a\x07\n\x05\x41udio\x1a\x0b\n\tAudioNext\x1a\x0f\n\rAudioPrevious\x1a\x0c\n\nVideoInput\x1a\t\n\x07Library\x1a\x06\n\x04Next\x1a\n\n\x08PreviousB\n\n\x08ResponseB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Trigger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_TRIGGER_REQUEST']._serialized_start=35
  _globals['_API_V1_TRIGGER_REQUEST']._serialized_end=1032
  _globals['_API_V1_TRIGGER_REQUEST_CUE']._serialized_start=806
  _globals['_API_V1_TRIGGER_REQUEST_CUE']._serialized_end=826
  _globals['_API_V1_TRIGGER_REQUEST_PLAYLIST']._serialized_start=828
  _globals['_API_V1_TRIGGER_REQUEST_PLAYLIST']._serialized_end=850
  _globals['_API_V1_TRIGGER_REQUEST_MEDIA']._serialized_start=852
  _globals['_API_V1_TRIGGER_REQUEST_MEDIA']._serialized_end=871
  _globals['_API_V1_TRIGGER_REQUEST_MEDIANEXT']._serialized_start=873
  _globals['_API_V1_TRIGGER_REQUEST_MEDIANEXT']._serialized_end=884
  _globals['_API_V1_TRIGGER_REQUEST_MEDIAPREVIOUS']._serialized_start=886
  _globals['_API_V1_TRIGGER_REQUEST_MEDIAPREVIOUS']._serialized_end=901
  _globals['_API_V1_TRIGGER_REQUEST_AUDIO']._serialized_start=903
  _globals['_API_V1_TRIGGER_REQUEST_AUDIO']._serialized_end=922
  _globals['_API_V1_TRIGGER_REQUEST_AUDIONEXT']._serialized_start=924
  _globals['_API_V1_TRIGGER_REQUEST_AUDIONEXT']._serialized_end=935
  _globals['_API_V1_TRIGGER_REQUEST_AUDIOPREVIOUS']._serialized_start=937
  _globals['_API_V1_TRIGGER_REQUEST_AUDIOPREVIOUS']._serialized_end=952
  _globals['_API_V1_TRIGGER_REQUEST_VIDEOINPUT']._serialized_start=954
  _globals['_API_V1_TRIGGER_REQUEST_VIDEOINPUT']._serialized_end=978
  _globals['_API_V1_TRIGGER_REQUEST_LIBRARY']._serialized_start=980
  _globals['_API_V1_TRIGGER_REQUEST_LIBRARY']._serialized_end=1001
  _globals['_API_V1_TRIGGER_REQUEST_NEXT']._serialized_start=1003
  _globals['_API_V1_TRIGGER_REQUEST_NEXT']._serialized_end=1009
  _globals['_API_V1_TRIGGER_REQUEST_PREVIOUS']._serialized_start=1011
  _globals['_API_V1_TRIGGER_REQUEST_PREVIOUS']._serialized_end=1021
  _globals['_API_V1_TRIGGER_RESPONSE']._serialized_start=1035
  _globals['_API_V1_TRIGGER_RESPONSE']._serialized_end=1971
  _globals['_API_V1_TRIGGER_RESPONSE_CUE']._serialized_start=806
  _globals['_API_V1_TRIGGER_RESPONSE_CUE']._serialized_end=811
  _globals['_API_V1_TRIGGER_RESPONSE_PLAYLIST']._serialized_start=828
  _globals['_API_V1_TRIGGER_RESPONSE_PLAYLIST']._serialized_end=838
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIA']._serialized_start=852
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIA']._serialized_end=859
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIANEXT']._serialized_start=873
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIANEXT']._serialized_end=884
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIAPREVIOUS']._serialized_start=886
  _globals['_API_V1_TRIGGER_RESPONSE_MEDIAPREVIOUS']._serialized_end=901
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIO']._serialized_start=903
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIO']._serialized_end=910
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIONEXT']._serialized_start=924
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIONEXT']._serialized_end=935
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIOPREVIOUS']._serialized_start=937
  _globals['_API_V1_TRIGGER_RESPONSE_AUDIOPREVIOUS']._serialized_end=952
  _globals['_API_V1_TRIGGER_RESPONSE_VIDEOINPUT']._serialized_start=954
  _globals['_API_V1_TRIGGER_RESPONSE_VIDEOINPUT']._serialized_end=966
  _globals['_API_V1_TRIGGER_RESPONSE_LIBRARY']._serialized_start=980
  _globals['_API_V1_TRIGGER_RESPONSE_LIBRARY']._serialized_end=989
  _globals['_API_V1_TRIGGER_RESPONSE_NEXT']._serialized_start=1003
  _globals['_API_V1_TRIGGER_RESPONSE_NEXT']._serialized_end=1009
  _globals['_API_V1_TRIGGER_RESPONSE_PREVIOUS']._serialized_start=1011
  _globals['_API_V1_TRIGGER_RESPONSE_PREVIOUS']._serialized_end=1021
# @@protoc_insertion_point(module_scope)
