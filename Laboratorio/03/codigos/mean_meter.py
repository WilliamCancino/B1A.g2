# Python blok - Cálculo de la media de una señal en tiempo real

import numpy as np
from gnuradio import gr


class mean_meter(gr.sync_block):  
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_mean_meter_ff',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
	self.contador = 0
	self.acum = 0

    def work(self, input_items, output_items):
        in0 = input_items[0]
	out0 = output_items[0]
	self.contador += len(in0)
	self.acum += np.sum(in0)
	out0[:] = self.acum/self.contador
        return len(output_items[0])
