import time
from game_of_life.board import *
from game_params.game_params import *

meassage = """This will run Conway's Game of Life for {} timesteps on a {}x{} grid
To modify the parameters use `game_cofig.json`
\nPress any key to continue ...""".format(time_steps, board_height, board_width)

 
if __name__ == "__main__" :
	b = Board()

	print(meassage)

	input()

	for _ in range(time_steps):
		print(b)
		b.step()
		time.sleep(anim_delay)
