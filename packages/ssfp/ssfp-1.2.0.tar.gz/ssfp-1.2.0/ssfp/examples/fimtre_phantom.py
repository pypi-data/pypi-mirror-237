'''Do a doped-water phantom.'''

import numpy as np
import matplotlib.pyplot as plt

from ssfp import planet, robustcc, fimtre

    
if __name__ == '__main__':
    data0 = np.load('data/tr6.npy')
    data1 = np.load('data/tr12.npy')
    TR0, TR1 = 6e-3, 12e-3
    alpha = np.deg2rad(70)
    nx, ny, nc, npcs = data0.shape[:]

    data0 = robustcc(data0, method='simple', mask=None, coil_axis=-2, pc_axis=-1)
    data0 = np.moveaxis(data0, 1, 2)
    data1 = robustcc(data1, method='simple', mask=None, coil_axis=-2, pc_axis=-1)
    data1 = np.moveaxis(data1, 1, 2)
    
    # virtual ellipse
    theta = fimtre(data0[..., ::2], data1[..., ::2], TR0, TR1, pc_axis=-1)[..., None]
    ve = np.concatenate((data0[..., ::2], data1[..., ::2]*np.exp(1j*theta)), axis=-1)
    ve = np.take_along_axis(ve, np.argsort(np.angle(ve), axis=-1), axis=-1)
    print(ve.shape)

    TRv = (TR0+TR1)/2
    _Meff, T1, T2, df = planet(ve, alpha=alpha, TR=TRv, pc_axis=-1)
    df = np.nan_to_num(df)

    nx, ny = 1, 3
    plt.subplot(nx, ny, 1)
    plt.imshow(T1, vmin=0, vmax=.2)

    plt.subplot(nx, ny, 2)
    plt.imshow(T2, vmin=0, vmax=.2)
    
    plt.subplot(nx, ny, 3)
    plt.imshow(theta)

    plt.show()
