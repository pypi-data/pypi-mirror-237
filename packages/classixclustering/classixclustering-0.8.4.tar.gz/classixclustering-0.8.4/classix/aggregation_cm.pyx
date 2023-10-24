# -*- coding: utf-8 -*-
#
# CLASSIX: Fast and explainable clustering based on sorting
#
# MIT License
#
# Copyright (c) 2022 Stefan Güttel, Xinye Chen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Cython implementation for aggregation


cimport cython
import numpy as np
cimport numpy as np 
from scipy.sparse.linalg import svds
np.import_array()

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.binding(True)

cpdef precompute_aggregate_pca(double[:,:] data, str sorting='pca', double tol=0.5):
    """Aggregate the data with PCA using precomputation

    Parameters
    ----------
    data : numpy.ndarray
        The input that is array-like of shape (n_samples,).
    
    tol : float
        The tolerance to control the aggregation, if the distance between the starting point 
        and the object is less than or equal than the tolerance,
        the object should allocated to the group which starting point belongs to.  
    
    
    Returns
    -------
    labels (numpy.ndarray) : 
        The group category of the data after aggregation.
    
    splist (list) : 
        The list of the starting points.
    
    nr_dist (int) :
        The number of pairwise distance calculations.
    """

    cdef Py_ssize_t len_ind, fdim, last_j
    len_ind, fdim = data.base.shape

    cdef double[:] sort_vals
    cdef double[:, :] U1, _
    cdef long long[:] ind
    cdef unsigned int lab=0, nr_dist=0, num_group
    cdef double[:] clustc 
    

    cdef long[:] labels = np.full(len_ind, -1, dtype=int) 
    cdef list splist = list() 
    cdef Py_ssize_t i, j
    
    cdef double rhs

    if fdim > 1:
        U1, s1, _ = svds(np.asarray(data), k=1, return_singular_vectors=True)
        sort_vals = U1[:,0]*s1[0]
    else:
        sort_vals = data[:,0]
        
    sort_vals = sort_vals*np.sign(-sort_vals[0]) # flip to enforce deterministic output
        
    ind = np.argsort(sort_vals)
    
    data = data.base[ind]
    sort_vals = sort_vals.base[ind] 
    cdef double half_r2 = tol**2 * 0.5
    cdef double[:] half_nrm2 = np.einsum('ij,ij->i', data, data) * 0.5
    
    for i in range(len_ind): 
        if labels[i] >= 0:
            continue
        
        clustc = data[i,:] 
        labels[i] = lab
        num_group = 1
        splist.append((ind[i], sort_vals[i], num_group))
            
        rhs = half_r2 - half_nrm2[i] # right-hand side of norm ineq.
        last_j = np.searchsorted(sort_vals, tol + sort_vals[i], side='right')
        ips = np.matmul(data.base[i+1:last_j,:], clustc)
        nr_dist += last_j - i - 1

        for j in range(i+1, last_j):
                    
            if labels[j] >= 0:
                continue
                
            if half_nrm2[j] - ips[j-i-1] <= rhs:
                num_group += 1
                labels[j] = lab

        lab += 1

    labels = labels.base[np.argsort(ind)]
    return np.asarray(labels), splist, nr_dist, ind




cpdef precompute_aggregate(double[:,:] data, str sorting, double tol=0.5):
    """Aggregate the data using precomputation

    Parameters
    ----------
    data : numpy.ndarray
        The input that is array-like of shape (n_samples,).
    
    sorting : str
        The sorting way refered for aggregation, default='pca', other options: 'norm-mean', 'norm-orthant'.
    
    tol : float
        The tolerance to control the aggregation, if the distance between the starting point 
        and the object is less than or equal than the tolerance,
        the object should allocated to the group which starting point belongs to.  
    
    
    Returns
    -------
    labels (numpy.ndarray) : 
        The group category of the data after aggregation.
    
    splist (list) : 
        The list of the starting points.
    
    nr_dist (int) :
        The number of pairwise distance calculations.
    """

    cdef Py_ssize_t fdim = data.shape[1] # feature dimension
    cdef Py_ssize_t len_ind = data.shape[0] # size of data
    cdef double[:] sort_vals
    cdef double[:, :] U1, _  # = np.empty((len_ind, ), dtype=float)
    cdef long long[:] ind # = np.empty((len_ind, ), dtype=int)
    cdef Py_ssize_t sp # starting point index
    cdef unsigned int lab=0, nr_dist=0, num_group
    cdef double[:] clustc # starting point coordinates
    cdef double dist
    cdef long[:] labels = np.full(len_ind, -1, dtype=int) # np.zeros(, dtype=int) - 1
    cdef list splist = list() # list of starting points
    cdef Py_ssize_t i, ii, j, coord
    
    cdef double half_r2 = tol**2 * 0.5
    cdef double[:] half_nrm2 = np.einsum('ij,ij->i', data, data) * 0.5
    cdef double[:] dataj
    cdef double rhs


    if sorting == "norm-mean" or sorting == "norm-orthant":
        sort_vals = np.linalg.norm(data, ord=2, axis=1)
    
    elif sorting == "pca":
        if fdim > 1:
            U1, s1, _ = svds(np.asarray(data), k=1, return_singular_vectors=True)
            sort_vals = U1[:,0]*s1[0]
        else:
            sort_vals = data[:,0]
            
        sort_vals = sort_vals*np.sign(-sort_vals[0]) # flip to enforce deterministic output
    
    else: # no sorting
        sort_vals = np.zeros(len_ind)
        
    ind = np.argsort(sort_vals)

    for i in range(len_ind): 
        sp = ind[i] # starting point
        
        if labels[sp] >= 0:
            continue
        
        clustc = data[sp,:] 
        labels[sp] = lab
        num_group = 1
            
        rhs = half_r2 - half_nrm2[sp] # right-hand side of norm ineq.

        for ii in range(i+1, len_ind): 
            j = ind[ii]
                    
            if labels[j] >= 0:
                continue
                
            if sort_vals[j] - sort_vals[sp] > tol:
                break       
            
            dist = 0

            dataj = data[j]
            for coord in range(fdim):
                dist += clustc[coord] * dataj[coord]
            
            nr_dist += 1
            
            if half_nrm2[j] - dist <= rhs:
                num_group += 1
                labels[j] = lab

        splist.append((sp, sort_vals[sp], num_group))  
        # list of [ starting point index of current group, sorting key, and number of group elements ]

        lab += 1
  
    return np.asarray(labels), splist, nr_dist, ind



cpdef aggregate(double[:,:] data, str sorting, double tol=0.5):
    """Aggregate the data
    
    Parameters
    ----------
    data : numpy.ndarray
        The input that is array-like of shape (n_samples,).
    
    sorting : str
        The sorting way refered for aggregation, default='pca', other options: 'norm-mean', 'norm-orthant'.
    
    tol : float
        The tolerance to control the aggregation, if the distance between the starting point 
        and the object is less than or equal than the tolerance,
        the object should allocated to the group which starting point belongs to.  
    
    
    Returns
    -------
    labels (numpy.ndarray) : 
        The group category of the data after aggregation.
    
    splist (list) : 
        The list of the starting points.
    
    nr_dist (int) :
        The number of pairwise distance calculations.
    """

    cdef Py_ssize_t fdim = data.shape[1] # feature dimension
    cdef Py_ssize_t len_ind = data.shape[0] # size of data
    cdef double[:] sort_vals
    cdef double[:, :] U1, _  # = np.empty((len_ind, ), dtype=float)
    cdef long long[:] ind # = np.empty((len_ind, ), dtype=int)
    cdef Py_ssize_t sp # starting point index
    cdef unsigned int lab=0, nr_dist=0, num_group
    cdef double[:] clustc # starting point coordinates
    cdef double dist
    cdef long[:] labels = np.full(len_ind, -1, dtype=int) # np.zeros(, dtype=int) - 1
    cdef list splist = list() # list of starting points
    cdef Py_ssize_t i, ii, j, coord
    
    
    if sorting == "norm-mean" or sorting == "norm-orthant":
        sort_vals = np.linalg.norm(data, ord=2, axis=1)
    
    elif sorting == "pca":
        if fdim > 1:
            U1, s1, _ = svds(np.asarray(data), k=1, return_singular_vectors=True)
            sort_vals = U1[:,0]*s1[0]
        else:
            sort_vals = data[:,0]
            
        sort_vals = sort_vals*np.sign(-sort_vals[0]) # flip to enforce deterministic output
    
    else: # no sorting
        sort_vals = np.zeros(len_ind)

    ind = np.argsort(sort_vals)
    for i in range(len_ind): 
        sp = ind[i] # starting point
        
        if labels[sp] >= 0:
            continue
        
        clustc = data[sp,:] 
        labels[sp] = lab
        num_group = 1
            
        for ii in range(i+1, len_ind): 
            j = ind[ii]
                    
            if labels[j] >= 0:
                continue
                
            if sort_vals[j] - sort_vals[sp] > tol:
                break       
            
            dist = 0
            for coord in range(fdim):
                dist += (clustc[coord] - data[j,coord])**2
            
            nr_dist += 1
            
            if dist <= tol**2:
                num_group += 1
                labels[j] = lab

        splist.append((sp, sort_vals[sp], num_group))  
        # list of [ starting point index of current group, sorting key, and number of group elements ]

        lab += 1
  
    return np.asarray(labels), splist, nr_dist, ind

