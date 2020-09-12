#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_PSD_c import b_PSD_c  # grc-generated hier_block
from b_binary_bipolar_source_f import b_binary_bipolar_source_f  # grc-generated hier_block
from b_bipolar_to_unipolar_ff import b_bipolar_to_unipolar_ff  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import coding  # embedded python module
import d_freq_cf
import e_VCO_fase_fc_0
import epy_block_0
import math
import numpy
import numpy.ma as ma
import random
import wform  # embedded python module
from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist(digital.constellation_qpsk().points(), (0,1,2,3),
        4, 1).base()
        self.Constelacion = Constelacion = MiconstellationObject.points()
        self.M = M = len(Constelacion)
        self.samp_rate_usrp_rx = samp_rate_usrp_rx = 100e6
        self.Rb = Rb = 100
        self.Bps = Bps = int(math.log(M,2))
        self.samp_rate_to_usrp = samp_rate_to_usrp = int(samp_rate_usrp_rx/512)
        self.samp_rate_audio = samp_rate_audio = 11000
        self.ntaps = ntaps = 128
        self.Sps = Sps = 160
        self.Rs = Rs = Rb/Bps
        self.Rolloff = Rolloff = 0.5
        self.NbpS = NbpS = 8
        self.samp_rate_0 = samp_rate_0 = int(Rs*Sps)
        self.samp_rate = samp_rate = Rb*Sps
        self.run_stop = run_stop = True
        self.mapinverse = mapinverse = coding.inverse_map(Constelacion)
        self.mapdirect = mapdirect = coding.direct_map(Constelacion)
        self.h_rrc = h_rrc = wform.rrcos(Sps,ntaps,Rolloff)
        self.Vp = Vp = 1.
        self.Tupdate = Tupdate = 1./Rb
        self.Sps_0 = Sps_0 = int(math.floor(samp_rate_to_usrp/Rs))
        self.Rb_0 = Rb_0 = NbpS*samp_rate_audio
        self.P = P = 0.
        self.NnivelesQ = NnivelesQ = int(math.pow(2,NbpS))
        self.Kf = Kf = 200
        self.F = F = 0.
        self.BW = BW = (Rs/2)*(1+Rolloff)
        self.Ar = Ar = 0.
        self.A = A = 1.

        ##################################################
        # Blocks
        ##################################################
        self._P_range = Range(-2.*math.pi, 2.*math.pi, (4.*math.pi)/360., 0., 200)
        self._P_win = RangeWidget(self._P_range, self.set_P, 'Fase', "counter_slider", float)
        self.top_grid_layout.addWidget(self._P_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Ar_range = Range(0, 4., (4.)/50., 0., 200)
        self._Ar_win = RangeWidget(self._Ar_range, self.set_Ar, 'Ruido', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Ar_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._A_range = Range(-1.5, 1.5, (1.5)/100., 1., 200)
        self._A_win = RangeWidget(self._A_range, self.set_A, 'A', "counter_slider", float)
        self.top_grid_layout.addWidget(self._A_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate_audio, #samp_rate
            'Nuevo', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-128, 128)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "compararacion entre mensaje y EC", #name
            3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('Amplitud', 'volts')

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Mensaje', 'FSK parte real', 'FSK parte Imaginaria', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win, 4, 1, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "Nivel de Amplitud", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitud', 'volts')

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "Nivel de Fase", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-2*math.pi, 2*math.pi)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Fase', 'radianes')

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "Nivel de frecuencia", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0.set_y_axis(-2.5, 2.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Frecuencia', 'Hz')

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 3, 2, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            8, #size
            '', #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(Tupdate)
        self.qtgui_const_sink_x_0_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_0.set_x_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.epy_block_0 = epy_block_0.blk()
        self.e_VCO_fase_fc_0 = e_VCO_fase_fc_0.blk()
        self.digital_map_bb_0 = digital.map_bb(mapdirect)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc(MiconstellationObject.points(), 1)
        self.d_freq_cf_assign_freq_cf_0 = d_freq_cf.assign_freq_cf()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0_0_1_0_0 = blocks.multiply_const_ff(Kf*2*math.pi/samp_rate)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_quantizer_fb_0 = b_quantizer_fb(
            NivelesQ=NnivelesQ,
            Vmax=Vp,
        )
        self.b_bipolar_to_unipolar_ff_0 = b_bipolar_to_unipolar_ff()
        self.b_binary_bipolar_source_f_0 = b_binary_bipolar_source_f(
            Am=1.,
            Spb=Sps,
        )
        self.b_PSD_c_0 = b_PSD_c(
            Ensayos=1000000,
            Fc=0,
            N=1024,
            Ymax=1e-5,
            samp_rate_audio=samp_rate,
        )

        self.top_grid_layout.addWidget(self.b_PSD_c_0, 5, 1, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_GAUSSIAN, Ar, 0)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, P)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, A)
        self._F_range = Range(-2.4, 2.4, (2*2.4)/1000., 0., 200)
        self._F_win = RangeWidget(self._F_range, self.set_F, 'Frecuencia', "counter_slider", float)
        self.top_grid_layout.addWidget(self._F_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_0, 0), (self.e_VCO_fase_fc_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.b_binary_bipolar_source_f_0, 0), (self.b_bipolar_to_unipolar_ff_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.b_quantizer_fb_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.epy_block_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.e_VCO_fase_fc_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_time_sink_x_0_0_0_0_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_1_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.d_freq_cf_assign_freq_cf_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.d_freq_cf_assign_freq_cf_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.b_PSD_c_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.d_freq_cf_assign_freq_cf_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_multiply_const_vxx_0_0_0_1_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.set_mapdirect(coding.direct_map(self.Constelacion))
        self.set_mapinverse(coding.inverse_map(self.Constelacion))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_samp_rate_usrp_rx(self):
        return self.samp_rate_usrp_rx

    def set_samp_rate_usrp_rx(self, samp_rate_usrp_rx):
        self.samp_rate_usrp_rx = samp_rate_usrp_rx
        self.set_samp_rate_to_usrp(int(self.samp_rate_usrp_rx/512))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.Bps)
        self.set_Tupdate(1./self.Rb)
        self.set_samp_rate(self.Rb*self.Sps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rs(self.Rb/self.Bps)

    def get_samp_rate_to_usrp(self):
        return self.samp_rate_to_usrp

    def set_samp_rate_to_usrp(self, samp_rate_to_usrp):
        self.samp_rate_to_usrp = samp_rate_to_usrp
        self.set_Sps_0(int(math.floor(self.samp_rate_to_usrp/self.Rs)))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb_0(self.NbpS*self.samp_rate_audio)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate_audio)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_samp_rate(self.Rb*self.Sps)
        self.set_samp_rate_0(int(self.Rs*self.Sps))
        self.b_binary_bipolar_source_f_0.set_Spb(self.Sps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_BW((self.Rs/2)*(1+self.Rolloff))
        self.set_Sps_0(int(math.floor(self.samp_rate_to_usrp/self.Rs)))
        self.set_samp_rate_0(int(self.Rs*self.Sps))

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff
        self.set_BW((self.Rs/2)*(1+self.Rolloff))
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_NnivelesQ(int(math.pow(2,self.NbpS)))
        self.set_Rb_0(self.NbpS*self.samp_rate_audio)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_PSD_c_0.set_samp_rate_audio(self.samp_rate)
        self.blocks_multiply_const_vxx_0_0_0_1_0_0.set_k(self.Kf*2*math.pi/self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate((self.samp_rate))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate((self.samp_rate))
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate((self.samp_rate))
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate((self.samp_rate))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_h_rrc(self):
        return self.h_rrc

    def set_h_rrc(self, h_rrc):
        self.h_rrc = h_rrc

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp
        self.b_quantizer_fb_0.set_Vmax(self.Vp)

    def get_Tupdate(self):
        return self.Tupdate

    def set_Tupdate(self, Tupdate):
        self.Tupdate = Tupdate
        self.qtgui_const_sink_x_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(self.Tupdate)

    def get_Sps_0(self):
        return self.Sps_0

    def set_Sps_0(self, Sps_0):
        self.Sps_0 = Sps_0

    def get_Rb_0(self):
        return self.Rb_0

    def set_Rb_0(self, Rb_0):
        self.Rb_0 = Rb_0

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self.analog_const_source_x_0_0_0.set_offset(self.P)

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ
        self.b_quantizer_fb_0.set_NivelesQ(self.NnivelesQ)

    def get_Kf(self):
        return self.Kf

    def set_Kf(self, Kf):
        self.Kf = Kf
        self.blocks_multiply_const_vxx_0_0_0_1_0_0.set_k(self.Kf*2*math.pi/self.samp_rate)

    def get_F(self):
        return self.F

    def set_F(self, F):
        self.F = F

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW

    def get_Ar(self):
        return self.Ar

    def set_Ar(self, Ar):
        self.Ar = Ar
        self.analog_noise_source_x_1.set_amplitude(self.Ar)

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.analog_const_source_x_0_0.set_offset(self.A)



def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
