from os import environ, path
from itertools import izip

from pocketsphinx import *
from sphinxbase import *

MODELDIR = "../../../model"
DATADIR = "../../../test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'hmm/en_US/hub4wsj_sc_8k'))
config.set_string('-lm', path.join(MODELDIR, 'lm/en_US/hub4.5000.DMP'))
config.set_string('-dict', path.join(MODELDIR, 'lm/en_US/hub4.5000.dic'))
decoder = Decoder(config)

# Decode static file.
decoder.decode_raw(open(path.join(DATADIR, 'goforward.raw'), 'rb'))

# Retrieve hypothesis.
hypothesis = decoder.hyp()
print 'Best hypothesis: ', hypothesis.best_score, hypothesis.hypstr

print 'Best hypothesis segments: ', [seg.word for seg in decoder.seg()]

# Access N best decodings.
print 'Best 10 hypothesis: '
for best, i in izip(decoder.nbest(), range(10)):
    print best.hyp().best_score, best.hyp().hypstr

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt('goforward')
stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()
print 'Stream decoding result:', decoder.hyp().hypstr