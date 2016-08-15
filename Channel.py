import moose
import numpy as np


CAMIN=0.01e-3   #10 nM
CAMAX=40e-3  #40 uM, might want to go up to 100 uM with spines
CADIVS=4001 #10 nM steps

VMIN=-120e-3
VMAX=50e-3
DELTAV=0.05e-3

VDIVS=(VMAX-VMIN)/DELTAV


def chanlib(ChanDict):
    if not moose.exists('/library'):
        lib=moose.Neutral('/library')
    #
    chan=[]
    for params in ChanDict.values():
            print params
            chan.append(chan_proto(params))
    #chan=[chan_proto(params) for params in ChanDict.values()]

def chan_proto(chanparams):
    chan=moose.HHChannel('/library/'+chanparams.name)
    chan.Ek=chanparams.Erev
    chan.Xpower=chanparams.Xpow
    if chanparams.Xpow>0:
        xGate=moose.HHGate(chan.path +'/gateX')
        xGate.setupAlpha(chanparams.xparams+(VDIVS,VMIN,VMAX))
    #
    chan.Ypower=chanparams.Ypow
    if chan.Ypower>0:
        yGate=moose.HHGate(chan.path + '/gateY')
        yGate.setupAlpha(chanparams.yparams+(VDIVS,VMIN,VMAX))
    #
    chan.Zpower=chanparams.Zpow
    if chan.Zpower != 0:  #Test for not equal since Zpow can be negative
        #chan.Zpower = chanparams.Zpow
        zgate=moose.HHGate(chan.path+'/gateZ')
        #print 'chan', chan.path,'zgate',zgate,zgate.name
        ca_array=np.linspace(CAMIN,CAMAX,CADIVS)
        zgate.min=CAMIN
        zgate.max=CAMAX
        caterm=(ca_array/chanparams.zparams.kd)**chanparams.zparams.power
        inf_z=caterm/(1+caterm)
        tau_z=chanparams.zparams.tau*np.ones(len(ca_array))
        zgate.tableA=inf_z/tau_z
        zgate.tableB=1/tau_z
       # moose.showfield(zgate)
        chan.useConcentration=True
    return chan



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

def Vmout(comp):
   data = moose.Neutral('/data')
   vm_tab= moose.Table('/data/Vm%s' %(comp.name))
   moose.connect(vm_tab,'requestOut',comp.path,'getVm')
   return vm_tab

