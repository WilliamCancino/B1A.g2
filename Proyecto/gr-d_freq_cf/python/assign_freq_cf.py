#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-d_freq_cf author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy
import math
from gnuradio import gr

class assign_freq_cf(gr.sync_block):
    """
    docstring for block assign_freq_cf
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="assign_freq_cf",
            in_sig=[numpy.complex64],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
    	#in0 = round(input_items[0], 4)
    	in0 = numpy.around(input_items[0].real,4)+(1j*numpy.around(input_items[0].imag,4))
    	#in0 = input_items[0]
    	out = output_items[0]
    	#print(in0[0])
    	#GR_M_SQRT2 = 1.41421356237309504880*math.sqrt(2)
    	GR_M_SQRT2 = round(math.sqrt(2)/2.0, 4)
    	#print(GR_M_SQRT2 + 1j*GR_M_SQRT2)
    	for i in range(len(in0)):
    		#print("Nuevo: ")
    		#print(round(in0[i].real,4)+(1j*round(in0[i].imag,4)))
    		#print(in0[i])
    		#print(complex(in0[i]) == complex((GR_M_SQRT2 + 1j*GR_M_SQRT2)))
    		if in0[i].real>=0.7 and in0[i].real<=0.75 and in0[i].imag>=0.7 and in0[i].imag<=0.75:
    			out[:] = 1
    		elif in0[i].real>=-0.75 and in0[i].real<=-0.7 and in0[i].imag>=0.7 and in0[i].imag<=0.75:
    			out[:] = 2
    		elif in0[i].real>=-0.75 and in0[i].real<=-0.7 and in0[i].imag>=-0.75 and in0[i].imag<=-0.7:
    			out[:] = 3
    		else:
    			out[:] = 4

    	return len(out)
