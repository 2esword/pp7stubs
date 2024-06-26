# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: graphicsData.proto
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
    'graphicsData.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import alphaType_pb2 as alphaType__pb2
from . import color_pb2 as color__pb2
from . import digitalAudio_pb2 as digitalAudio__pb2
from . import effects_pb2 as effects__pb2
from . import fileProperties_pb2 as fileProperties__pb2
from . import font_pb2 as font__pb2
from . import intRange_pb2 as intRange__pb2
from . import url_pb2 as url__pb2
from . import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12graphicsData.proto\x12\x07rv.data\x1a\x0f\x61lphaType.proto\x1a\x0b\x63olor.proto\x1a\x12\x64igitalAudio.proto\x1a\reffects.proto\x1a\x14\x66ileProperties.proto\x1a\nfont.proto\x1a\x0eintRange.proto\x1a\turl.proto\x1a\nuuid.proto\"\xab@\n\x08Graphics\x1a\x91\x05\n\x07\x45lement\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x06\x62ounds\x18\x03 \x01(\x0b\x32\x16.rv.data.Graphics.Rect\x12\x10\n\x08rotation\x18\x04 \x01(\x01\x12\x0f\n\x07opacity\x18\x05 \x01(\x01\x12\x0e\n\x06locked\x18\x06 \x01(\x08\x12\x1b\n\x13\x61spect_ratio_locked\x18\x07 \x01(\x08\x12$\n\x04path\x18\x08 \x01(\x0b\x32\x16.rv.data.Graphics.Path\x12$\n\x04\x66ill\x18\t \x01(\x0b\x32\x16.rv.data.Graphics.Fill\x12(\n\x06stroke\x18\n \x01(\x0b\x32\x18.rv.data.Graphics.Stroke\x12(\n\x06shadow\x18\x0b \x01(\x0b\x32\x18.rv.data.Graphics.Shadow\x12*\n\x07\x66\x65\x61ther\x18\x0c \x01(\x0b\x32\x19.rv.data.Graphics.Feather\x12$\n\x04text\x18\r \x01(\x0b\x32\x16.rv.data.Graphics.Text\x12\x34\n\x08\x66lipMode\x18\x0f \x01(\x0e\x32\".rv.data.Graphics.Element.FlipMode\x12\x0e\n\x06hidden\x18\x10 \x01(\x08\x12=\n\x0etext_line_mask\x18\x0e \x01(\x0b\x32#.rv.data.Graphics.Text.LineFillMaskH\x00\"d\n\x08\x46lipMode\x12\x12\n\x0e\x46LIP_MODE_NONE\x10\x00\x12\x16\n\x12\x46LIP_MODE_VERTICAL\x10\x01\x12\x18\n\x14\x46LIP_MODE_HORIZONTAL\x10\x02\x12\x12\n\x0e\x46LIP_MODE_BOTH\x10\x03\x42\x06\n\x04Mask\x1aU\n\x04Rect\x12\'\n\x06origin\x18\x01 \x01(\x0b\x32\x17.rv.data.Graphics.Point\x12$\n\x04size\x18\x02 \x01(\x0b\x32\x16.rv.data.Graphics.Size\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x01\x12\x0e\n\x06height\x18\x02 \x01(\x01\x1a\x46\n\nEdgeInsets\x12\x0c\n\x04left\x18\x01 \x01(\x01\x12\r\n\x05right\x18\x02 \x01(\x01\x12\x0b\n\x03top\x18\x03 \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x01\x1a\xf6\x07\n\x04Path\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x32\n\x06points\x18\x02 \x03(\x0b\x32\".rv.data.Graphics.Path.BezierPoint\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.rv.data.Graphics.Path.Shape\x1a\x8f\x01\n\x0b\x42\x65zierPoint\x12&\n\x05point\x18\x01 \x01(\x0b\x32\x17.rv.data.Graphics.Point\x12#\n\x02q0\x18\x02 \x01(\x0b\x32\x17.rv.data.Graphics.Point\x12#\n\x02q1\x18\x03 \x01(\x0b\x32\x17.rv.data.Graphics.Point\x12\x0e\n\x06\x63urved\x18\x04 \x01(\x08\x1a\xea\x05\n\x05Shape\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.rv.data.Graphics.Path.Shape.Type\x12J\n\x11rounded_rectangle\x18\x02 \x01(\x0b\x32-.rv.data.Graphics.Path.Shape.RoundedRectangleH\x00\x12\x37\n\x07polygon\x18\x03 \x01(\x0b\x32$.rv.data.Graphics.Path.Shape.PolygonH\x00\x12\x31\n\x04star\x18\x04 \x01(\x0b\x32!.rv.data.Graphics.Path.Shape.StarH\x00\x12\x33\n\x05\x61rrow\x18\x05 \x01(\x0b\x32\".rv.data.Graphics.Path.Shape.ArrowH\x00\x1a%\n\x10RoundedRectangle\x12\x11\n\troundness\x18\x01 \x01(\x01\x1a\x30\n\x05\x41rrow\x12\'\n\x06\x63orner\x18\x01 \x01(\x0b\x32\x17.rv.data.Graphics.Point\x1a\x1f\n\x07Polygon\x12\x14\n\x0cnumber_sides\x18\x01 \x01(\r\x1a\x33\n\x04Star\x12\x14\n\x0cinner_radius\x18\x01 \x01(\x01\x12\x15\n\rnumber_points\x18\x02 \x01(\r\"\x81\x02\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x12\n\x0eTYPE_RECTANGLE\x10\x01\x12\x10\n\x0cTYPE_ELLIPSE\x10\x02\x12\x1b\n\x17TYPE_ISOSCELES_TRIANGLE\x10\x03\x12\x17\n\x13TYPE_RIGHT_TRIANGLE\x10\x04\x12\x10\n\x0cTYPE_RHOMBUS\x10\x05\x12\r\n\tTYPE_STAR\x10\x06\x12\x10\n\x0cTYPE_POLYGON\x10\x07\x12\x0f\n\x0bTYPE_CUSTOM\x10\x08\x12\x14\n\x10TYPE_RIGHT_ARROW\x10\t\x12\x15\n\x11TYPE_DOUBLE_ARROW\x10\n\x12\x1a\n\x16TYPE_ROUNDED_RECTANGLE\x10\x0b\x42\x10\n\x0e\x41\x64\x64itionalData\x1a\xd4\x01\n\x04\x46ill\x12\x0e\n\x06\x65nable\x18\x04 \x01(\x08\x12\x1f\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.ColorH\x00\x12.\n\x08gradient\x18\x02 \x01(\x0b\x32\x1a.rv.data.Graphics.GradientH\x00\x12\x1f\n\x05media\x18\x03 \x01(\x0b\x32\x0e.rv.data.MediaH\x00\x12>\n\x10\x62\x61\x63kgroundEffect\x18\x05 \x01(\x0b\x32\".rv.data.Graphics.BackgroundEffectH\x00\x42\n\n\x08\x46illType\x1a\xb2\x02\n\x10\x42\x61\x63kgroundEffect\x12Q\n\x0e\x62\x61\x63kgroundBlur\x18\x02 \x01(\x0b\x32\x37.rv.data.Graphics.BackgroundEffect.BackgroundEffectBlurH\x00\x12U\n\x10\x62\x61\x63kgroundInvert\x18\x03 \x01(\x0b\x32\x39.rv.data.Graphics.BackgroundEffect.BackgroundEffectInvertH\x00\x1a?\n\x14\x42\x61\x63kgroundEffectBlur\x12\x12\n\nsaturation\x18\x01 \x01(\x01\x12\x13\n\x0b\x62lur_amount\x18\x02 \x01(\x01\x1a\x18\n\x16\x42\x61\x63kgroundEffectInvertB\x0c\n\nEffectTypeJ\x04\x08\x01\x10\x02R\x05layer\x1a\x9a\x02\n\x08Gradient\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.rv.data.Graphics.Gradient.Type\x12\r\n\x05\x61ngle\x18\x02 \x01(\x01\x12\x0e\n\x06length\x18\x03 \x01(\x01\x12\x33\n\x05stops\x18\x04 \x03(\x0b\x32$.rv.data.Graphics.Gradient.ColorStop\x1aQ\n\tColorStop\x12\x1d\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.Color\x12\x10\n\x08position\x18\x02 \x01(\x01\x12\x13\n\x0b\x62lend_point\x18\x03 \x01(\x01\"8\n\x04Type\x12\x0f\n\x0bTYPE_LINEAR\x10\x00\x12\x0f\n\x0bTYPE_RADIAL\x10\x01\x12\x0e\n\nTYPE_ANGLE\x10\x02\x1a\xbf\x01\n\x06Shadow\x12-\n\x05style\x18\x01 \x01(\x0e\x32\x1e.rv.data.Graphics.Shadow.Style\x12\r\n\x05\x61ngle\x18\x02 \x01(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x12\x0e\n\x06radius\x18\x04 \x01(\x01\x12\x1d\n\x05\x63olor\x18\x05 \x01(\x0b\x32\x0e.rv.data.Color\x12\x0f\n\x07opacity\x18\x06 \x01(\x01\x12\x0e\n\x06\x65nable\x18\x07 \x01(\x08\"\x17\n\x05Style\x12\x0e\n\nSTYLE_DROP\x10\x00\x1a\xe7\x01\n\x06Stroke\x12-\n\x05style\x18\x01 \x01(\x0e\x32\x1e.rv.data.Graphics.Stroke.Style\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x1d\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x0e.rv.data.Color\x12\x0f\n\x07pattern\x18\x04 \x03(\x01\x12\x0e\n\x06\x65nable\x18\x05 \x01(\x08\"_\n\x05Style\x12\x14\n\x10STYLE_SOLID_LINE\x10\x00\x12\x15\n\x11STYLE_SQUARE_DASH\x10\x01\x12\x14\n\x10STYLE_SHORT_DASH\x10\x02\x12\x13\n\x0fSTYLE_LONG_DASH\x10\x03\x1a\x99\x01\n\x07\x46\x65\x61ther\x12.\n\x05style\x18\x01 \x01(\x0e\x32\x1f.rv.data.Graphics.Feather.Style\x12\x0e\n\x06radius\x18\x02 \x01(\x01\x12\x0e\n\x06\x65nable\x18\x03 \x01(\x08\">\n\x05Style\x12\x10\n\x0cSTYLE_INSIDE\x10\x00\x12\x10\n\x0cSTYLE_CENTER\x10\x01\x12\x11\n\rSTYLE_OUTSIDE\x10\x02\x1a\xbb&\n\x04Text\x12\x35\n\nattributes\x18\x03 \x01(\x0b\x32!.rv.data.Graphics.Text.Attributes\x12(\n\x06shadow\x18\x04 \x01(\x0b\x32\x18.rv.data.Graphics.Shadow\x12\x10\n\x08rtf_data\x18\x05 \x01(\x0c\x12\x44\n\x12vertical_alignment\x18\x06 \x01(\x0e\x32(.rv.data.Graphics.Text.VerticalAlignment\x12<\n\x0escale_behavior\x18\x07 \x01(\x0e\x32$.rv.data.Graphics.Text.ScaleBehavior\x12-\n\x07margins\x18\x08 \x01(\x0b\x32\x1c.rv.data.Graphics.EdgeInsets\x12#\n\x1bis_superscript_standardized\x18\t \x01(\x08\x12\x33\n\ttransform\x18\n \x01(\x0e\x32 .rv.data.Graphics.Text.Transform\x12\x1a\n\x12transformDelimiter\x18\x0b \x01(\t\x12\x32\n\tchord_pro\x18\x0c \x01(\x0b\x32\x1f.rv.data.Graphics.Text.ChordPro\x1a\xbc\x02\n\x0cLineFillMask\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x15\n\rheight_offset\x18\x02 \x01(\x01\x12\x17\n\x0fvertical_offset\x18\x03 \x01(\x01\x12\x45\n\nmask_style\x18\x04 \x01(\x0e\x32\x31.rv.data.Graphics.Text.LineFillMask.LineMaskStyle\x12\x14\n\x0cwidth_offset\x18\x05 \x01(\x01\x12\x19\n\x11horizontal_offset\x18\x06 \x01(\x01\"s\n\rLineMaskStyle\x12\x1e\n\x1aLINE_MASK_STYLE_FULL_WIDTH\x10\x00\x12\x1e\n\x1aLINE_MASK_STYLE_LINE_WIDTH\x10\x01\x12\"\n\x1eLINE_MASK_STYLE_MAX_LINE_WIDTH\x10\x02\x1a`\n\x0cGradientFill\x12,\n\x08gradient\x18\x01 \x01(\x0b\x32\x1a.rv.data.Graphics.Gradient\x12\"\n\x1astretch_to_document_bounds\x18\x02 \x01(\x08\x1a\x0c\n\nCutOutFill\x1a*\n\tMediaFill\x12\x1d\n\x05media\x18\x01 \x01(\x0b\x32\x0e.rv.data.Media\x1a\xdb\x01\n\x08\x43hordPro\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12:\n\x08notation\x18\x02 \x01(\x0e\x32(.rv.data.Graphics.Text.ChordPro.Notation\x12\x1d\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x0e.rv.data.Color\"c\n\x08Notation\x12\x13\n\x0fNOTATION_CHORDS\x10\x00\x12\x14\n\x10NOTATION_NUMBERS\x10\x01\x12\x15\n\x11NOTATION_NUMERALS\x10\x02\x12\x15\n\x11NOTATION_DO_RE_MI\x10\x03\x1a\xc2\x19\n\nAttributes\x12\x1b\n\x04\x66ont\x18\x01 \x01(\x0b\x32\r.rv.data.Font\x12H\n\x0e\x63\x61pitalization\x18\x02 \x01(\x0e\x32\x30.rv.data.Graphics.Text.Attributes.Capitalization\x12\x44\n\x0funderline_style\x18\x04 \x01(\x0b\x32+.rv.data.Graphics.Text.Attributes.Underline\x12\'\n\x0funderline_color\x18\x05 \x01(\x0b\x32\x0e.rv.data.Color\x12\x44\n\x0fparagraph_style\x18\x06 \x01(\x0b\x32+.rv.data.Graphics.Text.Attributes.Paragraph\x12\x0f\n\x07kerning\x18\x07 \x01(\x01\x12\x13\n\x0bsuperscript\x18\x08 \x01(\x05\x12H\n\x13strikethrough_style\x18\t \x01(\x0b\x32+.rv.data.Graphics.Text.Attributes.Underline\x12+\n\x13strikethrough_color\x18\n \x01(\x0b\x32\x0e.rv.data.Color\x12\x14\n\x0cstroke_width\x18\x0b \x01(\x01\x12$\n\x0cstroke_color\x18\x0c \x01(\x0b\x32\x0e.rv.data.Color\x12L\n\x11\x63ustom_attributes\x18\r \x03(\x0b\x32\x31.rv.data.Graphics.Text.Attributes.CustomAttribute\x12(\n\x10\x62\x61\x63kground_color\x18\x0f \x01(\x0b\x32\x0e.rv.data.Color\x12)\n\x0ftext_solid_fill\x18\x03 \x01(\x0b\x32\x0e.rv.data.ColorH\x00\x12\x41\n\x12text_gradient_fill\x18\x0e \x01(\x0b\x32#.rv.data.Graphics.Text.GradientFillH\x00\x12\x39\n\x0c\x63ut_out_fill\x18\x10 \x01(\x0b\x32!.rv.data.Graphics.Text.CutOutFillH\x00\x12\x36\n\nmedia_fill\x18\x11 \x01(\x0b\x32 .rv.data.Graphics.Text.MediaFillH\x00\x12?\n\x11\x62\x61\x63kground_effect\x18\x12 \x01(\x0b\x32\".rv.data.Graphics.BackgroundEffectH\x00\x1a\xe3\x02\n\tUnderline\x12@\n\x05style\x18\x01 \x01(\x0e\x32\x31.rv.data.Graphics.Text.Attributes.Underline.Style\x12\x44\n\x07pattern\x18\x02 \x01(\x0e\x32\x33.rv.data.Graphics.Text.Attributes.Underline.Pattern\x12\x0f\n\x07\x62y_word\x18\x03 \x01(\x08\"L\n\x05Style\x12\x0e\n\nSTYLE_NONE\x10\x00\x12\x10\n\x0cSTYLE_SINGLE\x10\x01\x12\x0f\n\x0bSTYLE_THICK\x10\x02\x12\x10\n\x0cSTYLE_DOUBLE\x10\x03\"o\n\x07Pattern\x12\x11\n\rPATTERN_SOLID\x10\x00\x12\x0f\n\x0bPATTERN_DOT\x10\x01\x12\x10\n\x0cPATTERN_DASH\x10\x02\x12\x14\n\x10PATTERN_DASH_DOT\x10\x03\x12\x18\n\x14PATTERN_DASH_DOT_DOT\x10\x04\x1a\x96\t\n\tParagraph\x12>\n\talignment\x18\x01 \x01(\x0e\x32+.rv.data.Graphics.Text.Attributes.Alignment\x12\x1e\n\x16\x66irst_line_head_indent\x18\x02 \x01(\x01\x12\x13\n\x0bhead_indent\x18\x03 \x01(\x01\x12\x13\n\x0btail_indent\x18\x04 \x01(\x01\x12\x1c\n\x14line_height_multiple\x18\x05 \x01(\x01\x12\x1b\n\x13maximum_line_height\x18\x06 \x01(\x01\x12\x1b\n\x13minimum_line_height\x18\x07 \x01(\x01\x12\x14\n\x0cline_spacing\x18\x08 \x01(\x01\x12\x19\n\x11paragraph_spacing\x18\t \x01(\x01\x12 \n\x18paragraph_spacing_before\x18\n \x01(\x01\x12\x46\n\ttab_stops\x18\x0b \x03(\x0b\x32\x33.rv.data.Graphics.Text.Attributes.Paragraph.TabStop\x12\x1c\n\x14\x64\x65\x66\x61ult_tab_interval\x18\x0c \x01(\x01\x12G\n\ttext_list\x18\r \x01(\x0b\x32\x34.rv.data.Graphics.Text.Attributes.Paragraph.TextList\x12H\n\ntext_lists\x18\x0e \x03(\x0b\x32\x34.rv.data.Graphics.Text.Attributes.Paragraph.TextList\x1a[\n\x07TabStop\x12\x10\n\x08location\x18\x01 \x01(\x01\x12>\n\talignment\x18\x02 \x01(\x0e\x32+.rv.data.Graphics.Text.Attributes.Alignment\x1a\xfd\x03\n\x08TextList\x12\x12\n\nis_enabled\x18\x01 \x01(\x08\x12T\n\x0bnumber_type\x18\x02 \x01(\x0e\x32?.rv.data.Graphics.Text.Attributes.Paragraph.TextList.NumberType\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x0f\n\x07postfix\x18\x04 \x01(\t\x12\x17\n\x0fstarting_number\x18\x05 \x01(\x05\"\xcc\x02\n\nNumberType\x12\x13\n\x0fNUMBER_TYPE_BOX\x10\x00\x12\x15\n\x11NUMBER_TYPE_CHECK\x10\x01\x12\x16\n\x12NUMBER_TYPE_CIRCLE\x10\x02\x12\x17\n\x13NUMBER_TYPE_DIAMOND\x10\x03\x12\x14\n\x10NUMBER_TYPE_DISC\x10\x04\x12\x16\n\x12NUMBER_TYPE_HYPHEN\x10\x05\x12\x16\n\x12NUMBER_TYPE_SQUARE\x10\x06\x12\x17\n\x13NUMBER_TYPE_DECIMAL\x10\x07\x12\x1f\n\x1bNUMBER_TYPE_LOWERCASE_ALPHA\x10\x08\x12\x1f\n\x1bNUMBER_TYPE_UPPERCASE_ALPHA\x10\t\x12\x1f\n\x1bNUMBER_TYPE_LOWERCASE_ROMAN\x10\n\x12\x1f\n\x1bNUMBER_TYPE_UPPERCASE_ROMAN\x10\x0b\x1a\xfb\x03\n\x0f\x43ustomAttribute\x12 \n\x05range\x18\x01 \x01(\x0b\x32\x11.rv.data.IntRange\x12J\n\x0e\x63\x61pitalization\x18\x02 \x01(\x0e\x32\x30.rv.data.Graphics.Text.Attributes.CapitalizationH\x00\x12\x1c\n\x12original_font_size\x18\x03 \x01(\x01H\x00\x12\x1b\n\x11\x66ont_scale_factor\x18\x04 \x01(\x01H\x00\x12\x41\n\x12text_gradient_fill\x18\x05 \x01(\x0b\x32#.rv.data.Graphics.Text.GradientFillH\x00\x12*\n should_preserve_foreground_color\x18\x06 \x01(\x08H\x00\x12\x0f\n\x05\x63hord\x18\x07 \x01(\tH\x00\x12\x39\n\x0c\x63ut_out_fill\x18\x08 \x01(\x0b\x32!.rv.data.Graphics.Text.CutOutFillH\x00\x12\x36\n\nmedia_fill\x18\t \x01(\x0b\x32 .rv.data.Graphics.Text.MediaFillH\x00\x12?\n\x11\x62\x61\x63kground_effect\x18\n \x01(\x0b\x32\".rv.data.Graphics.BackgroundEffectH\x00\x42\x0b\n\tAttribute\"\xa3\x01\n\x0e\x43\x61pitalization\x12\x17\n\x13\x43\x41PITALIZATION_NONE\x10\x00\x12\x1b\n\x17\x43\x41PITALIZATION_ALL_CAPS\x10\x01\x12\x1d\n\x19\x43\x41PITALIZATION_SMALL_CAPS\x10\x02\x12\x1d\n\x19\x43\x41PITALIZATION_TITLE_CASE\x10\x03\x12\x1d\n\x19\x43\x41PITALIZATION_START_CASE\x10\x04\"z\n\tAlignment\x12\x12\n\x0e\x41LIGNMENT_LEFT\x10\x00\x12\x13\n\x0f\x41LIGNMENT_RIGHT\x10\x01\x12\x14\n\x10\x41LIGNMENT_CENTER\x10\x02\x12\x17\n\x13\x41LIGNMENT_JUSTIFIED\x10\x03\x12\x15\n\x11\x41LIGNMENT_NATURAL\x10\x04\x42\x06\n\x04\x66ill\"m\n\x11VerticalAlignment\x12\x1a\n\x16VERTICAL_ALIGNMENT_TOP\x10\x00\x12\x1d\n\x19VERTICAL_ALIGNMENT_MIDDLE\x10\x01\x12\x1d\n\x19VERTICAL_ALIGNMENT_BOTTOM\x10\x02\"\xc1\x01\n\rScaleBehavior\x12\x17\n\x13SCALE_BEHAVIOR_NONE\x10\x00\x12*\n&SCALE_BEHAVIOR_ADJUST_CONTAINER_HEIGHT\x10\x01\x12\"\n\x1eSCALE_BEHAVIOR_SCALE_FONT_DOWN\x10\x02\x12 \n\x1cSCALE_BEHAVIOR_SCALE_FONT_UP\x10\x03\x12%\n!SCALE_BEHAVIOR_SCALE_FONT_UP_DOWN\x10\x04\"\xa5\x01\n\tTransform\x12\x12\n\x0eTRANSFORM_NONE\x10\x00\x12\x19\n\x15TRANSFORM_SINGLE_LINE\x10\x01\x12\x1f\n\x1bTRANSFORM_ONE_WORD_PER_LINE\x10\x02\x12$\n TRANSFORM_ONE_CHARACTER_PER_LINE\x10\x03\x12\"\n\x1eTRANSFORM_REPLACE_LINE_RETURNS\x10\x04J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\xf8%\n\x05Media\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x19\n\x03url\x18\x02 \x01(\x0b\x32\x0c.rv.data.URL\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.rv.data.Media.Metadata\x12\x33\n\x05\x61udio\x18\x04 \x01(\x0b\x32\".rv.data.Media.AudioTypePropertiesH\x00\x12\x33\n\x05image\x18\x05 \x01(\x0b\x32\".rv.data.Media.ImageTypePropertiesH\x00\x12\x33\n\x05video\x18\x06 \x01(\x0b\x32\".rv.data.Media.VideoTypePropertiesH\x00\x12<\n\nlive_video\x18\x07 \x01(\x0b\x32&.rv.data.Media.LiveVideoTypePropertiesH\x00\x12>\n\x0bweb_content\x18\x08 \x01(\x0b\x32\'.rv.data.Media.WebContentTypePropertiesH\x00\x1a\x80\x01\n\x08Metadata\x12\x18\n\x10manufacture_name\x18\x01 \x01(\t\x12%\n\x0fmanufacture_url\x18\x02 \x01(\x0b\x32\x0c.rv.data.URL\x12\x13\n\x0binformation\x18\x03 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x1a\xd4\x02\n\x0bVideoDevice\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.rv.data.Media.VideoDevice.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tunique_id\x18\x03 \x01(\t\x12\x10\n\x08model_id\x18\x04 \x01(\t\x12\x14\n\x0c\x66ormat_index\x18\x05 \x01(\r\x12;\n\raudio_routing\x18\x06 \x01(\x0b\x32$.rv.data.DigitalAudio.Device.Routing\"\x8f\x01\n\x04Type\x12\x10\n\x0cTYPE_GENERIC\x10\x00\x12\x13\n\x0fTYPE_DIRECTSHOW\x10\x01\x12\x13\n\x0fTYPE_BLACKMAGIC\x10\x02\x12\x0c\n\x08TYPE_AJA\x10\x03\x12\x0b\n\x07TYPE_AV\x10\x04\x12\x0f\n\x0bTYPE_SYPHON\x10\x05\x12\x0c\n\x08TYPE_NDI\x10\x06\x12\x11\n\rTYPE_BLUEFISH\x10\x07\x1aW\n\x0b\x41udioDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tunique_id\x18\x02 \x01(\t\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x15\n\rchannel_count\x18\x04 \x01(\r\x1a\xb6\x01\n\x05\x41udio\x1a\xac\x01\n\x07\x43hannel\x12\r\n\x05index\x18\x01 \x01(\r\x12\r\n\x05muted\x18\x02 \x01(\x08\x12\x0e\n\x06volume\x18\x03 \x01(\x01\x12\x16\n\x0e\x63ompress_limit\x18\x04 \x01(\x08\x12\x34\n\x07outputs\x18\x05 \x03(\x0b\x32#.rv.data.Media.Audio.Channel.Output\x1a%\n\x06Output\x12\x15\n\rchannel_index\x18\x02 \x01(\x05J\x04\x08\x01\x10\x02\x1ar\n\x0f\x41udioProperties\x12\x0e\n\x06volume\x18\x01 \x01(\x01\x12\x34\n\x0e\x61udio_channels\x18\x02 \x03(\x0b\x32\x1c.rv.data.Media.Audio.Channel\x12\x19\n\x11is_custom_mapping\x18\x03 \x01(\x08\x1a\xf5\x05\n\x13TransportProperties\x12\x11\n\tplay_rate\x18\x01 \x01(\x01\x12\x10\n\x08in_point\x18\x02 \x01(\x01\x12\x11\n\tout_point\x18\x03 \x01(\x01\x12\x18\n\x10\x66\x61\x64\x65_in_duration\x18\x07 \x01(\x01\x12\x19\n\x11\x66\x61\x64\x65_out_duration\x18\x08 \x01(\x01\x12\x16\n\x0eshould_fade_in\x18\t \x01(\x08\x12\x17\n\x0fshould_fade_out\x18\n \x01(\x08\x12\x11\n\tend_point\x18\x0b \x01(\x01\x12N\n\x11playback_behavior\x18\x0c \x01(\x0e\x32\x33.rv.data.Media.TransportProperties.PlaybackBehavior\x12\x11\n\tloop_time\x18\r \x01(\x01\x12\x15\n\rtimes_to_loop\x18\x0e \x01(\r\x12\x46\n\tretrigger\x18\x0f \x01(\x0e\x32\x33.rv.data.Media.TransportProperties.RetriggerSetting\"\x95\x01\n\x10PlaybackBehavior\x12\x1a\n\x16PLAYBACK_BEHAVIOR_STOP\x10\x00\x12\x1a\n\x16PLAYBACK_BEHAVIOR_LOOP\x10\x01\x12$\n PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT\x10\x02\x12#\n\x1fPLAYBACK_BEHAVIOR_LOOP_FOR_TIME\x10\x03\"\x8b\x01\n\x10RetriggerSetting\x12\x1b\n\x17RETRIGGER_SETTING_UNSET\x10\x00\x12\x1c\n\x18RETRIGGER_SETTING_ALWAYS\x10\x01\x12\x1b\n\x17RETRIGGER_SETTING_NEVER\x10\x02\x12\x1f\n\x1bRETRIGGER_SETTING_AUTOMATIC\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07R\x0fstart_ramp_timeR\rend_ramp_timeR\x13\x66\x61\x64\x65_start_position\x1a\xd2\x06\n\x11\x44rawingProperties\x12\x34\n\x0escale_behavior\x18\x01 \x01(\x0e\x32\x1c.rv.data.Media.ScaleBehavior\x12\x12\n\nis_blurred\x18\x10 \x01(\x08\x12\x36\n\x0fscale_alignment\x18\x02 \x01(\x0e\x32\x1d.rv.data.Media.ScaleAlignment\x12\x1c\n\x14\x66lipped_horizontally\x18\x03 \x01(\x08\x12\x1a\n\x12\x66lipped_vertically\x18\x04 \x01(\x08\x12,\n\x0cnatural_size\x18\x05 \x01(\x0b\x32\x16.rv.data.Graphics.Size\x12\x1d\n\x15\x63ustom_image_rotation\x18\x06 \x01(\x01\x12\x33\n\x13\x63ustom_image_bounds\x18\x07 \x01(\x0b\x32\x16.rv.data.Graphics.Rect\x12\"\n\x1a\x63ustom_image_aspect_locked\x18\x08 \x01(\x08\x12\x16\n\x0e\x61lpha_inverted\x18\t \x01(\x08\x12L\n\x0fnative_rotation\x18\n \x01(\x0e\x32\x33.rv.data.Media.DrawingProperties.NativeRotationType\x12\x32\n\x1bselected_effect_preset_uuid\x18\x0b \x01(\x0b\x32\r.rv.data.UUID\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x0c \x03(\x0b\x32\x0f.rv.data.Effect\x12\x13\n\x0b\x63rop_enable\x18\r \x01(\x08\x12\x31\n\x0b\x63rop_insets\x18\x0e \x01(\x0b\x32\x1c.rv.data.Graphics.EdgeInsets\x12&\n\nalpha_type\x18\x0f \x01(\x0e\x32\x12.rv.data.AlphaType\"\xae\x01\n\x12NativeRotationType\x12(\n$NATIVE_ROTATION_TYPE_ROTATE_STANDARD\x10\x00\x12\"\n\x1eNATIVE_ROTATION_TYPE_ROTATE_90\x10Z\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_180\x10\xb4\x01\x12$\n\x1fNATIVE_ROTATION_TYPE_ROTATE_270\x10\x8e\x02\x1a\xa7\x04\n\x0fVideoProperties\x12\x12\n\nframe_rate\x18\x01 \x01(\x01\x12<\n\nfield_type\x18\x02 \x01(\x0e\x32(.rv.data.Media.VideoProperties.FieldType\x12\x1a\n\x12thumbnail_position\x18\x03 \x01(\x01\x12@\n\x0c\x65nd_behavior\x18\x04 \x01(\x0e\x32*.rv.data.Media.VideoProperties.EndBehavior\x12\x11\n\tsoft_loop\x18\x05 \x01(\x08\x12\x1a\n\x12soft_loop_duration\x18\x06 \x01(\x01\"\xa4\x01\n\x0b\x45ndBehavior\x12\x15\n\x11\x45ND_BEHAVIOR_STOP\x10\x00\x12\x1e\n\x1a\x45ND_BEHAVIOR_STOP_ON_BLACK\x10\x01\x12\x1e\n\x1a\x45ND_BEHAVIOR_STOP_ON_CLEAR\x10\x02\x12\x1e\n\x1a\x45ND_BEHAVIOR_FADE_TO_BLACK\x10\x03\x12\x1e\n\x1a\x45ND_BEHAVIOR_FADE_TO_CLEAR\x10\x04\"\x8d\x01\n\tFieldType\x12\x16\n\x12\x46IELD_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16\x46IELD_TYPE_PROGRESSIVE\x10\x01\x12%\n!FIELD_TYPE_INTERLACED_UPPER_FIRST\x10\x02\x12%\n!FIELD_TYPE_INTERLACED_LOWER_FIRST\x10\x03\x1a\x93\x01\n\x13LiveVideoProperties\x12\x30\n\x0cvideo_device\x18\x01 \x01(\x0b\x32\x1a.rv.data.Media.VideoDevice\x12\x30\n\x0c\x61udio_device\x18\x02 \x01(\x0b\x32\x1a.rv.data.Media.AudioDevice\x12\x18\n\x10live_video_index\x18\x03 \x01(\x05\x1a\xa2\x01\n\x13\x41udioTypeProperties\x12-\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x1e.rv.data.Media.AudioProperties\x12\x35\n\ttransport\x18\x02 \x01(\x0b\x32\".rv.data.Media.TransportProperties\x12%\n\x04\x66ile\x18\x03 \x01(\x0b\x32\x17.rv.data.FileProperties\x1ao\n\x13ImageTypeProperties\x12\x31\n\x07\x64rawing\x18\x01 \x01(\x0b\x32 .rv.data.Media.DrawingProperties\x12%\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x17.rv.data.FileProperties\x1a\x84\x02\n\x13VideoTypeProperties\x12\x31\n\x07\x64rawing\x18\x01 \x01(\x0b\x32 .rv.data.Media.DrawingProperties\x12-\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1e.rv.data.Media.AudioProperties\x12\x35\n\ttransport\x18\x03 \x01(\x0b\x32\".rv.data.Media.TransportProperties\x12-\n\x05video\x18\x04 \x01(\x0b\x32\x1e.rv.data.Media.VideoProperties\x12%\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x17.rv.data.FileProperties\x1a\xb3\x01\n\x17LiveVideoTypeProperties\x12\x31\n\x07\x64rawing\x18\x01 \x01(\x0b\x32 .rv.data.Media.DrawingProperties\x12-\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1e.rv.data.Media.AudioProperties\x12\x36\n\nlive_video\x18\x03 \x01(\x0b\x32\".rv.data.Media.LiveVideoProperties\x1ah\n\x18WebContentTypeProperties\x12\x31\n\x07\x64rawing\x18\x01 \x01(\x0b\x32 .rv.data.Media.DrawingProperties\x12\x19\n\x03url\x18\x02 \x01(\x0b\x32\x0c.rv.data.URL\"w\n\rScaleBehavior\x12\x16\n\x12SCALE_BEHAVIOR_FIT\x10\x00\x12\x17\n\x13SCALE_BEHAVIOR_FILL\x10\x01\x12\x1a\n\x16SCALE_BEHAVIOR_STRETCH\x10\x02\x12\x19\n\x15SCALE_BEHAVIOR_CUSTOM\x10\x03\"\xb9\x02\n\x0eScaleAlignment\x12!\n\x1dSCALE_ALIGNMENT_MIDDLE_CENTER\x10\x00\x12\x1c\n\x18SCALE_ALIGNMENT_TOP_LEFT\x10\x01\x12\x1e\n\x1aSCALE_ALIGNMENT_TOP_CENTER\x10\x02\x12\x1d\n\x19SCALE_ALIGNMENT_TOP_RIGHT\x10\x03\x12 \n\x1cSCALE_ALIGNMENT_MIDDLE_RIGHT\x10\x04\x12 \n\x1cSCALE_ALIGNMENT_BOTTOM_RIGHT\x10\x05\x12!\n\x1dSCALE_ALIGNMENT_BOTTOM_CENTER\x10\x06\x12\x1f\n\x1bSCALE_ALIGNMENT_BOTTOM_LEFT\x10\x07\x12\x1f\n\x1bSCALE_ALIGNMENT_MIDDLE_LEFT\x10\x08\x42\x10\n\x0eTypePropertiesB4\xf8\x01\x01\xaa\x02$Pro.SerializationInterop.RVProtoData\xba\x02\x07RVData_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'graphicsData_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002$Pro.SerializationInterop.RVProtoData\272\002\007RVData_'
  _globals['_GRAPHICS']._serialized_start=170
  _globals['_GRAPHICS']._serialized_end=8405
  _globals['_GRAPHICS_ELEMENT']._serialized_start=183
  _globals['_GRAPHICS_ELEMENT']._serialized_end=840
  _globals['_GRAPHICS_ELEMENT_FLIPMODE']._serialized_start=732
  _globals['_GRAPHICS_ELEMENT_FLIPMODE']._serialized_end=832
  _globals['_GRAPHICS_RECT']._serialized_start=842
  _globals['_GRAPHICS_RECT']._serialized_end=927
  _globals['_GRAPHICS_POINT']._serialized_start=929
  _globals['_GRAPHICS_POINT']._serialized_end=958
  _globals['_GRAPHICS_SIZE']._serialized_start=960
  _globals['_GRAPHICS_SIZE']._serialized_end=997
  _globals['_GRAPHICS_EDGEINSETS']._serialized_start=999
  _globals['_GRAPHICS_EDGEINSETS']._serialized_end=1069
  _globals['_GRAPHICS_PATH']._serialized_start=1072
  _globals['_GRAPHICS_PATH']._serialized_end=2086
  _globals['_GRAPHICS_PATH_BEZIERPOINT']._serialized_start=1194
  _globals['_GRAPHICS_PATH_BEZIERPOINT']._serialized_end=1337
  _globals['_GRAPHICS_PATH_SHAPE']._serialized_start=1340
  _globals['_GRAPHICS_PATH_SHAPE']._serialized_end=2086
  _globals['_GRAPHICS_PATH_SHAPE_ROUNDEDRECTANGLE']._serialized_start=1635
  _globals['_GRAPHICS_PATH_SHAPE_ROUNDEDRECTANGLE']._serialized_end=1672
  _globals['_GRAPHICS_PATH_SHAPE_ARROW']._serialized_start=1674
  _globals['_GRAPHICS_PATH_SHAPE_ARROW']._serialized_end=1722
  _globals['_GRAPHICS_PATH_SHAPE_POLYGON']._serialized_start=1724
  _globals['_GRAPHICS_PATH_SHAPE_POLYGON']._serialized_end=1755
  _globals['_GRAPHICS_PATH_SHAPE_STAR']._serialized_start=1757
  _globals['_GRAPHICS_PATH_SHAPE_STAR']._serialized_end=1808
  _globals['_GRAPHICS_PATH_SHAPE_TYPE']._serialized_start=1811
  _globals['_GRAPHICS_PATH_SHAPE_TYPE']._serialized_end=2068
  _globals['_GRAPHICS_FILL']._serialized_start=2089
  _globals['_GRAPHICS_FILL']._serialized_end=2301
  _globals['_GRAPHICS_BACKGROUNDEFFECT']._serialized_start=2304
  _globals['_GRAPHICS_BACKGROUNDEFFECT']._serialized_end=2610
  _globals['_GRAPHICS_BACKGROUNDEFFECT_BACKGROUNDEFFECTBLUR']._serialized_start=2494
  _globals['_GRAPHICS_BACKGROUNDEFFECT_BACKGROUNDEFFECTBLUR']._serialized_end=2557
  _globals['_GRAPHICS_BACKGROUNDEFFECT_BACKGROUNDEFFECTINVERT']._serialized_start=2559
  _globals['_GRAPHICS_BACKGROUNDEFFECT_BACKGROUNDEFFECTINVERT']._serialized_end=2583
  _globals['_GRAPHICS_GRADIENT']._serialized_start=2613
  _globals['_GRAPHICS_GRADIENT']._serialized_end=2895
  _globals['_GRAPHICS_GRADIENT_COLORSTOP']._serialized_start=2756
  _globals['_GRAPHICS_GRADIENT_COLORSTOP']._serialized_end=2837
  _globals['_GRAPHICS_GRADIENT_TYPE']._serialized_start=2839
  _globals['_GRAPHICS_GRADIENT_TYPE']._serialized_end=2895
  _globals['_GRAPHICS_SHADOW']._serialized_start=2898
  _globals['_GRAPHICS_SHADOW']._serialized_end=3089
  _globals['_GRAPHICS_SHADOW_STYLE']._serialized_start=3066
  _globals['_GRAPHICS_SHADOW_STYLE']._serialized_end=3089
  _globals['_GRAPHICS_STROKE']._serialized_start=3092
  _globals['_GRAPHICS_STROKE']._serialized_end=3323
  _globals['_GRAPHICS_STROKE_STYLE']._serialized_start=3228
  _globals['_GRAPHICS_STROKE_STYLE']._serialized_end=3323
  _globals['_GRAPHICS_FEATHER']._serialized_start=3326
  _globals['_GRAPHICS_FEATHER']._serialized_end=3479
  _globals['_GRAPHICS_FEATHER_STYLE']._serialized_start=3417
  _globals['_GRAPHICS_FEATHER_STYLE']._serialized_end=3479
  _globals['_GRAPHICS_TEXT']._serialized_start=3482
  _globals['_GRAPHICS_TEXT']._serialized_end=8405
  _globals['_GRAPHICS_TEXT_LINEFILLMASK']._serialized_start=3955
  _globals['_GRAPHICS_TEXT_LINEFILLMASK']._serialized_end=4271
  _globals['_GRAPHICS_TEXT_LINEFILLMASK_LINEMASKSTYLE']._serialized_start=4156
  _globals['_GRAPHICS_TEXT_LINEFILLMASK_LINEMASKSTYLE']._serialized_end=4271
  _globals['_GRAPHICS_TEXT_GRADIENTFILL']._serialized_start=4273
  _globals['_GRAPHICS_TEXT_GRADIENTFILL']._serialized_end=4369
  _globals['_GRAPHICS_TEXT_CUTOUTFILL']._serialized_start=4371
  _globals['_GRAPHICS_TEXT_CUTOUTFILL']._serialized_end=4383
  _globals['_GRAPHICS_TEXT_MEDIAFILL']._serialized_start=4385
  _globals['_GRAPHICS_TEXT_MEDIAFILL']._serialized_end=4427
  _globals['_GRAPHICS_TEXT_CHORDPRO']._serialized_start=4430
  _globals['_GRAPHICS_TEXT_CHORDPRO']._serialized_end=4649
  _globals['_GRAPHICS_TEXT_CHORDPRO_NOTATION']._serialized_start=4550
  _globals['_GRAPHICS_TEXT_CHORDPRO_NOTATION']._serialized_end=4649
  _globals['_GRAPHICS_TEXT_ATTRIBUTES']._serialized_start=4652
  _globals['_GRAPHICS_TEXT_ATTRIBUTES']._serialized_end=7918
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE']._serialized_start=5578
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE']._serialized_end=5933
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE_STYLE']._serialized_start=5744
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE_STYLE']._serialized_end=5820
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE_PATTERN']._serialized_start=5822
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_UNDERLINE_PATTERN']._serialized_end=5933
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH']._serialized_start=5936
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH']._serialized_end=7110
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TABSTOP']._serialized_start=6507
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TABSTOP']._serialized_end=6598
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TEXTLIST']._serialized_start=6601
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TEXTLIST']._serialized_end=7110
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TEXTLIST_NUMBERTYPE']._serialized_start=6778
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_PARAGRAPH_TEXTLIST_NUMBERTYPE']._serialized_end=7110
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_CUSTOMATTRIBUTE']._serialized_start=7113
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_CUSTOMATTRIBUTE']._serialized_end=7620
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_CAPITALIZATION']._serialized_start=7623
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_CAPITALIZATION']._serialized_end=7786
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_ALIGNMENT']._serialized_start=7788
  _globals['_GRAPHICS_TEXT_ATTRIBUTES_ALIGNMENT']._serialized_end=7910
  _globals['_GRAPHICS_TEXT_VERTICALALIGNMENT']._serialized_start=7920
  _globals['_GRAPHICS_TEXT_VERTICALALIGNMENT']._serialized_end=8029
  _globals['_GRAPHICS_TEXT_SCALEBEHAVIOR']._serialized_start=8032
  _globals['_GRAPHICS_TEXT_SCALEBEHAVIOR']._serialized_end=8225
  _globals['_GRAPHICS_TEXT_TRANSFORM']._serialized_start=8228
  _globals['_GRAPHICS_TEXT_TRANSFORM']._serialized_end=8393
  _globals['_MEDIA']._serialized_start=8408
  _globals['_MEDIA']._serialized_end=13264
  _globals['_MEDIA_METADATA']._serialized_start=8802
  _globals['_MEDIA_METADATA']._serialized_end=8930
  _globals['_MEDIA_VIDEODEVICE']._serialized_start=8933
  _globals['_MEDIA_VIDEODEVICE']._serialized_end=9273
  _globals['_MEDIA_VIDEODEVICE_TYPE']._serialized_start=9130
  _globals['_MEDIA_VIDEODEVICE_TYPE']._serialized_end=9273
  _globals['_MEDIA_AUDIODEVICE']._serialized_start=9275
  _globals['_MEDIA_AUDIODEVICE']._serialized_end=9362
  _globals['_MEDIA_AUDIO']._serialized_start=9365
  _globals['_MEDIA_AUDIO']._serialized_end=9547
  _globals['_MEDIA_AUDIO_CHANNEL']._serialized_start=9375
  _globals['_MEDIA_AUDIO_CHANNEL']._serialized_end=9547
  _globals['_MEDIA_AUDIO_CHANNEL_OUTPUT']._serialized_start=9510
  _globals['_MEDIA_AUDIO_CHANNEL_OUTPUT']._serialized_end=9547
  _globals['_MEDIA_AUDIOPROPERTIES']._serialized_start=9549
  _globals['_MEDIA_AUDIOPROPERTIES']._serialized_end=9663
  _globals['_MEDIA_TRANSPORTPROPERTIES']._serialized_start=9666
  _globals['_MEDIA_TRANSPORTPROPERTIES']._serialized_end=10423
  _globals['_MEDIA_TRANSPORTPROPERTIES_PLAYBACKBEHAVIOR']._serialized_start=10061
  _globals['_MEDIA_TRANSPORTPROPERTIES_PLAYBACKBEHAVIOR']._serialized_end=10210
  _globals['_MEDIA_TRANSPORTPROPERTIES_RETRIGGERSETTING']._serialized_start=10213
  _globals['_MEDIA_TRANSPORTPROPERTIES_RETRIGGERSETTING']._serialized_end=10352
  _globals['_MEDIA_DRAWINGPROPERTIES']._serialized_start=10426
  _globals['_MEDIA_DRAWINGPROPERTIES']._serialized_end=11276
  _globals['_MEDIA_DRAWINGPROPERTIES_NATIVEROTATIONTYPE']._serialized_start=11102
  _globals['_MEDIA_DRAWINGPROPERTIES_NATIVEROTATIONTYPE']._serialized_end=11276
  _globals['_MEDIA_VIDEOPROPERTIES']._serialized_start=11279
  _globals['_MEDIA_VIDEOPROPERTIES']._serialized_end=11830
  _globals['_MEDIA_VIDEOPROPERTIES_ENDBEHAVIOR']._serialized_start=11522
  _globals['_MEDIA_VIDEOPROPERTIES_ENDBEHAVIOR']._serialized_end=11686
  _globals['_MEDIA_VIDEOPROPERTIES_FIELDTYPE']._serialized_start=11689
  _globals['_MEDIA_VIDEOPROPERTIES_FIELDTYPE']._serialized_end=11830
  _globals['_MEDIA_LIVEVIDEOPROPERTIES']._serialized_start=11833
  _globals['_MEDIA_LIVEVIDEOPROPERTIES']._serialized_end=11980
  _globals['_MEDIA_AUDIOTYPEPROPERTIES']._serialized_start=11983
  _globals['_MEDIA_AUDIOTYPEPROPERTIES']._serialized_end=12145
  _globals['_MEDIA_IMAGETYPEPROPERTIES']._serialized_start=12147
  _globals['_MEDIA_IMAGETYPEPROPERTIES']._serialized_end=12258
  _globals['_MEDIA_VIDEOTYPEPROPERTIES']._serialized_start=12261
  _globals['_MEDIA_VIDEOTYPEPROPERTIES']._serialized_end=12521
  _globals['_MEDIA_LIVEVIDEOTYPEPROPERTIES']._serialized_start=12524
  _globals['_MEDIA_LIVEVIDEOTYPEPROPERTIES']._serialized_end=12703
  _globals['_MEDIA_WEBCONTENTTYPEPROPERTIES']._serialized_start=12705
  _globals['_MEDIA_WEBCONTENTTYPEPROPERTIES']._serialized_end=12809
  _globals['_MEDIA_SCALEBEHAVIOR']._serialized_start=12811
  _globals['_MEDIA_SCALEBEHAVIOR']._serialized_end=12930
  _globals['_MEDIA_SCALEALIGNMENT']._serialized_start=12933
  _globals['_MEDIA_SCALEALIGNMENT']._serialized_end=13246
# @@protoc_insertion_point(module_scope)
