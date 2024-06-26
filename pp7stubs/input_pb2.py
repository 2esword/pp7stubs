# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: input.proto
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
    'input.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import alphaType_pb2 as alphaType__pb2
from . import color_pb2 as color__pb2
from . import digitalAudio_pb2 as digitalAudio__pb2
from . import graphicsData_pb2 as graphicsData__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0binput.proto\x12\x07rv.data\x1a\x0f\x61lphaType.proto\x1a\x0b\x63olor.proto\x1a\x12\x64igitalAudio.proto\x1a\x12graphicsData.proto\x1a\turl.proto\x1a\nuuid.proto\"\xcd\x04\n\nVideoInput\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x18\n\x10user_description\x18\x02 \x01(\t\x12\x36\n\x12video_input_device\x18\x03 \x01(\x0b\x32\x1a.rv.data.Media.VideoDevice\x12%\n\rdisplay_color\x18\x04 \x01(\x0b\x32\x0e.rv.data.Color\x12$\n\x0ethumbnail_path\x18\x05 \x01(\x0b\x32\x0c.rv.data.URL\x12\x37\n\naudio_type\x18\x08 \x01(\x0e\x32#.rv.data.VideoInput.AudioDeviceType\x12&\n\nalpha_type\x18\t \x01(\x0e\x32\x12.rv.data.AlphaType\x12\x34\n\x0c\x61udio_device\x18\x06 \x01(\x0b\x32\x1c.rv.data.DigitalAudio.DeviceH\x00\x12\x32\n\x0cvideo_device\x18\x07 \x01(\x0b\x32\x1a.rv.data.Media.VideoDeviceH\x00\x1a\x37\n\x10SettingsDocument\x12#\n\x06inputs\x18\x01 \x03(\x0b\x32\x13.rv.data.VideoInput\"m\n\x0f\x41udioDeviceType\x12\x1d\n\x19\x41UDIO_DEVICE_TYPE_DEFAULT\x10\x00\x12\x1a\n\x16\x41UDIO_DEVICE_TYPE_NONE\x10\x01\x12\x1f\n\x1b\x41UDIO_DEVICE_TYPE_ALTERNATE\x10\x02\x42\x10\n\x0e\x41ltAudioSource\"\xaa\x04\n\nAudioInput\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x18\n\x10user_description\x18\x02 \x01(\t\x12\x37\n\rbehavior_mode\x18\x05 \x01(\x0b\x32 .rv.data.AudioInput.BehaviorMode\x12\x34\n\x0c\x61udio_device\x18\x03 \x01(\x0b\x32\x1c.rv.data.DigitalAudio.DeviceH\x00\x12\x32\n\x0cvideo_device\x18\x04 \x01(\x0b\x32\x1a.rv.data.Media.VideoDeviceH\x00\x1a\xb7\x02\n\x0c\x42\x65haviorMode\x12\x31\n\x02on\x18\x01 \x01(\x0b\x32#.rv.data.AudioInput.BehaviorMode.OnH\x00\x12\x33\n\x03off\x18\x02 \x01(\x0b\x32$.rv.data.AudioInput.BehaviorMode.OffH\x00\x12:\n\x07\x61uto_on\x18\x03 \x01(\x0b\x32\'.rv.data.AudioInput.BehaviorMode.AutoOnH\x00\x12<\n\x08\x61uto_off\x18\x04 \x01(\x0b\x32(.rv.data.AudioInput.BehaviorMode.AutoOffH\x00\x1a\x04\n\x02On\x1a\x05\n\x03Off\x1a\t\n\x07\x41utoOff\x1a%\n\x06\x41utoOn\x12\x1b\n\x13linked_video_inputs\x18\x01 \x03(\rB\x06\n\x04ModeB\x08\n\x06SourceB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'input_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_VIDEOINPUT']._serialized_start=118
  _globals['_VIDEOINPUT']._serialized_end=707
  _globals['_VIDEOINPUT_SETTINGSDOCUMENT']._serialized_start=523
  _globals['_VIDEOINPUT_SETTINGSDOCUMENT']._serialized_end=578
  _globals['_VIDEOINPUT_AUDIODEVICETYPE']._serialized_start=580
  _globals['_VIDEOINPUT_AUDIODEVICETYPE']._serialized_end=689
  _globals['_AUDIOINPUT']._serialized_start=710
  _globals['_AUDIOINPUT']._serialized_end=1264
  _globals['_AUDIOINPUT_BEHAVIORMODE']._serialized_start=943
  _globals['_AUDIOINPUT_BEHAVIORMODE']._serialized_end=1254
  _globals['_AUDIOINPUT_BEHAVIORMODE_ON']._serialized_start=1185
  _globals['_AUDIOINPUT_BEHAVIORMODE_ON']._serialized_end=1189
  _globals['_AUDIOINPUT_BEHAVIORMODE_OFF']._serialized_start=1191
  _globals['_AUDIOINPUT_BEHAVIORMODE_OFF']._serialized_end=1196
  _globals['_AUDIOINPUT_BEHAVIORMODE_AUTOOFF']._serialized_start=1198
  _globals['_AUDIOINPUT_BEHAVIORMODE_AUTOOFF']._serialized_end=1207
  _globals['_AUDIOINPUT_BEHAVIORMODE_AUTOON']._serialized_start=1209
  _globals['_AUDIOINPUT_BEHAVIORMODE_AUTOON']._serialized_end=1246
# @@protoc_insertion_point(module_scope)
