import moose
from collections import namedtuple
import calcium

import matplotlib.pyplot as plt
#plt.ion()
#poolname='Cachan'
channelsettings=namedtuple('channelsettings','BufCapacity CaBasal CaThick CaTau caName')

caparams=channelsettings(BufCapacity=2,CaThick=0.1e-6,CaBasal=0.05e-6,CaTau=20e-3,caName='caPool')


BKChannelParams=namedtuple('BKChannelParams','alphabeta K delta')

BK_X_params=[BKChannelParams(alphabeta=480,K=0.18,delta=-0.84),BKChannelParams(alphabeta=281,K=0.1,delta=-0.54)]

channelSettingsBk=namedtuple('channelSettingsBK','Xpow Ypow Zpow Erev name xparams yparams zparams')

chanparams=channelSettingsBk(Xpow=1,Ypow=0,Zpow=0,Erev=0.09,name='BK',xparams=BK_X_params,yparams=[],zparams=[])
