#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Ampm Cli
# Generated: Wed Sep 30 18:46:43 2015
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from Ampm import Ampm  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.ctrlport.monitor import *
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class ampm_cli(gr.top_block):

    def __init__(self, decim=50, decim_df=.2, decim_f=.4, device_address="type=b200", device_arguments="master_clock_rate=30.72e6", df_ref=0, df_test=10e3, f_dsp=2e6, f_sample=960e3, f_sig=6e9, g_ref=0, g_sig=0, g_test=49, n_samples=1<<24, name="test", pass_tags=False, port_base=6880):
        gr.top_block.__init__(self, "Ampm Cli")

        ##################################################
        # Parameters
        ##################################################
        self.decim = decim
        self.decim_df = decim_df
        self.decim_f = decim_f
        self.device_address = device_address
        self.device_arguments = device_arguments
        self.df_ref = df_ref
        self.df_test = df_test
        self.f_dsp = f_dsp
        self.f_sample = f_sample
        self.f_sig = f_sig
        self.g_ref = g_ref
        self.g_sig = g_sig
        self.g_test = g_test
        self.n_samples = n_samples
        self.name = name
        self.pass_tags = pass_tags
        self.port_base = port_base

        ##################################################
        # Variables
        ##################################################
        self.info = info = {"name":name, "f_sig":f_sig, "df_ref":df_ref, "f_sample":f_sample, "decim":decim}
        self.filename = filename = "{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(name, f_sig/1e6, df_ref, f_sample/1e6, decim)

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_sub_source_0_2_0 = zeromq.sub_source(gr.sizeof_float, decim**0, "tcp://localhost:{}".format(port_base + 9), 100, pass_tags)
        self.zeromq_sub_source_0_2 = zeromq.sub_source(gr.sizeof_gr_complex, decim**0, "tcp://localhost:{}".format(port_base + 0), 100, pass_tags)
        self.zeromq_sub_source_0_1 = zeromq.sub_source(gr.sizeof_gr_complex, decim**1, "tcp://localhost:6881", 100, pass_tags)
        self.zeromq_sub_source_0_0 = zeromq.sub_source(gr.sizeof_gr_complex, decim**3, "tcp://localhost:6883", 100, pass_tags)
        self.zeromq_sub_source_0 = zeromq.sub_source(gr.sizeof_gr_complex, decim**2, "tcp://localhost:6882", 100, pass_tags)
        self.zeromq_pub_sink_0_1_2 = zeromq.pub_sink(gr.sizeof_float, decim**0, "tcp://*:{}".format(port_base + 9), 100, pass_tags)
        self.zeromq_pub_sink_0_1_1 = zeromq.pub_sink(gr.sizeof_gr_complex, decim**1, "tcp://*:{}".format(port_base + 1), 100, pass_tags)
        self.zeromq_pub_sink_0_1_0_0 = zeromq.pub_sink(gr.sizeof_gr_complex, decim**3, "tcp://*:{}".format(port_base + 3), 100, pass_tags)
        self.zeromq_pub_sink_0_1_0 = zeromq.pub_sink(gr.sizeof_gr_complex, decim**2, "tcp://*:{}".format(port_base + 2), 100, pass_tags)
        self.zeromq_pub_sink_0_1 = zeromq.pub_sink(gr.sizeof_gr_complex, decim**0, "tcp://*:{}".format(port_base + 0), 100, pass_tags)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join((device_address, device_arguments)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0_0.set_subdev_spec("A:A A:B", 0)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0_0.set_samp_rate(f_sample)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(f_sig , f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_source_0_0.set_gain(g_sig, 0)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(f_sig + df_ref, f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)
        self.uhd_usrp_source_0_0.set_gain(g_ref, 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join((device_address, device_arguments)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_samp_rate(f_sample)
        self.uhd_usrp_sink_0.set_center_freq(f_sig, 0)
        self.uhd_usrp_sink_0.set_gain(g_test, 0)
        self.uhd_usrp_sink_0.set_center_freq(f_sig, 1)
        self.uhd_usrp_sink_0.set_gain(g_test, 1)
        self.blocks_stream_to_vector_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, decim**3)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, decim**2)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, decim**0)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, decim**0)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, decim**1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*decim**3, n_samples/decim**3)
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*decim**1, n_samples/decim**1)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*decim**3, n_samples/decim**3)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*decim**2, n_samples/decim**2)
        self.blocks_file_meta_sink_0_3_0 = blocks.file_meta_sink(gr.sizeof_float*decim**0, "{}_w.bin".format(filename), f_sample, decim**3, blocks.GR_FILE_FLOAT, False, 1<<20, "", True)
        self.blocks_file_meta_sink_0_3_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0_3 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**0, "{}_0.bin".format(filename), f_sample, decim**3, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0_3.set_unbuffered(False)
        self.blocks_file_meta_sink_0_1 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**1, "{}_1.bin".format(filename), f_sample, decim**2, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0_1.set_unbuffered(False)
        self.blocks_file_meta_sink_0_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**3, "{}_3.bin".format(filename), f_sample, decim**0, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*decim**2, "{}_2.bin".format(filename), f_sample, decim**1, blocks.GR_FILE_FLOAT, True, 1<<20, "", True)
        self.blocks_file_meta_sink_0.set_unbuffered(False)
        self.blocks_ctrlport_probe2_c_0_2_2 = blocks.ctrlport_probe2_c("d3", "diff3", 1024, gr.DISPTIME)
        self.blocks_ctrlport_probe2_c_0_2_1 = blocks.ctrlport_probe2_c("d2", "diff2", 1024, gr.DISPTIME)
        self.blocks_ctrlport_probe2_c_0_2_0 = blocks.ctrlport_probe2_c("d1", "diff1", 1024, gr.DISPTIME)
        self.blocks_ctrlport_probe2_c_0_1 = blocks.ctrlport_probe2_c("d0", "diff0", 1024, gr.DISPTIME)
        self.blocks_ctrlport_probe2_c_0_0 = blocks.ctrlport_probe2_c("b", "input b", 1024, gr.DISPTIME)
        self.blocks_ctrlport_probe2_c_0 = blocks.ctrlport_probe2_c("a", "input a", 1024, gr.DISPTIME)
        self.blocks_ctrlport_monitor_0 = not True or monitor()
        self.analog_sig_source_x_0 = analog.sig_source_c(f_sample, analog.GR_COS_WAVE, df_test, 1, 0)
        self.Ampm_0 = Ampm(
            decim=decim,
            decim_df=decim_df,
            decim_f=decim_f,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Ampm_0, 0), (self.blocks_ctrlport_probe2_c_0_1, 0))    
        self.connect((self.Ampm_0, 1), (self.blocks_ctrlport_probe2_c_0_2_0, 0))    
        self.connect((self.Ampm_0, 2), (self.blocks_ctrlport_probe2_c_0_2_1, 0))    
        self.connect((self.Ampm_0, 3), (self.blocks_ctrlport_probe2_c_0_2_2, 0))    
        self.connect((self.Ampm_0, 2), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.Ampm_0, 3), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.Ampm_0, 4), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.Ampm_0, 1), (self.blocks_stream_to_vector_0_1, 0))    
        self.connect((self.Ampm_0, 0), (self.blocks_stream_to_vector_0_1_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 1))    
        self.connect((self.blocks_head_0, 0), (self.blocks_file_meta_sink_0, 0))    
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_meta_sink_0_0, 0))    
        self.connect((self.blocks_head_0_1, 0), (self.blocks_file_meta_sink_0_1, 0))    
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_head_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.zeromq_pub_sink_0_1_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.zeromq_pub_sink_0_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.zeromq_pub_sink_0_1_2, 0))    
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.zeromq_pub_sink_0_1_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_1_0, 0), (self.zeromq_pub_sink_0_1_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.Ampm_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.Ampm_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_ctrlport_probe2_c_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_ctrlport_probe2_c_0_0, 0))    
        self.connect((self.zeromq_sub_source_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.zeromq_sub_source_0_0, 0), (self.blocks_skiphead_0, 0))    
        self.connect((self.zeromq_sub_source_0_1, 0), (self.blocks_head_0_1, 0))    
        self.connect((self.zeromq_sub_source_0_2, 0), (self.blocks_file_meta_sink_0_3, 0))    
        self.connect((self.zeromq_sub_source_0_2_0, 0), (self.blocks_file_meta_sink_0_3_0, 0))    


    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_filename("{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.df_ref, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "df_ref":self.df_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.Ampm_0.set_decim(self.decim)
        self.blocks_head_0.set_length(self.n_samples/self.decim**2)
        self.blocks_head_0_0.set_length(self.n_samples/self.decim**3)
        self.blocks_head_0_1.set_length(self.n_samples/self.decim**1)

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

    def get_device_address(self):
        return self.device_address

    def set_device_address(self, device_address):
        self.device_address = device_address

    def get_device_arguments(self):
        return self.device_arguments

    def set_device_arguments(self, device_arguments):
        self.device_arguments = device_arguments

    def get_df_ref(self):
        return self.df_ref

    def set_df_ref(self, df_ref):
        self.df_ref = df_ref
        self.set_filename("{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.df_ref, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "df_ref":self.df_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.f_sig + self.df_ref, self.f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)

    def get_df_test(self):
        return self.df_test

    def set_df_test(self, df_test):
        self.df_test = df_test
        self.analog_sig_source_x_0.set_frequency(self.df_test)

    def get_f_dsp(self):
        return self.f_dsp

    def set_f_dsp(self, f_dsp):
        self.f_dsp = f_dsp
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.f_sig , self.f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.f_sig + self.df_ref, self.f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)

    def get_f_sample(self):
        return self.f_sample

    def set_f_sample(self, f_sample):
        self.f_sample = f_sample
        self.set_filename("{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.df_ref, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "df_ref":self.df_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.analog_sig_source_x_0.set_sampling_freq(self.f_sample)
        self.uhd_usrp_sink_0.set_samp_rate(self.f_sample)
        self.uhd_usrp_source_0_0.set_samp_rate(self.f_sample)

    def get_f_sig(self):
        return self.f_sig

    def set_f_sig(self, f_sig):
        self.f_sig = f_sig
        self.set_filename("{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.df_ref, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "df_ref":self.df_ref, "f_sample":self.f_sample, "decim":self.decim})
        self.uhd_usrp_sink_0.set_center_freq(self.f_sig, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.f_sig, 1)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.f_sig , self.f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.f_sig + self.df_ref, self.f_dsp, rf_freq_policy=uhd.tune_request.POLICY_AUTO, dsp_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)

    def get_g_ref(self):
        return self.g_ref

    def set_g_ref(self, g_ref):
        self.g_ref = g_ref
        self.uhd_usrp_source_0_0.set_gain(self.g_ref, 1)
        	

    def get_g_sig(self):
        return self.g_sig

    def set_g_sig(self, g_sig):
        self.g_sig = g_sig
        self.uhd_usrp_source_0_0.set_gain(self.g_sig, 0)
        	

    def get_g_test(self):
        return self.g_test

    def set_g_test(self, g_test):
        self.g_test = g_test
        self.uhd_usrp_sink_0.set_gain(self.g_test, 0)
        	
        self.uhd_usrp_sink_0.set_gain(self.g_test, 1)
        	

    def get_n_samples(self):
        return self.n_samples

    def set_n_samples(self, n_samples):
        self.n_samples = n_samples
        self.blocks_head_0.set_length(self.n_samples/self.decim**2)
        self.blocks_head_0_0.set_length(self.n_samples/self.decim**3)
        self.blocks_head_0_1.set_length(self.n_samples/self.decim**1)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.set_filename("{:s}_f0{:.5g}_df{:.5g}_fs{:.5g}_d{:.5g}".format(self.name, self.f_sig/1e6, self.df_ref, self.f_sample/1e6, self.decim))
        self.set_info({"name":self.name, "f_sig":self.f_sig, "df_ref":self.df_ref, "f_sample":self.f_sample, "decim":self.decim})

    def get_pass_tags(self):
        return self.pass_tags

    def set_pass_tags(self, pass_tags):
        self.pass_tags = pass_tags

    def get_port_base(self):
        return self.port_base

    def set_port_base(self, port_base):
        self.port_base = port_base

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_meta_sink_0.open("{}_2.bin".format(self.filename))
        self.blocks_file_meta_sink_0_0.open("{}_3.bin".format(self.filename))
        self.blocks_file_meta_sink_0_1.open("{}_1.bin".format(self.filename))
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
    parser.add_option("", "--device-address", dest="device_address", type="string", default="type=b200",
        help="Set device_address [default=%default]")
    parser.add_option("", "--device-arguments", dest="device_arguments", type="string", default="master_clock_rate=30.72e6",
        help="Set device_arguments [default=%default]")
    parser.add_option("", "--df-ref", dest="df_ref", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set df_ref [default=%default]")
    parser.add_option("", "--df-test", dest="df_test", type="eng_float", default=eng_notation.num_to_str(10e3),
        help="Set df_test [default=%default]")
    parser.add_option("", "--f-dsp", dest="f_dsp", type="eng_float", default=eng_notation.num_to_str(2e6),
        help="Set f_dsp [default=%default]")
    parser.add_option("", "--f-sample", dest="f_sample", type="eng_float", default=eng_notation.num_to_str(960e3),
        help="Set f_sample [default=%default]")
    parser.add_option("", "--f-sig", dest="f_sig", type="eng_float", default=eng_notation.num_to_str(6e9),
        help="Set f_sig [default=%default]")
    parser.add_option("", "--g-ref", dest="g_ref", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set g_ref [default=%default]")
    parser.add_option("", "--g-sig", dest="g_sig", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set g_sig [default=%default]")
    parser.add_option("", "--g-test", dest="g_test", type="eng_float", default=eng_notation.num_to_str(49),
        help="Set g_test [default=%default]")
    parser.add_option("", "--n-samples", dest="n_samples", type="long", default=1<<24,
        help="Set n_samples [default=%default]")
    parser.add_option("", "--name", dest="name", type="string", default="test",
        help="Set name [default=%default]")
    parser.add_option("", "--pass-tags", dest="pass_tags", type="intx", default=False,
        help="Set pass_tags [default=%default]")
    parser.add_option("", "--port-base", dest="port_base", type="intx", default=6880,
        help="Set port_base [default=%default]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    tb = ampm_cli(decim=options.decim, decim_df=options.decim_df, decim_f=options.decim_f, device_address=options.device_address, device_arguments=options.device_arguments, df_ref=options.df_ref, df_test=options.df_test, f_dsp=options.f_dsp, f_sample=options.f_sample, f_sig=options.f_sig, g_ref=options.g_ref, g_sig=options.g_sig, g_test=options.g_test, n_samples=options.n_samples, name=options.name, pass_tags=options.pass_tags, port_base=options.port_base)
    tb.start()
    (tb.blocks_ctrlport_monitor_0).start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    (tb.blocks_ctrlport_monitor_0).start()
    tb.wait()
