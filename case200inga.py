# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:23:52 2024

@author: Ulrich Lumendo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:13:33 2023

@author: ULRICH_LUMENDO
"""

# Copyright (c) 1996-2015 PSERC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Power flow data for 6 bus, 3 gen case from Wood & Wollenberg.
"""

from numpy import array

def case():
    """Power flow data for 6 bus, 3 gen case from Wood & Wollenberg.
    Please see L{caseformat} for details on the case file format.

    This is the 6 bus example from pp. 104, 112, 119, 123-124, 549 of
    I{"Power Generation, Operation, and Control, 2nd Edition"},
    by Allen. J. Wood and Bruce F. Wollenberg, John Wiley & Sons, NY, Jan 1996.

    @return: Power flow data for 6 bus, 3 gen case from Wood & Wollenberg.
    """
    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base
    ppc["baseMVA"] = 100.0
    ppc['bus'] = 5
    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
	[1,	        2,	    2.5,	25,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [2,	        1,		13.1,	5,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [3,	        1,	 	20,	0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [4,	        1,	 	113.2,	54.8,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [5,         1,	 	12.6,	4.6,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [6,	        1,	 	6,	    2.3,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [7,	        1,	 	24.4,	2.4,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [8,	        2,	    0,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [11,	    1,	 	62.6,	21.6,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [13,	    1,	 	61,	    13.3,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [14,	    1,	 	0,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [15,	    3,	 	0,	0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [16,	    1,	 	23,	    7.8,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [17,	    1,	 	9.4,	3.6,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [18,	    1,	 	8.2,	3.2,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [19,	    1,	 	10.2,	4,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [20,	    1,	 	1.5,	0.8,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [21,	    1,	 	0,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [22,	    1,	 	45.2,	20,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [23,	    1,	 	0,	    0,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [24,	    1,	 	0,	0,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [25,	    1,	 	0,	0,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [26,	    1,	 	62.1,	11.6,	0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [27,	    1,	 	110,	56,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [28,	    1,	 	0,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [29,	    1,	 	0.6,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [30,	    1,	 	2.7,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [31,	    1,	 	4.1,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [32,	    1,	 	3.1,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [33,	    1,	 	2.1,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [34,	    1,	 	0.8,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [35,	    1,	 	0.6,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [36,	    1,	 	2.3,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [37,	    1,	 	0.5,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [38,	    1,	 	0.1,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [39,	    1,	 	2.1,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    [40,	    1,	 	0.8,	    0,	    0,	0,	1,	1,	0,	230,	1,	1.1,	0.9],
    

])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
	[1,	10042,	0,	30,	-30,	1,	100,	1,	40,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
	[8,	164.8,	0,	127.5,	-127.5,	1,	100,	1,	170,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
	[1,	    3,	7.8406*0.01,	24.58048*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360], 
    [1,	    3,	7.8406*0.01,	24.58048*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [1,	    23,	25.413*0.01,	79.6704*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [1,	    23,	25.413*0.01,	79.6704*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [1,	    13,	0.19*0.01,	0.4, 0,	400*0.01,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    5,	1.0896*0.01,	7.1784*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    5,	1.0896*0.01,	7.1784*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    23,	17.927*0.01,	56.2016*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    23,	17.927*0.01,	56.2016*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [23,	24,	1.182*0.01,	3.7056*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [24,	25,	0.591*0.01,	1.8528*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [23,	25,	1.538*0.01,	5.585*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [23,	27,	1.0835*0.01,	3.3968*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [23,	22,	6.7571*0.01,	21.18368*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [23,	21,	1.182*0.01,	3.7056*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [21,	22,	6.0085*0.01,	18.8368*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [22,	19,	11.1*0.01,	73.2*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [22,	28,	11.9*0.01,	46.3*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [28,	7,	3.99*0.01,	18.1*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [28,	6,	16.7*0.01,	64.5*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [25,	26,	0.22261*0.01,	0.697888*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [19,	18,	4.67*0.01,	30.8*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [18,	17,	3.7*0.01,	24.6*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [17,	16,	2.45*0.01,	16.15*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [8,	    11,	2.724*0.01,	17.946*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [8,	    11,	2.724*0.01,	17.946*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [15,	20,	11.892*0.01,	16.619*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [8,	    14,	5.39*0.01,	8.87*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [15,	14,	0.038*0.01,	0.084*0.01, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    29,	0.038,	0.082, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [29,	30,	0.029,	0.049, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [30,	31,	0.019,	0.041, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [31,	32,	0.057,	0.123, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [32,	33,	0.038,	0.082, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [33,	34,	0.042,	0.09, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [34,	8,	0.078,	0.168, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [3,	    35,	0.038,	0.082, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [35,	36,	0.029,	0.049, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [36,	37,	0.019,	0.041, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [37,	38,	0.057,	0.123, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [38,	39,	0.038,	0.082, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [39,	40,	0.042,	0.09, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [40,	8,	0.078,	0.168, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [2,	3,	0.015,	0.0171, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    [4,	28,	0.0125,	0.0171, 0,	400,	400,	400,	0,	0,	1,	-360,	360],
    
    
])

    return ppc



    

    
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						

    
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
					
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						






































































     
















































