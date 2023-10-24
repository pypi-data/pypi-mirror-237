"""
Description:
    Compare PyKrak coupled mode run KRAKEN

Date:
    10/9/2023

Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego
"""

import numpy as np
from matplotlib import pyplot as plt
from pyat.pyat.readwrite import read_env, write_env, write_fieldflp, read_shd, write_bathy

from pykrak import coupled_modes as cm
from pykrak.test_helpers import get_krak_inputs

from pykrak.linearized_model import LinearizedEnv
from pyat.pyat import env as pyat_env
import os

from pykrak.range_dep_model import RangeDepModel 
from pykrak.cm_model import CMModel
import time



#os.system('rm cm_log.txt')
def downslope_test():
    freq = 200.0
    omega = 2*np.pi*freq
    Z0 = 100.0
    Z1 = 200.0
    R = 10*1e3
    num_segs = 21
    Zvals = np.linspace(Z0, Z1, num_segs)
    Zmax = Zvals.max()
    rgrid = np.linspace(0.0, R, num_segs)
    rcm_grid = cm.get_seg_interface_grid(rgrid)
    cw = 1500.0
    rho_w = 1.0
    c_hs = 1800.0
    rho_hs = 2.0
    attn_hs = 0.2
    attn_units = 'dbpkmhz'
    mesh_dz = (1500 / freq) / 40 # lambda / N spacing

    cmin = 1500.0
    cmax = 1799.0

    # Pekeris waveguide at each segment
    krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list = [], [], [], [], [], []
    nmesh_list = []
    env_list = []
    # Loop over each segment and run pykrak to get the necessary values
    for seg_i in range(num_segs):
        Z = Zvals[seg_i]
        env_z_list = [np.array([0.0, Z]), np.array([Z, Zmax])]
        env_c_list = [np.array([cw, cw]), np.array([c_hs, c_hs])]
        env_rho_list = [np.array([rho_w, rho_w]), np.array([rho_hs, rho_hs])]
        env_attn_list = [np.array([0.0, 0.0]), np.array([attn_hs, attn_hs])]
        N_list = [max(int(np.ceil(Z / mesh_dz)), 20), max(int(np.ceil((Zmax - Z) / mesh_dz)), 10)]

        if Z == Zmax:
            env_z_list = [env_z_list[0]]
            env_c_list = [env_c_list[0]]
            env_rho_list = [env_rho_list[0]]
            env_attn_list = [env_attn_list[0]]
            N_list = [N_list[0]]


        nmesh_list.append(N_list)


        env = LinearizedEnv(freq, env_z_list, env_c_list, env_rho_list, env_attn_list, c_hs, rho_hs, attn_hs, attn_units, N_list, cmin, cmax)
        
        env_list.append(env)
        env.add_c_pert_matrix(env.z_arr, np.zeros((env.z_arr.size,1)))
        env.add_x0(np.array([0.0]))
        #tmp_krs = env.get_krs(**{'N_list': N_list, 'Nh':1})
        modes = env.full_forward_modes()
        krs = modes.krs
        krs_str = krs.astype(str)
        #with open('cm_log.txt', 'a') as f:
        #    f.write('Running pykrak for depth {0} with mesh N: {1}\n'.format(Z, N_list))
        #    for i in range(krs.size):
        #        f.write('{0}  {1}\n'.format(i + 1, krs_str[i]))
        phi = modes.phi
        zgrid = modes.z
        rhogrid = env.get_rho_grid(N_list)
    
        krs_list.append(krs)
        phi_list.append(phi)
        rho_list.append(rhogrid)
        zgrid_list.append(zgrid)
        c_hs_list.append(c_hs)
        rho_hs_list.append(rho_hs)


    # Now we have all the values we need to run the coupled mode model

    zs = 25.    

    same_grid = False
    ranges = np.linspace(100.0, 10*1e3, 1000)

    zout = np.linspace(0.0, Zvals.max(), nmesh_list[-1][0])
    zr = zout[1:]
    p_arr = np.zeros((zr.size, ranges.size-1), dtype=np.complex128)
    #for i in range(1,ranges.size):
    #    rs = ranges[i]
    #    p = cm.compute_cm_pressure(omega, krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list, rcm_grid, zs, zr, rs, same_grid, cont_part_velocity=False) # False for KRAKEN model comp
    #    p_arr[:,i-1] = p

    arr_zs = np.array([zs])
    p_arr = cm.compute_arr_cm_pressure(omega, krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list, rcm_grid, arr_zs, zr, ranges[1:], same_grid, cont_part_velocity=False) # False for KRAKEN model comp
    p_arr = np.squeeze(p_arr)

    p_tl = 20*np.log10(np.abs(p_arr)) 
    plt.figure()
    plt.pcolormesh(ranges[1:]*1e-3, zr, p_tl)
    plt.gca().invert_yaxis()
    plt.colorbar()

    zind = np.argmin(np.abs(zr - 100.0))
    plt.figure()
    plt.plot(ranges[1:]*1e-3, p_tl[zind,:], 'k')

    p_100 = p_arr[zind,:]


    # now use KRAKEN
    name = 'at_files/cm_pekeris_test.env'
    model='kraken'
    rmax = 0 # force use of the first mesh
    source = pyat_env.Source(np.array([zs]))
    dom = pyat_env.Dom(ranges*1e-3, zout)
    pos = pyat_env.Pos(source, dom)
    beam = None
    cint= pyat_env.cInt(cmin, cmax)

    for seg_i in range(num_segs):
        env = env_list[seg_i]
        ssp, bdy = get_krak_inputs(env, twod=True)

        NMESH = nmesh_list[seg_i]
        NMESH = [x-1 for x in NMESH]
        if seg_i == 0:
            append = False
        else:
            append=True
        write_env(name, model, 'Auto gen from Env object', freq, ssp, bdy, pos, beam, cint, rmax, NMESH=NMESH, append=append)
        

    #bathy_grid = np.zeros((rgrid.size, 2))
    #bathy_grid[:,0] = rgrid*1e-3
    #bathy_grid[:,1] = Zvals
    #write_bathy('at_files/cm_pekeris_test.bty', bathy_grid)
    
    # run kraken
    import os
    os.system('cd at_files && kraken.exe cm_pekeris_test')

    # run field
    #kwargs = {'rProf':rcm_grid*1e-3, 'NProf':rgrid.size}
    kwargs = {'rProf':rgrid*1e-3, 'NProf':rgrid.size}
    field_dom = pyat_env.Dom(ranges*1e-3,zr)
    pos_field = pyat_env.Pos(source, field_dom)
    write_fieldflp('at_files/cm_pekeris_test.flp', 'RCOC', pos_field, **kwargs)
    os.system('cd at_files && field.exe cm_pekeris_test')


    [ PlotTitle, PlotType, freqVec, atten, pos, pressure ] = read_shd('at_files/cm_pekeris_test.shd')
    pressure = np.squeeze(pressure)
    # correct KRAKEN scaling to agree with mine
    pressure /= np.sqrt(2*np.pi) 
    pressure /= np.sqrt(8 *np.pi)
    k_tl = 20*np.log10(np.abs(pressure))
    kp_100 = pressure[zind,:][1:]
    zind = np.argmin(np.abs(pos.r.depth - 100.0))
    plt.plot(ranges[1:]*1e-3, k_tl[zind,:][1:], 'b')

    plt.figure()
    plt.pcolormesh(ranges, zout[1:], k_tl)
    plt.gca().invert_yaxis()
    plt.colorbar()
    fig, axes = plt.subplots(2,1, sharex=True)
    axes[0].plot(ranges[1:]*1e-3, np.abs(p_100), 'k')
    axes[0].plot(ranges[1:]*1e-3, np.abs(kp_100), 'b')

    axes[1].plot(ranges[1:]*1e-3, np.angle(p_100), 'k')
    axes[1].plot(ranges[1:]*1e-3, np.angle(kp_100), 'b')

    plt.show()

def duct_test():
    """
    Put in a duct halfway between source and receiver in deep
    water
    """
    freq = 35.0
    omega = 2*np.pi*freq
    Z = 4000.0
    R = 100*1e3 
    num_segs = 21
    rgrid = np.linspace(0.0, R, num_segs)
    rcm_grid = cm.get_seg_interface_grid(rgrid)
    cw = 1500.0
    rho_w = 1.0
    c_hs = 1800.0
    rho_hs = 2.0
    attn_hs = 0.2
    attn_units = 'dbpkmhz'
    mesh_dz = (1500 / freq) / 20 # lambda /20 spacing

    cmin = 1500.0
    cmax = 1799.0

    # Pekeris waveguide at each segment
    krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list = [], [], [], [], [], []
    nmesh_list = []
    env_list = []
    # Loop over each segment and run pykrak to get the necessary values
    for seg_i in range(num_segs):
        Z = Zvals[seg_i]
        env_z_list = [np.array([0.0, Z]), np.array([Z, Zmax])]
        env_c_list = [np.array([cw, cw]), np.array([c_hs, c_hs])]
        env_rho_list = [np.array([rho_w, rho_w]), np.array([rho_hs, rho_hs])]
        env_attn_list = [np.array([0.0, 0.0]), np.array([attn_hs, attn_hs])]
        N_list = [max(int(np.ceil(Z / mesh_dz)), 20), max(int(np.ceil(Zmax - Z)), 10)]

        if Z == Zmax:
            env_z_list = [env_z_list[0]]
            env_c_list = [env_c_list[0]]
            env_rho_list = [env_rho_list[0]]
            env_attn_list = [env_attn_list[0]]
            N_list = [N_list[0]]


        nmesh_list.append(N_list)


        env = LinearizedEnv(freq, env_z_list, env_c_list, env_rho_list, env_attn_list, c_hs, rho_hs, attn_hs, attn_units, N_list, cmin, cmax)
        
        env_list.append(env)
        env.add_c_pert_matrix(env.z_arr, np.zeros((env.z_arr.size,1)))
        env.add_x0(np.array([0.0]))
        #tmp_krs = env.get_krs(**{'N_list': N_list, 'Nh':1})
        modes = env.full_forward_modes()
        krs = modes.krs
        krs_str = krs.astype(str)
        #with open('cm_log.txt', 'a') as f:
        #    f.write('Running pykrak for depth {0} with mesh N: {1}\n'.format(Z, N_list))
        #    for i in range(krs.size):
        #        f.write('{0}  {1}\n'.format(i + 1, krs_str[i]))
        phi = modes.phi
        zgrid = modes.z
        rhogrid = env.get_rho_grid(N_list)
    
        krs_list.append(krs)
        phi_list.append(phi)
        rho_list.append(rhogrid)
        zgrid_list.append(zgrid)
        c_hs_list.append(c_hs)
        rho_hs_list.append(rho_hs)


    # Now we have all the values we need to run the coupled mode model

    zs = 25.    

    same_grid = False
    ranges = np.linspace(100.0, 10*1e3, 1000)

    zout = np.linspace(0.0, Zvals.max(), nmesh_list[-1][0])
    zr = zout[1:]
    p_arr = np.zeros((zr.size, ranges.size-1), dtype=np.complex128)
    #for i in range(1,ranges.size):
    #    rs = ranges[i]
    #    p = cm.compute_cm_pressure(omega, krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list, rcm_grid, zs, zr, rs, same_grid, cont_part_velocity=False) # False for KRAKEN model comp
    #    p_arr[:,i-1] = p

    arr_zs = np.array([zs])
    p_arr = cm.compute_arr_cm_pressure(omega, krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list, rcm_grid, arr_zs, zr, ranges[1:], same_grid, cont_part_velocity=False) # False for KRAKEN model comp
    print(p_arr.shape)

    p_tl = 20*np.log10(np.abs(p_arr)) 
    plt.figure()
    plt.pcolormesh(ranges[1:]*1e-3, zr, p_tl)
    plt.gca().invert_yaxis()
    plt.colorbar()

    zind = np.argmin(np.abs(zr - 100.0))
    plt.figure()
    plt.plot(ranges[1:]*1e-3, p_tl[zind,:], 'k')

    p_100 = p_arr[zind,:]


    # now use KRAKEN
    name = 'at_files/cm_pekeris_test.env'
    model='kraken'
    rmax = 0 # force use of the first mesh
    source = pyat_env.Source(np.array([zs]))
    dom = pyat_env.Dom(ranges*1e-3, zout)
    pos = pyat_env.Pos(source, dom)
    beam = None
    cint= pyat_env.cInt(cmin, cmax)

    for seg_i in range(num_segs):
        env = env_list[seg_i]
        ssp, bdy = get_krak_inputs(env, twod=True)

        NMESH = nmesh_list[seg_i]
        NMESH = [x-1 for x in NMESH]
        if seg_i == 0:
            append = False
        else:
            append=True
        write_env(name, model, 'Auto gen from Env object', freq, ssp, bdy, pos, beam, cint, rmax, NMESH=NMESH, append=append)
        

    #bathy_grid = np.zeros((rgrid.size, 2))
    #bathy_grid[:,0] = rgrid*1e-3
    #bathy_grid[:,1] = Zvals
    #write_bathy('at_files/cm_pekeris_test.bty', bathy_grid)
    
    # run kraken
    import os
    os.system('cd at_files && kraken.exe cm_pekeris_test')

    # run field
    #kwargs = {'rProf':rcm_grid*1e-3, 'NProf':rgrid.size}
    kwargs = {'rProf':rgrid*1e-3, 'NProf':rgrid.size}
    field_dom = pyat_env.Dom(ranges*1e-3,zr)
    pos_field = pyat_env.Pos(source, field_dom)
    write_fieldflp('at_files/cm_pekeris_test.flp', 'RCOC', pos_field, **kwargs)
    os.system('cd at_files && field.exe cm_pekeris_test')


    [ PlotTitle, PlotType, freqVec, atten, pos, pressure ] = read_shd('at_files/cm_pekeris_test.shd')
    pressure = np.squeeze(pressure)
    # correct KRAKEN scaling to agree with mine
    pressure /= np.sqrt(2*np.pi) 
    pressure /= np.sqrt(8 *np.pi)
    k_tl = 20*np.log10(np.abs(pressure))
    kp_100 = pressure[zind,:][1:]
    zind = np.argmin(np.abs(pos.r.depth - 100.0))
    plt.plot(ranges[1:]*1e-3, k_tl[zind,:][1:], 'b')

    plt.figure()
    plt.pcolormesh(ranges, zout[1:], k_tl)
    plt.gca().invert_yaxis()
    plt.colorbar()
    fig, axes = plt.subplots(2,1, sharex=True)
    axes[0].plot(ranges[1:]*1e-3, np.abs(p_100), 'k')
    axes[0].plot(ranges[1:]*1e-3, np.abs(kp_100), 'b')

    axes[1].plot(ranges[1:]*1e-3, np.angle(p_100), 'k')
    axes[1].plot(ranges[1:]*1e-3, np.angle(kp_100), 'b')

    plt.show()

def range_dep_model_test():
    freq = 100.0
    omega = 2*np.pi*freq
    Z0 = 100.0
    Z1 = 200.0
    R = 10*1e3

    from mpi4py import MPI
    world_comm = MPI.COMM_WORLD
    world_rank = world_comm.Get_rank()
    world_size = world_comm.Get_size()

    num_segs = world_size
    Zvals = np.linspace(Z0, Z1, num_segs)
    Zmax = Zvals.max()
    rgrid = np.linspace(0.0, R, num_segs)
    rcm_grid = cm.get_seg_interface_grid(rgrid)
    cw = 1500.0
    rho_w = 1.0
    c_hs = 1800.0
    rho_hs = 2.0
    attn_hs = 0.2
    attn_units = 'dbpkmhz'
    mesh_dz = (1500 / freq) / 20 # lambda /20 spacing

    cmin = 1500.0
    cmax = 1799.0

    # Pekeris waveguide at each segment
    krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list = [], [], [], [], [], []
    nmesh_list = []
    env_list = []
    # Loop over each segment and run pykrak to get the necessary values
    for seg_i in range(num_segs):
        Z = Zvals[seg_i]
        env_z_list = [np.array([0.0, Z]), np.array([Z, Zmax])]
        env_c_list = [np.array([cw, cw]), np.array([c_hs, c_hs])]
        env_rho_list = [np.array([rho_w, rho_w]), np.array([rho_hs, rho_hs])]
        env_attn_list = [np.array([0.0, 0.0]), np.array([attn_hs, attn_hs])]
        N_list = [max(int(np.ceil(Z / mesh_dz)), 20), max(int(np.ceil(Zmax - Z)), 10)]

        if Z == Zmax:
            env_z_list = [env_z_list[0]]
            env_c_list = [env_c_list[0]]
            env_rho_list = [env_rho_list[0]]
            env_attn_list = [env_attn_list[0]]
            N_list = [N_list[0]]


        nmesh_list.append(N_list)


        env = LinearizedEnv(freq, env_z_list, env_c_list, env_rho_list, env_attn_list, c_hs, rho_hs, attn_hs, attn_units, N_list, cmin, cmax)
        
        env_list.append(env)
        env.add_c_pert_matrix(env.z_arr, np.zeros((env.z_arr.size,1)))
        env.add_x0(np.array([0.0]))


    rdm = CMModel(rgrid, env_list, world_comm)
    x0_list = [np.array([0.0]) for x in env_list]
    rdm.run_models(freq, x0_list)


    # Now we have all the values we need to run the coupled mode model

    zs = 25.    

    same_grid = False
    ranges = np.linspace(100.0, 10*1e3, 1000)

    zout = np.linspace(0.0, Zvals.max(), nmesh_list[-1][0])
    zr = zout[1:]
    if world_rank == 0:
        p_arr = rdm.compute_field(np.array([zs]), zr, ranges[1:])
        print(p_arr.shape)

        p_tl = 20*np.log10(np.abs(p_arr)) 
        plt.figure()
        plt.pcolormesh(ranges[1:]*1e-3, zr, p_tl)
        plt.gca().invert_yaxis()
        plt.colorbar()

        zind = np.argmin(np.abs(zr - 100.0))
        plt.figure()
        plt.plot(ranges[1:]*1e-3, p_tl[zind,:], 'k')

        p_100 = p_arr[zind,:]


        # now use KRAKEN
        name = 'at_files/cm_pekeris_test.env'
        model='kraken'
        rmax = 0 # force use of the first mesh
        source = pyat_env.Source(np.array([zs]))
        dom = pyat_env.Dom(ranges*1e-3, zout)
        pos = pyat_env.Pos(source, dom)
        beam = None
        cint= pyat_env.cInt(cmin, cmax)

        for seg_i in range(num_segs):
            env = env_list[seg_i]
            ssp, bdy = get_krak_inputs(env, twod=True)

            NMESH = nmesh_list[seg_i]
            NMESH = [x-1 for x in NMESH]
            if seg_i == 0:
                append = False
            else:
                append=True
            write_env(name, model, 'Auto gen from Env object', freq, ssp, bdy, pos, beam, cint, rmax, NMESH=NMESH, append=append)
            
        # run kraken
        import os
        os.system('cd at_files && kraken.exe cm_pekeris_test')

        # run field
        kwargs = {'rProf':rgrid*1e-3, 'NProf':rgrid.size}
        field_dom = pyat_env.Dom(ranges*1e-3,zr)
        pos_field = pyat_env.Pos(source, field_dom)
        write_fieldflp('at_files/cm_pekeris_test.flp', 'RCOC', pos_field, **kwargs)
        os.system('cd at_files && field.exe cm_pekeris_test')


        [ PlotTitle, PlotType, freqVec, atten, pos, pressure ] = read_shd('at_files/cm_pekeris_test.shd')
        pressure = np.squeeze(pressure)
        # correct KRAKEN scaling to agree with mine
        pressure /= np.sqrt(2*np.pi) 
        pressure /= np.sqrt(8 *np.pi)
        k_tl = 20*np.log10(np.abs(pressure))
        kp_100 = pressure[zind,:][1:]
        zind = np.argmin(np.abs(pos.r.depth - 100.0))
        plt.plot(ranges[1:]*1e-3, k_tl[zind,:][1:], 'b')

        plt.figure()
        plt.pcolormesh(ranges, zout[1:], k_tl)
        plt.gca().invert_yaxis()
        plt.colorbar()
        fig, axes = plt.subplots(2,1, sharex=True)
        axes[0].plot(ranges[1:]*1e-3, np.abs(p_100), 'k')
        axes[0].plot(ranges[1:]*1e-3, np.abs(kp_100), 'b', label='KRAKEN')

        axes[1].plot(ranges[1:]*1e-3, np.angle(p_100), 'k')
        axes[1].plot(ranges[1:]*1e-3, np.angle(kp_100), 'b')

def range_dep_time_test():
    now = time.time()
    freq = 35.0
    omega = 2*np.pi*freq
    Z0 = 1000.0
    Z1 = 1200.0
    R = 10*1e4

    from mpi4py import MPI
    world_comm = MPI.COMM_WORLD
    world_rank = world_comm.Get_rank()
    world_size = world_comm.Get_size()

    num_segs = world_size
    Zvals = np.linspace(Z0, Z1, num_segs)
    Zmax = Zvals.max()
    rgrid = np.linspace(0.0, R, num_segs)
    rcm_grid = cm.get_seg_interface_grid(rgrid)
    cw = 1500.0
    rho_w = 1.0
    c_hs = 1800.0
    rho_hs = 2.0
    attn_hs = 0.2
    attn_units = 'dbpkmhz'
    mesh_dz = (1500 / freq) / 20 # lambda /20 spacing

    cmin = 1500.0
    cmax = 1799.0

    # Pekeris waveguide at each segment
    krs_list, phi_list, zgrid_list, rho_list, rho_hs_list, c_hs_list = [], [], [], [], [], []
    nmesh_list = []
    env_list = []
    # Loop over each segment and run pykrak to get the necessary values
    for seg_i in range(num_segs):
        Z = Zvals[seg_i]
        env_z_list = [np.array([0.0, Z]), np.array([Z, Zmax])]
        env_c_list = [np.array([cw, cw]), np.array([c_hs, c_hs])]
        env_rho_list = [np.array([rho_w, rho_w]), np.array([rho_hs, rho_hs])]
        env_attn_list = [np.array([0.0, 0.0]), np.array([attn_hs, attn_hs])]
        N_list = [max(int(np.ceil(Z / mesh_dz)), 20), max(int(np.ceil(Zmax - Z)), 10)]

        if Z == Zmax:
            env_z_list = [env_z_list[0]]
            env_c_list = [env_c_list[0]]
            env_rho_list = [env_rho_list[0]]
            env_attn_list = [env_attn_list[0]]
            N_list = [N_list[0]]


        nmesh_list.append(N_list)


        env = LinearizedEnv(freq, env_z_list, env_c_list, env_rho_list, env_attn_list, c_hs, rho_hs, attn_hs, attn_units, N_list, cmin, cmax)
        
        env_list.append(env)
        env.add_c_pert_matrix(env.z_arr, np.zeros((env.z_arr.size,1)))
        env.add_x0(np.array([0.0]))


    rdm = CMModel(rgrid, env_list, world_comm)
    x0_list = [np.array([0.0]) for x in env_list]
    rdm.run_models(freq, x0_list)


    # Now we have all the values we need to run the coupled mode model

    zs = np.array([25., 50.0, 100.0])

    same_grid = False
    ranges = np.linspace(100.0, R, 1000)

    zout = np.linspace(0.0, Zvals.max(), nmesh_list[-1][0])
    zr = zout[1:]
    if world_rank == 0:
        p_arr = rdm.compute_field(zs, zr, ranges[1:])
        print('time elapsed', time.time()-now)
    else:
        p_arr = None
    return world_rank, zs, zr, ranges[1:], p_arr

#downslope_test()

#range_dep_model_test()
range_dep_time_test()
rank, zs, zr, ranges, p_arr = range_dep_time_test()


if rank == 0:
    for zs_i in range(zs.size):
        plt.figure()
        plt.pcolormesh(ranges, zr, 20*np.log10(np.abs(p_arr[zs_i, :])))
        plt.colorbar()
        plt.gca().invert_yaxis()
    plt.show()
