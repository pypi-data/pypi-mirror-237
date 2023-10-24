"""
Description:
    Range independent pulse synthesis with gradients

Date:
    9/22/2023

Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego
"""

import numpy as np
from pykrak import pykrak_env, pressure_calc
from matplotlib import pyplot as plt
import mpi4py.MPI as MPI
from interp.interp import get_spline, splint, vec_splint
from adjoint import get_zfg_eta_ai, 
from pykrak.sturm_seq



def get_modes(env, freq, **kwargs):
    env.add_freq(freq)
    env.get_krs(**kwargs) 
    modes = pykrak_env.Modes(env.freq, env.krs, env.phi, env.M, env.phi_z)
    return modes

def single_mode_freq_interp(des_freq_arr, freq_arr, kr_arr, phi_zs_vals_arr, phi_zr_vals_arr):
    """
    Interpolate a single modes values onto a frequency grid
    des_freq_arr - desired frequencies, assumed to be wihtin the bounds of freq_arr
    freq_arr- frequencies at which the modes have been computed
    kr_arr - kr value at each frequency
    phi_zs_vals_arr - phi_zs values at each frequency
    phi_zr_vals_arr - phi_zr values at each frequency
    """
    if des_freq_arr.min() < freq_arr.min() or (des_freq_arr.max() > freq_arr.max()):
        raise ValueError('Attemptimg to extrapolate beyond frequency bounds')

    num_zs = phi_zs_vals_arr.shape[0]
    num_zr = phi_zr_vals_arr.shape[0]
    num_freq_out = des_freq_arr.size
    phi_zs_out = np.zeros((num_zs, num_freq_out))
    phi_zr_out = np.zeros((num_zr, num_freq_out))

    """
    First interpolate the wave number
    """
    kr_r_spline = get_spline(freq_arr, kr_arr.real, 1e30, 1e30) # uses default 0 second derivative on edges
    kr_i_spline = get_spline(freq_arr, kr_arr.imag, 1e30, 1e30) # uses default 0 second derivative on edges
    kr_r_out, dkr_df_out = vec_splint(des_freq_arr, freq_arr, kr_arr.real, kr_r_spline)
    kr_i_out, dkr_df_out = vec_splint(des_freq_arr, freq_arr, kr_arr.imag, kr_i_spline)
    kr_out = kr_r_out + 1j*kr_i_out

    """
    Now interpolate the mode amplitudes
    """
    for i in range(num_zs):
        phi_zs_vals = phi_zs_vals_arr[i,:]
        phi_zs_spline = get_spline(freq_arr, phi_zs_vals, 1e30, 1e30)
        phi_zs_out[i,:] = vec_splint(des_freq_arr, freq_arr, phi_zs_vals, phi_zs_spline)[0]

    for i in range(num_zr):
        phi_zr_vals = phi_zr_vals_arr[i,:]
        phi_zr_spline = get_spline(freq_arr, phi_zr_vals, 1e30, 1e30)
        phi_zr_out[i,:] = vec_splint(des_freq_arr, freq_arr, phi_zr_vals, phi_zr_spline)[0]
    return kr_out, phi_zs_out, phi_zr_out


class MultiFrequencyModel:
    def __init__(self, env, comm, model_freqs, pulse_freqs):
        self.env = env
        self.comm = comm
        self.rank = self.comm.Get_rank()
        self.num_freqs = self.comm.Get_size()
        self.model_freqs = model_freqs
        self.pulse_freqs = pulse_freqs # array
        self.freq = self.model_freqs[self.rank]
        print('rank, freq', self.rank, self.freq)

    def run_model(self, zs, zr, rs, **model_kwargs):
        """
        Run the forward model to get modes at each frequency
        in model_freqs
        zs is np array
        zr is np array
        rs is scalar 
        Then, interpolate these to get the 
        - modes at source position
        - modes at receiver positions
        - mean propagation wavenumbers 
        at each frequency in pulse freqs using ?
            spline?
        """

        # step 1: run model at the model frequencies
        modes = get_modes(self.env, self.freq, **model_kwargs) 
        M =modes.M
        krs = modes.krs
        phi_zs = modes.get_phi_zr(zs)
        phi_zr = modes.get_phi_zr(zr)

        # step 2: use the rank 0 process to collect all the modal information
        self.comm.Barrier()
        krs_freq_list = self.comm.gather(krs, root=0)
        phi_zs_freqs_list = self.comm.gather(phi_zs, root=0)
        phi_zr_freqs_list = self.comm.gather(phi_zr, root=0)
        if self.rank == 0: # interpolate the modal values onto all the frequencies using a spline

            plt.figure()
            for i in range(self.num_freqs):
                krs = krs_freq_list[i]
                plt.plot([self.model_freqs[i]]*krs.size,krs.real, 'ko')



        # step 3: interpolate the modal values onto the pulse frequencies
        if self.rank == 0:
            M_freq_list = [x.size for x in krs_freq_list] #
            print('M list for freqs in the model', M_freq_list)
            M_max = max(M_freq_list)
            krs_pulse_freq_list = [[] for x in self.pulse_freqs]
            phi_zs_pulse_freq_list = [[] for x in self.pulse_freqs]
            phi_zr_pulse_freq_list = [[] for x in self.pulse_freqs]
            for i in range(M_max): # interpolate onto grid pulse_freqs, add to list
                """ get the frequencies that this mode exists at """
                mode_i_freq_inds = [x for x in range(self.num_freqs) if i < M_freq_list[x]] # these index frequencies that have mode
                mode_i_freqs = np.array([self.model_freqs[x] for x in mode_i_freq_inds])
                kr_vals = np.array([krs_freq_list[x][i] for x in mode_i_freq_inds])
                phi_zs_vals = np.array([phi_zs_freqs_list[x][:,i] for x in mode_i_freq_inds]).T # so first index is z, second is frequency
                phi_zr_vals = np.array([phi_zr_freqs_list[x][:,i] for x in mode_i_freq_inds]).T

                min_f = mode_i_freqs.min()
                max_f = mode_i_freqs.max()


                """ interpolate onto pulse_freqs that support mode """
                pulse_freq_mask = (self.pulse_freqs >= min_f) & (self.pulse_freqs <= max_f) 
                if np.sum(pulse_freq_mask) > 0:
                    freqs = np.array(mode_i_freqs)
                    kr_vals = np.array(kr_vals)
                    phi_zs_vals = np.array(phi_zs_vals)
                    phi_zr_vals = np.array(phi_zr_vals)
                    kr_interp, phi_zs_interp, phi_zr_interp = single_mode_freq_interp(self.pulse_freqs[pulse_freq_mask], freqs, kr_vals, phi_zs_vals, phi_zr_vals)

                    ind_counter = 0
                    for j in range(len(self.pulse_freqs)):
                        if pulse_freq_mask[j]:
                            krs_pulse_freq_list[j].append(kr_interp[ind_counter])
                            phi_zs_pulse_freq_list[j].append(phi_zs_interp[:,ind_counter])
                            phi_zr_pulse_freq_list[j].append(phi_zr_interp[:,ind_counter])
                            ind_counter += 1

        fields = np.zeros((zs.size, zr.size, len(self.pulse_freqs)), dtype=np.complex128)
        # step 4: use interpolated modal values to get fields at each pulse frequency
        if self.rank == 0:
            for pulse_freq_index in range(len(self.pulse_freqs)):
                field = np.zeros((zs.size, zr.size), dtype=np.complex128)
                phi_zs_list = phi_zs_pulse_freq_list[pulse_freq_index]
                phi_zs_arr = np.array(phi_zs_list).T
                phi_zr_list = phi_zr_pulse_freq_list[pulse_freq_index]
                phi_zr_arr = np.array(phi_zr_list).T
                krs = np.array(krs_pulse_freq_list[pulse_freq_index])
                M = krs.size
                if M == 0:
                    pass
                else:
                    plt.plot(self.pulse_freqs[pulse_freq_index]*np.ones(M), krs.real, 'ro')
                    for i in range(zs.size):
                        phi_zs_arr = phi_zs_arr[i,:].reshape(1, M)
                        p = pressure_calc.get_pressure(phi_zr_arr, phi_zs_arr, krs, rs)
                        field[i,:] = p[:,0]
                fields[...,pulse_freq_index] = field


        return fields
            
                





        #p = self.model.compute_field(zs, zr, rs)
        #p = p[0,0]
        #self.p = p
        return p


