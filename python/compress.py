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

import numpy as n
import scipy.interpolate as sint
from gnuradio import gr
import matplotlib.pyplot as plt

class compress(gr.sync_block):
    
    def comp(self,x):
        return(n.sign(x)*n.minimum(n.abs(self.a*x),self.b))
    
    def __init__(self, a, b):
        self.a=a
        self.b=b        

        gr.sync_block.__init__(self,
            name="compress",
            in_sig=[n.float32],
            out_sig=[n.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # compress signal using spline function self.comp
        # limit output amplitude to 0.5
        out[:]=self.comp(in0)
        return len(output_items[0])

