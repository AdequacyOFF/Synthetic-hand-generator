# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: HandGenerator.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'HandGenerator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13HandGenerator.proto\x12\rHandGenerator\"c\n\x0bHandRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\"\n\x04race\x18\x02 \x01(\x0e\x32\x14.HandGenerator.Races\x12!\n\x04hand\x18\x03 \x01(\x0e\x32\x13.HandGenerator.Hand\"0\n\tHandReply\x12\x10\n\x08\x46ileName\x18\x01 \x01(\t\x12\x11\n\tFileBytes\x18\x02 \x01(\x0c*\x1c\n\x05Races\x12\x08\n\x04\x44\x41RK\x10\x00\x12\t\n\x05LIGHT\x10\x01*\x1b\n\x04Hand\x12\t\n\x05RIGHT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x32\xb1\x01\n\rHandGenerator\x12K\n\x13GenerateHandDataset\x12\x1a.HandGenerator.HandRequest\x1a\x18.HandGenerator.HandReply\x12S\n\x19GenerateHandDatasetStream\x12\x1a.HandGenerator.HandRequest\x1a\x18.HandGenerator.HandReply0\x01\x42\x1a\xaa\x02\x17GrpcHandGeneratorClientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HandGenerator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\027GrpcHandGeneratorClient'
  _globals['_RACES']._serialized_start=189
  _globals['_RACES']._serialized_end=217
  _globals['_HAND']._serialized_start=219
  _globals['_HAND']._serialized_end=246
  _globals['_HANDREQUEST']._serialized_start=38
  _globals['_HANDREQUEST']._serialized_end=137
  _globals['_HANDREPLY']._serialized_start=139
  _globals['_HANDREPLY']._serialized_end=187
  _globals['_HANDGENERATOR']._serialized_start=249
  _globals['_HANDGENERATOR']._serialized_end=426
# @@protoc_insertion_point(module_scope)
