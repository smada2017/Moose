import moose
import Channel
import numpy as np
# from Ca_param import caparams
# import calcium


def create_cell(ChanDict,name,pfile):
  comp_names=list()
  Ch=Channel.chanlib(ChanDict)
  cell= moose.loadModel(pfile,name)
  moose.Neutral(name)
  for comp in moose.wildcardFind('%s/#[TYPE=Compartment]'%(name)):
    print comp
    #comp=moose.element('/cell/soma')
    nachan=moose.copy('/library/NaF',comp,'NaF')
    kchan=moose.copy('/library/kDr',comp,'kDr')
    #skchan=moose.copy('/library/SKCa',comp,'SKCa')
    len =comp.length
    dia = comp.diameter
    SA= np.pi * len * dia
    #print SA
    kchan.Gbar= SA * 200e-2
    nachan.Gbar=SA * 30e-2
    #skchan.Gbar=SA*10
    moose.connect(nachan,'channel',comp,'channel')
    moose.connect(kchan,'channel',comp,'channel')
    #moose.connect(skchan,'channel',comp,'channel')
    #comp_names.append(comp.name)
    #print comp_names
  return comp


