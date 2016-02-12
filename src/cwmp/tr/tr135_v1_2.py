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
"""Auto-generated from spec: urn:broadband-forum-org:tr-135-1-2."""

import core
from tr135_v1_1 import STBService_v1_1


class STBService_v1_2(STBService_v1_1):
  """Represents STBService_v1_2."""

  def __init__(self, **defaults):
    STBService_v1_1.__init__(self, defaults=defaults)
    self.Export(lists=['STBService'])

  class STBService(STBService_v1_1.STBService):
    """Represents STBService_v1_2.STBService.{i}."""

    def __init__(self, **defaults):
      STBService_v1_1.STBService.__init__(self, defaults=defaults)
      self.Export(params=['Alias'],
                  objects=['AVPlayers',
                           'AVStreams',
                           'Applications',
                           'Capabilities',
                           'Components',
                           'ServiceMonitoring'])

    class AVPlayers(STBService_v1_1.STBService.AVPlayers):
      """Represents STBService_v1_2.STBService.{i}.AVPlayers."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.AVPlayers.__init__(self, defaults=defaults)
        self.Export(lists=['AVPlayer'])

      class AVPlayer(STBService_v1_1.STBService.AVPlayers.AVPlayer):
        """Represents STBService_v1_2.STBService.{i}.AVPlayers.AVPlayer.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.AVPlayers.AVPlayer.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class AVStreams(STBService_v1_1.STBService.AVStreams):
      """Represents STBService_v1_2.STBService.{i}.AVStreams."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.AVStreams.__init__(self, defaults=defaults)
        self.Export(lists=['AVStream'])

      class AVStream(STBService_v1_1.STBService.AVStreams.AVStream):
        """Represents STBService_v1_2.STBService.{i}.AVStreams.AVStream.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.AVStreams.AVStream.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class Applications(STBService_v1_1.STBService.Applications):
      """Represents STBService_v1_2.STBService.{i}.Applications."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.Applications.__init__(self, defaults=defaults)
        self.Export(objects=['AudienceStats',
                             'CDSPull',
                             'CDSPush'],
                    lists=['ServiceProvider'])

      class AudienceStats(STBService_v1_1.STBService.Applications.AudienceStats):
        """Represents STBService_v1_2.STBService.{i}.Applications.AudienceStats."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Applications.AudienceStats.__init__(self, defaults=defaults)
          self.Export(lists=['Channel'])

        class Channel(STBService_v1_1.STBService.Applications.AudienceStats.Channel):
          """Represents STBService_v1_2.STBService.{i}.Applications.AudienceStats.Channel.{i}."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Applications.AudienceStats.Channel.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class CDSPull(STBService_v1_1.STBService.Applications.CDSPull):
        """Represents STBService_v1_2.STBService.{i}.Applications.CDSPull."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Applications.CDSPull.__init__(self, defaults=defaults)
          self.Export(lists=['ContentItem'])

        class ContentItem(STBService_v1_1.STBService.Applications.CDSPull.ContentItem):
          """Represents STBService_v1_2.STBService.{i}.Applications.CDSPull.ContentItem.{i}."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Applications.CDSPull.ContentItem.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class CDSPush(STBService_v1_1.STBService.Applications.CDSPush):
        """Represents STBService_v1_2.STBService.{i}.Applications.CDSPush."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Applications.CDSPush.__init__(self, defaults=defaults)
          self.Export(lists=['ContentItem'])

        class ContentItem(STBService_v1_1.STBService.Applications.CDSPush.ContentItem):
          """Represents STBService_v1_2.STBService.{i}.Applications.CDSPush.ContentItem.{i}."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Applications.CDSPush.ContentItem.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class ServiceProvider(STBService_v1_1.STBService.Applications.ServiceProvider):
        """Represents STBService_v1_2.STBService.{i}.Applications.ServiceProvider.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Applications.ServiceProvider.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class Capabilities(STBService_v1_1.STBService.Capabilities):
      """Represents STBService_v1_2.STBService.{i}.Capabilities."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.Capabilities.__init__(self, defaults=defaults)
        self.Export(objects=['VideoDecoder'])

      class VideoDecoder(STBService_v1_1.STBService.Capabilities.VideoDecoder):
        """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Capabilities.VideoDecoder.__init__(self, defaults=defaults)
          self.Export(objects=['MPEG2Part2',
                               'MPEG4Part10',
                               'MPEG4Part2',
                               'SMPTEVC1'])

        class MPEG2Part2(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG2Part2):
          """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG2Part2."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG2Part2.__init__(self, defaults=defaults)
            self.Export(lists=['ProfileLevel'])

          class ProfileLevel(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG2Part2.ProfileLevel):
            """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG2Part2.ProfileLevel.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG2Part2.ProfileLevel.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

        class MPEG4Part10(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part10):
          """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG4Part10."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part10.__init__(self, defaults=defaults)
            self.Export(lists=['ProfileLevel'])

          class ProfileLevel(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part10.ProfileLevel):
            """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG4Part10.ProfileLevel.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part10.ProfileLevel.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

        class MPEG4Part2(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part2):
          """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG4Part2."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part2.__init__(self, defaults=defaults)
            self.Export(lists=['ProfileLevel'])

          class ProfileLevel(STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part2.ProfileLevel):
            """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.MPEG4Part2.ProfileLevel.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Capabilities.VideoDecoder.MPEG4Part2.ProfileLevel.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

        class SMPTEVC1(STBService_v1_1.STBService.Capabilities.VideoDecoder.SMPTEVC1):
          """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.SMPTEVC1."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Capabilities.VideoDecoder.SMPTEVC1.__init__(self, defaults=defaults)
            self.Export(lists=['ProfileLevel'])

          class ProfileLevel(STBService_v1_1.STBService.Capabilities.VideoDecoder.SMPTEVC1.ProfileLevel):
            """Represents STBService_v1_2.STBService.{i}.Capabilities.VideoDecoder.SMPTEVC1.ProfileLevel.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Capabilities.VideoDecoder.SMPTEVC1.ProfileLevel.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

    class Components(STBService_v1_1.STBService.Components):
      """Represents STBService_v1_2.STBService.{i}.Components."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.Components.__init__(self, defaults=defaults)
        self.Export(objects=['PVR'],
                    lists=['AudioDecoder',
                           'AudioOutput',
                           'CA',
                           'DRM',
                           'FrontEnd',
                           'HDMI',
                           'SCART',
                           'SPDIF',
                           'VideoDecoder',
                           'VideoOutput'])

      class AudioDecoder(STBService_v1_1.STBService.Components.AudioDecoder):
        """Represents STBService_v1_2.STBService.{i}.Components.AudioDecoder.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.AudioDecoder.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class AudioOutput(STBService_v1_1.STBService.Components.AudioOutput):
        """Represents STBService_v1_2.STBService.{i}.Components.AudioOutput.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.AudioOutput.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class CA(STBService_v1_1.STBService.Components.CA):
        """Represents STBService_v1_2.STBService.{i}.Components.CA.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.CA.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class DRM(STBService_v1_1.STBService.Components.DRM):
        """Represents STBService_v1_2.STBService.{i}.Components.DRM.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.DRM.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class FrontEnd(STBService_v1_1.STBService.Components.FrontEnd):
        """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.FrontEnd.__init__(self, defaults=defaults)
          self.Export(params=['Alias'],
                      objects=['DVBT',
                               'IP'])

        class DVBT(STBService_v1_1.STBService.Components.FrontEnd.DVBT):
          """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.DVBT."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Components.FrontEnd.DVBT.__init__(self, defaults=defaults)
            self.Export(objects=['ServiceListDatabase'])

          class ServiceListDatabase(STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase):
            """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.__init__(self, defaults=defaults)
              self.Export(lists=['LogicalChannel'])

            class LogicalChannel(STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel):
              """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase.LogicalChannel.{i}."""

              def __init__(self, **defaults):
                STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.__init__(self, defaults=defaults)
                self.Export(params=['Alias'],
                            lists=['Service'])

              class Service(STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.Service):
                """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase.LogicalChannel.{i}.Service.{i}."""

                def __init__(self, **defaults):
                  STBService_v1_1.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.Service.__init__(self, defaults=defaults)
                  self.Export(params=['Alias'])

        class IP(STBService_v1_1.STBService.Components.FrontEnd.IP):
          """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Components.FrontEnd.IP.__init__(self, defaults=defaults)
            self.Export(objects=['IGMP'],
                        lists=['Inbound',
                               'Outbound'])

          class IGMP(STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP):
            """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP.__init__(self, defaults=defaults)
              self.Export(lists=['ClientGroup',
                                 'ClientGroupStats'])

            class ClientGroup(STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP.ClientGroup):
              """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP.ClientGroup.{i}."""

              def __init__(self, **defaults):
                STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP.ClientGroup.__init__(self, defaults=defaults)
                self.Export(params=['Alias'])

            class ClientGroupStats(STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP.ClientGroupStats):
              """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP.ClientGroupStats.{i}."""

              def __init__(self, **defaults):
                STBService_v1_1.STBService.Components.FrontEnd.IP.IGMP.ClientGroupStats.__init__(self, defaults=defaults)
                self.Export(params=['Alias'])

          class Inbound(STBService_v1_1.STBService.Components.FrontEnd.IP.Inbound):
            """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP.Inbound.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Components.FrontEnd.IP.Inbound.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

          class Outbound(STBService_v1_1.STBService.Components.FrontEnd.IP.Outbound):
            """Represents STBService_v1_2.STBService.{i}.Components.FrontEnd.{i}.IP.Outbound.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.Components.FrontEnd.IP.Outbound.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

      class HDMI(STBService_v1_1.STBService.Components.HDMI):
        """Represents STBService_v1_2.STBService.{i}.Components.HDMI.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.HDMI.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class PVR(STBService_v1_1.STBService.Components.PVR):
        """Represents STBService_v1_2.STBService.{i}.Components.PVR."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.PVR.__init__(self, defaults=defaults)
          self.Export(lists=['Storage'])

        class Storage(STBService_v1_1.STBService.Components.PVR.Storage):
          """Represents STBService_v1_2.STBService.{i}.Components.PVR.Storage.{i}."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.Components.PVR.Storage.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class SCART(STBService_v1_1.STBService.Components.SCART):
        """Represents STBService_v1_2.STBService.{i}.Components.SCART.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.SCART.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class SPDIF(STBService_v1_1.STBService.Components.SPDIF):
        """Represents STBService_v1_2.STBService.{i}.Components.SPDIF.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.SPDIF.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class VideoDecoder(STBService_v1_1.STBService.Components.VideoDecoder):
        """Represents STBService_v1_2.STBService.{i}.Components.VideoDecoder.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.VideoDecoder.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

      class VideoOutput(STBService_v1_1.STBService.Components.VideoOutput):
        """Represents STBService_v1_2.STBService.{i}.Components.VideoOutput.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.Components.VideoOutput.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class ServiceMonitoring(STBService_v1_1.STBService.ServiceMonitoring):
      """Represents STBService_v1_2.STBService.{i}.ServiceMonitoring."""

      def __init__(self, **defaults):
        STBService_v1_1.STBService.ServiceMonitoring.__init__(self, defaults=defaults)
        self.Export(lists=['MainStream'])

      class MainStream(STBService_v1_1.STBService.ServiceMonitoring.MainStream):
        """Represents STBService_v1_2.STBService.{i}.ServiceMonitoring.MainStream.{i}."""

        def __init__(self, **defaults):
          STBService_v1_1.STBService.ServiceMonitoring.MainStream.__init__(self, defaults=defaults)
          self.Export(params=['Alias'],
                      objects=['Sample'])

        class Sample(STBService_v1_1.STBService.ServiceMonitoring.MainStream.Sample):
          """Represents STBService_v1_2.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample."""

          def __init__(self, **defaults):
            STBService_v1_1.STBService.ServiceMonitoring.MainStream.Sample.__init__(self, defaults=defaults)
            self.Export(lists=['HighLevelMetricStats'])

          class HighLevelMetricStats(STBService_v1_1.STBService.ServiceMonitoring.MainStream.Sample.HighLevelMetricStats):
            """Represents STBService_v1_2.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.HighLevelMetricStats.{i}."""

            def __init__(self, **defaults):
              STBService_v1_1.STBService.ServiceMonitoring.MainStream.Sample.HighLevelMetricStats.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])


if __name__ == '__main__':
  print core.DumpSchema(STBService_v1_2)
