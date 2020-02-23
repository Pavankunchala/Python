#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:13:35 2020

@author: pavankunchala
"""


#developing a RL cycle
import gym

#creating an environment

env = gym.make("CartPole-v1")
# reseting the environment before starting 
env.reset()
#loop for 10

for i in range(0, 10):
    #takiNG A random action
    env.step(env.action_space.sample())
    
    # render the game
    
    env.render()
    
#closing the environment
env.close()