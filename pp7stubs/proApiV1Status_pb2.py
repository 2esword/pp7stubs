# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Status.proto
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
    'proApiV1Status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import proApiV1Identifier_pb2 as proApiV1Identifier__pb2
from . import proApiV1Size_pb2 as proApiV1Size__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proApiV1Status.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\x1a\x12proApiV1Size.proto\"G\n\x1a\x41PI_v1_SlideDisplayDetails\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05notes\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\"\x92\x01\n\x13\x41PI_v1_ScreenConfig\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\"\n\x04size\x18\x02 \x01(\x0b\x32\x14.rv.data.API_v1_Size\x12/\n\x0bscreen_type\x18\x03 \x01(\x0e\x32\x1a.rv.data.API_v1_ScreenType\"\xbd\x05\n\x15\x41PI_v1_Status_Request\x12>\n\nget_layers\x18\x01 \x01(\x0b\x32(.rv.data.API_v1_Status_Request.GetLayersH\x00\x12K\n\x11get_stage_screens\x18\x02 \x01(\x0b\x32..rv.data.API_v1_Status_Request.GetStageScreensH\x00\x12K\n\x11put_stage_screens\x18\x03 \x01(\x0b\x32..rv.data.API_v1_Status_Request.PutStageScreensH\x00\x12Q\n\x14get_audience_screens\x18\x04 \x01(\x0b\x32\x31.rv.data.API_v1_Status_Request.GetAudienceScreensH\x00\x12Q\n\x14put_audience_screens\x18\x05 \x01(\x0b\x32\x31.rv.data.API_v1_Status_Request.PutAudienceScreensH\x00\x12@\n\x0bget_screens\x18\x06 \x01(\x0b\x32).rv.data.API_v1_Status_Request.GetScreensH\x00\x12<\n\tget_slide\x18\x07 \x01(\x0b\x32\'.rv.data.API_v1_Status_Request.GetSlideH\x00\x1a\x0b\n\tGetLayers\x1a\x11\n\x0fGetStageScreens\x1a\"\n\x0fPutStageScreens\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a\x14\n\x12GetAudienceScreens\x1a%\n\x12PutAudienceScreens\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a\x0c\n\nGetScreens\x1a\n\n\x08GetSlideB\t\n\x07Request\"\xd9\x07\n\x16\x41PI_v1_Status_Response\x12?\n\nget_layers\x18\x01 \x01(\x0b\x32).rv.data.API_v1_Status_Response.GetLayersH\x00\x12L\n\x11get_stage_screens\x18\x02 \x01(\x0b\x32/.rv.data.API_v1_Status_Response.GetStageScreensH\x00\x12L\n\x11put_stage_screens\x18\x03 \x01(\x0b\x32/.rv.data.API_v1_Status_Response.PutStageScreensH\x00\x12R\n\x14get_audience_screens\x18\x04 \x01(\x0b\x32\x32.rv.data.API_v1_Status_Response.GetAudienceScreensH\x00\x12R\n\x14put_audience_screens\x18\x05 \x01(\x0b\x32\x32.rv.data.API_v1_Status_Response.PutAudienceScreensH\x00\x12\x41\n\x0bget_screens\x18\x06 \x01(\x0b\x32*.rv.data.API_v1_Status_Response.GetScreensH\x00\x12=\n\tget_slide\x18\x07 \x01(\x0b\x32(.rv.data.API_v1_Status_Response.GetSlideH\x00\x1a\x85\x01\n\tGetLayers\x12\x13\n\x0bvideo_input\x18\x01 \x01(\x08\x12\r\n\x05media\x18\x02 \x01(\x08\x12\r\n\x05slide\x18\x03 \x01(\x08\x12\x15\n\rannouncements\x18\x04 \x01(\x08\x12\r\n\x05props\x18\x05 \x01(\x08\x12\x10\n\x08messages\x18\x06 \x01(\x08\x12\r\n\x05\x61udio\x18\x07 \x01(\x08\x1a\"\n\x0fGetStageScreens\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a\x11\n\x0fPutStageScreens\x1a%\n\x12GetAudienceScreens\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a\x14\n\x12PutAudienceScreens\x1a;\n\nGetScreens\x12-\n\x07screens\x18\x01 \x03(\x0b\x32\x1c.rv.data.API_v1_ScreenConfig\x1as\n\x08GetSlide\x12\x34\n\x07\x63urrent\x18\x01 \x01(\x0b\x32#.rv.data.API_v1_SlideDisplayDetails\x12\x31\n\x04next\x18\x02 \x01(\x0b\x32#.rv.data.API_v1_SlideDisplayDetailsB\n\n\x08Response*,\n\x11\x41PI_v1_ScreenType\x12\x0c\n\x08\x61udience\x10\x00\x12\t\n\x05stage\x10\x01\x42\x34\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_SCREENTYPE']._serialized_start=1993
  _globals['_API_V1_SCREENTYPE']._serialized_end=2037
  _globals['_API_V1_SLIDEDISPLAYDETAILS']._serialized_start=79
  _globals['_API_V1_SLIDEDISPLAYDETAILS']._serialized_end=150
  _globals['_API_V1_SCREENCONFIG']._serialized_start=153
  _globals['_API_V1_SCREENCONFIG']._serialized_end=299
  _globals['_API_V1_STATUS_REQUEST']._serialized_start=302
  _globals['_API_V1_STATUS_REQUEST']._serialized_end=1003
  _globals['_API_V1_STATUS_REQUEST_GETLAYERS']._serialized_start=839
  _globals['_API_V1_STATUS_REQUEST_GETLAYERS']._serialized_end=850
  _globals['_API_V1_STATUS_REQUEST_GETSTAGESCREENS']._serialized_start=852
  _globals['_API_V1_STATUS_REQUEST_GETSTAGESCREENS']._serialized_end=869
  _globals['_API_V1_STATUS_REQUEST_PUTSTAGESCREENS']._serialized_start=871
  _globals['_API_V1_STATUS_REQUEST_PUTSTAGESCREENS']._serialized_end=905
  _globals['_API_V1_STATUS_REQUEST_GETAUDIENCESCREENS']._serialized_start=907
  _globals['_API_V1_STATUS_REQUEST_GETAUDIENCESCREENS']._serialized_end=927
  _globals['_API_V1_STATUS_REQUEST_PUTAUDIENCESCREENS']._serialized_start=929
  _globals['_API_V1_STATUS_REQUEST_PUTAUDIENCESCREENS']._serialized_end=966
  _globals['_API_V1_STATUS_REQUEST_GETSCREENS']._serialized_start=968
  _globals['_API_V1_STATUS_REQUEST_GETSCREENS']._serialized_end=980
  _globals['_API_V1_STATUS_REQUEST_GETSLIDE']._serialized_start=982
  _globals['_API_V1_STATUS_REQUEST_GETSLIDE']._serialized_end=992
  _globals['_API_V1_STATUS_RESPONSE']._serialized_start=1006
  _globals['_API_V1_STATUS_RESPONSE']._serialized_end=1991
  _globals['_API_V1_STATUS_RESPONSE_GETLAYERS']._serialized_start=1552
  _globals['_API_V1_STATUS_RESPONSE_GETLAYERS']._serialized_end=1685
  _globals['_API_V1_STATUS_RESPONSE_GETSTAGESCREENS']._serialized_start=1687
  _globals['_API_V1_STATUS_RESPONSE_GETSTAGESCREENS']._serialized_end=1721
  _globals['_API_V1_STATUS_RESPONSE_PUTSTAGESCREENS']._serialized_start=871
  _globals['_API_V1_STATUS_RESPONSE_PUTSTAGESCREENS']._serialized_end=888
  _globals['_API_V1_STATUS_RESPONSE_GETAUDIENCESCREENS']._serialized_start=1742
  _globals['_API_V1_STATUS_RESPONSE_GETAUDIENCESCREENS']._serialized_end=1779
  _globals['_API_V1_STATUS_RESPONSE_PUTAUDIENCESCREENS']._serialized_start=929
  _globals['_API_V1_STATUS_RESPONSE_PUTAUDIENCESCREENS']._serialized_end=949
  _globals['_API_V1_STATUS_RESPONSE_GETSCREENS']._serialized_start=1803
  _globals['_API_V1_STATUS_RESPONSE_GETSCREENS']._serialized_end=1862
  _globals['_API_V1_STATUS_RESPONSE_GETSLIDE']._serialized_start=1864
  _globals['_API_V1_STATUS_RESPONSE_GETSLIDE']._serialized_end=1979
# @@protoc_insertion_point(module_scope)
