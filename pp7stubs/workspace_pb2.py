# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: workspace.proto
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
    'workspace.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import alignmentGuide_pb2 as alignmentGuide__pb2
from . import calendar_pb2 as calendar__pb2
from . import effects_pb2 as effects__pb2
from . import graphicsData_pb2 as graphicsData__pb2
from . import hotKey_pb2 as hotKey__pb2
from . import layers_pb2 as layers__pb2
from . import liveVideoPlaylist_pb2 as liveVideoPlaylist__pb2
from . import masks_pb2 as masks__pb2
from . import playlist_pb2 as playlist__pb2
from . import screens_pb2 as screens__pb2
from . import targets_pb2 as targets__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworkspace.proto\x12\x07rv.data\x1a\x14\x61lignmentGuide.proto\x1a\x0e\x63\x61lendar.proto\x1a\reffects.proto\x1a\x12graphicsData.proto\x1a\x0chotKey.proto\x1a\x0clayers.proto\x1a\x17liveVideoPlaylist.proto\x1a\x0bmasks.proto\x1a\x0eplaylist.proto\x1a\rscreens.proto\x1a\rtargets.proto\x1a\turl.proto\x1a\nuuid.proto\"\xb6\t\n\tWorkspace\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\r\n\x05muted\x18\x02 \x01(\x08\x12\x0e\n\x06hidden\x18\x03 \x01(\x08\x12>\n\x11\x65\x64itor_background\x18\x04 \x01(\x0b\x32#.rv.data.Workspace.EditorBackground\x12)\n\x12\x65\x66\x66\x65\x63t_preset_uuid\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\x12\x1d\n\x15\x65\x66\x66\x65\x63t_build_duration\x18\x06 \x01(\x01\x12\'\n\ntransition\x18\x07 \x01(\x0b\x32\x13.rv.data.Transition\x12\'\n\x10\x61\x63tive_mask_uuid\x18\x08 \x01(\x0b\x32\r.rv.data.UUID\x12#\n\x08playlist\x18\t \x01(\x0b\x32\x11.rv.data.Playlist\x12\x34\n\x0cunit_scaling\x18\n \x01(\x0b\x32\x1e.rv.data.Workspace.UnitScaling\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x10 \x03(\x0b\x32\x0f.rv.data.Effect\x12\x1c\n\x05masks\x18\x11 \x03(\x0b\x32\r.rv.data.Mask\x12 \n\x07screens\x18\x12 \x03(\x0b\x32\x0f.rv.data.Screen\x12\'\n\x0b\x65\x64ge_blends\x18\x13 \x03(\x0b\x32\x12.rv.data.EdgeBlend\x12\x1e\n\x06layers\x18\x14 \x03(\x0b\x32\x0e.rv.data.Layer\x12\'\n\x0btarget_sets\x18\x15 \x03(\x0b\x32\x12.rv.data.TargetSet\x12!\n\x08hot_keys\x18\x16 \x03(\x0b\x32\x0f.rv.data.HotKey\x12#\n\x08\x63\x61lendar\x18\x17 \x01(\x0b\x32\x11.rv.data.Calendar\x12\x31\n\x10\x61lignment_guides\x18\x18 \x03(\x0b\x32\x17.rv.data.AlignmentGuide\x12\x37\n\x13live_video_playlist\x18\x19 \x01(\x0b\x32\x1a.rv.data.LiveVideoPlaylist\x12\x36\n\x16output_preview_display\x18\x1a \x01(\x0b\x32\x16.rv.data.OutputDisplay\x1av\n\x10\x45\x64itorBackground\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12%\n\x05\x66rame\x18\x02 \x01(\x0b\x32\x16.rv.data.Graphics.Rect\x12\x19\n\x03url\x18\x03 \x01(\x0b\x32\x0c.rv.data.URL\x12\x0f\n\x07opacity\x18\x04 \x01(\x01\x1a\xfd\x01\n\x0bUnitScaling\x12\x0e\n\x06length\x18\x01 \x01(\x01\x12\x35\n\x04unit\x18\x02 \x01(\x0e\x32\'.rv.data.Workspace.UnitScaling.UnitType\x12\x0e\n\x06points\x18\x03 \x01(\x01\"\x96\x01\n\x08UnitType\x12\x14\n\x10UNIT_TYPE_POINTS\x10\x00\x12\x19\n\x15UNIT_TYPE_MILLIMETERS\x10\x01\x12\x19\n\x15UNIT_TYPE_CENTIMETERS\x10\x02\x12\x14\n\x10UNIT_TYPE_METERS\x10\x03\x12\x14\n\x10UNIT_TYPE_INCHES\x10\x04\x12\x12\n\x0eUNIT_TYPE_FEET\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workspace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WORKSPACE']._serialized_start=237
  _globals['_WORKSPACE']._serialized_end=1443
  _globals['_WORKSPACE_EDITORBACKGROUND']._serialized_start=1069
  _globals['_WORKSPACE_EDITORBACKGROUND']._serialized_end=1187
  _globals['_WORKSPACE_UNITSCALING']._serialized_start=1190
  _globals['_WORKSPACE_UNITSCALING']._serialized_end=1443
  _globals['_WORKSPACE_UNITSCALING_UNITTYPE']._serialized_start=1293
  _globals['_WORKSPACE_UNITSCALING_UNITTYPE']._serialized_end=1443
# @@protoc_insertion_point(module_scope)
