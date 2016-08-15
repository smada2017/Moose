import moose
import numpy as np
import matplotlib.pyplot as plt
import cell_ip
import Channel
from param_chan import ChanDict
#from Ca_param import caparams,chanparams
#import calcium
#import syn_chan
#import temo
#from para_syn import nmda_param, ampa_param
#import nmda_ampa_param
import plt_chan  as plt_chan

#plt.ion()

#----parameters-----#
Temp=30
simtime = 0.05
simdt = 25e-6
plotdt = 0.25e-3
VMIN=-120e-3
VMAX=50e-3
CAMIN=0.01e-3   #10 nM
CAMAX=40e-3
   #10 nM

#---synapses---
# no_of_synapse=3
# synapse_delay=5e-3
# plotpow=1

#---cellname---##
# syn_name='cell1'
p='ri04_v3'
# syn_hand_name='cell4'

pfile= 'ri04_v3.p' #--loading cell file--
#---synapse functions--##
# synapse=syn_chan.synchan(pfile,ChanDict,syn_name)
# syn=nmda_ampa_param.syn(ChanDict,pfile,syn_hand_name,nmda_param)
# syn_h=nmda_ampa_param.synhand(syn,no_of_synapse,synapse_delay,synapse)

# --reading cell and craeting channels--###
# x = Channel.chanlib(ChanDict)
c=cell_ip.create_cell(ChanDict,p,pfile)
for chan in ChanDict.keys():
	libchan = moose.element('/library/'+chan)
	plt_chan.plot_gate_params(libchan, 0, VMIN,VMAX,CAMIN,CAMAX)



# #----calcium channels--###
# Ca=calcium.CaProto(caparams)
# ch = calcium.addCapool(c,caparams)
# Bk_chan=calcium.Bkchan_proto(chanparams,Temp)
# chan=moose.element('/library/BK')
# chan_plt_ca=plt_chan.plot_gate_params(chan,plotpow,VMIN,VMAX,CAMIN,CAMAX)
# chan=moose.element('/library/kDr')
# chan_plt=plt_chan.plot_gate_params(chan,plotpow,VMIN,VMAX,CAMIN,CAMAX)



#---voltage table of chnnels--#
vmtab1=Channel.Vmout(c)

pulse=Channel.current_step_test(c) # pulse generator

#--simulation--##

moose.reinit()
moose.start(simtime)

ts = np.linspace(0,simtime,np.size(vmtab1.vector))
volt=plt.plot(ts,vmtab1.vector*1e3,label='Vm(mV)')

plt.show(volt)

#plt.show(chan_plt)
