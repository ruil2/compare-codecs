"""A codec picker."""

import encoder
import h261
import h263
import mjpeg
import vp8
import vp8_cq
import vp8_mpeg
import vp8_mpeg_1d
import ffmpeg

class CodecInfo(object):
  def __init__(self, constructor, shortname, longname):
    self.constructor = constructor
    self.shortname = shortname
    self.longname = longname

codec_map = {
  'vp8': CodecInfo(vp8.Vp8Codec, 'VP8', 'VP8'),
  'vp8_cq' : CodecInfo(vp8_cq.Vp8CodecCqMode, 'VP8CQ',
                       'VP8 in Constant QP mode'),
  'vp8_mpeg' : CodecInfo(vp8_mpeg.Vp8CodecMpegMode, 'VP8MP',
                         'VP8 in MPEG-compatible mode'),
  'vp8_mpeg_1d' : CodecInfo(vp8_mpeg_1d.Vp8CodecMpeg1dMode, 'VP8M1',
                            'VP8 in 1-variable MPEG mode'),
  'ffmpeg' : CodecInfo(ffmpeg.FfmpegCodec, 'FFMPEG', 'FFMPEG'),
  'mjpeg' : CodecInfo(mjpeg.MotionJpegCodec, 'MJPEG', 'Motion JPEG'),
  'h261': CodecInfo(h261.H261Codec, 'H261', 'H.261'),
  'h263': CodecInfo(h263.H263Codec, 'H263', 'H.263'),
}

def PickCodec(name):
  if name is None:
    name = 'vp8'
  if name in codec_map:
    return codec_map[name].constructor()
  raise encoder.Error('Unrecognized codec name %s' % name)

def ShortName(name):
  """Return a pretty but short name for the codec."""
  if name in codec_map:
    return codec_map[name].shortname
  raise encoder.Error('Unrecognized codec name %s' % name)

def LongName(name):
  """Return a pretty but long name for the codec."""
  if name in codec_map:
    return codec_map[name].longname
  raise encoder.Error('Unrecognized codec name %s' % name)



