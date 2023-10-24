"""
Description:

Date:

Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib
from pyat.pyat.readwrite import read_env, read_modes
from pyat.pyat.env import SSP, plot_ssp
from pykrak.pykrak_env import Env
from pyat.pyat import env as pyat_env
import os

def read_krs_from_prt_file(prt_file):
    """
    .mod files have krs in single precision
    .prt files are 16 digit rounded krs in double precision
    which is more accurate
    """
    with open(prt_file, 'r') as x:
        i = 0
        lines = x.readlines()
        for line in lines:
            line = line.strip(' ')
            if line[0] == 'I':
                print(i)
                break
            i += 1
        i += 1 # now i is the first mode one
        krs = []
        while True:
            line = lines[i]
            line = line.strip(' ')
            if line[0] == '_':
                return krs      
            split_line = line.split(' ')
            krs.append(float(split_line[2]))
            i += 1
            
def init_pykrak_env(freq, ssp, bdry, pos, beam, cint, RMax):
    """
    Initialize a pykrak env obj from the values read in from the env files
    """

    N_list = ssp.N
    z_list = [np.array(x.z) for x in ssp.raw]
    c_list = [np.array(x.alphaR) for x in ssp.raw]
    rho_list = [np.array(x.rho) for x in ssp.raw]
    attn_list = [np.array(x.alphaI) for x in ssp.raw]
    #attn_list = [2*np.pi*freq *x / y**2 for x,y in zip(cI_list, c_list)]
    # this is npm ...so need to reverse convert?
    bot_bdry = bdry.Bot
    opt = bot_bdry.Opt
    hs = bot_bdry.hs
    # I don't handle shear
    c_hs = hs.alphaR
    if hs.betaR != 0:
        print('Warning. Ignoring halfspace shear')
    rho_hs = hs.rho
    c_hs = float(c_hs)
    rho_hs = float(rho_hs)
    #cI_hs = hs.alphaI
    #attn_hs = 2*np.pi*freq * cI_hs / c_hs**2
    attn_hs = hs.alphaI
    print('attn_hs', attn_hs)
    top_opt = bdry.Top.Opt
    top_opt = top_opt.strip()
    atten_opt = top_opt[2]
    atten_opts = ['N', 'F', 'M', 'W', 'Q']
    py_opts = ['npm', 'dbpkmhz', 'dbpm', 'dbplam', 'q']
    attn_units = py_opts[atten_opts.index(atten_opt)]
    print('attn units', attn_units)
    env= Env(z_list, c_list, rho_list, attn_list, c_hs, rho_hs, attn_hs, attn_units)
    env.add_freq(freq)
    return env, N_list

def get_krak_inputs(env, twod=False):
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
    if twod:
        Opt += '*'
    bottom = pyat_env.BotBndry(Opt, hs)
    Topopt = 'CVF'
    top = pyat_env.TopBndry(Topopt) # C linear, vaccuum surface bndry, dbpkmhz attenuation
    bdy = pyat_env.Bndry(top, bottom)
    return ssp, bdy 

