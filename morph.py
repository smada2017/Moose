# -*- coding: utf-8 -*-
import moose
import numpy as np
import functions as util
import pylab


p_file="out_ri04_v3.p"

simtime = 0.4
simdt = 1e-7
plotdt = 0.25e-3

container='cell'
cell=moose.loadModel(p_file,container)
moose.le("/")

comp='/cell/soma'
stim = util.current_step_test(comp)
currenttab,vmtab=util.vmoutput(comp,stim)

#print "stim",stim.tick, stim.dt,"vm", vm.tick,vm.dt
for ticks in range(0,7):
	moose.setClock(ticks,simdt)

hsolve = moose.HSolve( '%s/hsolve' % (container))	
moose.setClock(stim.tick,simdt)
moose.setClock(vmtab[0].tick,plotdt)
moose.setClock(currenttab.tick,plotdt)

moose.reinit()
moose.start(simtime)

t = pylab.linspace(0, simtime, len(vmtab[0].vector)) 
pylab.plot(t, 1e3*vmtab[0].vector, label="Vm1")
pylab.plot(t, 1e3*vmtab[1].vector, label="Vm2")  
#pylab.plot(t, 1e9*currenttab.vector, label="Current")
pylab.legend()
pylab.show()

