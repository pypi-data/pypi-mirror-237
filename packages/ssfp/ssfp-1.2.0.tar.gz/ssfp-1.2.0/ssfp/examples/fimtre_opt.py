'''Try finding T1, T2 the old fashioned way.'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

from ssfp import bssfp, gs_recon, fimtre


if __name__ == '__main__':

    T1 = 1.75
    T2 = 1
    M0 = 11
    alpha = np.deg2rad(90)
    TR0, TR1 = 3e-3, 6e-3
    df = 1/(2*TR0)

    pcs4 = np.linspace(0, 2*np.pi, 4, endpoint=False)
    pcs2 = np.linspace(0, 2*np.pi, 2, endpoint=False)
    
    I0 = bssfp(T1, T2, TR0, alpha, field_map=df, phase_cyc=pcs4[None, None, :], M0=M0)
    I1 = bssfp(T1, T2, TR1, alpha, field_map=df, phase_cyc=pcs2[None, None, :], M0=M0)

    def obj(x, df0):
        T10, T20, M00 = x[:]
        I00 = bssfp(T10, T20, TR0, alpha, field_map=df0, phase_cyc=pcs4[None, None, :], M0=M00)
        I11 = bssfp(T10, T20, TR1, alpha, field_map=df0, phase_cyc=pcs2[None, None, :], M0=M00)
        return np.linalg.norm(I0 - I00) + np.linalg.norm(I1 - I11)

    Meff = np.abs(gs_recon(I0, pc_axis=-1))[0][0]
    df0 = fimtre(I0, I1, TR0, TR1, rad=False)
    print(df, df0)
    print(M0, Meff)
    res = minimize(obj, [1, 1, Meff], args=(df0,), bounds=[(0, 5), (0, 5), (0, 100)])
    print(res)
