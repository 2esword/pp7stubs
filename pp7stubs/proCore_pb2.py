# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proCore.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import action_pb2 as action__pb2
from . import alphaType_pb2 as alphaType__pb2
from . import ccli_pb2 as ccli__pb2
from . import cue_pb2 as cue__pb2
from . import effects_pb2 as effects__pb2
from . import graphicsData_pb2 as graphicsData__pb2
from . import input_pb2 as input__pb2
from . import macros_pb2 as macros__pb2
from . import messages_pb2 as messages__pb2
from . import playlist_pb2 as playlist__pb2
from . import preferences_pb2 as preferences__pb2
from . import presentation_pb2 as presentation__pb2
from . import proCoreTestPatterns_pb2 as proCoreTestPatterns__pb2
from . import propDocument_pb2 as propDocument__pb2
from . import propresenter_pb2 as propresenter__pb2
from . import slide_pb2 as slide__pb2
from . import recording_pb2 as recording__pb2
from . import stage_pb2 as stage__pb2
from . import timers_pb2 as timers__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2
from . import proworkspace_pb2 as proworkspace__pb2
from . import digitalAudio_pb2 as digitalAudio__pb2
from . import proAudienceLook_pb2 as proAudienceLook__pb2
from . import proMask_pb2 as proMask__pb2
from . import timedPlayback_pb2 as timedPlayback__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproCore.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\x0f\x61lphaType.proto\x1a\nccli.proto\x1a\tcue.proto\x1a\reffects.proto\x1a\x12graphicsData.proto\x1a\x0binput.proto\x1a\x0cmacros.proto\x1a\x0emessages.proto\x1a\x0eplaylist.proto\x1a\x11preferences.proto\x1a\x12presentation.proto\x1a\x19proCoreTestPatterns.proto\x1a\x12propDocument.proto\x1a\x12propresenter.proto\x1a\x0bslide.proto\x1a\x0frecording.proto\x1a\x0bstage.proto\x1a\x0ctimers.proto\x1a\turl.proto\x1a\nuuid.proto\x1a\x12proworkspace.proto\x1a\x12\x64igitalAudio.proto\x1a\x15proAudienceLook.proto\x1a\rproMask.proto\x1a\x13timedPlayback.proto\"\x86\x05\n\x18MediaMetadataRequestInfo\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x05 \x03(\x0b\x32\x0f.rv.data.Effect\x12\x31\n\x0b\x63rop_insets\x18\x06 \x01(\x0b\x32\x1c.rv.data.Graphics.EdgeInsets\x12M\n\x0fnative_rotation\x18\x07 \x01(\x0e\x32\x34.rv.data.MediaMetadataRequestInfo.NativeRotationType\x12\x1c\n\x14\x66lipped_horizontally\x18\x08 \x01(\x08\x12\x1a\n\x12\x66lipped_vertically\x18\t \x01(\x08\x12?\n\nalpha_type\x18\n \x01(\x0e\x32+.rv.data.MediaMetadataRequestInfo.AlphaType\"\xae\x01\n\x12NativeRotationType\x12(\n$NATIVE_ROTATION_TYPE_ROTATE_STANDARD\x10\x00\x12\"\n\x1eNATIVE_ROTATION_TYPE_ROTATE_90\x10Z\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_180\x10\xb4\x01\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_270\x10\x8e\x02\"Z\n\tAlphaType\x12\x16\n\x12\x41LPHA_TYPE_UNKNOWN\x10\x00\x12\x17\n\x13\x41LPHA_TYPE_STRAIGHT\x10\x01\x12\x1c\n\x18\x41LPHA_TYPE_PREMULTIPLIED\x10\x02\"\xe6\x04\n\x1cMediaMetadataRequestResponse\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..rv.data.MediaMetadataRequestResponse.Metadata\x12O\n\x15generated_bitmap_info\x18\x02 \x01(\x0b\x32\x30.rv.data.MediaMetadataRequestResponse.BitmapInfo\x1a\x85\x03\n\x08Metadata\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x02\x12\x10\n\x08\x64uration\x18\x04 \x01(\x02\x12\x1d\n\x15number_audio_channels\x18\x05 \x01(\r\x12\r\n\x05\x63odec\x18\x06 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x07 \x01(\t\x12\r\n\x05title\x18\x08 \x01(\t\x12\x10\n\x08rotation\x18\t \x01(\x02\x12P\n\x0c\x63ontent_type\x18\n \x01(\x0e\x32:.rv.data.MediaMetadataRequestResponse.Metadata.ContentType\x12\x19\n\x11has_alpha_channel\x18\x0b \x01(\x08\"o\n\x0b\x43ontentType\x12\x18\n\x14\x43ONTENT_TYPE_UNKNOWN\x10\x00\x12\x16\n\x12\x43ONTENT_TYPE_AUDIO\x10\x01\x12\x16\n\x12\x43ONTENT_TYPE_IMAGE\x10\x02\x12\x16\n\x12\x43ONTENT_TYPE_VIDEO\x10\x03\x1a+\n\nBitmapInfo\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"\x8d\x01\n\x11NetworkIdentifier\x12;\n\x0bidentifiers\x18\x01 \x03(\x0b\x32&.rv.data.NetworkIdentifier.IndexOrName\x1a;\n\x0bIndexOrName\x12\x0f\n\x05index\x18\x01 \x01(\x05H\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x42\x0b\n\tComponent\"\xa0\x04\n\x0eTriggerOptions\x12G\n\x13\x63ontent_destination\x18\x01 \x01(\x0e\x32*.rv.data.TriggerOptions.ContentDestination\x12!\n\x19suppress_auto_start_video\x18\x02 \x01(\x08\x12!\n\x19suppress_media_background\x18\x03 \x01(\x08\x12\x17\n\x0f\x66orce_retrigger\x18\x04 \x01(\x08\x12\x19\n\x11reset_chord_chart\x18\x05 \x01(\x08\x12\x1d\n\x15\x66rom_playlist_library\x18\x06 \x01(\x08\x12\x15\n\rfrom_timeline\x18\x07 \x01(\x08\x12\x18\n\x10ignore_analytics\x18\x08 \x01(\x08\x12\x16\n\x0estart_position\x18\t \x01(\x01\x12.\n\x0etrigger_source\x18\n \x01(\x0b\x32\x16.rv.data.TriggerSource\x12\x36\n\x12network_identifier\x18\x0b \x01(\x0b\x32\x1a.rv.data.NetworkIdentifier\x12\x1e\n\x16request_client_context\x18\x0c \x01(\x08\"[\n\x12\x43ontentDestination\x12\x1e\n\x1a\x43ONTENT_DESTINATION_GLOBAL\x10\x00\x12%\n!CONTENT_DESTINATION_ANNOUNCEMENTS\x10\x01\"\xe3!\n\x10\x43ontrolTransport\x12\x39\n\x04play\x18\x01 \x01(\x0b\x32).rv.data.ControlTransport.PlayControlTypeH\x00\x12;\n\x05pause\x18\x02 \x01(\x0b\x32*.rv.data.ControlTransport.PauseControlTypeH\x00\x12=\n\x06rewind\x18\x03 \x01(\x0b\x32+.rv.data.ControlTransport.RewindControlTypeH\x00\x12G\n\x0b\x66\x61stforward\x18\x04 \x01(\x0b\x32\x30.rv.data.ControlTransport.FastForwardControlTypeH\x00\x12\x42\n\tskip_back\x18\x05 \x01(\x0b\x32-.rv.data.ControlTransport.SkipBackControlTypeH\x00\x12H\n\x0cskip_forward\x18\x06 \x01(\x0b\x32\x30.rv.data.ControlTransport.SkipForwardControlTypeH\x00\x12\x42\n\tstep_back\x18\x07 \x01(\x0b\x32-.rv.data.ControlTransport.StepBackControlTypeH\x00\x12H\n\x0cstep_forward\x18\x08 \x01(\x0b\x32\x30.rv.data.ControlTransport.StepForwardControlTypeH\x00\x12\x45\n\x0bgo_to_start\x18\t \x01(\x0b\x32..rv.data.ControlTransport.GoToStartControlTypeH\x00\x12\x41\n\tgo_to_end\x18\n \x01(\x0b\x32,.rv.data.ControlTransport.GoToEndControlTypeH\x00\x12G\n\x0cjump_to_time\x18\x0b \x01(\x0b\x32/.rv.data.ControlTransport.JumpToTimeControlTypeH\x00\x12M\n\x0fjump_to_percent\x18\x0c \x01(\x0b\x32\x32.rv.data.ControlTransport.JumpToPercentControlTypeH\x00\x12\x43\n\x07mark_in\x18\r \x01(\x0b\x32\x30.rv.data.ControlTransport.MarkInPointControlTypeH\x00\x12\x45\n\x08mark_out\x18\x0e \x01(\x0b\x32\x31.rv.data.ControlTransport.MarkOutPointControlTypeH\x00\x12K\n\x0eset_scale_mode\x18\x0f \x01(\x0b\x32\x31.rv.data.ControlTransport.SetScaleModeControlTypeH\x00\x12O\n\x10set_flipped_mode\x18\x10 \x01(\x0b\x32\x33.rv.data.ControlTransport.SetFlippedModeControlTypeH\x00\x12I\n\rset_play_rate\x18\x11 \x01(\x0b\x32\x30.rv.data.ControlTransport.SetPlayRateControlTypeH\x00\x12N\n\x0cset_rotation\x18\x12 \x01(\x0b\x32\x36.rv.data.ControlTransport.SetNativeRotationControlTypeH\x00\x12N\n\x0ftoggle_playback\x18\x13 \x01(\x0b\x32\x33.rv.data.ControlTransport.TogglePlaybackControlTypeH\x00\x12\x46\n\x0bset_effects\x18\x14 \x01(\x0b\x32/.rv.data.ControlTransport.SetEffectsControlTypeH\x00\x12J\n\rupdate_effect\x18\x15 \x01(\x0b\x32\x31.rv.data.ControlTransport.UpdateEffectControlTypeH\x00\x12\x46\n\x0b\x62\x65gin_scrub\x18\x16 \x01(\x0b\x32/.rv.data.ControlTransport.BeginScrubControlTypeH\x00\x12\x42\n\tend_scrub\x18\x17 \x01(\x0b\x32-.rv.data.ControlTransport.EndScrubControlTypeH\x00\x12I\n\rscrub_to_time\x18\x18 \x01(\x0b\x32\x30.rv.data.ControlTransport.ScrubToTimeControlTypeH\x00\x12O\n\x10scrub_to_percent\x18\x19 \x01(\x0b\x32\x33.rv.data.ControlTransport.ScrubToPercentControlTypeH\x00\x12\x44\n\x0eset_audio_fade\x18\x1a \x01(\x0b\x32*.rv.data.ControlTransport.SetAudioFadeTypeH\x00\x12P\n\x14set_audio_properties\x18\x1b \x01(\x0b\x32\x30.rv.data.ControlTransport.SetAudioPropertiesTypeH\x00\x12K\n\x0eset_alpha_type\x18\x1c \x01(\x0b\x32\x31.rv.data.ControlTransport.SetAlphaTypeControlTypeH\x00\x1a\x11\n\x0fPlayControlType\x1a\x12\n\x10PauseControlType\x1a\x13\n\x11RewindControlType\x1a\x18\n\x16\x46\x61stForwardControlType\x1a%\n\x13SkipBackControlType\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x1a(\n\x16SkipForwardControlType\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x1a\x15\n\x13StepBackControlType\x1a\x18\n\x16StepForwardControlType\x1a&\n\x14GoToStartControlType\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x1a$\n\x12GoToEndControlType\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x1a%\n\x15JumpToTimeControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a+\n\x18JumpToPercentControlType\x12\x0f\n\x07percent\x18\x01 \x01(\x01\x1a&\n\x16MarkInPointControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a\'\n\x17MarkOutPointControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a\x86\x05\n\x17SetScaleModeControlType\x12M\n\x04mode\x18\x01 \x01(\x0e\x32?.rv.data.ControlTransport.SetScaleModeControlType.ScaleBehavior\x12\x12\n\nis_blurred\x18\x03 \x01(\x08\x12S\n\talignment\x18\x02 \x01(\x0e\x32@.rv.data.ControlTransport.SetScaleModeControlType.ScaleAlignment\"w\n\rScaleBehavior\x12\x16\n\x12SCALE_BEHAVIOR_FIT\x10\x00\x12\x17\n\x13SCALE_BEHAVIOR_FILL\x10\x01\x12\x1a\n\x16SCALE_BEHAVIOR_STRETCH\x10\x02\x12\x19\n\x15SCALE_BEHAVIOR_CUSTOM\x10\x03\"\xb9\x02\n\x0eScaleAlignment\x12!\n\x1dSCALE_ALIGNMENT_MIDDLE_CENTER\x10\x00\x12\x1c\n\x18SCALE_ALIGNMENT_TOP_LEFT\x10\x01\x12\x1e\n\x1aSCALE_ALIGNMENT_TOP_CENTER\x10\x02\x12\x1d\n\x19SCALE_ALIGNMENT_TOP_RIGHT\x10\x03\x12 \n\x1cSCALE_ALIGNMENT_MIDDLE_RIGHT\x10\x04\x12 \n\x1cSCALE_ALIGNMENT_BOTTOM_RIGHT\x10\x05\x12!\n\x1dSCALE_ALIGNMENT_BOTTOM_CENTER\x10\x06\x12\x1f\n\x1bSCALE_ALIGNMENT_BOTTOM_LEFT\x10\x07\x12\x1f\n\x1bSCALE_ALIGNMENT_MIDDLE_LEFT\x10\x08\x1a\x41\n\x19SetFlippedModeControlType\x12\x12\n\nhorizontal\x18\x01 \x01(\x08\x12\x10\n\x08vertical\x18\x02 \x01(\x08\x1a+\n\x16SetPlayRateControlType\x12\x11\n\tplay_rate\x18\x01 \x01(\x01\x1a\xac\x02\n\x1cSetNativeRotationControlType\x12[\n\x08rotation\x18\x01 \x01(\x0e\x32I.rv.data.ControlTransport.SetNativeRotationControlType.NativeRotationType\"\xae\x01\n\x12NativeRotationType\x12(\n$NATIVE_ROTATION_TYPE_ROTATE_STANDARD\x10\x00\x12\"\n\x1eNATIVE_ROTATION_TYPE_ROTATE_90\x10Z\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_180\x10\xb4\x01\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_270\x10\x8e\x02\x1a\xc6\x01\n\x17SetAlphaTypeControlType\x12O\n\nalpha_type\x18\x01 \x01(\x0e\x32;.rv.data.ControlTransport.SetAlphaTypeControlType.AlphaType\"Z\n\tAlphaType\x12\x16\n\x12\x41LPHA_TYPE_UNKNOWN\x10\x00\x12\x17\n\x13\x41LPHA_TYPE_STRAIGHT\x10\x01\x12\x1c\n\x18\x41LPHA_TYPE_PREMULTIPLIED\x10\x02\x1a\x1b\n\x19TogglePlaybackControlType\x1a\x39\n\x15SetEffectsControlType\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x01 \x03(\x0b\x32\x0f.rv.data.Effect\x1a:\n\x17UpdateEffectControlType\x12\x1f\n\x06\x65\x66\x66\x65\x63t\x18\x01 \x01(\x0b\x32\x0f.rv.data.Effect\x1a%\n\x15\x42\x65ginScrubControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a#\n\x13\x45ndScrubControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a&\n\x16ScrubToTimeControlType\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a,\n\x19ScrubToPercentControlType\x12\x0f\n\x07percent\x18\x01 \x01(\x01\x1ax\n\x10SetAudioFadeType\x12\x18\n\x10\x66\x61\x64\x65_in_duration\x18\x01 \x01(\x01\x12\x19\n\x11\x66\x61\x64\x65_out_duration\x18\x02 \x01(\x01\x12\x16\n\x0eshould_fade_in\x18\x03 \x01(\x08\x12\x17\n\x0fshould_fade_out\x18\x04 \x01(\x08\x1a`\n\x16SetAudioPropertiesType\x12\x38\n\x10\x61udio_properties\x18\x01 \x01(\x0b\x32\x1e.rv.data.Media.AudioProperties\x12\x0c\n\x04solo\x18\x02 \x03(\x08\x42\r\n\x0b\x43ontrolType\"Q\n\x12\x41udioInputSettings\x12#\n\x06inputs\x18\x01 \x03(\x0b\x32\x13.rv.data.AudioInput\x12\x16\n\x0etransitionTime\x18\x02 \x01(\x01\"9\n\x12VideoInputSettings\x12#\n\x06inputs\x18\x01 \x03(\x0b\x32\x13.rv.data.VideoInput\"\xb7\x02\n\rRecordRequest\x12)\n\x06stream\x18\x01 \x01(\x0b\x32\x19.rv.data.Recording.Stream\x12\'\n\x11working_directory\x18\x02 \x01(\x0b\x32\x0c.rv.data.URL\x12)\n\x04resi\x18\x03 \x01(\x0b\x32\x1b.rv.data.RecordRequest.Resi\x1a\xa6\x01\n\x04Resi\x12\x0b\n\x03gop\x18\x01 \x01(\r\x12\x13\n\x0bsegmentSize\x18\x02 \x01(\x01\x12\x1a\n\x12\x64\x65stinationGroupId\x18\x03 \x01(\t\x12\x0f\n\x07\x62ufSize\x18\x04 \x01(\r\x12\x0f\n\x07minRate\x18\x05 \x01(\r\x12\x0f\n\x07maxRate\x18\x06 \x01(\r\x12\x11\n\teventName\x18\x07 \x01(\t\x12\x1a\n\x12social_description\x18\x08 \x01(\t\"\x8b\x01\n\x12TextSegmentRequest\x12\x35\n\x08segments\x18\x01 \x03(\x0b\x32#.rv.data.TextSegmentRequest.Segment\x12\x16\n\x0estart_position\x18\x02 \x01(\x01\x1a&\n\x07Segment\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0c\n\x04size\x18\x02 \x01(\x01\"\xe0\x02\n\nTriggerCue\x12\x16\n\x0etrigger_handle\x18\x01 \x01(\x04\x12\x30\n\x0ftrigger_options\x18\x02 \x01(\x0b\x32\x17.rv.data.TriggerOptions\x12\x19\n\x03\x63ue\x18\x03 \x01(\x0b\x32\x0c.rv.data.Cue\x12\x39\n\x0cpresentation\x18\x04 \x01(\x0b\x32#.rv.data.TriggerCue.PresentationCue\x12#\n\x08playlist\x18\x05 \x01(\x0b\x32\x11.rv.data.Playlist\x12\x13\n\x0b\x63lient_data\x18\x06 \x01(\x04\x1ax\n\x0fPresentationCue\x12+\n\x0cpresentation\x18\x01 \x01(\x0b\x32\x15.rv.data.Presentation\x12%\n\x0e\x61rrangement_id\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x12\x11\n\tcue_index\x18\x03 \x01(\x05\"\xbc\x01\n\x16NetworkTriggerDataItem\x12\x30\n\x0ftrigger_options\x18\x03 \x01(\x0b\x32\x17.rv.data.TriggerOptions\x12(\n\x0btrigger_cue\x18\x04 \x01(\x0b\x32\x13.rv.data.TriggerCue\x12!\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x0f.rv.data.ActionH\x00\x12\x1b\n\x03\x63ue\x18\x02 \x01(\x0b\x32\x0c.rv.data.CueH\x00\x42\x06\n\x04Type\"\xef\x03\n\x1aSlideElementTextRenderInfo\x12\x39\n\x06layers\x18\x01 \x03(\x0b\x32).rv.data.SlideElementTextRenderInfo.Layer\x1a\x95\x03\n\x05Layer\x12G\n\nlayer_type\x18\x01 \x01(\x0e\x32\x33.rv.data.SlideElementTextRenderInfo.Layer.LayerType\x12\x18\n\x10text_build_index\x18\x05 \x01(\x05\x12\x39\n\x0c\x63ut_out_fill\x18\x02 \x01(\x0b\x32!.rv.data.Graphics.Text.CutOutFillH\x00\x12\x36\n\nmedia_fill\x18\x03 \x01(\x0b\x32 .rv.data.Graphics.Text.MediaFillH\x00\x12?\n\x11\x62\x61\x63kground_effect\x18\x04 \x01(\x0b\x32\".rv.data.Graphics.BackgroundEffectH\x00\"e\n\tLayerType\x12\x18\n\x14LAYER_TYPE_COMPOSITE\x10\x00\x12\x13\n\x0fLAYER_TYPE_MASK\x10\x01\x12\x13\n\x0fLAYER_TYPE_OVER\x10\x02\x12\x14\n\x10LAYER_TYPE_UNDER\x10\x03\x42\x0e\n\x0c\x41\x64vancedFill\"L\n\x16ValidateEncoderRequest\x12\x32\n\x07\x65ncoder\x18\x01 \x01(\x0b\x32!.rv.data.Recording.Stream.Encoder\"+\n\x17ValidateEncoderResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\"\xcb\x02\n\x14\x43\x61ptureActionRequest\x12=\n\nstart_resi\x18\x01 \x01(\x0b\x32\'.rv.data.CaptureActionRequest.StartResiH\x00\x12\x41\n\x0cstop_capture\x18\x02 \x01(\x0b\x32).rv.data.CaptureActionRequest.StopCaptureH\x00\x12\x34\n\x05\x65rror\x18\x03 \x01(\x0b\x32#.rv.data.CaptureActionRequest.ErrorH\x00\x1a\x0b\n\tStartResi\x1a\r\n\x0bStopCapture\x1aP\n\x05\x45rror\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x33\n\x0e\x63\x61pture_action\x18\x02 \x01(\x0b\x32\x1b.rv.data.Action.CaptureTypeB\r\n\x0bRequestType\"\xf8\x02\n\x15\x43\x61ptureActionResponse\x12>\n\nstart_resi\x18\x01 \x01(\x0b\x32(.rv.data.CaptureActionResponse.StartResiH\x00\x12\x42\n\x0cstop_capture\x18\x02 \x01(\x0b\x32*.rv.data.CaptureActionResponse.StopCaptureH\x00\x12S\n\x15\x63\x61ncel_capture_action\x18\x03 \x01(\x0b\x32\x32.rv.data.CaptureActionResponse.CancelCaptureActionH\x00\x1a\x15\n\x13\x43\x61ncelCaptureAction\x1a:\n\tStartResi\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x19\n\x11\x65vent_description\x18\x02 \x01(\t\x1a#\n\x0bStopCapture\x12\x14\n\x0cstop_capture\x18\x01 \x01(\x08\x42\x0e\n\x0cResponseType\"\xdb\x0b\n\nMacroIcons\x12,\n\x05icons\x18\x01 \x03(\x0b\x32\x1d.rv.data.MacroIcons.MacroIcon\x1a\x9e\x0b\n\tMacroIcon\x12;\n\nimage_type\x18\x01 \x01(\x0e\x32\'.rv.data.MacroIcons.MacroIcon.ImageType\x12\x12\n\nimage_data\x18\x02 \x01(\x0c\"\xbf\n\n\tImageType\x12\x14\n\x10ImageTypeDefault\x10\x00\x12\x10\n\x0cImageTypeOne\x10\x01\x12\x10\n\x0cImageTypeTwo\x10\x02\x12\x12\n\x0eImageTypeThree\x10\x03\x12\x11\n\rImageTypeFour\x10\x04\x12\x11\n\rImageTypeFive\x10\x05\x12\x10\n\x0cImageTypeSix\x10\x06\x12\x12\n\x0eImageTypeSeven\x10\x07\x12\x12\n\x0eImageTypeEight\x10\x08\x12\x11\n\rImageTypeNine\x10\t\x12\x11\n\rImageTypeZero\x10\n\x12\x12\n\x0eImageTypeArrow\x10\x0b\x12\x12\n\x0eImageTypeAudio\x10\x0c\x12\x11\n\rImageTypeBell\x10\r\x12\x11\n\rImageTypeBulb\x10\x0e\x12\x12\n\x0eImageTypeCloud\x10\x0f\x12\x14\n\x10ImageTypeCupcake\x10\x10\x12\x18\n\x14ImageTypeExclamation\x10\x11\x12\x12\n\x0eImageTypeFlask\x10\x12\x12\x13\n\x0fImageTypeFlower\x10\x13\x12\x14\n\x10ImageTypeGlasses\x10\x14\x12\x14\n\x10ImageTypeHashtag\x10\x15\x12\x10\n\x0cImageTypeHat\x10\x16\x12\x12\n\x0eImageTypeHeart\x10\x17\x12\x16\n\x12ImageTypeMegaphone\x10\x18\x12\x14\n\x10ImageTypeMessage\x10\x19\x12\x16\n\x12ImageTypePaperclip\x10\x1a\x12\x11\n\rImageTypePlay\x10\x1b\x12\x12\n\x0eImageTypeSlide\x10\x1c\x12\x11\n\rImageTypeStar\x10\x1d\x12\x10\n\x0cImageTypeSun\x10\x1e\x12\x17\n\x13ImageTypeSunglasses\x10\x1f\x12\x13\n\x0fImageTypeTarget\x10 \x12\x12\n\x0eImageTypeTimer\x10!\x12\x17\n\x13ImageTypeVideoInput\x10\"\x12\x13\n\x0fImageTypeXClear\x10#\x12\x14\n\x10ImageTypeLetterA\x10$\x12\x14\n\x10ImageTypeLetterB\x10%\x12\x14\n\x10ImageTypeLetterC\x10&\x12\x14\n\x10ImageTypeLetterD\x10\'\x12\x14\n\x10ImageTypeLetterE\x10(\x12\x14\n\x10ImageTypeLetterF\x10)\x12\x14\n\x10ImageTypeLetterG\x10*\x12\x14\n\x10ImageTypeLetterH\x10+\x12\x14\n\x10ImageTypeLetterI\x10,\x12\x14\n\x10ImageTypeLetterJ\x10-\x12\x14\n\x10ImageTypeLetterK\x10.\x12\x14\n\x10ImageTypeLetterL\x10/\x12\x14\n\x10ImageTypeLetterM\x10\x30\x12\x14\n\x10ImageTypeLetterN\x10\x31\x12\x14\n\x10ImageTypeLetterO\x10\x32\x12\x14\n\x10ImageTypeLetterP\x10\x33\x12\x14\n\x10ImageTypeLetterQ\x10\x34\x12\x14\n\x10ImageTypeLetterR\x10\x35\x12\x14\n\x10ImageTypeLetterS\x10\x36\x12\x14\n\x10ImageTypeLetterT\x10\x37\x12\x14\n\x10ImageTypeLetterU\x10\x38\x12\x14\n\x10ImageTypeLetterV\x10\x39\x12\x14\n\x10ImageTypeLetterW\x10:\x12\x14\n\x10ImageTypeLetterX\x10;\x12\x14\n\x10ImageTypeLetterY\x10<\x12\x14\n\x10ImageTypeLetterZ\x10=\x12\x13\n\x0fImageTypeCustom\x10>\"\x0e\n\x0cGenericEvent\"\x8c\x0e\n\x08SendData\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12\x33\n\tworkspace\x18\x02 \x01(\x0b\x32\x1e.rv.data.ProPresenterWorkspaceH\x00\x12\x31\n\x0estage_document\x18\x03 \x01(\x0b\x32\x17.rv.data.Stage.DocumentH\x00\x12\x32\n\x0ftimers_document\x18\x04 \x01(\x0b\x32\x17.rv.data.TimersDocumentH\x00\x12\x43\n\x18validate_encoder_request\x18\x05 \x01(\x0b\x32\x1f.rv.data.ValidateEncoderRequestH\x00\x12*\n\x0btrigger_cue\x18\x06 \x01(\x0b\x32\x13.rv.data.TriggerCueH\x00\x12:\n\x13\x64igital_audio_setup\x18\x07 \x01(\x0b\x32\x1b.rv.data.DigitalAudio.SetupH\x00\x12\x32\n\x0fmacros_document\x18\x08 \x01(\x0b\x32\x17.rv.data.MacrosDocumentH\x00\x12\x34\n\x10message_document\x18\t \x01(\x0b\x32\x18.rv.data.MessageDocumentH\x00\x12.\n\rprop_document\x18\n \x01(\x0b\x32\x15.rv.data.PropDocumentH\x00\x12.\n\rccli_document\x18\x0b \x01(\x0b\x32\x15.rv.data.CCLIDocumentH\x00\x12\x39\n\x0e\x61udience_looks\x18\x0c \x01(\x0b\x32\x1f.rv.data.AudienceLookCollectionH\x00\x12\x36\n\x12live_audience_look\x18\r \x01(\x0b\x32\x18.rv.data.ProAudienceLookH\x00\x12(\n\x05masks\x18\x0e \x01(\x0b\x32\x17.rv.data.MaskCollectionH\x00\x12J\n\x1brecording_settings_document\x18\x0f \x01(\x0b\x32#.rv.data.Recording.SettingsDocumentH\x00\x12\x41\n\x17\x63\x61pture_action_response\x18\x10 \x01(\x0b\x32\x1e.rv.data.CaptureActionResponseH\x00\x12\x34\n\x10\x63opyright_layout\x18\x11 \x01(\x0b\x32\x18.rv.data.CopyrightLayoutH\x00\x12;\n\x1cglobal_background_transition\x18\x12 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12\x39\n\x1aglobal_messages_transition\x18\x13 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12;\n\x1cglobal_foreground_transition\x18\x14 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12\x36\n\x17global_bible_transition\x18\x15 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12\x36\n\x17global_props_transition\x18\x16 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12\x36\n\x17global_audio_transition\x18\x17 \x01(\x0b\x32\x13.rv.data.TransitionH\x00\x12+\n\x0bpreferences\x18\x18 \x01(\x0b\x32\x14.rv.data.PreferencesH\x00\x12\x33\n\x0ctest_pattern\x18\x19 \x01(\x0b\x32\x1b.rv.data.TestPatternRequestH\x00\x12\x31\n\x10startup_complete\x18\x1a \x01(\x0b\x32\x15.rv.data.GenericEventH\x00\x12\x38\n\x13visual_playlist_doc\x18\x1b \x01(\x0b\x32\x19.rv.data.PlaylistDocumentH\x00\x12\x37\n\x12\x61udio_playlist_doc\x18\x1c \x01(\x0b\x32\x19.rv.data.PlaylistDocumentH\x00\x12.\n\rkill_watchdog\x18\x1d \x01(\x0b\x32\x15.rv.data.GenericEventH\x00\x12*\n\x0bmacro_icons\x18\x1e \x01(\x0b\x32\x13.rv.data.MacroIconsH\x00\x12\x38\n\x17\x64\x65\x62ug_trigger_data_dump\x18\x1f \x01(\x0b\x32\x15.rv.data.GenericEventH\x00\x12\x39\n\x14library_playlist_doc\x18  \x01(\x0b\x32\x19.rv.data.PlaylistDocumentH\x00\x12\x32\n\x19\x61udio_playlist_focus_uuid\x18! \x01(\x0b\x32\r.rv.data.UUIDH\x00\x42\r\n\x0bMessageType\"\xce\x02\n\x11TimerRuntimeState\x12!\n\ntimer_uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x12\n\ntimer_name\x18\x02 \x01(\t\x12.\n\x0b\x61\x63tion_type\x18\x03 \x01(\x0b\x32\x19.rv.data.Action.TimerType\x12\x12\n\nis_running\x18\x04 \x01(\x08\x12\x13\n\x0bhas_overrun\x18\x05 \x01(\x08\x12\x37\n\x05state\x18\x06 \x01(\x0e\x32(.rv.data.TimerRuntimeState.ResourceState\x12\x14\n\x0c\x63urrent_time\x18\x07 \x01(\x01\"Z\n\rResourceState\x12\x0e\n\nPREROLLING\x10\x00\x12\r\n\tACTIVATED\x10\x01\x12\x0b\n\x07UPDATED\x10\x02\x12\x0f\n\x0b\x44\x45\x41\x43TIVATED\x10\x03\x12\x0c\n\x08RELEASED\x10\x04\"\\\n\x10TimerStateUpdate\x12\x1d\n\x05timer\x18\x01 \x01(\x0b\x32\x0e.rv.data.Timer\x12)\n\x05state\x18\x02 \x01(\x0b\x32\x1a.rv.data.TimerRuntimeState\"\'\n\x10HandledException\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"<\n\x11\x43oreDataStateDump\x12\'\n\x06macros\x18\x01 \x01(\x0b\x32\x17.rv.data.MacrosDocument\"\x85\x04\n\x10SendDataResponse\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12\x45\n\x19validate_encoder_response\x18\x02 \x01(\x0b\x32 .rv.data.ValidateEncoderResponseH\x00\x12\x30\n\x0btimer_state\x18\x03 \x01(\x0b\x32\x19.rv.data.TimerStateUpdateH\x00\x12?\n\x16\x63\x61pture_action_request\x18\x04 \x01(\x0b\x32\x1d.rv.data.CaptureActionRequestH\x00\x12\x34\n\x0ctest_pattern\x18\x05 \x01(\x0b\x32\x1c.rv.data.TestPatternResponseH\x00\x12\x36\n\x11handled_exception\x18\x06 \x01(\x0b\x32\x19.rv.data.HandledExceptionH\x00\x12\x35\n\x0ftest_state_dump\x18\x07 \x01(\x0b\x32\x1a.rv.data.CoreDataStateDumpH\x00\x12\x32\n\x19\x61udio_playlist_focus_uuid\x18\x08 \x01(\x0b\x32\r.rv.data.UUIDH\x00\x12;\n\"audio_playlist_item_triggered_uuid\x18\t \x01(\x0b\x32\r.rv.data.UUIDH\x00\x42\r\n\x0bMessageType\"\xec\x0e\n\x1aTriggerTransferRenderState\x12\x1d\n\x05slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12\x15\n\rstage_message\x18\x02 \x01(\t\x12J\n\x12presentation_media\x18\x03 \x01(\x0b\x32..rv.data.TriggerTransferRenderState.MediaState\x12J\n\x12\x61nnouncement_media\x18\x04 \x01(\x0b\x32..rv.data.TriggerTransferRenderState.MediaState\x12\x43\n\x0b\x61udio_media\x18\x05 \x01(\x0b\x32..rv.data.TriggerTransferRenderState.MediaState\x12(\n\x10live_video_media\x18\x06 \x01(\x0b\x32\x0e.rv.data.Media\x12\x44\n\x0cpresentation\x18\x07 \x01(\x0b\x32..rv.data.TriggerTransferRenderState.SlideState\x12\x44\n\x0c\x61nnouncement\x18\x08 \x01(\x0b\x32..rv.data.TriggerTransferRenderState.SlideState\x12>\n\x06timers\x18\t \x03(\x0b\x32..rv.data.TriggerTransferRenderState.TimerState\x12\x41\n\x07\x63\x61pture\x18\n \x01(\x0b\x32\x30.rv.data.TriggerTransferRenderState.CaptureState\x12\x43\n\x08timecode\x18\x0b \x01(\x0b\x32\x31.rv.data.TriggerTransferRenderState.TimecodeState\x12\x13\n\x0bsystem_time\x18\x0c \x01(\x04\x1a\x63\n\nTimerState\x12\x1d\n\x05timer\x18\x01 \x01(\x0b\x32\x0e.rv.data.Timer\x12\x12\n\nis_running\x18\x02 \x01(\x08\x12\x13\n\x0bhas_overrun\x18\x03 \x01(\x08\x12\r\n\x05value\x18\x04 \x01(\x02\x1a\x81\x02\n\nMediaState\x12%\n\rcurrent_media\x18\x01 \x01(\x0b\x32\x0e.rv.data.Media\x12\x12\n\nis_playing\x18\x02 \x01(\x08\x12\x12\n\nis_looping\x18\x03 \x01(\x08\x12\x14\n\x0c\x63urrent_time\x18\x04 \x01(\x02\x12\x16\n\x0etime_remaining\x18\x05 \x01(\x02\x12$\n\rplaylist_uuid\x18\x06 \x01(\x0b\x32\r.rv.data.UUID\x12\x15\n\rplaylist_name\x18\x07 \x01(\t\x12\x39\n\x07markers\x18\x08 \x03(\x0b\x32(.rv.data.Action.MediaType.PlaybackMarker\x1a\xa0\x01\n\x0c\x43\x61ptureState\x12G\n\x06status\x18\x01 \x01(\x0e\x32\x37.rv.data.TriggerTransferRenderState.CaptureState.Status\x12\x0c\n\x04time\x18\x02 \x01(\x02\"9\n\x06Status\x12\x0b\n\x07Stopped\x10\x00\x12\n\n\x06\x41\x63tive\x10\x01\x12\x0b\n\x07\x43\x61ution\x10\x02\x12\t\n\x05\x45rror\x10\x03\x1a:\n\x10\x41utoAdvanceState\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x16\n\x0eremaining_time\x18\x02 \x01(\x02\x1aO\n\rTimelineState\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x02\x12\x18\n\x10last_slide_index\x18\x03 \x01(\x05\x1a\xf5\x02\n\nSlideState\x12+\n\x0cpresentation\x18\x01 \x01(\x0b\x32\x15.rv.data.Presentation\x12#\n\x08playlist\x18\x02 \x01(\x0b\x32\x11.rv.data.Playlist\x12\"\n\x0b\x63urrent_cue\x18\x03 \x01(\x0b\x32\r.rv.data.UUID\x12\x1f\n\x08next_cue\x18\x04 \x01(\x0b\x32\r.rv.data.UUID\x12J\n\x0c\x61uto_advance\x18\x05 \x01(\x0b\x32\x34.rv.data.TriggerTransferRenderState.AutoAdvanceState\x12I\n\x0etimeline_state\x18\x06 \x01(\x0b\x32\x31.rv.data.TriggerTransferRenderState.TimelineState\x12\x19\n\x11\x63urrent_cue_index\x18\x07 \x01(\x05\x12\x1e\n\x16\x63urrent_playlist_index\x18\x08 \x01(\x05\x1a\x96\x01\n\rTimecodeState\x12H\n\x06status\x18\x01 \x01(\x0e\x32\x38.rv.data.TriggerTransferRenderState.TimecodeState.Status\x12\x0c\n\x04time\x18\x02 \x01(\x02\"-\n\x06Status\x12\x0b\n\x07Stopped\x10\x00\x12\x0b\n\x07Playing\x10\x01\x12\t\n\x05\x45rror\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proCore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MEDIAMETADATAREQUESTINFO']._serialized_start=460
  _globals['_MEDIAMETADATAREQUESTINFO']._serialized_end=1106
  _globals['_MEDIAMETADATAREQUESTINFO_NATIVEROTATIONTYPE']._serialized_start=840
  _globals['_MEDIAMETADATAREQUESTINFO_NATIVEROTATIONTYPE']._serialized_end=1014
  _globals['_MEDIAMETADATAREQUESTINFO_ALPHATYPE']._serialized_start=1016
  _globals['_MEDIAMETADATAREQUESTINFO_ALPHATYPE']._serialized_end=1106
  _globals['_MEDIAMETADATAREQUESTRESPONSE']._serialized_start=1109
  _globals['_MEDIAMETADATAREQUESTRESPONSE']._serialized_end=1723
  _globals['_MEDIAMETADATAREQUESTRESPONSE_METADATA']._serialized_start=1289
  _globals['_MEDIAMETADATAREQUESTRESPONSE_METADATA']._serialized_end=1678
  _globals['_MEDIAMETADATAREQUESTRESPONSE_METADATA_CONTENTTYPE']._serialized_start=1567
  _globals['_MEDIAMETADATAREQUESTRESPONSE_METADATA_CONTENTTYPE']._serialized_end=1678
  _globals['_MEDIAMETADATAREQUESTRESPONSE_BITMAPINFO']._serialized_start=1680
  _globals['_MEDIAMETADATAREQUESTRESPONSE_BITMAPINFO']._serialized_end=1723
  _globals['_NETWORKIDENTIFIER']._serialized_start=1726
  _globals['_NETWORKIDENTIFIER']._serialized_end=1867
  _globals['_NETWORKIDENTIFIER_INDEXORNAME']._serialized_start=1808
  _globals['_NETWORKIDENTIFIER_INDEXORNAME']._serialized_end=1867
  _globals['_TRIGGEROPTIONS']._serialized_start=1870
  _globals['_TRIGGEROPTIONS']._serialized_end=2414
  _globals['_TRIGGEROPTIONS_CONTENTDESTINATION']._serialized_start=2323
  _globals['_TRIGGEROPTIONS_CONTENTDESTINATION']._serialized_end=2414
  _globals['_CONTROLTRANSPORT']._serialized_start=2417
  _globals['_CONTROLTRANSPORT']._serialized_end=6740
  _globals['_CONTROLTRANSPORT_PLAYCONTROLTYPE']._serialized_start=4473
  _globals['_CONTROLTRANSPORT_PLAYCONTROLTYPE']._serialized_end=4490
  _globals['_CONTROLTRANSPORT_PAUSECONTROLTYPE']._serialized_start=4492
  _globals['_CONTROLTRANSPORT_PAUSECONTROLTYPE']._serialized_end=4510
  _globals['_CONTROLTRANSPORT_REWINDCONTROLTYPE']._serialized_start=4512
  _globals['_CONTROLTRANSPORT_REWINDCONTROLTYPE']._serialized_end=4531
  _globals['_CONTROLTRANSPORT_FASTFORWARDCONTROLTYPE']._serialized_start=4533
  _globals['_CONTROLTRANSPORT_FASTFORWARDCONTROLTYPE']._serialized_end=4557
  _globals['_CONTROLTRANSPORT_SKIPBACKCONTROLTYPE']._serialized_start=4559
  _globals['_CONTROLTRANSPORT_SKIPBACKCONTROLTYPE']._serialized_end=4596
  _globals['_CONTROLTRANSPORT_SKIPFORWARDCONTROLTYPE']._serialized_start=4598
  _globals['_CONTROLTRANSPORT_SKIPFORWARDCONTROLTYPE']._serialized_end=4638
  _globals['_CONTROLTRANSPORT_STEPBACKCONTROLTYPE']._serialized_start=4640
  _globals['_CONTROLTRANSPORT_STEPBACKCONTROLTYPE']._serialized_end=4661
  _globals['_CONTROLTRANSPORT_STEPFORWARDCONTROLTYPE']._serialized_start=4663
  _globals['_CONTROLTRANSPORT_STEPFORWARDCONTROLTYPE']._serialized_end=4687
  _globals['_CONTROLTRANSPORT_GOTOSTARTCONTROLTYPE']._serialized_start=4689
  _globals['_CONTROLTRANSPORT_GOTOSTARTCONTROLTYPE']._serialized_end=4727
  _globals['_CONTROLTRANSPORT_GOTOENDCONTROLTYPE']._serialized_start=4729
  _globals['_CONTROLTRANSPORT_GOTOENDCONTROLTYPE']._serialized_end=4765
  _globals['_CONTROLTRANSPORT_JUMPTOTIMECONTROLTYPE']._serialized_start=4767
  _globals['_CONTROLTRANSPORT_JUMPTOTIMECONTROLTYPE']._serialized_end=4804
  _globals['_CONTROLTRANSPORT_JUMPTOPERCENTCONTROLTYPE']._serialized_start=4806
  _globals['_CONTROLTRANSPORT_JUMPTOPERCENTCONTROLTYPE']._serialized_end=4849
  _globals['_CONTROLTRANSPORT_MARKINPOINTCONTROLTYPE']._serialized_start=4851
  _globals['_CONTROLTRANSPORT_MARKINPOINTCONTROLTYPE']._serialized_end=4889
  _globals['_CONTROLTRANSPORT_MARKOUTPOINTCONTROLTYPE']._serialized_start=4891
  _globals['_CONTROLTRANSPORT_MARKOUTPOINTCONTROLTYPE']._serialized_end=4930
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE']._serialized_start=4933
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE']._serialized_end=5579
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE_SCALEBEHAVIOR']._serialized_start=5144
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE_SCALEBEHAVIOR']._serialized_end=5263
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE_SCALEALIGNMENT']._serialized_start=5266
  _globals['_CONTROLTRANSPORT_SETSCALEMODECONTROLTYPE_SCALEALIGNMENT']._serialized_end=5579
  _globals['_CONTROLTRANSPORT_SETFLIPPEDMODECONTROLTYPE']._serialized_start=5581
  _globals['_CONTROLTRANSPORT_SETFLIPPEDMODECONTROLTYPE']._serialized_end=5646
  _globals['_CONTROLTRANSPORT_SETPLAYRATECONTROLTYPE']._serialized_start=5648
  _globals['_CONTROLTRANSPORT_SETPLAYRATECONTROLTYPE']._serialized_end=5691
  _globals['_CONTROLTRANSPORT_SETNATIVEROTATIONCONTROLTYPE']._serialized_start=5694
  _globals['_CONTROLTRANSPORT_SETNATIVEROTATIONCONTROLTYPE']._serialized_end=5994
  _globals['_CONTROLTRANSPORT_SETNATIVEROTATIONCONTROLTYPE_NATIVEROTATIONTYPE']._serialized_start=840
  _globals['_CONTROLTRANSPORT_SETNATIVEROTATIONCONTROLTYPE_NATIVEROTATIONTYPE']._serialized_end=1014
  _globals['_CONTROLTRANSPORT_SETALPHATYPECONTROLTYPE']._serialized_start=5997
  _globals['_CONTROLTRANSPORT_SETALPHATYPECONTROLTYPE']._serialized_end=6195
  _globals['_CONTROLTRANSPORT_SETALPHATYPECONTROLTYPE_ALPHATYPE']._serialized_start=1016
  _globals['_CONTROLTRANSPORT_SETALPHATYPECONTROLTYPE_ALPHATYPE']._serialized_end=1106
  _globals['_CONTROLTRANSPORT_TOGGLEPLAYBACKCONTROLTYPE']._serialized_start=6197
  _globals['_CONTROLTRANSPORT_TOGGLEPLAYBACKCONTROLTYPE']._serialized_end=6224
  _globals['_CONTROLTRANSPORT_SETEFFECTSCONTROLTYPE']._serialized_start=6226
  _globals['_CONTROLTRANSPORT_SETEFFECTSCONTROLTYPE']._serialized_end=6283
  _globals['_CONTROLTRANSPORT_UPDATEEFFECTCONTROLTYPE']._serialized_start=6285
  _globals['_CONTROLTRANSPORT_UPDATEEFFECTCONTROLTYPE']._serialized_end=6343
  _globals['_CONTROLTRANSPORT_BEGINSCRUBCONTROLTYPE']._serialized_start=6345
  _globals['_CONTROLTRANSPORT_BEGINSCRUBCONTROLTYPE']._serialized_end=6382
  _globals['_CONTROLTRANSPORT_ENDSCRUBCONTROLTYPE']._serialized_start=6384
  _globals['_CONTROLTRANSPORT_ENDSCRUBCONTROLTYPE']._serialized_end=6419
  _globals['_CONTROLTRANSPORT_SCRUBTOTIMECONTROLTYPE']._serialized_start=6421
  _globals['_CONTROLTRANSPORT_SCRUBTOTIMECONTROLTYPE']._serialized_end=6459
  _globals['_CONTROLTRANSPORT_SCRUBTOPERCENTCONTROLTYPE']._serialized_start=6461
  _globals['_CONTROLTRANSPORT_SCRUBTOPERCENTCONTROLTYPE']._serialized_end=6505
  _globals['_CONTROLTRANSPORT_SETAUDIOFADETYPE']._serialized_start=6507
  _globals['_CONTROLTRANSPORT_SETAUDIOFADETYPE']._serialized_end=6627
  _globals['_CONTROLTRANSPORT_SETAUDIOPROPERTIESTYPE']._serialized_start=6629
  _globals['_CONTROLTRANSPORT_SETAUDIOPROPERTIESTYPE']._serialized_end=6725
  _globals['_AUDIOINPUTSETTINGS']._serialized_start=6742
  _globals['_AUDIOINPUTSETTINGS']._serialized_end=6823
  _globals['_VIDEOINPUTSETTINGS']._serialized_start=6825
  _globals['_VIDEOINPUTSETTINGS']._serialized_end=6882
  _globals['_RECORDREQUEST']._serialized_start=6885
  _globals['_RECORDREQUEST']._serialized_end=7196
  _globals['_RECORDREQUEST_RESI']._serialized_start=7030
  _globals['_RECORDREQUEST_RESI']._serialized_end=7196
  _globals['_TEXTSEGMENTREQUEST']._serialized_start=7199
  _globals['_TEXTSEGMENTREQUEST']._serialized_end=7338
  _globals['_TEXTSEGMENTREQUEST_SEGMENT']._serialized_start=7300
  _globals['_TEXTSEGMENTREQUEST_SEGMENT']._serialized_end=7338
  _globals['_TRIGGERCUE']._serialized_start=7341
  _globals['_TRIGGERCUE']._serialized_end=7693
  _globals['_TRIGGERCUE_PRESENTATIONCUE']._serialized_start=7573
  _globals['_TRIGGERCUE_PRESENTATIONCUE']._serialized_end=7693
  _globals['_NETWORKTRIGGERDATAITEM']._serialized_start=7696
  _globals['_NETWORKTRIGGERDATAITEM']._serialized_end=7884
  _globals['_SLIDEELEMENTTEXTRENDERINFO']._serialized_start=7887
  _globals['_SLIDEELEMENTTEXTRENDERINFO']._serialized_end=8382
  _globals['_SLIDEELEMENTTEXTRENDERINFO_LAYER']._serialized_start=7977
  _globals['_SLIDEELEMENTTEXTRENDERINFO_LAYER']._serialized_end=8382
  _globals['_SLIDEELEMENTTEXTRENDERINFO_LAYER_LAYERTYPE']._serialized_start=8265
  _globals['_SLIDEELEMENTTEXTRENDERINFO_LAYER_LAYERTYPE']._serialized_end=8366
  _globals['_VALIDATEENCODERREQUEST']._serialized_start=8384
  _globals['_VALIDATEENCODERREQUEST']._serialized_end=8460
  _globals['_VALIDATEENCODERRESPONSE']._serialized_start=8462
  _globals['_VALIDATEENCODERRESPONSE']._serialized_end=8505
  _globals['_CAPTUREACTIONREQUEST']._serialized_start=8508
  _globals['_CAPTUREACTIONREQUEST']._serialized_end=8839
  _globals['_CAPTUREACTIONREQUEST_STARTRESI']._serialized_start=8716
  _globals['_CAPTUREACTIONREQUEST_STARTRESI']._serialized_end=8727
  _globals['_CAPTUREACTIONREQUEST_STOPCAPTURE']._serialized_start=8729
  _globals['_CAPTUREACTIONREQUEST_STOPCAPTURE']._serialized_end=8742
  _globals['_CAPTUREACTIONREQUEST_ERROR']._serialized_start=8744
  _globals['_CAPTUREACTIONREQUEST_ERROR']._serialized_end=8824
  _globals['_CAPTUREACTIONRESPONSE']._serialized_start=8842
  _globals['_CAPTUREACTIONRESPONSE']._serialized_end=9218
  _globals['_CAPTUREACTIONRESPONSE_CANCELCAPTUREACTION']._serialized_start=9084
  _globals['_CAPTUREACTIONRESPONSE_CANCELCAPTUREACTION']._serialized_end=9105
  _globals['_CAPTUREACTIONRESPONSE_STARTRESI']._serialized_start=9107
  _globals['_CAPTUREACTIONRESPONSE_STARTRESI']._serialized_end=9165
  _globals['_CAPTUREACTIONRESPONSE_STOPCAPTURE']._serialized_start=9167
  _globals['_CAPTUREACTIONRESPONSE_STOPCAPTURE']._serialized_end=9202
  _globals['_MACROICONS']._serialized_start=9221
  _globals['_MACROICONS']._serialized_end=10720
  _globals['_MACROICONS_MACROICON']._serialized_start=9282
  _globals['_MACROICONS_MACROICON']._serialized_end=10720
  _globals['_MACROICONS_MACROICON_IMAGETYPE']._serialized_start=9377
  _globals['_MACROICONS_MACROICON_IMAGETYPE']._serialized_end=10720
  _globals['_GENERICEVENT']._serialized_start=10722
  _globals['_GENERICEVENT']._serialized_end=10736
  _globals['_SENDDATA']._serialized_start=10739
  _globals['_SENDDATA']._serialized_end=12543
  _globals['_TIMERRUNTIMESTATE']._serialized_start=12546
  _globals['_TIMERRUNTIMESTATE']._serialized_end=12880
  _globals['_TIMERRUNTIMESTATE_RESOURCESTATE']._serialized_start=12790
  _globals['_TIMERRUNTIMESTATE_RESOURCESTATE']._serialized_end=12880
  _globals['_TIMERSTATEUPDATE']._serialized_start=12882
  _globals['_TIMERSTATEUPDATE']._serialized_end=12974
  _globals['_HANDLEDEXCEPTION']._serialized_start=12976
  _globals['_HANDLEDEXCEPTION']._serialized_end=13015
  _globals['_COREDATASTATEDUMP']._serialized_start=13017
  _globals['_COREDATASTATEDUMP']._serialized_end=13077
  _globals['_SENDDATARESPONSE']._serialized_start=13080
  _globals['_SENDDATARESPONSE']._serialized_end=13597
  _globals['_TRIGGERTRANSFERRENDERSTATE']._serialized_start=13600
  _globals['_TRIGGERTRANSFERRENDERSTATE']._serialized_end=15500
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMERSTATE']._serialized_start=14308
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMERSTATE']._serialized_end=14407
  _globals['_TRIGGERTRANSFERRENDERSTATE_MEDIASTATE']._serialized_start=14410
  _globals['_TRIGGERTRANSFERRENDERSTATE_MEDIASTATE']._serialized_end=14667
  _globals['_TRIGGERTRANSFERRENDERSTATE_CAPTURESTATE']._serialized_start=14670
  _globals['_TRIGGERTRANSFERRENDERSTATE_CAPTURESTATE']._serialized_end=14830
  _globals['_TRIGGERTRANSFERRENDERSTATE_CAPTURESTATE_STATUS']._serialized_start=14773
  _globals['_TRIGGERTRANSFERRENDERSTATE_CAPTURESTATE_STATUS']._serialized_end=14830
  _globals['_TRIGGERTRANSFERRENDERSTATE_AUTOADVANCESTATE']._serialized_start=14832
  _globals['_TRIGGERTRANSFERRENDERSTATE_AUTOADVANCESTATE']._serialized_end=14890
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMELINESTATE']._serialized_start=14892
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMELINESTATE']._serialized_end=14971
  _globals['_TRIGGERTRANSFERRENDERSTATE_SLIDESTATE']._serialized_start=14974
  _globals['_TRIGGERTRANSFERRENDERSTATE_SLIDESTATE']._serialized_end=15347
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMECODESTATE']._serialized_start=15350
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMECODESTATE']._serialized_end=15500
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMECODESTATE_STATUS']._serialized_start=15455
  _globals['_TRIGGERTRANSFERRENDERSTATE_TIMECODESTATE_STATUS']._serialized_end=15500
# @@protoc_insertion_point(module_scope)
