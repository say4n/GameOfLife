import json

with open('game_config.json') as data_file:    
    params = json.load(data_file)

# board params
board_height = params['board'][0]['height']
board_width  = params['board'][1]['width']

# display params
live_marker = params['markers'][0]['live']
dead_marker = params['markers'][1]['dead']

# game params
alive_cells = params['alive_cells']

# sim params
anim_delay = params['anim_delay']
time_steps = params['time_steps']

"""
Sample alive_cells :
[2,1], // start of glider
[2,2], 
[2,3], 
[1,3], 
[0,2], // end of glider
[7,0], // start of beacon
[7,1], 
[8,0], 
[8,1], 
[9,2], 
[9,3], 
[10,2], 
[10,3], // end of beacon
[13,4], // start of blinker
[13,5], 
[13,6]  // end of beacon
"""

if __name__ == '__main__':
	print(params)