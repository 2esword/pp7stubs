# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: playlist.proto
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
    'playlist.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import action_pb2 as action__pb2
from . import color_pb2 as color__pb2
from . import cue_pb2 as cue__pb2
from . import hotKey_pb2 as hotKey__pb2
from . import musicKeyScale_pb2 as musicKeyScale__pb2
from . import planningCenter_pb2 as planningCenter__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eplaylist.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\x0b\x63olor.proto\x1a\tcue.proto\x1a\x0chotKey.proto\x1a\x13musicKeyScale.proto\x1a\x14planningCenter.proto\x1a\turl.proto\x1a\nuuid.proto\"\x91\n\n\x08Playlist\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x04type\x18\x03 \x01(\x0e\x32\x16.rv.data.Playlist.Type\x12\x10\n\x08\x65xpanded\x18\x04 \x01(\x08\x12*\n\x13targeted_layer_uuid\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\x12*\n\x14smart_directory_path\x18\x06 \x01(\x0b\x32\x0c.rv.data.URL\x12 \n\x07hot_key\x18\x07 \x01(\x0b\x32\x0f.rv.data.HotKey\x12\x1a\n\x04\x63ues\x18\x08 \x03(\x0b\x32\x0c.rv.data.Cue\x12#\n\x08\x63hildren\x18\t \x03(\x0b\x32\x11.rv.data.Playlist\x12\x18\n\x10timecode_enabled\x18\n \x01(\x08\x12,\n\x06timing\x18\x0b \x01(\x0e\x32\x1c.rv.data.Playlist.TimingType\x12\x33\n\x0cstartup_info\x18\x10 \x01(\x0b\x32\x1d.rv.data.Playlist.StartupInfo\x12\x34\n\tplaylists\x18\x0c \x01(\x0b\x32\x1f.rv.data.Playlist.PlaylistArrayH\x00\x12\x30\n\x05items\x18\r \x01(\x0b\x32\x1f.rv.data.Playlist.PlaylistItemsH\x00\x12<\n\x0fsmart_directory\x18\x0e \x01(\x0b\x32!.rv.data.Playlist.FolderDirectoryH\x01\x12/\n\x08pco_plan\x18\x0f \x01(\x0b\x32\x1b.rv.data.PlanningCenterPlanH\x01\x1a\x35\n\rPlaylistArray\x12$\n\tplaylists\x18\x01 \x03(\x0b\x32\x11.rv.data.Playlist\x1a\x35\n\rPlaylistItems\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x15.rv.data.PlaylistItem\x1a\xd5\x01\n\x0f\x46olderDirectory\x12%\n\x0fsmart_directory\x18\x01 \x01(\x0b\x32\x0c.rv.data.URL\x12I\n\x0fimport_behavior\x18\x02 \x01(\x0e\x32\x30.rv.data.Playlist.FolderDirectory.ImportBehavior\"P\n\x0eImportBehavior\x12\x1e\n\x1aIMPORT_BEHAVIOR_BACKGROUND\x10\x00\x12\x1e\n\x1aIMPORT_BEHAVIOR_FOREGROUND\x10\x01\x1aO\n\x03Tag\x12\x1d\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.Color\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x04uuid\x18\x03 \x01(\x0b\x32\r.rv.data.UUID\x1a)\n\x0bStartupInfo\x12\x1a\n\x12trigger_on_startup\x18\x01 \x01(\x08\"Z\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x11\n\rTYPE_PLAYLIST\x10\x01\x12\x0e\n\nTYPE_GROUP\x10\x02\x12\x0e\n\nTYPE_SMART\x10\x03\x12\r\n\tTYPE_ROOT\x10\x04\"Y\n\nTimingType\x12\x14\n\x10TIMING_TYPE_NONE\x10\x00\x12\x18\n\x14TIMING_TYPE_TIMECODE\x10\x01\x12\x1b\n\x17TIMING_TYPE_TIME_OF_DAY\x10\x02\x42\x0e\n\x0c\x43hildrenTypeB\n\n\x08LinkData\"\xbc\x06\n\x0cPlaylistItem\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x04tags\x18\x07 \x03(\x0b\x32\r.rv.data.UUID\x12\x11\n\tis_hidden\x18\t \x01(\x08\x12.\n\x06header\x18\x03 \x01(\x0b\x32\x1c.rv.data.PlaylistItem.HeaderH\x00\x12:\n\x0cpresentation\x18\x04 \x01(\x0b\x32\".rv.data.PlaylistItem.PresentationH\x00\x12\x1b\n\x03\x63ue\x18\x05 \x01(\x0b\x32\x0c.rv.data.CueH\x00\x12?\n\x0fplanning_center\x18\x06 \x01(\x0b\x32$.rv.data.PlaylistItem.PlanningCenterH\x00\x12\x38\n\x0bplaceholder\x18\x08 \x01(\x0b\x32!.rv.data.PlaylistItem.PlaceholderH\x00\x1aI\n\x06Header\x12\x1d\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.Color\x12 \n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x0f.rv.data.Action\x1a\xc8\x01\n\x0cPresentation\x12#\n\rdocument_path\x18\x01 \x01(\x0b\x32\x0c.rv.data.URL\x12\"\n\x0b\x61rrangement\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x12?\n\x13\x63ontent_destination\x18\x03 \x01(\x0e\x32\".rv.data.Action.ContentDestination\x12.\n\x0euser_music_key\x18\x04 \x01(\x0b\x32\x16.rv.data.MusicKeyScale\x1ap\n\x0ePlanningCenter\x12\x32\n\x04item\x18\x01 \x01(\x0b\x32$.rv.data.PlanningCenterPlan.PlanItem\x12*\n\x0blinked_data\x18\x02 \x01(\x0b\x32\x15.rv.data.PlaylistItem\x1a\x39\n\x0bPlaceholder\x12*\n\x0blinked_data\x18\x01 \x01(\x0b\x32\x15.rv.data.PlaylistItemB\n\n\x08ItemTypeB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'playlist_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_PLAYLIST']._serialized_start=146
  _globals['_PLAYLIST']._serialized_end=1443
  _globals['_PLAYLIST_PLAYLISTARRAY']._serialized_start=784
  _globals['_PLAYLIST_PLAYLISTARRAY']._serialized_end=837
  _globals['_PLAYLIST_PLAYLISTITEMS']._serialized_start=839
  _globals['_PLAYLIST_PLAYLISTITEMS']._serialized_end=892
  _globals['_PLAYLIST_FOLDERDIRECTORY']._serialized_start=895
  _globals['_PLAYLIST_FOLDERDIRECTORY']._serialized_end=1108
  _globals['_PLAYLIST_FOLDERDIRECTORY_IMPORTBEHAVIOR']._serialized_start=1028
  _globals['_PLAYLIST_FOLDERDIRECTORY_IMPORTBEHAVIOR']._serialized_end=1108
  _globals['_PLAYLIST_TAG']._serialized_start=1110
  _globals['_PLAYLIST_TAG']._serialized_end=1189
  _globals['_PLAYLIST_STARTUPINFO']._serialized_start=1191
  _globals['_PLAYLIST_STARTUPINFO']._serialized_end=1232
  _globals['_PLAYLIST_TYPE']._serialized_start=1234
  _globals['_PLAYLIST_TYPE']._serialized_end=1324
  _globals['_PLAYLIST_TIMINGTYPE']._serialized_start=1326
  _globals['_PLAYLIST_TIMINGTYPE']._serialized_end=1415
  _globals['_PLAYLISTITEM']._serialized_start=1446
  _globals['_PLAYLISTITEM']._serialized_end=2274
  _globals['_PLAYLISTITEM_HEADER']._serialized_start=1813
  _globals['_PLAYLISTITEM_HEADER']._serialized_end=1886
  _globals['_PLAYLISTITEM_PRESENTATION']._serialized_start=1889
  _globals['_PLAYLISTITEM_PRESENTATION']._serialized_end=2089
  _globals['_PLAYLISTITEM_PLANNINGCENTER']._serialized_start=2091
  _globals['_PLAYLISTITEM_PLANNINGCENTER']._serialized_end=2203
  _globals['_PLAYLISTITEM_PLACEHOLDER']._serialized_start=2205
  _globals['_PLAYLISTITEM_PLACEHOLDER']._serialized_end=2262
# @@protoc_insertion_point(module_scope)
