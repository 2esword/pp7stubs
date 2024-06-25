# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analyticsCapture.proto
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
    'analyticsCapture.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61nalyticsCapture.proto\x12\x0crv.analytics\"\xbc\x0b\n\x07\x43\x61pture\x12,\n\x05start\x18\x01 \x01(\x0b\x32\x1b.rv.analytics.Capture.StartH\x00\x1a+\n\nResolution\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x1a\xa5\x06\n\x05Start\x12\x30\n\x04rtmp\x18\x01 \x01(\x0b\x32 .rv.analytics.Capture.Start.RTMPH\x00\x12\x30\n\x04\x64isk\x18\x02 \x01(\x0b\x32 .rv.analytics.Capture.Start.DiskH\x00\x12\x30\n\x04resi\x18\x03 \x01(\x0b\x32 .rv.analytics.Capture.Start.ResiH\x00\x1a\xda\x01\n\x04RTMP\x12*\n\x05\x63odec\x18\x01 \x01(\x0e\x32\x1b.rv.analytics.Capture.Codec\x12\x33\n\nframe_rate\x18\x02 \x01(\x0e\x32\x1f.rv.analytics.Capture.FrameRate\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x34\n\nresolution\x18\x04 \x01(\x0b\x32 .rv.analytics.Capture.Resolution\x12\x16\n\x0estream_started\x18\x05 \x01(\x08\x12\x15\n\rvideo_bitrate\x18\x06 \x01(\x05\x1a\xcc\x01\n\x04\x44isk\x12*\n\x05\x63odec\x18\x01 \x01(\x0e\x32\x1b.rv.analytics.Capture.Codec\x12\x33\n\nframe_rate\x18\x02 \x01(\x0e\x32\x1f.rv.analytics.Capture.FrameRate\x12\x34\n\nresolution\x18\x03 \x01(\x0b\x32 .rv.analytics.Capture.Resolution\x12\x16\n\x0estream_started\x18\x04 \x01(\x08\x12\x15\n\rvideo_bitrate\x18\x05 \x01(\x05\x1a\xcc\x01\n\x04Resi\x12*\n\x05\x63odec\x18\x01 \x01(\x0e\x32\x1b.rv.analytics.Capture.Codec\x12\x33\n\nframe_rate\x18\x02 \x01(\x0e\x32\x1f.rv.analytics.Capture.FrameRate\x12\x34\n\nresolution\x18\x03 \x01(\x0b\x32 .rv.analytics.Capture.Resolution\x12\x16\n\x0estream_started\x18\x04 \x01(\x08\x12\x15\n\rvideo_bitrate\x18\x05 \x01(\x05\x42\x0b\n\tComponent\"\xf3\x02\n\x05\x43odec\x12\x11\n\rCODEC_UNKNOWN\x10\x00\x12\x13\n\x0f\x43ODEC_AUTOMATIC\x10\x01\x12\x0e\n\nCODEC_H264\x10\x02\x12\x17\n\x13\x43ODEC_H264_SOFTWARE\x10\x03\x12\x0e\n\nCODEC_H265\x10\x04\x12\x17\n\x13\x43ODEC_H265_SOFTWARE\x10\x05\x12\x1a\n\x16\x43ODEC_PRORES_422_PROXY\x10\x06\x12\x17\n\x13\x43ODEC_PRORES_422_LT\x10\x07\x12\x14\n\x10\x43ODEC_PRORES_422\x10\x08\x12\x17\n\x13\x43ODEC_PRORES_422_HQ\x10\t\x12\x15\n\x11\x43ODEC_PRORES_4444\x10\n\x12\x18\n\x14\x43ODEC_PRORES_4444_XQ\x10\x0b\x12\r\n\tCODEC_HAP\x10\x0c\x12\x13\n\x0f\x43ODEC_HAP_ALPHA\x10\r\x12\x0f\n\x0b\x43ODEC_HAP_Q\x10\x0e\x12\x15\n\x11\x43ODEC_HAP_Q_ALPHA\x10\x0f\x12\x0f\n\x0b\x43ODEC_NOTCH\x10\x10\"\xae\x01\n\tFrameRate\x12\x16\n\x12\x46RAME_RATE_UNKNOWN\x10\x00\x12\x11\n\rFRAME_RATE_24\x10\x01\x12\x11\n\rFRAME_RATE_25\x10\x02\x12\x14\n\x10\x46RAME_RATE_29_97\x10\x03\x12\x11\n\rFRAME_RATE_30\x10\x04\x12\x11\n\rFRAME_RATE_50\x10\x05\x12\x14\n\x10\x46RAME_RATE_59_94\x10\x06\x12\x11\n\rFRAME_RATE_60\x10\x07\x42\x07\n\x05\x45ventBA\xf8\x01\x01\xaa\x02.Pro.SerializationInterop.RVProtoData.Analytics\xba\x02\nAnalytics_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analyticsCapture_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002.Pro.SerializationInterop.RVProtoData.Analytics\272\002\nAnalytics_'
  _globals['_CAPTURE']._serialized_start=41
  _globals['_CAPTURE']._serialized_end=1509
  _globals['_CAPTURE_RESOLUTION']._serialized_start=98
  _globals['_CAPTURE_RESOLUTION']._serialized_end=141
  _globals['_CAPTURE_START']._serialized_start=144
  _globals['_CAPTURE_START']._serialized_end=949
  _globals['_CAPTURE_START_RTMP']._serialized_start=304
  _globals['_CAPTURE_START_RTMP']._serialized_end=522
  _globals['_CAPTURE_START_DISK']._serialized_start=525
  _globals['_CAPTURE_START_DISK']._serialized_end=729
  _globals['_CAPTURE_START_RESI']._serialized_start=732
  _globals['_CAPTURE_START_RESI']._serialized_end=936
  _globals['_CAPTURE_CODEC']._serialized_start=952
  _globals['_CAPTURE_CODEC']._serialized_end=1323
  _globals['_CAPTURE_FRAMERATE']._serialized_start=1326
  _globals['_CAPTURE_FRAMERATE']._serialized_end=1500
# @@protoc_insertion_point(module_scope)
