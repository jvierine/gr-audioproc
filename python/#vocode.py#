#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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
import numpy as np
from gnuradio import gr

class vocode(gr.sync_block):
    """
    docstring for block vocode
    """
    def __init__(self, n,n0,n1,dec):
        self.tmp_in = np.zeros(4*n,dtype=np.float32)
        self.tmp_out = np.zeros(4*n,dtype=np.float32)        
        self.fin = np.zeros(n,dtype=np.float32)        
        self.n = n                               # fft size
        self.n0 = n0                             # first bin (mapped to dc freq)
        self.n1 = n1                             # last bin (mapped to dc+(n1-n0) freq)
        self.w=np.zeros(n,dtype=np.float32)      # window function        
        l2=int(n/2)
        self.w[0:l2]=np.linspace(0,1.0,num=l2) 
        self.w[l2:n]=np.linspace(1.0,0.0,num=l2) 
        self.dec = dec                           # how much do we decimate spectrum
        self.idx_bufin  = self.n # output lags by n due to buffering req in sync block

        self.w_idx=0
        
        self.idx_out = 0

        gr.sync_block.__init__(self,
            name="vocode",
            in_sig=[np.float32],
            out_sig=[np.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        L=len(in0)
        self.tmp_in[np.mod(self.idx_bufin+np.arange(L),self.n*4)]=in0

        # if we have enough data, we can do a windowed fft
        if (self.idx_bufin+L) >= (self.n/2)*self.w_idx + self.n:            
            # window
            i0=self.w_idx*self.n/2
            fin=self.tmp_in[np.mod(i0+np.arange(self.n),self.n*4)]
            # compress and shift spectrum
            F=np.fft.rfft(self.w*fin)
            Fc=np.convolve(F,np.repeat(1.0/float(self.dec),self.dec),mode="same")
            idxs=np.arange(self.n0,self.n1,self.dec)
            Fc2=np.copy(Fc) ; Fc2[:]=0.0
            Fc2[np.arange(len(idxs))]=Fc[idxs]
            self.tmp_out[np.mod(i0+np.arange(self.n),self.n*4)]+=self.w*np.fft.irfft(Fc2)

            # empty tail of buffer
            self.tmp_out[np.mod(i0-2*self.n+np.arange(self.n),self.n*4)]=0.0
            self.w_idx+=1
            
        self.idx_bufin+=L
        out[:]=self.tmp_out[np.mod(self.idx_out+np.arange(L),self.n*4)]
        self.idx_out+=L
        return L

