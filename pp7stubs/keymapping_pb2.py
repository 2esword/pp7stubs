# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keymapping.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import applicationInfo_pb2 as applicationInfo__pb2
from . import collectionElementType_pb2 as collectionElementType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10keymapping.proto\x12\x07rv.data\x1a\x15\x61pplicationInfo.proto\x1a\x1b\x63ollectionElementType.proto\"\xfd\x06\n\nKeyMapping\x12\x36\n\x08keyboard\x18\x01 \x01(\x0b\x32$.rv.data.KeyMapping.ComputerKeyboard\x12.\n\x04midi\x18\x02 \x01(\x0b\x32 .rv.data.KeyMapping.MIDIKeyboard\x12\x13\n\tmenu_item\x18\x64 \x01(\tH\x00\x12@\n\x16\x63lear_group_identifier\x18\x65 \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x12\x38\n\x0e\x63ue_identifier\x18\x66 \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x12:\n\x10group_identifier\x18g \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x12:\n\x10macro_identifier\x18h \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x12\x39\n\x0fprop_identifier\x18i \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x12:\n\x10timer_identifier\x18j \x01(\x0b\x32\x1e.rv.data.CollectionElementTypeH\x00\x1a\xb0\x02\n\x10\x43omputerKeyboard\x12\x16\n\x0ekey_equivalent\x18\x01 \x01(\t\x12Y\n\x1dkey_equivalent_modifier_flags\x18\x02 \x03(\x0e\x32\x32.rv.data.KeyMapping.ComputerKeyboard.ModifierFlags\"\xa8\x01\n\rModifierFlags\x12\x1d\n\x19MODIFIERFLAGS_COMMAND_KEY\x10\x00\x12\x1b\n\x17MODIFIERFLAGS_SHIFT_KEY\x10\x01\x12\x1c\n\x18MODIFIERFLAGS_OPTION_KEY\x10\x02\x12\x1d\n\x19MODIFIERFLAGS_CONTROL_KEY\x10\x03\x12\x1e\n\x1aMODIFIERFLAGS_FUNCTION_KEY\x10\x04\x1a@\n\x0cMIDIKeyboard\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x05\x12\r\n\x05pitch\x18\x02 \x01(\x05\x12\x10\n\x08velocity\x18\x03 \x01(\x05\x42\x12\n\x10TargetIdentifier\"\xd4\x01\n\x12KeyMappingDocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12(\n\x0bkeymappings\x18\x02 \x03(\x0b\x32\x13.rv.data.KeyMapping\x12.\n\x11macos_keymappings\x18\x03 \x03(\x0b\x32\x13.rv.data.KeyMapping\x12\x30\n\x13windows_keymappings\x18\x04 \x03(\x0b\x32\x13.rv.data.KeyMappingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'keymapping_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KEYMAPPING']._serialized_start=82
  _globals['_KEYMAPPING']._serialized_end=975
  _globals['_KEYMAPPING_COMPUTERKEYBOARD']._serialized_start=585
  _globals['_KEYMAPPING_COMPUTERKEYBOARD']._serialized_end=889
  _globals['_KEYMAPPING_COMPUTERKEYBOARD_MODIFIERFLAGS']._serialized_start=721
  _globals['_KEYMAPPING_COMPUTERKEYBOARD_MODIFIERFLAGS']._serialized_end=889
  _globals['_KEYMAPPING_MIDIKEYBOARD']._serialized_start=891
  _globals['_KEYMAPPING_MIDIKEYBOARD']._serialized_end=955
  _globals['_KEYMAPPINGDOCUMENT']._serialized_start=978
  _globals['_KEYMAPPINGDOCUMENT']._serialized_end=1190
# @@protoc_insertion_point(module_scope)
