import numpy as np
from pprint import pprint 
import json

X = 0.97

POSITIONS = []
for i in range(2):
    for j in range(4):
        POSITIONS.append((i,j))

ACTIONS = ["UP", "LEFT", "DOWN", "RIGHT", "STAY"]
CALL = ["off" , "on"]

TRANSITION_TABLE = {}

for agent_position in POSITIONS:
    for target_position in POSITIONS:
        for c in CALL:
            state = (agent_position , target_position , c)
            TRANSITION_TABLE[state] = {}

for state in TRANSITION_TABLE:
    actions_dict = {"UP": [], "LEFT": [], "DOWN": [], "RIGHT": [], "STAY": []}
    TRANSITION_TABLE[state] = actions_dict

# pprint(TRANSITION_TABLE)

for state in TRANSITION_TABLE.keys():
    agent_pos = state[0]
    target_pos = state[1]
    call = state[2]
    for action in TRANSITION_TABLE[state].keys():
        if action == "UP":
            #SUCCESS
            
            #target_up
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':

                # on to off with 1 probability when target agent same cell
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (0,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                
            #target_left
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            
            #target_down
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            #target_right
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
            
            #target_stay
            if call == 'off':
                # off to off
                prob = X*0.6*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.6*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.6*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.6*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.6
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            #FAILURE

            #target_up
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ((1,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ((1,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            #target_left
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_down
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
    
            #target_right
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_stay
            if call == 'off':
                # off to off
                prob = (1-X)*0.6*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.6*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.6*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.6*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.6
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
        
        if action == "LEFT":
            #SUCCESS
            #target_up
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                else:
                    # on to off
                    prob = X*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_left
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                
                else:

                    # on to off
                    prob = X*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            
            #target_down
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = X*0.1*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_right
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = X*0.1*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_stay
            if call == 'off':
                # off to off
                prob = X*0.6*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.6*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = X*0.6*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.6*0.9
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.6
                    nbr = ((agent_pos[0],max(0 , agent_pos[1]-1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    

            #FAILURE

            #target_up
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_left
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':

                if agent_pos != target_pos:
                
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                     
                    
            
            #target_down
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    

            #target_right
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                     # on to off
                    prob = (1-X)*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                        
            #target_stay
            if call == 'off':
                # off to off
                prob = (1-X)*0.6*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.6*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.6*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.6*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.6
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1]+1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    
    
        if action == "DOWN":
            #SUCCESS
            #target_up
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = X*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else :
                    prob = X*0.1
                    nbr = ( (1,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_left
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = X*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else :
                    prob = X*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                                
            #target_down
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = X*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else :
                    prob = X*0.1
                    nbr = ( (1,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
                    

            #target_right
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = X*0.1*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else :
                    prob = X*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_stay
            if call == 'off':
                # off to off
                prob = X*0.6*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.6*0.5
                nbr = ((1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = X*0.6*0.1
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.6*0.9
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    prob = X*0.6
                    nbr = ( (1,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #FAILURE

            #target_up
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = (1-X)*0.1*0.1
                    nbr = ((0,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    prob = (1-X)*0.1
                    nbr = ((0,agent_pos[1]) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            #target_left
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = (1-X)*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    prob = (1-X)*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            
            #target_down
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = (1-X)*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    prob = (1-X)*0.1
                    nbr = ( (0,agent_pos[1]) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_right
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                # on to off
                if agent_pos != target_pos:
                    prob = (1-X)*0.1*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    prob = (1-X)*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            #target_stay
            if call == 'off':
                # off to off
                prob = (1-X)*0.6*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.6*0.5
                nbr = ((0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = (1-X)*0.6*0.1
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.6*0.9
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
                else:
                    prob = (1-X)*0.6
                    nbr = ( (0,agent_pos[1]) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

        if action == "RIGHT":
            #SUCCESS
            
            #target_up
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)), (0,target_pos[1]) , call)
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    

            #target_left
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_down
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            #target_right
            if call == 'off':
                # off to off
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.1*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = X*0.1*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.1*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = X*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_stay
            if call == 'off':
                # off to off
                prob = X*0.6*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = X*0.6*0.5
                nbr = ((agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                
                    # on to off
                    prob = X*0.6*0.1
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = X*0.6*0.9
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:

                    # on to off
                    prob = X*0.6
                    nbr = ( (agent_pos[0],min(3 , agent_pos[1] + 1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            #FAILURE

            #target_up
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_left
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            
            #target_down
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':

                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            #target_right
            if call == 'off':
                # off to off
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.1*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.1*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.1*0.9
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            #target_stay
            if call == 'off':
                # off to off
                prob = (1-X)*0.6*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = (1-X)*0.6*0.5
                nbr = ((agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:

                    # on to off
                    prob = (1-X)*0.6*0.1
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = (1-X)*0.6*0.9
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = (1-X)*0.6
                    nbr = ( (agent_pos[0],max(0 , agent_pos[1] - 1)) , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


        if action == "STAY":
            #SUCCESS
            #target_up
            if call == 'off':
                # off to off
                prob = 0.1*0.5
                nbr = ( agent_pos , (0,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = 0.1*0.5
                nbr = (agent_pos , (0,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = 0.1*0.1
                    nbr = ( agent_pos , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = 0.1*0.9
                    nbr = ( agent_pos , (0,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = 0.1
                    nbr = ( agent_pos , (0,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    

            #target_left
            if call == 'off':
                # off to off
                prob = 0.1*0.5
                nbr = (agent_pos , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = 0.1*0.5
                nbr = (agent_pos , (target_pos[0],max(0 , target_pos[1] - 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = 0.1*0.1
                    nbr = ( agent_pos , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = 0.1*0.9
                    nbr = ( agent_pos , (target_pos[0],max(0 , target_pos[1] - 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = 0.1
                    nbr = ( agent_pos , (target_pos[0],max(0 , target_pos[1] - 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

            
            #target_down
            if call == 'off':
                # off to off
                prob = 0.1*0.5
                nbr = (agent_pos , (1,target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = 0.1*0.5
                nbr = (agent_pos , (1,target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = 0.1*0.1
                    nbr = ( agent_pos , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = 0.1*0.9
                    nbr = ( agent_pos , (1,target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = 0.1
                    nbr = ( agent_pos , (1,target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            #target_right
            if call == 'off':
                # off to off
                prob = 0.1*0.5
                nbr = (agent_pos , (target_pos[0],min(3 , target_pos[1] + 1)) , call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = 0.1*0.5
                nbr = (agent_pos , (target_pos[0],min(3 , target_pos[1] + 1)), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = 0.1*0.1
                    nbr = ( agent_pos , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = 0.1*0.9
                    nbr = ( agent_pos , (target_pos[0],min(3 , target_pos[1] + 1)), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = 0.1
                    nbr = ( agent_pos , (target_pos[0],min(3 , target_pos[1] + 1)), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                    
            
            #target_stay
            if call == 'off':
                # off to off
                prob = 0.6*0.5
                nbr = (agent_pos , (target_pos[0],target_pos[1]), call) 
                TRANSITION_TABLE[state][action].append((nbr , prob))

                # off to on
                prob = 0.6*0.5
                nbr = (agent_pos , (target_pos[0],target_pos[1]), 'on') 
                TRANSITION_TABLE[state][action].append((nbr , prob))
            
            if call == 'on':
                if agent_pos != target_pos:
                    # on to off
                    prob = 0.6*0.1
                    nbr = ( agent_pos , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))

                    # on to on
                    prob = 0.6*0.9
                    nbr = ( agent_pos , (target_pos[0],target_pos[1]), call) 
                    TRANSITION_TABLE[state][action].append((nbr , prob))
                else:
                    # on to off
                    prob = 0.6
                    nbr = ( agent_pos , (target_pos[0],target_pos[1]), 'off') 
                    TRANSITION_TABLE[state][action].append((nbr , prob))


            

f = open("./transition.txt" , '+w')
# f.write(str(TRANSITION_TABLE))
# f.close()

for state in TRANSITION_TABLE.keys():
    for action in TRANSITION_TABLE[state].keys():
        sum = 0
        for nbr in TRANSITION_TABLE[state][action]:
            sum += nbr[1]
        
        for i in range(len(TRANSITION_TABLE[state][action])):
            TRANSITION_TABLE[state][action][i] = (TRANSITION_TABLE[state][action][i][0], TRANSITION_TABLE[state][action][i][1]/sum )


for state in TRANSITION_TABLE.keys():
    for action in TRANSITION_TABLE[state].keys():
        # dict key - nbr += value as 0
        neighbor = {}
        for nbr in TRANSITION_TABLE[state][action]:
            if(nbr[0] not in neighbor.keys()): neighbor[nbr[0]] = (nbr[1])
            else: neighbor[nbr[0]] += (nbr[1])

        for nbr in neighbor.keys():
            temp = "T: " + str(action) + " : " + str('s') + str(state).replace(' ', '') + " : " + str('s') + str(nbr).replace(' ','') + " " + str((neighbor[nbr]))
            f.write(temp)
            f.write("\n")

f.close()

for state in TRANSITION_TABLE.keys():
    for action in TRANSITION_TABLE[state].keys():
        sum = 0
        for nbr in TRANSITION_TABLE[state][action]:
            sum += nbr[1]
        
        print(sum)
        


            



