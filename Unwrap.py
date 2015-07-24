from gnuradio import gr
import numpy as np


class Unwrap(gr.sync_block):
    def __init__(self, discont=np.pi):
        gr.sync_block.__init__(
            self, "unwrap",
            [np.float32],
            [np.float32],
        )
        self.discont = discont
        self.offset = 0.

    def get_discont(self):
        return self.discont

    def set_discont(self, discont):
        self.discont = discont

    def work(self, input_items, output_items):
        output_items[0][:] = np.unwrap(input_items[0], self.discont)
        output_items[0] += self.offset
        self.offset = output_items[0][-1] - input_items[0][-1]
        return len(output_items[0])
