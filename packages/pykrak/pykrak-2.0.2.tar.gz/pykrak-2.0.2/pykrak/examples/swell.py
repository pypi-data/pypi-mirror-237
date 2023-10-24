"""
def get_krak_inputs(env):
    z_list, c_list, rho_list, attn_list = env.z_list, env.c_list, env.rho_list, env.attn_list
    shear_list = [np.zeros(x.size) for x in z_list]
    shear_attn_list = [np.zeros(x.size) for x in z_list]
    ssp_list = [pyat_env.SSPraw(z, c, shear, rho, attn, shear_attn) for z, c, shear, rho, attn, shear_attn in zip(z_list, c_list, shear_list, rho_list, attn_list, shear_attn_list)]
    nmedia = len(z_list)
    depths = [z[0] for z in z_list]
    depths.append(z_list[-1][-1])
    sigma = [0 for x in depths]
    ssp = pyat_env.SSP(ssp_list, depths, nmedia, sigma=sigma)
    hs = pyat_env.HS(alphaR=env.c_hs, betaR=0.0, rho = env.rho_hs, alphaI=env.attn_hs, betaI=0)
    Opt = 'A'
    bottom = pyat_env.BotBndry(Opt, hs)
    top = pyat_env.TopBndry('CVF') # C linear, vaccuum surface bndry, dbpkmhz attenuation
    bdy = pyat_env.Bndry(top, bottom)
    return ssp, bdy 
Description:

Date:
Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib
import time
from pykrak.pykrak_env import Env
from pyat.pyat import readwrite as rw
from pyat.pyat import env as pyat_env
from pykrak.test_helpers import read_krs_from_prt_file, init_pykrak_env, get_krak_inputs

def get_swellex_env():
    z1 =  np.array([0.0, 0.83, 1.39, 2.13, 2.95, 3.65, 4.53, 5.44, 6.15, 6.8, 7.73, 8.69, 9.45, 10.12, 11.0, 12.0, 12.79, 13.53, 14.29, 15.27, 16.1, 16.85, 17.87, 19.03, 19.78, 20.33, 21.16, 22.17, 23.25, 24.5, 25.77, 26.97, 28.12, 29.1, 29.5, 29.73, 29.9, 30.27, 30.59, 30.98, 31.19, 31.31, 31.44, 31.81, 31.94, 32.08, 32.33, 32.55, 32.71, 32.9, 33.41, 34.17, 35.03, 35.89, 36.78, 37.82, 38.9, 39.81, 40.48, 41.16, 42.24, 43.42, 44.51, 45.65, 46.72, 47.72, 48.72, 49.65, 50.6, 51.08, 51.48, 51.85, 51.98, 52.68, 53.81, 54.86, 55.96, 57.07, 58.15, 59.0, 59.73, 60.6, 61.77, 62.85, 63.85, 64.82, 66.0, 66.96, 67.83, 68.74, 69.74, 70.71, 71.69, 72.65, 73.7, 74.72, 75.93, 77.04, 78.0, 78.83, 79.65, 80.5, 81.32, 81.94, 82.69, 83.79, 84.95, 86.11, 87.25, 88.26, 89.06, 89.88, 90.7, 91.39, 92.02, 92.73, 93.35, 93.85, 94.59, 95.56, 96.08, 96.4, 96.69, 96.88, 97.34, 97.79, 98.42, 98.95, 99.06, 99.28, 99.59, 100.5, 101.39, 102.16, 102.88, 103.66, 104.46, 104.97, 105.47, 106.24, 107.04, 107.6, 108.18, 108.84, 109.53, 109.98, 110.23, 110.71, 111.21, 111.44, 111.68, 112.09, 112.38, 112.75, 113.2, 113.61, 113.93, 114.22, 114.8, 115.94, 117.19, 118.56, 119.98, 121.38, 122.57, 123.74, 125.02, 126.39, 127.67, 129.04, 130.4, 131.52, 132.62, 133.9, 135.11, 136.24, 137.41, 138.69, 139.93, 140.97, 142.04, 143.16, 144.22, 145.22, 146.23, 147.28, 148.25, 149.29, 150.45, 151.46, 152.52, 153.76, 154.85, 155.8, 156.82, 157.94, 159.05, 160.21, 161.33, 162.35, 163.46, 164.52, 164.75, 168.17, 169.2, 170.18, 171.13, 172.08, 172.96, 173.84, 174.68, 175.51, 176.39, 177.13, 177.9, 178.75, 179.73, 180.38, 181.09, 181.78, 182.41, 183.02, 183.57, 184.15, 184.9, 185.59, 186.25, 187.01, 187.95, 188.96, 189.98, 191.04, 192.18, 193.13, 193.9, 194.43, 195.05, 195.71, 196.17, 196.67, 197.27, 197.92, 198.47, 198.97, 199.32, 199.59, 199.95, 200.16, 208.35, 216.5])
    c1 = np.array([1521.94, 1521.95, 1521.94, 1521.9, 1521.84, 1521.74, 1521.53, 1521.18, 1520.84, 1520.51, 1520.04, 1519.58, 1519.13, 1518.59, 1517.45, 1515.25, 1512.28, 1509.48, 1507.26, 1505.05, 1503.4, 1502.35, 1501.27, 1500.28, 1499.89, 1499.64, 1499.22, 1498.59, 1497.96, 1497.13, 1496.52, 1496.12, 1495.77, 1495.49, 1495.4, 1495.34, 1495.3, 1495.21, 1495.12, 1495.02, 1494.95, 1494.91, 1494.87, 1494.7, 1494.63, 1494.56, 1494.4, 1494.27, 1494.21, 1494.14, 1493.93, 1493.67, 1493.44, 1493.25, 1493.1, 1492.92, 1492.68, 1492.54, 1492.45, 1492.37, 1492.27, 1492.18, 1492.13, 1492.08, 1492.03, 1491.98, 1491.93, 1491.89, 1491.84, 1491.82, 1491.79, 1491.77, 1491.76, 1491.69, 1491.54, 1491.37, 1491.23, 1491.13, 1491.04, 1490.97, 1490.91, 1490.84, 1490.74, 1490.66, 1490.59, 1490.51, 1490.42, 1490.35, 1490.3, 1490.24, 1490.17, 1490.07, 1489.93, 1489.85, 1489.79, 1489.73, 1489.68, 1489.66, 1489.63, 1489.61, 1489.61, 1489.62, 1489.62, 1489.63, 1489.63, 1489.63, 1489.62, 1489.59, 1489.55, 1489.51, 1489.46, 1489.41, 1489.33, 1489.24, 1489.16, 1489.14, 1489.13, 1489.12, 1489.07, 1488.96, 1488.89, 1488.83, 1488.78, 1488.75, 1488.65, 1488.59, 1488.55, 1488.51, 1488.5, 1488.49, 1488.46, 1488.33, 1488.25, 1488.2, 1488.18, 1488.17, 1488.16, 1488.15, 1488.13, 1488.08, 1488.05, 1488.03, 1488.0, 1487.99, 1487.97, 1487.96, 1487.95, 1487.92, 1487.87, 1487.84, 1487.81, 1487.77, 1487.75, 1487.73, 1487.71, 1487.7, 1487.69, 1487.69, 1487.7, 1487.73, 1487.78, 1487.83, 1487.91, 1488.02, 1488.09, 1488.14, 1488.19, 1488.28, 1488.4, 1488.54, 1488.67, 1488.74, 1488.81, 1488.87, 1488.92, 1488.95, 1488.97, 1488.96, 1488.95, 1488.93, 1488.92, 1488.91, 1488.91, 1488.91, 1488.91, 1488.89, 1488.89, 1488.89, 1488.9, 1488.9, 1488.92, 1488.93, 1488.95, 1488.96, 1488.98, 1488.99, 1489.0, 1489.0, 1488.99, 1488.96, 1488.92, 1488.9, 1488.88, 1488.53, 1488.47, 1488.42, 1488.44, 1488.43, 1488.45, 1488.46, 1488.48, 1488.48, 1488.5, 1488.51, 1488.53, 1488.57, 1488.55, 1488.6, 1488.61, 1488.61, 1488.55, 1488.55, 1488.54, 1488.54, 1488.55, 1488.53, 1488.5, 1488.51, 1488.53, 1488.51, 1488.47, 1488.4, 1488.35, 1488.34, 1488.32, 1488.31, 1488.27, 1488.25, 1488.25, 1488.26, 1488.27, 1488.29, 1488.3, 1488.3, 1488.32, 1488.31, 1488.31, 1488.26, 1488.26, 1488.26])
    rho1 = np.ones((c1.size))
    attn1 = np.zeros((c1.size))

    z2= np.array([216.5, 240.0])
    c2 = np.array([1572.4, 1593.00])
    rho2 = np.array([1.8, 1.8])
    attn2 = np.array([0.3, 0.3])
    #attn2 *= 0

    c_hs = 1880.
    rho_hs = 2.00
    #attn_hs = 0.0
    attn_hs = 0.1
    attn_units = 'dbpkmhz'
    z_list = [z1, z2]
    c_list = [c1, c2]
    rho_list = [rho1, rho2]
    attn_list = [attn1, attn2]
    #z_list = [z1]
    #c_list = [c1]
    #rho_list = [rho1]
    #attn_list = [attn1]
    

    env = Env(z_list, c_list, rho_list, attn_list, c_hs, rho_hs, attn_hs, attn_units)
    return env


def test_swell_env():
    env = get_swellex_env()
    env.plot_env()
    plt.show()
    freq = 100.0
    env.add_freq(freq)

    dz = freq / 1500
    h_desired = dz / 20

    N_list = [int(np.ceil((z[-1] - z[0]) / h_desired)) for z in env.z_list]

    zs = 50.0
    source = pyat_env.Source(np.array([zs]))

    zr = np.linspace(0.0, 220.0, 100)
    rs = 10*1e3
    ranges = np.linspace(100.0, rs, 1000)
    dom = pyat_env.Dom(ranges, zr)

    pos = pyat_env.Pos(source, dom)

    ssp, bdy = get_krak_inputs(env)


    model = 'KRAKEN'
    envfil = 'at_files/swell_env'
    TitleEnv = 'SWellEx 96'

    cInt = pyat_env.cInt(0, 0) # automatic?
    cInt = pyat_env.cInt(np.min(env.c_list[0]), env.c_hs)
    RMax = 0
    NMESH = [x  for x in N_list]
    rw.write_env(envfil, model, TitleEnv, freq, ssp, bdy, pos, [], cInt, RMax, NMESH=NMESH)
    import os
    os.system('cd at_files && kraken.exe swell_env')

    #env,_ = init_pykrak_env(freq, ssp, bdy, pos, None, cInt, RMax)

    fname = 'at_files/swell_env.mod'
    options = {'fname':fname, 'freq':freq}
    modes = rw.read_modes(**options)
    krak_krs = modes.k
    print('krak krs', krak_krs)

    pykrak_krs = env.get_krs(**{'cmin':np.min(env.c_list[0]), 'cmax':env.c_hs-1e-9, 'N_list':N_list, 'Nh':1})
    print('pykrak', pykrak_krs.astype(str))

    prt_krs = np.array(read_krs_from_prt_file('at_files/swell_env.prt'))
    print('prt file',[str(x) for x in prt_krs])

    plt.figure()

    plt.plot((krak_krs.conj() - pykrak_krs).real)
    plt.figure()
    plt.plot((prt_krs.conj() - pykrak_krs).real)
    plt.show()


test_swell_env()
