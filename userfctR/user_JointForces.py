# -*- coding: utf-8 -*-
"""Module for the definition of joint forces."""
# Author: Robotran Team
# (c) Universite catholique de Louvain, 2020


def user_JointForces(mbs_data, tsim):
    """Compute the force and torques in the joint.

    It fills the MBsysPy.MbsData.Qq array.

    Parameters
    ----------
    mbs_data : MBsysPy.MbsData
        The multibody system associated to this computation.
    tsim : float
        The current time of the simulation.

    Notes
    -----
    The numpy.ndarray MBsysPy.MbsData.Qq is 1D array with index starting at 1.
    The first index (array[0]) must not be modified. The first index to be
    filled is array[1].

    Returns
    -------
    None
    """
    # cleaning previous forces value
    mbs_data.Qq[1:] = 0.
    K = 940000  #Nm/rad
    
    id1 = mbs_data.joint_id["R1_caisse1"]
    id2 = mbs_data.joint_id["R1_caisse2"]
    
    mbs_data.Qq[id1] = -K * mbs_data.q[id1]
    mbs_data.Qq[id2] = -K * mbs_data.q[id2]

    return
