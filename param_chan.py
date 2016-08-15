import moose
import Channel
from collections import namedtuple


AlphaBetaChannelParams = namedtuple('AlphaBetaChannelParams', '''
    A_rate
    A_B
    A_C
    Avhalf
    A_vslope
    B_rate
    B_B
    B_C
    Bvhalf
    B_vslope''')


kDr_X_params= AlphaBetaChannelParams (
    A_rate=6.5,
    A_B=0,
    A_C=0,
    Avhalf=0,
    A_vslope=-12.5e-3,
    B_rate=24,
    B_B=0,
    B_C=0,
    Bvhalf=0,
    B_vslope=33.5e-3)

kDr_Y_params=[]

channelSettings=namedtuple('channelSettings','Xpow Ypow Zpow Erev name xparams yparams zparams')
kDrparams=channelSettings(Xpow=1,Ypow=0,Zpow=0,Erev=-0.09,name='kDr',xparams=kDr_X_params,yparams=kDr_Y_params,zparams=[])


SSTauChannelParams = namedtuple('SSTauChannelParams', '''
    Arate
    A_B
    A_C
    Avhalf
    Avslope
    taumin
    tauVdep
    tauPow
    tauVhalf
    tauVslope''')

Na_m_params= AlphaBetaChannelParams (
    A_rate=-12.0052e-3*2.14e6,
    A_B=-0.4*2.14e6,
    A_C=-1,
    Avhalf=30.013e-3,
    A_vslope=-7.2e-3,
    B_rate=3.722e-3*2.14e6,
    B_B=0.124*2.14e6,
    B_C=-1,
    Bvhalf=30.013e-3,
    B_vslope=7.2e-3)

Na_h_params= AlphaBetaChannelParams (
    A_rate=(45.013e-3+15.0e-3)*0.03*2.14e6,
    A_B=0.03*2.14e6,
    A_C=-1,
    Avhalf=45.013e-3+15e-3,
    A_vslope=3.5e-3,
    B_rate=-(45.013e-3+15e-3)*0.01*2.14e6,
    B_B=-0.01*2.14e6,
    B_C=-1,
    Bvhalf=45.013e-3+15e-3,
    B_vslope=-3.5e-3)


naFparams=channelSettings(Xpow=3,Ypow=1,Zpow=0,Erev=55.0e-3,name='NaF',xparams=Na_m_params,yparams=Na_h_params,zparams=[])

# zchannelparams=namedtuple('zchannelparams','kd power tau')

# SK_Z_params=zchannelparams(kd=0.57e-3,
#                            power=5.2,
#                            tau=4.9e-3)
# skparams=channelSettings(Xpow=0,Ypow=0,Zpow=1,Erev=-87e-3,name='SKCa',xparams=[],yparams=[],zparams=SK_Z_params)

ChanDict={'kDr':kDrparams,'NaF':naFparams} #ChanDict={'kDr':kDrparams,'NaF':naFparams,'SKCa':skparams}

#ChanDict={'SKCa':skparams}


