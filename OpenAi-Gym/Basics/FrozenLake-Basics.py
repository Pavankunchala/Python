#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:46:26 2020

@author: pavankunchala
"""


import gym 
import numpy as np


#creating the environment 
env = gym.make("FrozenLake-v0")
env = env.unwrapped

#action space
nA = env.action_space.n

#observation Space
nS = env.observation_space.n

# zeros 
V = np.zeros(nS)

policy = np.zeros(nS)

policy_stable = False
it = 0

def policy_evaluation(V,policy,eps =0.0001):
    while True:
        delta = 0
        for s  in range(nS):
            old_v = V[s]
            V[s]= eval_state_action(V,s,policy[s])
            delta= max(delta,np.abs(old_v - V[s]))
        if delta < eps:
            break
    

def eval_state_action(V,s,a,gamma = 0.99):
    return np.sum([p*(rew + gamma*V[next_s]) for p , next_s, rew , _ in env.P[s][a]])



def policy_improvement(V,policy):
    policy_stable = True
    for s in range(nS):
        old_a = policy[s]
        policy[s] = np.argmax([eval_state_action(V, s, a)] for a in range(nA))
        if old_a != policy[s]:
            policy_stable = False
            
    return policy_stable

        

while not policy_stable:
    policy_evaluation(V,policy)
    policy_stable = policy_improvement(V,policy)
    
    it +=1
    
    
def run_episodes(env,V, policy,num_games = 100):
    total_rew = 0
    state = env.reset()
    for _ in range(num_games):
        next_state , reward ,done ,_ = env.step(policy[state])
        state = next_state
        total_rew +=reward
        if done:
            state = env.reset()
            
    print("Won %i of %i games! "%(total_rew,num_games))
        
    
print('Converged after %i policy iterations'%(it))
run_episodes(env, V, policy)
print(V.reshape((4,4)))
print(policy.reshape((4,4)))

    
    


    
    

        



    
            
            
            
            
            
            
            
            
            
            
            
            
            
            