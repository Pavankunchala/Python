#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:02:55 2020

@author: pavankunchala
"""


import tensorflow as tf

#importingb gym
import gym

import numpy as np


#let's set up our networks
num_inputs = 4

num_hidden = 4

num_of_outputs = 1 #The Probablilty to go left

#the probably to go right is 1-Left = Right

initaliazer = tf.keras.layers.variance_scaling_initalizer()

#create a place holder
X = tf.compat.v1.placeholder(tf.float32,shape =[None,num_inputs])

#hidden layer
hidden_layer_one = tf.keras.layers.dense(X,num_hidden)
