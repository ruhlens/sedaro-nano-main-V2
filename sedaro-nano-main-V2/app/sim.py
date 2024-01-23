import doctest
import json
from functools import reduce
from operator import __or__
from random import random
from QRangeStore import QRangeStore
import sys 

"""
Not much has changed in this file! I just made some minor changes to make it a tad easier to read.
"""

#Set the recursion limit high because get and set methods of the IntervalTree are both written recursively.
sys.setrecursionlimit(10000)

# MODELING & SIMULATION
def propagate(agentId, universe):
    """Propagate agentId from `time` to `time + timeStep`."""
    state = universe[agentId]
    time, timeStep, x, y, vx, vy = state['time'], state['timeStep'], state['x'], state['y'], state['vx'], state['vy']
    if agentId == 'Satellite':
        px, py = universe['Planet']['x'], universe['Planet']['y']
        dx = px - x
        dy = py - y
        fx = dx / (dx**2 + dy**2)**(3/2)
        fy = dy / (dx**2 + dy**2)**(3/2)
        vx += fx * timeStep
        vy += fy * timeStep
    x += vx * timeStep
    y += vy * timeStep
    return {'time': time + timeStep, 'timeStep': 0.01+random()*0.09, 'x': x, 'y': y, 'vx': vx, 'vy': vy}


# SIMULATOR
def read(t, qrStore):
    try:
        data = qrStore[t]
    except IndexError:
        data = []
    #return reduce(__or__, data, {})
    result = {}
    for entry in data:
        for key, val in entry.items():
            result[key] = val 
    return result

doctest.testmod()

"""
Main method to run the simulator.
"""
def main():
    init = {
    'Planet': {'time': 0, 'timeStep': 0.01, 'x': 0, 'y': 0.1, 'vx': 0.1, 'vy': 0},
    'Satellite': {'time': 0, 'timeStep': 0.01, 'x': 0, 'y': 1, 'vx': 1, 'vy': 0}
    }
    store = QRangeStore() 
    store[-999999999, 0] = init
    times = {agentId: state['time'] for agentId, state in init.items()}
    for _ in range(500):
        for agentId in init:
            t = times[agentId]
            universe = read(t - 0.001, store)
            if set(universe) == set(init):
                newState = propagate(agentId, universe)
                store[t, newState['time']] = {agentId: newState}
                times[agentId] = newState['time']
    storeList = store.getList()
    print(f"Final Node Count: {store.getNodeCount()}")
    print(store.getNodeCount())
    with open('./public/data.json', 'w') as f:
        f.write(json.dumps(storeList, indent=4)) 

if __name__ == "__main__":
    main()