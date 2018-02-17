#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:44:47 2018

@author: suman
"""

import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
import tensorflow as tf
from tensorflow.python.framework import ops
import sys
#from cnn_utils import *


sys.path.append('/home/suman/Desktop/cnn')

import CnnHelperFns as cnhelp


# Loading the data (signs)
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = cnhelp.load_dataset()

#examining the shape of the data

X_train = X_train_orig/255.
X_test = X_test_orig/255.
Y_train = cnhelp.convert_to_one_hot(Y_train_orig, 6).T
Y_test = cnhelp.convert_to_one_hot(Y_test_orig, 6).T
print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))
conv_layers = {}

trainAccuracy,TestAccuracy, parameters = cnhelp.model(X_train, Y_train, X_test, Y_test)