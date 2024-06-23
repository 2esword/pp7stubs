# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cue.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import action_pb2 as action__pb2
from . import hotKey_pb2 as hotKey__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tcue.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\x0chotKey.proto\x1a\turl.proto\x1a\nuuid.proto\"\xbc\x07\n\x03\x43ue\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x41\n\x16\x63ompletion_target_type\x18\x03 \x01(\x0e\x32!.rv.data.Cue.CompletionTargetType\x12-\n\x16\x63ompletion_target_uuid\x18\x04 \x01(\x0b\x32\r.rv.data.UUID\x12\x41\n\x16\x63ompletion_action_type\x18\x05 \x01(\x0e\x32!.rv.data.Cue.CompletionActionType\x12-\n\x16\x63ompletion_action_uuid\x18\x06 \x01(\x0b\x32\r.rv.data.UUID\x12/\n\x0ctrigger_time\x18\x07 \x01(\x0b\x32\x19.rv.data.Cue.TimecodeTime\x12 \n\x07hot_key\x18\x08 \x01(\x0b\x32\x0f.rv.data.HotKey\x12 \n\x07\x61\x63tions\x18\n \x03(\x0b\x32\x0f.rv.data.Action\x12\x39\n\x0fpending_imports\x18\x0b \x03(\x0b\x32 .rv.data.Cue.PendingImportsEntry\x12\x11\n\tisEnabled\x18\x0c \x01(\x08\x12\x17\n\x0f\x63ompletion_time\x18\r \x01(\x01\x1a\x1c\n\x0cTimecodeTime\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a@\n\x13PendingImportsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.rv.data.URLs\"\xbd\x01\n\x14\x43ompletionTargetType\x12\x1f\n\x1b\x43OMPLETION_TARGET_TYPE_NONE\x10\x00\x12\x1f\n\x1b\x43OMPLETION_TARGET_TYPE_NEXT\x10\x01\x12!\n\x1d\x43OMPLETION_TARGET_TYPE_RANDOM\x10\x02\x12\x1e\n\x1a\x43OMPLETION_TARGET_TYPE_CUE\x10\x03\x12 \n\x1c\x43OMPLETION_TARGET_TYPE_FIRST\x10\x04\"\xa9\x01\n\x14\x43ompletionActionType\x12 \n\x1c\x43OMPLETION_ACTION_TYPE_FIRST\x10\x00\x12\x1f\n\x1b\x43OMPLETION_ACTION_TYPE_LAST\x10\x01\x12\'\n#COMPLETION_ACTION_TYPE_AFTER_ACTION\x10\x02\x12%\n!COMPLETION_ACTION_TYPE_AFTER_TIME\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cue_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CUE']._serialized_start=74
  _globals['_CUE']._serialized_end=1030
  _globals['_CUE_TIMECODETIME']._serialized_start=572
  _globals['_CUE_TIMECODETIME']._serialized_end=600
  _globals['_CUE_PENDINGIMPORTSENTRY']._serialized_start=602
  _globals['_CUE_PENDINGIMPORTSENTRY']._serialized_end=666
  _globals['_CUE_COMPLETIONTARGETTYPE']._serialized_start=669
  _globals['_CUE_COMPLETIONTARGETTYPE']._serialized_end=858
  _globals['_CUE_COMPLETIONACTIONTYPE']._serialized_start=861
  _globals['_CUE_COMPLETIONACTIONTYPE']._serialized_end=1030
# @@protoc_insertion_point(module_scope)
