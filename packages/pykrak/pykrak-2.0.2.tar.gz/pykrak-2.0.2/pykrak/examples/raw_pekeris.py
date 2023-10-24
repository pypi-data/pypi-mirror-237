""" Description:
Calculate normal modes and TL for Pekeris waveguide
Using raw_pykrak

Date:
4/18/2023

Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib

from pykrak.pykrak_env import Env
from pykrak.raw_pykrak import get_modes
from pykrak.attn_pert import get_attn_conv_factor, get_c_imag
from pykrak.sturm_seq import get_arrs, cat_list_to_arr

z_list = [np.array([0, 5000.])]
c_list = [np.array([1500., 1500.])]
rho_list = [np.ones(2)]
attn_list = [.001*np.ones(2)]
c_hs = 2000.
rho_hs = 2.0
attn_hs = .0
attn_units ='dbpkmhz'

freq = 10.
omega = 2*np.pi*freq
#conv_factor = get_attn_conv_factor(attn_units, freq)

#attn_hs_npm = attn_hs * conv_factor
c_hs_imag = get_c_imag(c_hs, attn_hs, attn_units, omega)
c_hs += 1j*c_hs_imag
k_hs_sq = omega**2 / c_hs**2

env = Env(z_list, c_list, rho_list, attn_list, c_hs, rho_hs, attn_hs, attn_units)
env.add_freq(freq)
dz = 1500 / (60*freq) #
N_list = [int((z_list[i][-1] - z_list[i][0])/ dz) + 1 for i in range(len(z_list))]
z_list, c_list, rho_list, attn_list, k_sq_list= env.interp_env_vals(N_list)
env.add_freq(freq)
h_list = [x[1] - x[0] for x in z_list]
h_arr, ind_arr, z_arr, c_arr, rho_arr = get_arrs(h_list, z_list, c_list, rho_list)
k_sq_arr, _ = cat_list_to_arr(k_sq_list)

cmin = 1500.
cmax = 1999.

krs, phi, phi_z = get_modes(freq, h_arr, ind_arr, z_arr, k_sq_arr, rho_arr,  k_hs_sq, rho_hs,  cmin, cmax)
print(krs.astype(str))

zr = np.array([2500.])
zs = np.array([500.])
r = np.linspace(2*1e5, 2.2*1e5, 1000)

from pykrak import pressure_calc as pc
p = pc.get_grid_pressure(zr, phi_z, phi, krs, zs, r)
tmp_r = np.array([1.0])
tmp_p = pc.get_grid_pressure(zr, phi_z, phi, krs, zr, tmp_r)
print(abs(tmp_p), 1/(4*np.pi))

print(p.shape)
p = np.squeeze(p)
tl = -20*np.log10(np.sqrt(2*np.pi)*abs(p)) # this is actually incorrect, it should be 4pi
# this factor gets agreement with the KRAKEN manual. I think the figure in the manual does not account for the fact that the pressure field calculation has a factor of 1/sqrt(8 pi) in it 
plt.figure()
plt.plot(r*1e-3, tl,'k')
plt.xlabel('Range (km)')
plt.ylabel('Loss (dB)')
plt.annotate('f = 10 Hz\nsd=500 m\n rd=2500 m', xy=(0.9, 0.9), xycoords='axes fraction')
plt.ylim([110, 70])
plt.show()



