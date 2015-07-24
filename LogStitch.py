from gnuradio import gr
import numpy as np


class log_stitch_cc(gr.sync_block):
    def __init__(self, decim=10, width=128, stages=5,
                 cutoff=.45, owidth=None):
        in_freqs = np.fft.fftfreq(width)
        self.take = [(in_freqs > 0) & (in_freqs <= cutoff)]
        stitch = (in_freqs > cutoff/decim) & (in_freqs <= cutoff)
        self.take.extend([stitch] * (stages - 1))
        self.freqs = np.concatenate([
            in_freqs[take]/decim**(stages - stage - 1)
            for stage, take in enumerate(self.take)])
        gr.sync_block.__init__(
            self, "log_stitch_cc",
            [(np.complex64, width)] * stages,
            [(np.float32, owidth),
             (np.complex64, owidth)],
        )

    def work(self, input_items, output_items):
        o = np.concatenate([
            ini[:, takei] for ini, takei in zip(input_items, self.take)
        ], axis=1)
        output_items[0][:, :o.shape[1]] = self.freqs
        output_items[0][:, o.shape[1]:] = 0
        output_items[1][:, :o.shape[1]] = o
        output_items[1][:, o.shape[1]:] = 0
        return len(output_items[0])
