# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: presentationSlide.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import alignmentGuide_pb2 as alignmentGuide__pb2
from . import effects_pb2 as effects__pb2
from . import graphicsData_pb2 as graphicsData__pb2
from . import slide_pb2 as slide__pb2
from . import url_pb2 as url__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17presentationSlide.proto\x12\x07rv.data\x1a\x14\x61lignmentGuide.proto\x1a\reffects.proto\x1a\x12graphicsData.proto\x1a\x0bslide.proto\x1a\turl.proto\"\xbc\x02\n\x11PresentationSlide\x12\"\n\nbase_slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12/\n\x05notes\x18\x02 \x01(\x0b\x32 .rv.data.PresentationSlide.Notes\x12\x34\n\x13template_guidelines\x18\x03 \x03(\x0b\x32\x17.rv.data.AlignmentGuide\x12!\n\x0b\x63hord_chart\x18\x04 \x01(\x0b\x32\x0c.rv.data.URL\x12\'\n\ntransition\x18\x05 \x01(\x0b\x32\x13.rv.data.Transition\x1aP\n\x05Notes\x12\x10\n\x08rtf_data\x18\x01 \x01(\x0c\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.rv.data.Graphics.Text.Attributesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'presentationSlide_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PRESENTATIONSLIDE']._serialized_start=118
  _globals['_PRESENTATIONSLIDE']._serialized_end=434
  _globals['_PRESENTATIONSLIDE_NOTES']._serialized_start=354
  _globals['_PRESENTATIONSLIDE_NOTES']._serialized_end=434
# @@protoc_insertion_point(module_scope)