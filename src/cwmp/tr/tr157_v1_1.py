#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-157-1-1."""

import core
from tr157_v1_0 import Device_v1_3
from tr157_v1_0 import InternetGatewayDevice_v1_5


class Device_v1_4(Device_v1_3):
  """Represents Device_v1_4."""

  def __init__(self, **defaults):
    Device_v1_3.__init__(self, defaults=defaults)
    self.Export(objects=['Device',
                         'DeviceInfo'])

  class Device(Device_v1_3.Device):
    """Represents Device_v1_4.Device."""

    def __init__(self, **defaults):
      Device_v1_3.Device.__init__(self, defaults=defaults)
      self.Export(params=['DeviceSummary'])

  class DeviceInfo(Device_v1_3.DeviceInfo):
    """Represents Device_v1_4.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v1_3.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['SupportedDataModelNumberOfEntries'],
                  lists=['SupportedDataModel'])

    class SupportedDataModel(core.Exporter):
      """Represents Device_v1_4.DeviceInfo.SupportedDataModel.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Features',
                            'URL',
                            'URN'])


class InternetGatewayDevice_v1_6(InternetGatewayDevice_v1_5):
  """Represents InternetGatewayDevice_v1_6."""

  def __init__(self, **defaults):
    InternetGatewayDevice_v1_5.__init__(self, defaults=defaults)
    self.Export(objects=['DeviceInfo',
                         'InternetGatewayDevice'])

  class DeviceInfo(InternetGatewayDevice_v1_5.DeviceInfo):
    """Represents InternetGatewayDevice_v1_6.DeviceInfo."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_5.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['SupportedDataModelNumberOfEntries'],
                  lists=['SupportedDataModel'])

    class SupportedDataModel(core.Exporter):
      """Represents InternetGatewayDevice_v1_6.DeviceInfo.SupportedDataModel.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Features',
                            'URL',
                            'URN'])

  class InternetGatewayDevice(InternetGatewayDevice_v1_5.InternetGatewayDevice):
    """Represents InternetGatewayDevice_v1_6.InternetGatewayDevice."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_5.InternetGatewayDevice.__init__(self, defaults=defaults)
      self.Export(params=['DeviceSummary'])


if __name__ == '__main__':
  print core.DumpSchema(Device_v1_4)
  print core.DumpSchema(InternetGatewayDevice_v1_6)
