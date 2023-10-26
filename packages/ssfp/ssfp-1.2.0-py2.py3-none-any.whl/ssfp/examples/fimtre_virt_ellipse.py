'''Construct virtual ellipses and run PLANET.'''

import numpy as np
import matplotlib.pyplot as plt

from ssfp import bssfp, fimtre, planet


if __name__ == '__main__':

    N = 32
    
    T1 = 2*np.ones((N, N))
    T2 = 1*np.ones((N, N))
    M0 = np.ones((N, N))

    TR0, TR1 = 3e-3, 2*3e-3# 6e-3
    alpha_hi = np.deg2rad(100)
    alpha_lo = np.deg2rad(10)
    pcs8 = np.linspace(0, 2*np.pi, 8, endpoint=False)
    pcs6 = np.linspace(0, 2*np.pi, 6, endpoint=False)
    pcs4 = np.linspace(0, 2*np.pi, 4, endpoint=False)
    pcs2 = np.linspace(0, 2*np.pi, 2, endpoint=False)    
    df, _ = np.meshgrid(
        np.linspace(1/(8*TR1), 1/(4*TR1), N),
        np.linspace(1/(8*TR1), 1/(4*TR1), N))

    pbssfp = lambda TR0, alpha0, pcs0: bssfp(T1, T2, TR0, alpha0, field_map=df, phase_cyc=pcs0[None, None, :], M0=M0)
    
    TR0_2_hi = pbssfp(TR0, alpha_hi, pcs2)
    TR0_4_hi = pbssfp(TR0, alpha_hi, pcs4)
    TR0_6_hi = pbssfp(TR0, alpha_hi, pcs6)
    TR0_8_hi = pbssfp(TR0, alpha_hi, pcs8)

    TR0_2_lo = pbssfp(TR0, alpha_lo, pcs2)
    TR0_4_lo = pbssfp(TR0, alpha_lo, pcs4)
    TR0_6_lo = pbssfp(TR0, alpha_lo, pcs6)
    TR0_8_lo = pbssfp(TR0, alpha_lo, pcs8)

    TR1_2_hi = pbssfp(TR1, alpha_hi, pcs2)
    TR1_4_hi = pbssfp(TR1, alpha_hi, pcs4)
    TR1_6_hi = pbssfp(TR1, alpha_hi, pcs6)
    TR1_8_hi = pbssfp(TR1, alpha_hi, pcs8)

    TR1_2_lo = pbssfp(TR1, alpha_lo, pcs2)
    TR1_4_lo = pbssfp(TR1, alpha_lo, pcs4)
    TR1_6_lo = pbssfp(TR1, alpha_lo, pcs6)
    TR1_8_lo = pbssfp(TR1, alpha_lo, pcs8)

    ## Make 4+2 virtual ellipses
    virt_4_2_hi = np.concatenate((TR0_4_hi, TR1_2_hi*np.exp(-1j*fimtre(TR0_4_hi, TR1_2_hi, TR0=TR0, TR1=TR1, rad=True)[..., None])), axis=-1)
    virt_4_2_hi = np.take_along_axis(virt_4_2_hi, np.argsort(np.angle(virt_4_2_hi), axis=-1), axis=-1)    

    #plt.imshow(df)
    #plt.imshow(-1*fimtre(TR0_4_hi, TR1_2_hi, TR0=TR0, TR1=TR1, rad=False) - df)
    #plt.show()
    
    virt_4_2_lo = np.concatenate((TR0_4_lo, TR1_2_lo*np.exp(-1j*fimtre(TR0_4_lo, TR1_2_lo, TR0=TR0, TR1=TR1, rad=True)[..., None])), axis=-1)
    virt_4_2_lo = np.take_along_axis(virt_4_2_lo, np.argsort(np.angle(virt_4_2_lo), axis=-1), axis=-1)
    
    virt_4_4_hi = np.concatenate((TR0_4_hi, TR1_4_hi*np.exp(1j*fimtre(TR0_4_hi, TR1_4_hi, TR0=TR0, TR1=TR1, rad=True)[..., None])), axis=-1)
    virt_4_4_hi = np.take_along_axis(virt_4_4_hi, np.argsort(np.angle(virt_4_4_hi), axis=-1), axis=-1)    

    virt_4_4_lo = np.concatenate((TR0_4_lo, TR1_4_lo*np.exp(1j*fimtre(TR0_4_lo, TR1_4_lo, TR0=TR0, TR1=TR1, rad=True)[..., None])), axis=-1)

    # controls
    _Meff, T1_6_0_hi, T2_6_0_hi, _df = planet(TR0_6_hi, alpha=alpha_hi, TR=TR0, pc_axis=-1)
    _Meff, T1_8_0_hi, T2_8_0_hi, _df = planet(TR0_8_hi, alpha=alpha_hi, TR=TR0, pc_axis=-1)
    _Meff, T1_6_0_lo, T2_6_0_lo, _df = planet(TR0_6_lo, alpha=alpha_lo, TR=TR0, pc_axis=-1)
    _Meff, T1_8_0_lo, T2_8_0_lo, _df = planet(TR0_8_lo, alpha=alpha_lo, TR=TR0, pc_axis=-1)

    # Virt ellipse recons
    TRv = (TR0+TR1)/2
    _Meff, T1_4_2_hi, T2_4_2_hi, _df = planet(virt_4_2_hi, alpha=alpha_hi, TR=TRv, pc_axis=-1)
    _Meff, T1_4_2_lo, T2_4_2_lo, _df = planet(virt_4_2_lo, alpha=alpha_lo, TR=TRv, pc_axis=-1)
    _Meff, T1_4_4_hi, T2_4_4_hi, _df = planet(virt_4_4_hi, alpha=alpha_hi, TR=TRv, pc_axis=-1)
    _Meff, T1_4_4_lo, T2_4_4_lo, _df = planet(virt_4_4_lo, alpha=alpha_lo, TR=TRv, pc_axis=-1)

    #T1_4_2_hi, T2_4_2_hi, _Meff = fimtre_opt(TR0_4_hi, TR1_2_hi, TR0, TR1, pcs4, pcs2, alpha=alpha_hi, pc_axis=-1)
    

    plt.imshow(T2_6_0_lo)
    plt.show()
    plt.imshow(T2_4_2_hi)
    plt.show()
