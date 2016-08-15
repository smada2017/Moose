import moose
import numpy as np


def vmoutput(comp,stim):
    data = moose.Neutral('/data')
    current_tab = moose.Table('/data/current')
    moose.connect(current_tab, 'requestOut', stim, 'getOutputValue')
    vm_tab = []
    vm_tab.append(moose.Table('/data/Vm'))
    vm_tab.append(moose.Table('/data/Vm2'))
    moose.connect(vm_tab[1], 'requestOut', '/cell/2_1', 'getVm')
    moose.connect(vm_tab[0], 'requestOut', comp, 'getVm')
    return current_tab, vm_tab


def current_step_test(comp):
  #stimu = moose.Neutral('/stimulus')
  stim = moose.PulseGen('/stimulus')
  stim.delay[0] = 20e-3
  stim.level[0] = -50e-12
  stim.width[0] = 400e-3
  stim.delay[1] = 600e-3
  stim.level[1] = -1.5e-9
  stim.width[1] = 1e-3
  moose.connect(stim, 'output', comp, 'injectMsg')
  return stim
