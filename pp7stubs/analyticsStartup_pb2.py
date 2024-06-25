# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analyticsStartup.proto
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
    'analyticsStartup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import analyticsMultiTracks_pb2 as analyticsMultiTracks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61nalyticsStartup.proto\x12\x0crv.analytics\x1a\x1a\x61nalyticsMultiTracks.proto\"\xf8=\n\x07Startup\x12,\n\x05looks\x18\x01 \x01(\x0b\x32\x1b.rv.analytics.Startup.LooksH\x00\x12I\n\x14screen_configuration\x18\x02 \x01(\x0b\x32).rv.analytics.Startup.ScreenConfigurationH\x00\x12\x38\n\x0bpreferences\x18\x03 \x01(\x0b\x32!.rv.analytics.Startup.PreferencesH\x00\x12\x30\n\x07screens\x18\x04 \x01(\x0b\x32\x1d.rv.analytics.Startup.ScreensH\x00\x12?\n\x0fplanning_center\x18\x05 \x01(\x0b\x32$.rv.analytics.Startup.PlanningCenterH\x00\x12\x37\n\x0bsong_select\x18\x06 \x01(\x0b\x32 .rv.analytics.Startup.SongSelectH\x00\x12,\n\x05\x61udio\x18\x07 \x01(\x0b\x32\x1b.rv.analytics.Startup.AudioH\x00\x12>\n\x0e\x63ommunications\x18\x08 \x01(\x0b\x32$.rv.analytics.Startup.CommunicationsH\x00\x12*\n\x04resi\x18\t \x01(\x0b\x32\x1a.rv.analytics.Startup.ResiH\x00\x12\x34\n\tinterface\x18\n \x01(\x0b\x32\x1f.rv.analytics.Startup.InterfaceH\x00\x12\x30\n\x07\x63ontent\x18\x0b \x01(\x0b\x32\x1d.rv.analytics.Startup.ContentH\x00\x12.\n\x06themes\x18\x0c \x01(\x0b\x32\x1c.rv.analytics.Startup.ThemesH\x00\x12,\n\x05macro\x18\r \x01(\x0b\x32\x1b.rv.analytics.Startup.MacroH\x00\x12\x37\n\x0b\x63lear_group\x18\x0e \x01(\x0b\x32 .rv.analytics.Startup.ClearGroupH\x00\x12\x37\n\x0bkey_mapping\x18\x0f \x01(\x0b\x32 .rv.analytics.Startup.KeyMappingH\x00\x12\x38\n\x0bmultitracks\x18\x10 \x01(\x0b\x32!.rv.analytics.MultiTracks.StartupH\x00\x12\x39\n\x0cnetwork_link\x18\x11 \x01(\x0b\x32!.rv.analytics.Startup.NetworkLinkH\x00\x12\x30\n\x07\x63\x61pture\x18\x12 \x01(\x0b\x32\x1d.rv.analytics.Startup.CaptureH\x00\x1a\x1f\n\x05Looks\x12\x16\n\x0enumber_presets\x18\x01 \x01(\x05\x1a\x88\x13\n\x13ScreenConfiguration\x12\x44\n\x07summary\x18\x01 \x01(\x0b\x32\x31.rv.analytics.Startup.ScreenConfiguration.SummaryH\x00\x12\x42\n\x06output\x18\x02 \x01(\x0b\x32\x30.rv.analytics.Startup.ScreenConfiguration.OutputH\x00\x12\x42\n\x06single\x18\x03 \x01(\x0b\x32\x30.rv.analytics.Startup.ScreenConfiguration.SingleH\x00\x12\x46\n\x08mirrored\x18\x04 \x01(\x0b\x32\x32.rv.analytics.Startup.ScreenConfiguration.MirroredH\x00\x12I\n\nedge_blend\x18\x05 \x01(\x0b\x32\x33.rv.analytics.Startup.ScreenConfiguration.EdgeBlendH\x00\x12\x44\n\x07grouped\x18\x06 \x01(\x0b\x32\x31.rv.analytics.Startup.ScreenConfiguration.GroupedH\x00\x1a[\n\x07Summary\x12\x15\n\rtotal_screens\x18\x01 \x01(\x05\x12\x1d\n\x15\x61udience_screen_count\x18\x02 \x01(\x05\x12\x1a\n\x12stage_screen_count\x18\x03 \x01(\x05\x1a\x82\x07\n\x06Output\x12V\n\x0eproscreen_type\x18\x01 \x01(\x0e\x32>.rv.analytics.Startup.ScreenConfiguration.Output.ProScreenType\x12P\n\x0boutput_type\x18\x02 \x01(\x0e\x32;.rv.analytics.Startup.ScreenConfiguration.Output.OutputType\x12 \n\x18\x63olor_correction_enabled\x18\x03 \x01(\x08\x12\x1a\n\x12\x63orner_pin_enabled\x18\x04 \x01(\x08\x12M\n\talignment\x18\x06 \x01(\x0e\x32:.rv.analytics.Startup.ScreenConfiguration.Output.Alignment\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x0e\n\x06height\x18\x08 \x01(\x05\x12@\n\x06screen\x18\t \x01(\x0b\x32\x30.rv.analytics.Startup.ScreenConfiguration.Screen\"\xa3\x01\n\rProScreenType\x12\x1b\n\x17PRO_SCREEN_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16PRO_SCREEN_TYPE_SINGLE\x10\x01\x12\x1c\n\x18PRO_SCREEN_TYPE_MIRRORED\x10\x02\x12\x1e\n\x1aPRO_SCREEN_TYPE_EDGE_BLEND\x10\x03\x12\x1b\n\x17PRO_SCREEN_TYPE_GROUPED\x10\x04\"\xb1\x01\n\nOutputType\x12\x17\n\x13OUTPUT_TYPE_UNKNOWN\x10\x00\x12\x13\n\x0fOUTPUT_TYPE_SDI\x10\x01\x12\x13\n\x0fOUTPUT_TYPE_NDI\x10\x02\x12\x16\n\x12OUTPUT_TYPE_SYPHON\x10\x03\x12\x16\n\x12OUTPUT_TYPE_SYSTEM\x10\x04\x12\x1b\n\x17OUTPUT_TYPE_PLACEHOLDER\x10\x05\x12\x13\n\x0fOUTPUT_TYPE_DVI\x10\x06\"\x85\x01\n\tAlignment\x12\x15\n\x11\x41LIGNMENT_UNKNOWN\x10\x00\x12\x12\n\x0e\x41LIGNMENT_FULL\x10\x01\x12\x11\n\rALIGNMENT_2X1\x10\x02\x12\x11\n\rALIGNMENT_3X1\x10\x03\x12\x11\n\rALIGNMENT_2X2\x10\x04\x12\x14\n\x10\x41LIGNMENT_CUSTOM\x10\x05\x1aq\n\x06Single\x12I\n\x0bscreen_type\x18\x01 \x01(\x0e\x32\x34.rv.analytics.Startup.ScreenConfiguration.ScreenType\x12\x1c\n\x14screen_color_enabled\x18\x02 \x01(\x08\x1a\x82\x01\n\x08Mirrored\x12I\n\x0bscreen_type\x18\x01 \x01(\x0e\x32\x34.rv.analytics.Startup.ScreenConfiguration.ScreenType\x12\x1c\n\x14screen_color_enabled\x18\x02 \x01(\x08\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x1a\x83\x01\n\tEdgeBlend\x12I\n\x0bscreen_type\x18\x01 \x01(\x0e\x32\x34.rv.analytics.Startup.ScreenConfiguration.ScreenType\x12\x1c\n\x14screen_color_enabled\x18\x02 \x01(\x08\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x1a\x91\x01\n\x07Grouped\x12I\n\x0bscreen_type\x18\x01 \x01(\x0e\x32\x34.rv.analytics.Startup.ScreenConfiguration.ScreenType\x12\x1c\n\x14screen_color_enabled\x18\x02 \x01(\x08\x12\x0f\n\x07\x63olumns\x18\x03 \x01(\x05\x12\x0c\n\x04rows\x18\x04 \x01(\x05\x1a\xf0\x02\n\x06Screen\x12U\n\x0e\x61lpha_key_mode\x18\x01 \x01(\x0e\x32=.rv.analytics.Startup.ScreenConfiguration.Screen.AlphaKeyMode\x12R\n\x0c\x61lpha_device\x18\x02 \x01(\x0e\x32<.rv.analytics.Startup.ScreenConfiguration.Screen.AlphaDevice\"f\n\x0c\x41lphaKeyMode\x12\x17\n\x13\x41LPHA_KEY_MODE_NONE\x10\x00\x12 \n\x1c\x41LPHA_KEY_MODE_PREMULTIPLIED\x10\x01\x12\x1b\n\x17\x41LPHA_KEY_MODE_STRAIGHT\x10\x02\"S\n\x0b\x41lphaDevice\x12\x15\n\x11\x41LPHA_DEVICE_NONE\x10\x00\x12\x15\n\x11\x41LPHA_DEVICE_SELF\x10\x01\x12\x16\n\x12\x41LPHA_DEVICE_OTHER\x10\x02\"V\n\nScreenType\x12\x17\n\x13SCREEN_TYPE_UNKNOWN\x10\x00\x12\x18\n\x14SCREEN_TYPE_AUDIENCE\x10\x01\x12\x15\n\x11SCREEN_TYPE_STAGE\x10\x02\x42\x0b\n\tComponent\x1a\xa9\x06\n\x0bPreferences\x12\x18\n\x10house_of_worship\x18\x01 \x01(\x08\x12\x17\n\x0fhas_custom_logo\x18\x02 \x01(\x08\x12\x19\n\x11\x63opyright_enabled\x18\x03 \x01(\x08\x12I\n\x0f\x63opyright_style\x18\x04 \x01(\x0e\x32\x30.rv.analytics.Startup.Preferences.CopyrightStyle\x12\x1d\n\x15\x63opyright_has_license\x18\x05 \x01(\x08\x12\x41\n\x0brender_mode\x18\x06 \x01(\x0e\x32,.rv.analytics.Startup.Preferences.RenderMode\x12\x1b\n\x13suppress_auto_start\x18\x07 \x01(\x08\x12\"\n\x1amanage_media_automatically\x18\x08 \x01(\x08\x12\x1b\n\x13search_paths_relink\x18\t \x01(\x08\x12G\n\x0eupdate_channel\x18\n \x01(\x0e\x32/.rv.analytics.Startup.Preferences.UpdateChannel\"\xa6\x01\n\x0e\x43opyrightStyle\x12\x1b\n\x17\x43OPYRIGHT_STYLE_UNKNOWN\x10\x00\x12\x19\n\x15\x43OPYRIGHT_STYLE_FIRST\x10\x01\x12\x18\n\x14\x43OPYRIGHT_STYLE_LAST\x10\x02\x12\"\n\x1e\x43OPYRIGHT_STYLE_FIRST_AND_LAST\x10\x03\x12\x1e\n\x1a\x43OPYRIGHT_STYLE_ALL_SLIDES\x10\x04\"m\n\nRenderMode\x12\x17\n\x13RENDER_MODE_UNKNOWN\x10\x00\x12\x16\n\x12RENDER_MODE_OPENGL\x10\x01\x12\x15\n\x11RENDER_MODE_METAL\x10\x02\x12\x17\n\x13RENDER_MODE_DIRECTX\x10\x03\"`\n\rUpdateChannel\x12\x1a\n\x16UPDATE_CHANNEL_UNKNOWN\x10\x00\x12\x1a\n\x16UPDATE_CHANNEL_RELEASE\x10\x01\x12\x17\n\x13UPDATE_CHANNEL_BETA\x10\x02\x1a\x8e\x01\n\x07Screens\x12\x1b\n\x13show_screens_launch\x18\x01 \x01(\x08\x12\"\n\x1ashow_performance_on_screen\x18\x02 \x01(\x08\x12 \n\x18ignore_background_colors\x18\x03 \x01(\x08\x12 \n\x18show_keynote_ppt_screens\x18\x04 \x01(\x08\x1a\xaa\x01\n\x0ePlanningCenter\x12\x11\n\tlogged_in\x18\x01 \x01(\x08\x12\x13\n\x0b\x61uto_update\x18\x02 \x01(\x08\x12\x13\n\x0bmatch_songs\x18\x03 \x01(\x08\x12\x14\n\x0cshow_history\x18\x04 \x01(\x08\x12\x19\n\x11make_arrangements\x18\x05 \x01(\x08\x12\x13\n\x0b\x61uto_upload\x18\x06 \x01(\x08\x12\x15\n\rauto_download\x18\x07 \x01(\x08\x1a\x1f\n\nSongSelect\x12\x11\n\tlogged_in\x18\x01 \x01(\x08\x1a\xfc\x05\n\x05\x41udio\x12\x11\n\tbus_count\x18\x01 \x01(\x05\x12\x41\n\x10inspector_device\x18\x02 \x01(\x0e\x32\'.rv.analytics.Startup.Audio.AudioDevice\x12G\n\x11inspector_routing\x18\x03 \x01(\x0e\x32,.rv.analytics.Startup.Audio.InspectorRouting\x12<\n\x0bmain_device\x18\x04 \x01(\x0e\x32\'.rv.analytics.Startup.Audio.AudioDevice\x12>\n\x0cmain_routing\x18\x05 \x01(\x0e\x32(.rv.analytics.Startup.Audio.AudioRouting\x12\x12\n\nmain_delay\x18\x06 \x01(\x05\x12\x0f\n\x07sdi_ndi\x18\x07 \x01(\x08\x12\x41\n\x0fsdi_ndi_routing\x18\x08 \x01(\x0e\x32(.rv.analytics.Startup.Audio.AudioRouting\x12\x15\n\rsdi_ndi_delay\x18\t \x01(\x05\"\x86\x01\n\x0b\x41udioDevice\x12\x18\n\x14\x41UDIO_DEVICE_UNKNOWN\x10\x00\x12\x15\n\x11\x41UDIO_DEVICE_MAIN\x10\x01\x12\x17\n\x13\x41UDIO_DEVICE_SYSTEM\x10\x02\x12\x16\n\x12\x41UDIO_DEVICE_OTHER\x10\x03\x12\x15\n\x11\x41UDIO_DEVICE_NONE\x10\x04\"n\n\x10InspectorRouting\x12\x1d\n\x19INSPECTOR_ROUTING_UNKNOWN\x10\x00\x12\x1d\n\x19INSPECTOR_ROUTING_DEFAULT\x10\x01\x12\x1c\n\x18INSPECTOR_ROUTING_CUSTOM\x10\x02\"^\n\x0c\x41udioRouting\x12\x19\n\x15\x41UDIO_ROUTING_UNKNOWN\x10\x00\x12\x19\n\x15\x41UDIO_ROUTING_DEFAULT\x10\x01\x12\x18\n\x14\x41UDIO_ROUTING_CUSTOM\x10\x02\x1a,\n\x0e\x43ommunications\x12\x1a\n\x12total_device_count\x18\x01 \x01(\x05\x1a\x19\n\x04Resi\x12\x11\n\tlogged_in\x18\x01 \x01(\x08\x1a\xe4\x08\n\tInterface\x12G\n\x0flibrary_outline\x18\x01 \x01(\x0e\x32..rv.analytics.Startup.Interface.SplitViewState\x12\x45\n\rmedia_outline\x18\x02 \x01(\x0e\x32..rv.analytics.Startup.Interface.SplitViewState\x12\x45\n\raudio_outline\x18\x03 \x01(\x0e\x32..rv.analytics.Startup.Interface.SplitViewState\x12\x1b\n\x13\x63ontinuous_playlist\x18\x04 \x01(\x08\x12\x41\n\tmedia_bin\x18\x05 \x01(\x0e\x32..rv.analytics.Startup.Interface.SplitViewState\x12V\n\x17presentation_view_style\x18\x06 \x01(\x0e\x32\x35.rv.analytics.Startup.Interface.PresentationViewStyle\x12&\n\x1epresentation_grid_column_count\x18\x07 \x01(\x05\x12\'\n\x1fpresentation_table_column_count\x18\x08 \x01(\x05\x12O\n\x14media_bin_view_style\x18\t \x01(\x0e\x32\x31.rv.analytics.Startup.Interface.MediaBinViewStyle\x12#\n\x1bmedia_bin_grid_column_count\x18\n \x01(\x05\x12$\n\x1cmedia_bin_table_column_count\x18\x0b \x01(\x05\x12\x1f\n\x17presentation_transition\x18\x0c \x01(\t\x12\x18\n\x10media_transition\x18\r \x01(\t\x12\x15\n\raudio_shuffle\x18\x0e \x01(\x08\"m\n\x0eSplitViewState\x12\x1c\n\x18SPLIT_VIEW_STATE_UNKNOWN\x10\x00\x12\x1e\n\x1aSPLIT_VIEW_STATE_COLLAPSED\x10\x01\x12\x1d\n\x19SPLIT_VIEW_STATE_EXPANDED\x10\x02\"\xa3\x01\n\x15PresentationViewStyle\x12#\n\x1fPRESENTATION_VIEW_STYLE_UNKNOWN\x10\x00\x12 \n\x1cPRESENTATION_VIEW_STYLE_GRID\x10\x01\x12 \n\x1cPRESENTATION_VIEW_STYLE_EASY\x10\x02\x12!\n\x1dPRESENTATION_VIEW_STYLE_TABLE\x10\x03\"t\n\x11MediaBinViewStyle\x12 \n\x1cMEDIA_BIN_VIEW_STYLE_UNKNOWN\x10\x00\x12\x1d\n\x19MEDIA_BIN_VIEW_STYLE_GRID\x10\x01\x12\x1e\n\x1aMEDIA_BIN_VIEW_STYLE_TABLE\x10\x02\x1a\xbf\x05\n\x07\x43ontent\x12\x15\n\rlibrary_count\x18\x01 \x01(\x05\x12\x1e\n\x16library_playlist_count\x18\x02 \x01(\x05\x12%\n\x1dlibrary_playlist_folder_count\x18\x03 \x01(\x05\x12\"\n\x1alibrary_playlist_max_depth\x18\x04 \x01(\x05\x12&\n\x1emedia_bin_total_playlist_count\x18\x05 \x01(\x05\x12\'\n\x1fmedia_bin_playlist_folder_count\x18\x06 \x01(\x05\x12$\n\x1cmedia_bin_playlist_max_depth\x18\x07 \x01(\x05\x12\'\n\x1fmedia_bin_normal_playlist_count\x18\x08 \x01(\x05\x12&\n\x1emedia_bin_smart_playlist_count\x18\t \x01(\x05\x12#\n\x1bmedia_bin_video_input_count\x18\n \x01(\x05\x12 \n\x18\x61udio_bin_playlist_count\x18\x0b \x01(\x05\x12\'\n\x1f\x61udio_bin_playlist_folder_count\x18\x0c \x01(\x05\x12$\n\x1c\x61udio_bin_playlist_max_depth\x18\r \x01(\x05\x12\x13\n\x0btimer_count\x18\x0e \x01(\x05\x12\x16\n\x0emessages_count\x18\x0f \x01(\x05\x12\x13\n\x0bprops_count\x18\x10 \x01(\x05\x12\x1a\n\x12stage_layout_count\x18\x11 \x01(\x05\x12\x14\n\x0cmacros_count\x18\x12 \x01(\x05\x12 \n\x18macros_collections_count\x18\x13 \x01(\x05\x12\x1b\n\x13macros_custom_icons\x18\x14 \x01(\x05\x12!\n\x19ubiquitous_show_directory\x18\x15 \x01(\x08\x1au\n\x06Themes\x12\x13\n\x0btheme_count\x18\x01 \x01(\x05\x12\x1a\n\x12theme_folder_count\x18\x02 \x01(\x05\x12\x1e\n\x16theme_folder_max_depth\x18\x03 \x01(\x05\x12\x1a\n\x12theme_slides_count\x18\x04 \x01(\x05\x1a)\n\x05Macro\x12 \n\x18trigger_on_startup_count\x18\x01 \x01(\x05\x1a\x99\x01\n\nClearGroup\x12\x19\n\x11\x63lear_group_count\x18\x01 \x01(\x05\x12 \n\x18hidden_clear_group_count\x18\x02 \x01(\x05\x12\x1a\n\x12\x64\x65\x66\x61ult_icon_count\x18\x03 \x01(\x05\x12\x19\n\x11\x63ustom_icon_count\x18\x04 \x01(\x05\x12\x17\n\x0ficon_tint_count\x18\x05 \x01(\x05\x1av\n\nKeyMapping\x12\x14\n\x0ctotal_mapped\x18\x01 \x01(\x05\x12\x14\n\x0c\x63lear_groups\x18\x02 \x01(\x05\x12\x0e\n\x06groups\x18\x03 \x01(\x05\x12\x0e\n\x06macros\x18\x04 \x01(\x05\x12\r\n\x05props\x18\x05 \x01(\x05\x12\r\n\x05menus\x18\x06 \x01(\x05\x1a\x34\n\x0bNetworkLink\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x14\n\x0cmember_count\x18\x02 \x01(\r\x1at\n\x07\x43\x61pture\x12\x15\n\rpresets_count\x18\x01 \x01(\x05\x12\x1a\n\x12\x64isk_presets_count\x18\x02 \x01(\x05\x12\x1a\n\x12rtmp_presets_count\x18\x03 \x01(\x05\x12\x1a\n\x12resi_presets_count\x18\x04 \x01(\x05\x42\x0b\n\tComponentBA\xf8\x01\x01\xaa\x02.Pro.SerializationInterop.RVProtoData.Analytics\xba\x02\nAnalytics_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analyticsStartup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002.Pro.SerializationInterop.RVProtoData.Analytics\272\002\nAnalytics_'
  _globals['_STARTUP']._serialized_start=69
  _globals['_STARTUP']._serialized_end=7997
  _globals['_STARTUP_LOOKS']._serialized_start=1064
  _globals['_STARTUP_LOOKS']._serialized_end=1095
  _globals['_STARTUP_SCREENCONFIGURATION']._serialized_start=1098
  _globals['_STARTUP_SCREENCONFIGURATION']._serialized_end=3538
  _globals['_STARTUP_SCREENCONFIGURATION_SUMMARY']._serialized_start=1544
  _globals['_STARTUP_SCREENCONFIGURATION_SUMMARY']._serialized_end=1635
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT']._serialized_start=1638
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT']._serialized_end=2536
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_PROSCREENTYPE']._serialized_start=2057
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_PROSCREENTYPE']._serialized_end=2220
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_OUTPUTTYPE']._serialized_start=2223
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_OUTPUTTYPE']._serialized_end=2400
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_ALIGNMENT']._serialized_start=2403
  _globals['_STARTUP_SCREENCONFIGURATION_OUTPUT_ALIGNMENT']._serialized_end=2536
  _globals['_STARTUP_SCREENCONFIGURATION_SINGLE']._serialized_start=2538
  _globals['_STARTUP_SCREENCONFIGURATION_SINGLE']._serialized_end=2651
  _globals['_STARTUP_SCREENCONFIGURATION_MIRRORED']._serialized_start=2654
  _globals['_STARTUP_SCREENCONFIGURATION_MIRRORED']._serialized_end=2784
  _globals['_STARTUP_SCREENCONFIGURATION_EDGEBLEND']._serialized_start=2787
  _globals['_STARTUP_SCREENCONFIGURATION_EDGEBLEND']._serialized_end=2918
  _globals['_STARTUP_SCREENCONFIGURATION_GROUPED']._serialized_start=2921
  _globals['_STARTUP_SCREENCONFIGURATION_GROUPED']._serialized_end=3066
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN']._serialized_start=3069
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN']._serialized_end=3437
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN_ALPHAKEYMODE']._serialized_start=3250
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN_ALPHAKEYMODE']._serialized_end=3352
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN_ALPHADEVICE']._serialized_start=3354
  _globals['_STARTUP_SCREENCONFIGURATION_SCREEN_ALPHADEVICE']._serialized_end=3437
  _globals['_STARTUP_SCREENCONFIGURATION_SCREENTYPE']._serialized_start=3439
  _globals['_STARTUP_SCREENCONFIGURATION_SCREENTYPE']._serialized_end=3525
  _globals['_STARTUP_PREFERENCES']._serialized_start=3541
  _globals['_STARTUP_PREFERENCES']._serialized_end=4350
  _globals['_STARTUP_PREFERENCES_COPYRIGHTSTYLE']._serialized_start=3975
  _globals['_STARTUP_PREFERENCES_COPYRIGHTSTYLE']._serialized_end=4141
  _globals['_STARTUP_PREFERENCES_RENDERMODE']._serialized_start=4143
  _globals['_STARTUP_PREFERENCES_RENDERMODE']._serialized_end=4252
  _globals['_STARTUP_PREFERENCES_UPDATECHANNEL']._serialized_start=4254
  _globals['_STARTUP_PREFERENCES_UPDATECHANNEL']._serialized_end=4350
  _globals['_STARTUP_SCREENS']._serialized_start=4353
  _globals['_STARTUP_SCREENS']._serialized_end=4495
  _globals['_STARTUP_PLANNINGCENTER']._serialized_start=4498
  _globals['_STARTUP_PLANNINGCENTER']._serialized_end=4668
  _globals['_STARTUP_SONGSELECT']._serialized_start=4670
  _globals['_STARTUP_SONGSELECT']._serialized_end=4701
  _globals['_STARTUP_AUDIO']._serialized_start=4704
  _globals['_STARTUP_AUDIO']._serialized_end=5468
  _globals['_STARTUP_AUDIO_AUDIODEVICE']._serialized_start=5126
  _globals['_STARTUP_AUDIO_AUDIODEVICE']._serialized_end=5260
  _globals['_STARTUP_AUDIO_INSPECTORROUTING']._serialized_start=5262
  _globals['_STARTUP_AUDIO_INSPECTORROUTING']._serialized_end=5372
  _globals['_STARTUP_AUDIO_AUDIOROUTING']._serialized_start=5374
  _globals['_STARTUP_AUDIO_AUDIOROUTING']._serialized_end=5468
  _globals['_STARTUP_COMMUNICATIONS']._serialized_start=5470
  _globals['_STARTUP_COMMUNICATIONS']._serialized_end=5514
  _globals['_STARTUP_RESI']._serialized_start=5516
  _globals['_STARTUP_RESI']._serialized_end=5541
  _globals['_STARTUP_INTERFACE']._serialized_start=5544
  _globals['_STARTUP_INTERFACE']._serialized_end=6668
  _globals['_STARTUP_INTERFACE_SPLITVIEWSTATE']._serialized_start=6275
  _globals['_STARTUP_INTERFACE_SPLITVIEWSTATE']._serialized_end=6384
  _globals['_STARTUP_INTERFACE_PRESENTATIONVIEWSTYLE']._serialized_start=6387
  _globals['_STARTUP_INTERFACE_PRESENTATIONVIEWSTYLE']._serialized_end=6550
  _globals['_STARTUP_INTERFACE_MEDIABINVIEWSTYLE']._serialized_start=6552
  _globals['_STARTUP_INTERFACE_MEDIABINVIEWSTYLE']._serialized_end=6668
  _globals['_STARTUP_CONTENT']._serialized_start=6671
  _globals['_STARTUP_CONTENT']._serialized_end=7374
  _globals['_STARTUP_THEMES']._serialized_start=7376
  _globals['_STARTUP_THEMES']._serialized_end=7493
  _globals['_STARTUP_MACRO']._serialized_start=7495
  _globals['_STARTUP_MACRO']._serialized_end=7536
  _globals['_STARTUP_CLEARGROUP']._serialized_start=7539
  _globals['_STARTUP_CLEARGROUP']._serialized_end=7692
  _globals['_STARTUP_KEYMAPPING']._serialized_start=7694
  _globals['_STARTUP_KEYMAPPING']._serialized_end=7812
  _globals['_STARTUP_NETWORKLINK']._serialized_start=7814
  _globals['_STARTUP_NETWORKLINK']._serialized_end=7866
  _globals['_STARTUP_CAPTURE']._serialized_start=7868
  _globals['_STARTUP_CAPTURE']._serialized_end=7984
# @@protoc_insertion_point(module_scope)
