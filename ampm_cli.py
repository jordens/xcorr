#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Ampm Cli
# Generated: Thu Aug  6 21:19:05 2015
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from Ampm import Ampm  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class ampm_cli(gr.top_block):

    def __init__(self, decim=50, decim_df=.2, decim_f=.4, f_ref=5e6, f_sample=0.5e6, f_sig=5e6, n_samples=1<<24, name="test", pass_tags=False):
        gr.top_block.__init__(self, "Ampm Cli")

        ##################################################
        # Parameters
        ##################################################
        self.decim = decim
        self.decim_df = decim_df
        self.decim_f = decim_f
        self.f_ref = f_ref
        self.f_sample = f_sample
        self.f_sig = f_sig
        self.n_samples = n_samples
        self.name = name
        self.pass_tags = pass_tags

        ##################################################
        # Variables
        ##################################################
        self.info = info = {"name":name, "f_sig":f_sig, "f_ref":f_ref, "f_sample":f_sample, "decim":decim}
        self.filename = filename = "{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(name, f_sig/1e6, f_ref/1e6, f_sample/1e6, decim)

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_sub_source_0_2_0 = zeromq.sub_source(gr.sizeof_gr_complex, decim**0, "tcp://localhost:6889", 100, pass_tags)
        self.zeromq_sub_source_0_2 = zeromq.sub_source(gr.sizeof_gr_complex, decim**0, "tcp://localhost:6880", 100, pass_tags)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_file_meta_sink_0_3_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**0, "{}_w.bin".format(filename), f_sample, decim**3, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0_3_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0_3 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**0, "{}_0.bin".format(filename), f_sample, decim**3, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0_3.set_unbuffered(False)
        self.Ampm_0 = Ampm(
            decim=decim,
            decim_df=decim_df,
            decim_f=decim_f,
            f_ref=f_ref,
            f_sample=f_sample,
            f_sig=f_sig,
            pass_tags=pass_tags,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Ampm_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.Ampm_0, 1), (self.blocks_null_sink_0, 1))    
        self.connect((self.zeromq_sub_source_0_2, 0), (self.blocks_file_meta_sink_0_3, 0))    
        self.connect((self.zeromq_sub_source_0_2_0, 0), (self.blocks_file_meta_sink_0_3_0, 0))    


    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_filename("{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.f_ref/1e6, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "f_ref":self.f_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.Ampm_0.set_decim(self.decim)

    def get_decim_df(self):
        return self.decim_df

    def set_decim_df(self, decim_df):
        self.decim_df = decim_df
        self.Ampm_0.set_decim_df(self.decim_df)

    def get_decim_f(self):
        return self.decim_f

    def set_decim_f(self, decim_f):
        self.decim_f = decim_f
        self.Ampm_0.set_decim_f(self.decim_f)

    def get_f_ref(self):
        return self.f_ref

    def set_f_ref(self, f_ref):
        self.f_ref = f_ref
        self.set_filename("{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.f_ref/1e6, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "f_ref":self.f_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.Ampm_0.set_f_ref(self.f_ref)

    def get_f_sample(self):
        return self.f_sample

    def set_f_sample(self, f_sample):
        self.f_sample = f_sample
        self.set_filename("{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.f_ref/1e6, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "f_ref":self.f_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.Ampm_0.set_f_sample(self.f_sample)

    def get_f_sig(self):
        return self.f_sig

    def set_f_sig(self, f_sig):
        self.f_sig = f_sig
        self.set_filename("{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.f_ref/1e6, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "f_ref":self.f_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.Ampm_0.set_f_sig(self.f_sig)

    def get_n_samples(self):
        return self.n_samples

    def set_n_samples(self, n_samples):
        self.n_samples = n_samples

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.set_filename("{:s}_f0{:.5g}_f1{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.f_ref/1e6, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "f_ref":self.f_ref, "f_sample":self.f_sample, "decim":self.decim})

    def get_pass_tags(self):
        return self.pass_tags

    def set_pass_tags(self, pass_tags):
        self.pass_tags = pass_tags
        self.Ampm_0.set_pass_tags(self.pass_tags)

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_meta_sink_0_3.open("{}_0.bin".format(self.filename))
        self.blocks_file_meta_sink_0_3_0.open("{}_w.bin".format(self.filename))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--decim", dest="decim", type="intx", default=50,
        help="Set decim [default=%default]")
    parser.add_option("", "--decim-df", dest="decim_df", type="eng_float", default=eng_notation.num_to_str(.2),
        help="Set decim_df [default=%default]")
    parser.add_option("", "--decim-f", dest="decim_f", type="eng_float", default=eng_notation.num_to_str(.4),
        help="Set decim_f [default=%default]")
    parser.add_option("", "--f-ref", dest="f_ref", type="eng_float", default=eng_notation.num_to_str(5e6),
        help="Set f_ref [default=%default]")
    parser.add_option("", "--f-sample", dest="f_sample", type="eng_float", default=eng_notation.num_to_str(0.5e6),
        help="Set f_sample [default=%default]")
    parser.add_option("", "--f-sig", dest="f_sig", type="eng_float", default=eng_notation.num_to_str(5e6),
        help="Set f_sig [default=%default]")
    parser.add_option("", "--n-samples", dest="n_samples", type="long", default=1<<24,
        help="Set n_samples [default=%default]")
    parser.add_option("", "--name", dest="name", type="string", default="test",
        help="Set name [default=%default]")
    parser.add_option("", "--pass-tags", dest="pass_tags", type="intx", default=False,
        help="Set pass_tags [default=%default]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    tb = ampm_cli(decim=options.decim, decim_df=options.decim_df, decim_f=options.decim_f, f_ref=options.f_ref, f_sample=options.f_sample, f_sig=options.f_sig, n_samples=options.n_samples, name=options.name, pass_tags=options.pass_tags)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
