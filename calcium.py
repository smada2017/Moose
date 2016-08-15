import moose
import numpy as np
from Channel import VMIN,VMAX,VDIVS,CADIVS,CAMAX,CAMIN

Faraday=9.68e4
R=13




def CaProto(caparams):
    if not moose.exists('/library'):
        lib=moose.Neutral('/library')
    poolproto=moose.CaConc('/library/'+ caparams.caName)
    poolproto.CaBasal=caparams.CaBasal
    poolproto.ceiling=1
    poolproto.floor=0
    poolproto.thick=caparams.CaThick
    poolproto.tau=caparams.CaTau
    return poolproto

def addCapool(comp,caparams):
    caproto = moose.element('/library/' + caparams.caName)
    #print caproto
    capool= moose.copy(caproto, comp, caparams.caName)
    #print capool
    len = comp.length
    #print len
    dia= comp.diameter
    SA= np.pi*len*dia
    vol=SA*capool.thick
    capool.B=1/(Faraday*vol*2)/caparams.BufCapacity
    return capool


def Bkchan_proto(chanparams,Temp):
    ZFbyRT=2*Faraday/(R*(Temp+273.15))
    v_array=np.linspace(VMIN,VMAX,VDIVS)
    ca_array=np.linspace(CAMIN,CAMAX,CADIVS)
    gatingMatrix=[]
    print chanparams
    for i,pars in enumerate(chanparams.xparams):
        print pars
        Vdepgating=pars.K*np.exp(pars.delta*ZFbyRT*v_array)
        if i==0:
            gatingMatrix.append(pars.alphabeta*ca_array[None,:]/(ca_array[None,:]+pars.K*Vdepgating[:,None]))
        else:
            gatingMatrix.append(pars.alphabeta/(1+ca_array[None,:]/pars.K*Vdepgating[:,None]))
            gatingMatrix[i]+=gatingMatrix[0]

    if not moose.exists('/library'):
        lib = moose.Neutral('/library')
    chan= moose.HHChannel2D('/library/' + chanparams.name)
    chan.Xpower=chanparams.Xpow
    chan.Ek=chanparams.Erev
    chan.Xindex="VOLT_C1_INDEX"
    xGate=moose.HHGate2D(chan.path+'/gateX')
    xGate.xminA=xGate.xminB=VMIN
    xGate.xmaxA=xGate.xmaxB=VMAX
    xGate.xdivsA=xGate.xdivsB=VDIVS
    xGate.yminA=xGate.yminB=CAMIN
    xGate.ymaxA=xGate.ymaxB=CAMAX
    xGate.ydivsA=xGate.ydivsB=CADIVS
    xGate.tableA=gatingMatrix[0]
    xGate.tableB=gatingMatrix[1]
    return chan
