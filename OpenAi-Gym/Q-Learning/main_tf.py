#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:22:57 2020

@author: pavankunchala
"""


import gym
from dqn_tf import DeepQNetwork,Agent
import numpy as np
from gym import wrappers


def preprocess(observation):
    return np.mean(observation[30:,:],axis = 2).reshape(180,160,1)


def stack_frames(stacked_frames, frame, buffer_size):
    if stacked_frames is None:
        stacked_frames =np.zeros((buffer_size,*frame.shape))
        for idx, _ in enumerate(stacked_frames):
            stacked_frames[idx,:]= frame
            
    else:
        
        stacked_frames[0:buffer_size-1,:] = stacked_frames[1:,:]
        stacked_frames[buffer_size-1 , :]
        
        
    stacked_frames = stacked_frames.reshape(1,*frame.shape[0:2], buffer_size)
    
    return stacked_frames


if __name__ == '__main__':
    env = gym.make('Breakout-v0')
    load_checkpoint = False
    agent = Agent(gamma = 0.99,epsilon = 1.0,alpha = 0.00025,input_dims = (180,160,4),
                  n_actions = 3,mem_size = 25000,batch_size = 32)
    
        
    
    
    if load_checkpoint:
        agent.load_models()
        
    scores = []
    numGames = 200
    stack_size= 4
    score = 0 
    
    
    while agent.mem_cntr < 25000:
        done = False
        observation = env.reset()
        observation = preprocess(observation)
        stacked_frames = None
        observation= stack_frames(stacked_frames, observation, stack_size)
        
        while not done:
            action = np.random.choice([0,1,2])
            actions = None
            actions +=1
            
            observation_,reward ,done,info = env.step(action)
            observation_= stack_frames(stacked_frames, preprocess(observation_),
                                        stack_size)
            
            action -=1
            agent.store_transistion(observation, action, reward, observation_, int(done))
            
            observation = observation_
            
    
    
    print("Done with random game play gamew  on")
    
    
for i in range(numGames):
    
    done = False
    if i %10 ==0 and i >0:
        
        avg_score = np.mean(scores[max(0, i-10):(i+1)])
        
        print("episode", i ,' score',score,
              'average_score %.3f'%avg_score ,
              'epsilon %.3f'%agent.epsilon)
        
        agent.save_models()
        
    else:
        print('episode', i ,' score', score)
     
    
    
    
    
    observation = env.reset()
    observation = preprocess(observation)
    stacked_frames = None
    observation= stack_frames(stacked_frames, observation, stack_size)

    while not done:
        
         action = agent.choose_action(observation)
           
         actions +=1
            
         observation_,reward ,done,info = env.step(action)
         observation_= stack_frames(stacked_frames, preprocess(observation_),
                                        stack_size)
            
         action -=1
         agent.store_transistion(observation, action, reward, observation_, int(done))
            
         observation = observation_
         agent.learn()
         score += reward

    scores.append(score)
        
    
    

    
    
    
    
    
    
    
    
    
    