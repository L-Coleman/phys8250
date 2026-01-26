import numpy as np
def bv(tmean, dTdz, g):
    cp = 1005
    bv = np.sqrt((g/tmean)*(g/cp + dTdz/1000))

    return bv, 1./bv

print("tropo",bv(260,-6.5,9.8),"\n")
print("strato",bv(230,1.,9.7),"\n")
print("meso",bv(200,-1.6,9.6),"\n")
print("tropo",bv(550,6.,9.4),"\n")
print("tropo",bv(800,0.,8.6),"\n")