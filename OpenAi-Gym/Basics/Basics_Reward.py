#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:32:06 2020

@author: pavankunchala
"""


import gym

#creating the environment
env = gym.make("CartPole-v1")

env.reset()

#Play 10 games

for i in range(0, 10):
    #initalizing the variables
    done = False
    game_rew = 0
    
    while not done:
        #choosing a random action
        action = env.action_space.sample()
        # take a step in the environmwenr
        new_obs ,reward, done ,info = env.step(action)
        game_rew += reward
        
        # printing the cumulative reward after done
        
        
        if done:
            print("Episode %d finished , Reward %d "%(i,game_rew))
            env.reset()