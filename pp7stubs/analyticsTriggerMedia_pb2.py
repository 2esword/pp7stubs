# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analyticsTriggerMedia.proto
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
    'analyticsTriggerMedia.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61nalyticsTriggerMedia.proto\x12\x0crv.analytics\"\x80\x1c\n\x17TriggerMediaInformation\x12\x45\n\x0bsource_type\x18\x01 \x01(\x0e\x32\x30.rv.analytics.TriggerMediaInformation.SourceType\x12<\n\x05video\x18\x02 \x01(\x0b\x32+.rv.analytics.TriggerMediaInformation.VideoH\x00\x12<\n\x05image\x18\x03 \x01(\x0b\x32+.rv.analytics.TriggerMediaInformation.ImageH\x00\x12<\n\x05\x61udio\x18\x04 \x01(\x0b\x32+.rv.analytics.TriggerMediaInformation.AudioH\x00\x12\x45\n\nlive_video\x18\x05 \x01(\x0b\x32/.rv.analytics.TriggerMediaInformation.LiveVideoH\x00\x1a.\n\nTransition\x12\x12\n\nis_default\x18\x01 \x01(\x08\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xe6\x07\n\x0bVisualMedia\x12L\n\x08\x62\x65havior\x18\x01 \x01(\x0e\x32:.rv.analytics.TriggerMediaInformation.VisualMedia.Behavior\x12O\n\nscale_mode\x18\x02 \x01(\x0e\x32;.rv.analytics.TriggerMediaInformation.VisualMedia.ScaleMode\x12M\n\tflip_mode\x18\x03 \x01(\x0e\x32:.rv.analytics.TriggerMediaInformation.VisualMedia.FlipMode\x12Y\n\x0fnative_rotation\x18\x04 \x01(\x0e\x32@.rv.analytics.TriggerMediaInformation.VisualMedia.NativeRotation\x12J\n\nresolution\x18\x05 \x01(\x0b\x32\x36.rv.analytics.TriggerMediaInformation.VisualMedia.Size\x12\x1d\n\x15\x65nabled_effects_count\x18\x06 \x01(\r\x12\x19\n\x11has_effect_preset\x18\x07 \x01(\x08\x12\x44\n\ntransition\x18\x08 \x01(\x0b\x32\x30.rv.analytics.TriggerMediaInformation.Transition\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"V\n\x08\x42\x65havior\x12\x17\n\x13\x42\x45HAVIOR_BACKGROUND\x10\x00\x12\x17\n\x13\x42\x45HAVIOR_FOREGROUND\x10\x01\x12\x18\n\x14\x42\x45HAVIOR_VIDEO_INPUT\x10\x02\"a\n\tScaleMode\x12\x12\n\x0eSCALE_MODE_FIT\x10\x00\x12\x13\n\x0fSCALE_MODE_FILL\x10\x01\x12\x16\n\x12SCALE_MODE_STRETCH\x10\x02\x12\x13\n\x0fSCALE_MODE_BLUR\x10\x03\"d\n\x08\x46lipMode\x12\x12\n\x0e\x46LIP_MODE_NONE\x10\x00\x12\x18\n\x14\x46LIP_MODE_HORIZONTAL\x10\x01\x12\x16\n\x12\x46LIP_MODE_VERTICAL\x10\x02\x12\x12\n\x0e\x46LIP_MODE_BOTH\x10\x03\"z\n\x0eNativeRotation\x12\x1c\n\x18NATIVE_ROTATION_STANDARD\x10\x00\x12\x16\n\x12NATIVE_ROTATION_90\x10Z\x12\x18\n\x13NATIVE_ROTATION_180\x10\xb4\x01\x12\x18\n\x13NATIVE_ROTATION_270\x10\x8e\x02\x1a\xe9\x03\n\tTransport\x12\\\n\x15source_duration_range\x18\x01 \x01(\x0e\x32=.rv.analytics.TriggerMediaInformation.Transport.DurationRange\x12\x19\n\x11has_audio_ramp_in\x18\x02 \x01(\x08\x12\x1a\n\x12has_audio_ramp_out\x18\x03 \x01(\x08\x12\x14\n\x0chas_in_point\x18\x04 \x01(\x08\x12\x15\n\rhas_out_point\x18\x05 \x01(\x08\x12\x11\n\tplay_rate\x18\x06 \x01(\x01\x12\x1d\n\x15playback_marker_count\x18\x07 \x01(\r\"\xe7\x01\n\rDurationRange\x12\x16\n\x12\x44URATION_UNDER_10S\x10\x00\x12\x17\n\x13\x44URATION_10S_TO_30S\x10\x01\x12\x17\n\x13\x44URATION_30S_TO_60S\x10\x02\x12\x15\n\x11\x44URATION_1M_TO_5M\x10\x03\x12\x16\n\x12\x44URATION_5M_TO_10M\x10\x04\x12\x17\n\x13\x44URATION_10M_TO_30M\x10\x05\x12\x17\n\x13\x44URATION_30M_TO_60M\x10\x06\x12\x15\n\x11\x44URATION_1H_TO_2H\x10\x07\x12\x14\n\x10\x44URATION_OVER_2H\x10\x08\x1a\xc5\x04\n\x05Video\x12G\n\x0cvisual_media\x18\x07 \x01(\x0b\x32\x31.rv.analytics.TriggerMediaInformation.VisualMedia\x12W\n\x11playback_behavior\x18\x08 \x01(\x0e\x32<.rv.analytics.TriggerMediaInformation.Video.PlaybackBehavior\x12Q\n\x11\x63ompletion_target\x18\t \x01(\x0e\x32\x36.rv.analytics.TriggerMediaInformation.CompletionTarget\x12\x19\n\x11soft_loop_enabled\x18\n \x01(\x08\x12\x1a\n\x12soft_loop_duration\x18\x0b \x01(\x01\x12\x12\n\nframe_rate\x18\x0c \x01(\x01\x12\x1b\n\x13\x61udio_channel_count\x18\r \x01(\r\x12\x42\n\ttransport\x18\x0e \x01(\x0b\x32/.rv.analytics.TriggerMediaInformation.Transport\"\x9a\x01\n\x10PlaybackBehavior\x12\x1a\n\x16PLAYBACK_BEHAVIOR_STOP\x10\x00\x12\x1a\n\x16PLAYBACK_BEHAVIOR_LOOP\x10\x01\x12)\n%PLAYBACK_BEHAVIOR_LOOP_FOR_PLAY_COUNT\x10\x02\x12#\n\x1fPLAYBACK_BEHAVIOR_LOOP_FOR_TIME\x10\x03\x1a\xea\x03\n\x05\x41udio\x12\x46\n\x08\x62\x65havior\x18\x01 \x01(\x0e\x32\x34.rv.analytics.TriggerMediaInformation.Audio.Behavior\x12W\n\x11playback_behavior\x18\x02 \x01(\x0e\x32<.rv.analytics.TriggerMediaInformation.Audio.PlaybackBehavior\x12\x44\n\ntransition\x18\x03 \x01(\x0b\x32\x30.rv.analytics.TriggerMediaInformation.Transition\x12\x1b\n\x13\x61udio_channel_count\x18\x04 \x01(\r\x12\x42\n\ttransport\x18\x05 \x01(\x0b\x32/.rv.analytics.TriggerMediaInformation.Transport\"1\n\x08\x42\x65havior\x12\x11\n\rBEHAVIOR_TUNE\x10\x00\x12\x12\n\x0e\x42\x45HAVIOR_SOUND\x10\x01\"f\n\x10PlaybackBehavior\x12\x1a\n\x16PLAYBACK_BEHAVIOR_STOP\x10\x00\x12\x1a\n\x16PLAYBACK_BEHAVIOR_LOOP\x10\x01\x12\x1a\n\x16PLAYBACK_BEHAVIOR_NEXT\x10\x02\x1a\xe9\x01\n\x05Image\x12G\n\x0cvisual_media\x18\x01 \x01(\x0b\x32\x31.rv.analytics.TriggerMediaInformation.VisualMedia\x12\x44\n\ntransition\x18\x02 \x01(\x0b\x32\x30.rv.analytics.TriggerMediaInformation.Transition\x12Q\n\x11\x63ompletion_target\x18\x03 \x01(\x0e\x32\x36.rv.analytics.TriggerMediaInformation.CompletionTarget\x1a\x85\x01\n\tLiveVideo\x12G\n\x0cvisual_media\x18\x01 \x01(\x0b\x32\x31.rv.analytics.TriggerMediaInformation.VisualMedia\x12\x12\n\nframe_rate\x18\x02 \x01(\x01\x12\x1b\n\x13\x61udio_channel_count\x18\x03 \x01(\r\"\xa0\x01\n\x10\x43ompletionTarget\x12\x1a\n\x16\x43OMPLETION_TARGET_NONE\x10\x00\x12\x1a\n\x16\x43OMPLETION_TARGET_NEXT\x10\x01\x12\x1c\n\x18\x43OMPLETION_TARGET_RANDOM\x10\x02\x12\x19\n\x15\x43OMPLETION_TARGET_CUE\x10\x03\x12\x1b\n\x17\x43OMPLETION_TARGET_FIRST\x10\x04\"?\n\nSourceType\x12\x15\n\x11SOURCE_TYPE_LOCAL\x10\x00\x12\x1a\n\x16SOURCE_TYPE_PROCONTENT\x10\x01\x42\x0b\n\tMediaTypeBA\xf8\x01\x01\xaa\x02.Pro.SerializationInterop.RVProtoData.Analytics\xba\x02\nAnalytics_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analyticsTriggerMedia_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002.Pro.SerializationInterop.RVProtoData.Analytics\272\002\nAnalytics_'
  _globals['_TRIGGERMEDIAINFORMATION']._serialized_start=46
  _globals['_TRIGGERMEDIAINFORMATION']._serialized_end=3630
  _globals['_TRIGGERMEDIAINFORMATION_TRANSITION']._serialized_start=401
  _globals['_TRIGGERMEDIAINFORMATION_TRANSITION']._serialized_end=447
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA']._serialized_start=450
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA']._serialized_end=1448
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_SIZE']._serialized_start=998
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_SIZE']._serialized_end=1035
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_BEHAVIOR']._serialized_start=1037
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_BEHAVIOR']._serialized_end=1123
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_SCALEMODE']._serialized_start=1125
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_SCALEMODE']._serialized_end=1222
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_FLIPMODE']._serialized_start=1224
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_FLIPMODE']._serialized_end=1324
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_NATIVEROTATION']._serialized_start=1326
  _globals['_TRIGGERMEDIAINFORMATION_VISUALMEDIA_NATIVEROTATION']._serialized_end=1448
  _globals['_TRIGGERMEDIAINFORMATION_TRANSPORT']._serialized_start=1451
  _globals['_TRIGGERMEDIAINFORMATION_TRANSPORT']._serialized_end=1940
  _globals['_TRIGGERMEDIAINFORMATION_TRANSPORT_DURATIONRANGE']._serialized_start=1709
  _globals['_TRIGGERMEDIAINFORMATION_TRANSPORT_DURATIONRANGE']._serialized_end=1940
  _globals['_TRIGGERMEDIAINFORMATION_VIDEO']._serialized_start=1943
  _globals['_TRIGGERMEDIAINFORMATION_VIDEO']._serialized_end=2524
  _globals['_TRIGGERMEDIAINFORMATION_VIDEO_PLAYBACKBEHAVIOR']._serialized_start=2370
  _globals['_TRIGGERMEDIAINFORMATION_VIDEO_PLAYBACKBEHAVIOR']._serialized_end=2524
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO']._serialized_start=2527
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO']._serialized_end=3017
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO_BEHAVIOR']._serialized_start=2864
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO_BEHAVIOR']._serialized_end=2913
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO_PLAYBACKBEHAVIOR']._serialized_start=2915
  _globals['_TRIGGERMEDIAINFORMATION_AUDIO_PLAYBACKBEHAVIOR']._serialized_end=3017
  _globals['_TRIGGERMEDIAINFORMATION_IMAGE']._serialized_start=3020
  _globals['_TRIGGERMEDIAINFORMATION_IMAGE']._serialized_end=3253
  _globals['_TRIGGERMEDIAINFORMATION_LIVEVIDEO']._serialized_start=3256
  _globals['_TRIGGERMEDIAINFORMATION_LIVEVIDEO']._serialized_end=3389
  _globals['_TRIGGERMEDIAINFORMATION_COMPLETIONTARGET']._serialized_start=3392
  _globals['_TRIGGERMEDIAINFORMATION_COMPLETIONTARGET']._serialized_end=3552
  _globals['_TRIGGERMEDIAINFORMATION_SOURCETYPE']._serialized_start=3554
  _globals['_TRIGGERMEDIAINFORMATION_SOURCETYPE']._serialized_end=3617
# @@protoc_insertion_point(module_scope)
