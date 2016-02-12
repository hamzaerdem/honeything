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
"""Auto-generated from spec: urn:catawampus-org:x-catawampus-tr181-2-0."""

import core
from tr181_v2_4 import Device_v2_4


class X_CATAWAMPUS_ORG_Device_v2_0(Device_v2_4):
  """Represents X_CATAWAMPUS_ORG_Device_v2_0."""

  def __init__(self, **defaults):
    Device_v2_4.__init__(self, defaults=defaults)
    self.Export(objects=['Device',
                         'DeviceInfo'])

  class Device(Device_v2_4.Device):
    """Represents X_CATAWAMPUS_ORG_Device_v2_0.Device."""

    def __init__(self, **defaults):
      Device_v2_4.Device.__init__(self, defaults=defaults)
      self.Export(objects=['Ethernet'])

    class Ethernet(Device_v2_4.Device.Ethernet):
      """Represents X_CATAWAMPUS_ORG_Device_v2_0.Device.Ethernet."""

      def __init__(self, **defaults):
        Device_v2_4.Device.Ethernet.__init__(self, defaults=defaults)
        self.Export(lists=['Interface'])

      class Interface(Device_v2_4.Device.Ethernet.Interface):
        """Represents X_CATAWAMPUS_ORG_Device_v2_0.Device.Ethernet.Interface.{i}."""

        def __init__(self, **defaults):
          Device_v2_4.Device.Ethernet.Interface.__init__(self, defaults=defaults)
          self.Export(params=['X_CATAWAMPUS-ORG_ActualBitRate',
                              'X_CATAWAMPUS-ORG_ActualDuplexMode'])

  class DeviceInfo(Device_v2_4.DeviceInfo):
    """Represents X_CATAWAMPUS_ORG_Device_v2_0.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v2_4.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['X_CATAWAMPUS-ORG_LedStatusNumberOfEntries'],
                  objects=['TemperatureStatus'],
                  lists=['X_CATAWAMPUS-ORG_LedStatus'])

    class TemperatureStatus(Device_v2_4.DeviceInfo.TemperatureStatus):
      """Represents X_CATAWAMPUS_ORG_Device_v2_0.DeviceInfo.TemperatureStatus."""

      def __init__(self, **defaults):
        Device_v2_4.DeviceInfo.TemperatureStatus.__init__(self, defaults=defaults)
        self.Export(lists=['X_CATAWAMPUS-ORG_Fan'])

      class X_CATAWAMPUS_ORG_Fan(core.Exporter):
        """Represents X_CATAWAMPUS_ORG_Device_v2_0.DeviceInfo.TemperatureStatus.X_CATAWAMPUS-ORG_Fan.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['DesiredPercentage',
                              'DesiredRPM',
                              'Name',
                              'RPM'])

    class X_CATAWAMPUS_ORG_LedStatus(core.Exporter):
      """Represents X_CATAWAMPUS_ORG_Device_v2_0.DeviceInfo.X_CATAWAMPUS-ORG_LedStatus.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Name',
                            'Status'])


if __name__ == '__main__':
  print core.DumpSchema(X_CATAWAMPUS_ORG_Device_v2_0)
