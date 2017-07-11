#!/usr/bin/python
from sys import stdout # for print control
import random

class Dungeon:
    n_rooms = 0 # total number of rooms (not including passageways)
    DEFAULT_SIZE = 51
    '''Contains list of rooms and their coordinates. Handles printing. 
    Can generate additional rooms.'''
    def __init__(self):
        self.rooms = [] # logical structures
        self.grid = [['#' for x in range(Dungeon.DEFAULT_SIZE)] for y in range(Dungeon.DEFAULT_SIZE)] # map itself
    def __str__(self):
        return '\n'.join([''.join(self.grid[y]) for y in range(len(self.grid))])
    def render(self): # After running generation algorithm, call this to update self.grid
        all_floor_tiles = [(local_coord[0]+room.origin[0], local_coord[1]+room.origin[1]) for room in self.rooms for local_coord in room.floor]
        print all_floor_tiles
    def generate(self): # run DMG algorithm
        self.rooms.append(Room_1((0,0)))

class Room_1(): # 20x20 ft; passage on each wall
    '''Knows its room number (may be zero), 
    exits (connections to passage rooms, which don't get numbers),
    and a set of its floor tiles.
    Floor tiles do NOT include walls but DO include one (1) exit tile.
    Exit tiles know where they go?'''
    def __init__(self, origin):
        self.origin = origin
        self.floor = set((x,y) for x in range(4) for y in range(4))
        self.exits = set((-1,1),(4,1),(1,4),(4,-1)) # this is probably wrong
        Dungeon.n_rooms += 1

if __name__=='__main__':
    my_dungeon = Dungeon()
    print my_dungeon
