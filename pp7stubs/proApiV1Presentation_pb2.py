# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proApiV1Presentation.proto
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
    'proApiV1Presentation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import proApiV1Color_pb2 as proApiV1Color__pb2
from . import proApiV1ContentType_pb2 as proApiV1ContentType__pb2
from . import proApiV1Identifier_pb2 as proApiV1Identifier__pb2
from . import proApiV1Size_pb2 as proApiV1Size__pb2
from . import proApiV1TimelineOperation_pb2 as proApiV1TimelineOperation__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aproApiV1Presentation.proto\x12\x07rv.data\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x13proApiV1Color.proto\x1a\x19proApiV1ContentType.proto\x1a\x18proApiV1Identifier.proto\x1a\x12proApiV1Size.proto\x1a\x1fproApiV1TimelineOperation.proto\x1a\nuuid.proto\"W\n\x11\x41PI_v1_SlideIndex\x12\r\n\x05index\x18\x01 \x01(\r\x12\x33\n\x0fpresentation_id\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\"\x86\x04\n\x13\x41PI_v1_Presentation\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x37\n\x06groups\x18\x02 \x03(\x0b\x32\'.rv.data.API_v1_Presentation.SlideGroup\x12\x14\n\x0chas_timeline\x18\x03 \x01(\x08\x12\x19\n\x11presentation_path\x18\x04 \x01(\t\x12=\n\x0b\x64\x65stination\x18\x05 \x01(\x0e\x32(.rv.data.API_v1_Presentation.Destination\x1a\xe9\x01\n\nSlideGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x15.rv.data.API_v1_Color\x12=\n\x06slides\x18\x03 \x03(\x0b\x32-.rv.data.API_v1_Presentation.SlideGroup.Slide\x1ah\n\x05Slide\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05notes\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05label\x18\x05 \x01(\t\x12\"\n\x04size\x18\x06 \x01(\x0b\x32\x14.rv.data.API_v1_Size\"2\n\x0b\x44\x65stination\x12\x10\n\x0cpresentation\x10\x00\x12\x11\n\rannouncements\x10\x01\"\xfe\x15\n\x1b\x41PI_v1_Presentation_Request\x12=\n\x06\x61\x63tive\x18\x01 \x01(\x0b\x32+.rv.data.API_v1_Presentation_Request.ActiveH\x00\x12\x44\n\x07\x66ocused\x18\x02 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12\x46\n\x0bslide_index\x18\x03 \x01(\x0b\x32/.rv.data.API_v1_Presentation_Request.SlideIndexH\x00\x12\x46\n\x0b\x63hord_chart\x18\x04 \x01(\x0b\x32/.rv.data.API_v1_Presentation_Request.ChordChartH\x00\x12U\n\x13\x63hord_chart_updates\x18\x05 \x01(\x0b\x32\x36.rv.data.API_v1_Presentation_Request.ChordChartUpdatesH\x00\x12I\n\x0cpresentation\x18\x06 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.PresentationH\x00\x12V\n\x13\x64\x65lete_presentation\x18\x07 \x01(\x0b\x32\x37.rv.data.API_v1_Presentation_Request.DeletePresentationH\x00\x12T\n\x12timeline_operation\x18\x08 \x01(\x0b\x32\x36.rv.data.API_v1_Presentation_Request.TimelineOperationH\x00\x12z\n&active_presentation_timeline_operation\x18\t \x01(\x0b\x32H.rv.data.API_v1_Presentation_Request.ActivePresentationTimelineOperationH\x00\x12|\n\'focused_presentation_timeline_operation\x18\n \x01(\x0b\x32I.rv.data.API_v1_Presentation_Request.FocusedPresentationTimelineOperationH\x00\x12t\n#active_presentation_timeline_status\x18\x0b \x01(\x0b\x32\x45.rv.data.API_v1_Presentation_Request.ActivePresentationTimelineStatusH\x00\x12v\n$focused_presentation_timeline_status\x18\x0c \x01(\x0b\x32\x46.rv.data.API_v1_Presentation_Request.FocusedPresentationTimelineStatusH\x00\x12\x43\n\tthumbnail\x18\r \x01(\x0b\x32..rv.data.API_v1_Presentation_Request.ThumbnailH\x00\x12\x42\n\x05\x66ocus\x18\x0e \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.FocusMessageH\x00\x12\x46\n\x07trigger\x18\x0f \x01(\x0b\x32\x33.rv.data.API_v1_Presentation_Request.TriggerMessageH\x00\x1a\x08\n\x06\x41\x63tive\x1a\x0c\n\nSlideIndex\x1a\x1d\n\nChordChart\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x1a\x13\n\x11\x43hordChartUpdates\x1a+\n\x0cPresentation\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x1a\x31\n\x12\x44\x65letePresentation\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x1a\x66\n\x11TimelineOperation\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x34\n\toperation\x18\x02 \x01(\x0e\x32!.rv.data.API_v1_TimelineOperation\x1a[\n#ActivePresentationTimelineOperation\x12\x34\n\toperation\x18\x01 \x01(\x0e\x32!.rv.data.API_v1_TimelineOperation\x1a\\\n$FocusedPresentationTimelineOperation\x12\x34\n\toperation\x18\x01 \x01(\x0e\x32!.rv.data.API_v1_TimelineOperation\x1a\"\n ActivePresentationTimelineStatus\x1a#\n!FocusedPresentationTimelineStatus\x1a\x7f\n\tThumbnail\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x11\n\tcue_index\x18\x02 \x01(\r\x12\x0f\n\x07quality\x18\x03 \x01(\x05\x12\x31\n\x0c\x63ontent_type\x18\x04 \x01(\x0e\x32\x1b.rv.data.API_v1_ContentType\x1a\x0e\n\x0c\x45mptyMessage\x1a\xfd\x01\n\x0c\x46ocusMessage\x12\x41\n\x04next\x18\x01 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12\x45\n\x08previous\x18\x02 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12\x43\n\x06\x61\x63tive\x18\x03 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12\x0e\n\x04uuid\x18\x04 \x01(\tH\x00\x42\x0e\n\x0cPresentation\x1a\x8c\x04\n\x0eTriggerMessage\x12\x44\n\x07\x66ocused\x18\x01 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12\x43\n\x06\x61\x63tive\x18\x02 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x00\x12,\n\x04uuid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12\x42\n\x05\x66irst\x18\x04 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x01\x12\x41\n\x04next\x18\x05 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x01\x12\x45\n\x08previous\x18\x06 \x01(\x0b\x32\x31.rv.data.API_v1_Presentation_Request.EmptyMessageH\x01\x12-\n\x05index\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x01\x12-\n\x05group\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x42\x0e\n\x0cPresentationB\x05\n\x03\x43ueB\t\n\x07Request\"\xc0\x11\n\x1c\x41PI_v1_Presentation_Response\x12>\n\x06\x61\x63tive\x18\x01 \x01(\x0b\x32,.rv.data.API_v1_Presentation_Response.ActiveH\x00\x12G\n\x0bslide_index\x18\x02 \x01(\x0b\x32\x30.rv.data.API_v1_Presentation_Response.SlideIndexH\x00\x12G\n\x0b\x63hord_chart\x18\x03 \x01(\x0b\x32\x30.rv.data.API_v1_Presentation_Response.ChordChartH\x00\x12U\n\x12\x63hord_chart_update\x18\x04 \x01(\x0b\x32\x37.rv.data.API_v1_Presentation_Response.ChordChartUpdatesH\x00\x12J\n\x0cpresentation\x18\x05 \x01(\x0b\x32\x32.rv.data.API_v1_Presentation_Response.PresentationH\x00\x12W\n\x13\x64\x65lete_presentation\x18\x06 \x01(\x0b\x32\x38.rv.data.API_v1_Presentation_Response.DeletePresentationH\x00\x12Y\n\x14trigger_presentation\x18\x07 \x01(\x0b\x32\x39.rv.data.API_v1_Presentation_Response.TriggerPresentationH\x00\x12G\n\x0btrigger_cue\x18\x08 \x01(\x0b\x32\x30.rv.data.API_v1_Presentation_Response.TriggerCueH\x00\x12U\n\x12timeline_operation\x18\t \x01(\x0b\x32\x37.rv.data.API_v1_Presentation_Response.TimelineOperationH\x00\x12{\n&active_presentation_timeline_operation\x18\n \x01(\x0b\x32I.rv.data.API_v1_Presentation_Response.ActivePresentationTimelineOperationH\x00\x12}\n\'focused_presentation_timeline_operation\x18\x0b \x01(\x0b\x32J.rv.data.API_v1_Presentation_Response.FocusedPresentationTimelineOperationH\x00\x12u\n#active_presentation_timeline_status\x18\x0c \x01(\x0b\x32\x46.rv.data.API_v1_Presentation_Response.ActivePresentationTimelineStatusH\x00\x12w\n$focused_presentation_timeline_status\x18\r \x01(\x0b\x32G.rv.data.API_v1_Presentation_Response.FocusedPresentationTimelineStatusH\x00\x12\x44\n\tthumbnail\x18\x0e \x01(\x0b\x32/.rv.data.API_v1_Presentation_Response.ThumbnailH\x00\x12@\n\x07\x66ocused\x18\x0f \x01(\x0b\x32-.rv.data.API_v1_Presentation_Response.FocusedH\x00\x12\x43\n\x05\x66ocus\x18\x10 \x01(\x0b\x32\x32.rv.data.API_v1_Presentation_Response.EmptyMessageH\x00\x12\x45\n\x07trigger\x18\x11 \x01(\x0b\x32\x32.rv.data.API_v1_Presentation_Response.EmptyMessageH\x00\x1a<\n\x06\x41\x63tive\x12\x32\n\x0cpresentation\x18\x01 \x01(\x0b\x32\x1c.rv.data.API_v1_Presentation\x1a\x44\n\nSlideIndex\x12\x36\n\x12presentation_index\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_SlideIndex\x1a!\n\nChordChart\x12\x13\n\x0b\x63hord_chart\x18\x01 \x01(\x0c\x1a\x13\n\x11\x43hordChartUpdates\x1a\x42\n\x0cPresentation\x12\x32\n\x0cpresentation\x18\x01 \x01(\x0b\x32\x1c.rv.data.API_v1_Presentation\x1a\x14\n\x12\x44\x65letePresentation\x1a\x15\n\x13TriggerPresentation\x1a\x0c\n\nTriggerCue\x1a\x13\n\x11TimelineOperation\x1a%\n#ActivePresentationTimelineOperation\x1a&\n$FocusedPresentationTimelineOperation\x1aL\n ActivePresentationTimelineStatus\x12\x12\n\nis_running\x18\x01 \x01(\x08\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x01\x1aM\n!FocusedPresentationTimelineStatus\x12\x12\n\nis_running\x18\x01 \x01(\x08\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x01\x1aL\n\tThumbnail\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x31\n\x0c\x63ontent_type\x18\x02 \x01(\x0e\x32\x1b.rv.data.API_v1_ContentType\x1a\x31\n\x07\x46ocused\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\x0e\n\x0c\x45mptyMessageB\n\n\x08ResponseB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Presentation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_API_V1_SLIDEINDEX']._serialized_start=210
  _globals['_API_V1_SLIDEINDEX']._serialized_end=297
  _globals['_API_V1_PRESENTATION']._serialized_start=300
  _globals['_API_V1_PRESENTATION']._serialized_end=818
  _globals['_API_V1_PRESENTATION_SLIDEGROUP']._serialized_start=533
  _globals['_API_V1_PRESENTATION_SLIDEGROUP']._serialized_end=766
  _globals['_API_V1_PRESENTATION_SLIDEGROUP_SLIDE']._serialized_start=662
  _globals['_API_V1_PRESENTATION_SLIDEGROUP_SLIDE']._serialized_end=766
  _globals['_API_V1_PRESENTATION_DESTINATION']._serialized_start=768
  _globals['_API_V1_PRESENTATION_DESTINATION']._serialized_end=818
  _globals['_API_V1_PRESENTATION_REQUEST']._serialized_start=821
  _globals['_API_V1_PRESENTATION_REQUEST']._serialized_end=3635
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVE']._serialized_start=2162
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVE']._serialized_end=2170
  _globals['_API_V1_PRESENTATION_REQUEST_SLIDEINDEX']._serialized_start=2172
  _globals['_API_V1_PRESENTATION_REQUEST_SLIDEINDEX']._serialized_end=2184
  _globals['_API_V1_PRESENTATION_REQUEST_CHORDCHART']._serialized_start=2186
  _globals['_API_V1_PRESENTATION_REQUEST_CHORDCHART']._serialized_end=2215
  _globals['_API_V1_PRESENTATION_REQUEST_CHORDCHARTUPDATES']._serialized_start=2217
  _globals['_API_V1_PRESENTATION_REQUEST_CHORDCHARTUPDATES']._serialized_end=2236
  _globals['_API_V1_PRESENTATION_REQUEST_PRESENTATION']._serialized_start=2238
  _globals['_API_V1_PRESENTATION_REQUEST_PRESENTATION']._serialized_end=2281
  _globals['_API_V1_PRESENTATION_REQUEST_DELETEPRESENTATION']._serialized_start=2283
  _globals['_API_V1_PRESENTATION_REQUEST_DELETEPRESENTATION']._serialized_end=2332
  _globals['_API_V1_PRESENTATION_REQUEST_TIMELINEOPERATION']._serialized_start=2334
  _globals['_API_V1_PRESENTATION_REQUEST_TIMELINEOPERATION']._serialized_end=2436
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVEPRESENTATIONTIMELINEOPERATION']._serialized_start=2438
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVEPRESENTATIONTIMELINEOPERATION']._serialized_end=2529
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSEDPRESENTATIONTIMELINEOPERATION']._serialized_start=2531
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSEDPRESENTATIONTIMELINEOPERATION']._serialized_end=2623
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVEPRESENTATIONTIMELINESTATUS']._serialized_start=2625
  _globals['_API_V1_PRESENTATION_REQUEST_ACTIVEPRESENTATIONTIMELINESTATUS']._serialized_end=2659
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSEDPRESENTATIONTIMELINESTATUS']._serialized_start=2661
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSEDPRESENTATIONTIMELINESTATUS']._serialized_end=2696
  _globals['_API_V1_PRESENTATION_REQUEST_THUMBNAIL']._serialized_start=2698
  _globals['_API_V1_PRESENTATION_REQUEST_THUMBNAIL']._serialized_end=2825
  _globals['_API_V1_PRESENTATION_REQUEST_EMPTYMESSAGE']._serialized_start=2827
  _globals['_API_V1_PRESENTATION_REQUEST_EMPTYMESSAGE']._serialized_end=2841
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSMESSAGE']._serialized_start=2844
  _globals['_API_V1_PRESENTATION_REQUEST_FOCUSMESSAGE']._serialized_end=3097
  _globals['_API_V1_PRESENTATION_REQUEST_TRIGGERMESSAGE']._serialized_start=3100
  _globals['_API_V1_PRESENTATION_REQUEST_TRIGGERMESSAGE']._serialized_end=3624
  _globals['_API_V1_PRESENTATION_RESPONSE']._serialized_start=3638
  _globals['_API_V1_PRESENTATION_RESPONSE']._serialized_end=5878
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVE']._serialized_start=5151
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVE']._serialized_end=5211
  _globals['_API_V1_PRESENTATION_RESPONSE_SLIDEINDEX']._serialized_start=5213
  _globals['_API_V1_PRESENTATION_RESPONSE_SLIDEINDEX']._serialized_end=5281
  _globals['_API_V1_PRESENTATION_RESPONSE_CHORDCHART']._serialized_start=5283
  _globals['_API_V1_PRESENTATION_RESPONSE_CHORDCHART']._serialized_end=5316
  _globals['_API_V1_PRESENTATION_RESPONSE_CHORDCHARTUPDATES']._serialized_start=2217
  _globals['_API_V1_PRESENTATION_RESPONSE_CHORDCHARTUPDATES']._serialized_end=2236
  _globals['_API_V1_PRESENTATION_RESPONSE_PRESENTATION']._serialized_start=5339
  _globals['_API_V1_PRESENTATION_RESPONSE_PRESENTATION']._serialized_end=5405
  _globals['_API_V1_PRESENTATION_RESPONSE_DELETEPRESENTATION']._serialized_start=2283
  _globals['_API_V1_PRESENTATION_RESPONSE_DELETEPRESENTATION']._serialized_end=2303
  _globals['_API_V1_PRESENTATION_RESPONSE_TRIGGERPRESENTATION']._serialized_start=5429
  _globals['_API_V1_PRESENTATION_RESPONSE_TRIGGERPRESENTATION']._serialized_end=5450
  _globals['_API_V1_PRESENTATION_RESPONSE_TRIGGERCUE']._serialized_start=5452
  _globals['_API_V1_PRESENTATION_RESPONSE_TRIGGERCUE']._serialized_end=5464
  _globals['_API_V1_PRESENTATION_RESPONSE_TIMELINEOPERATION']._serialized_start=2334
  _globals['_API_V1_PRESENTATION_RESPONSE_TIMELINEOPERATION']._serialized_end=2353
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVEPRESENTATIONTIMELINEOPERATION']._serialized_start=2438
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVEPRESENTATIONTIMELINEOPERATION']._serialized_end=2475
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSEDPRESENTATIONTIMELINEOPERATION']._serialized_start=2531
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSEDPRESENTATIONTIMELINEOPERATION']._serialized_end=2569
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVEPRESENTATIONTIMELINESTATUS']._serialized_start=5566
  _globals['_API_V1_PRESENTATION_RESPONSE_ACTIVEPRESENTATIONTIMELINESTATUS']._serialized_end=5642
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSEDPRESENTATIONTIMELINESTATUS']._serialized_start=5644
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSEDPRESENTATIONTIMELINESTATUS']._serialized_end=5721
  _globals['_API_V1_PRESENTATION_RESPONSE_THUMBNAIL']._serialized_start=5723
  _globals['_API_V1_PRESENTATION_RESPONSE_THUMBNAIL']._serialized_end=5799
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSED']._serialized_start=5801
  _globals['_API_V1_PRESENTATION_RESPONSE_FOCUSED']._serialized_end=5850
  _globals['_API_V1_PRESENTATION_RESPONSE_EMPTYMESSAGE']._serialized_start=2827
  _globals['_API_V1_PRESENTATION_RESPONSE_EMPTYMESSAGE']._serialized_end=2841
# @@protoc_insertion_point(module_scope)
