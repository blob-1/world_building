from Worlds import World
from random import seed

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, default = "world", help="set the name of the world")
parser.add_argument("--size", type=int, default = 100, help="Set the size of the world (s*s)")
parser.add_argument("--smooth", type=int, default = 10, help="Set the smoothness of the perlin world")
parser.add_argument("--seed", type=int, default = 100, help="Set the seed of the world")
parser.add_argument("--load", type=bool, default = False, help="load a world")

# for testing purposes only
parser.add_argument("--test", type=bool, default = False, help="load a world")

args = parser.parse_args()

seed(args.seed);


def main(name, size, smooth):

	print("world name : "+args.name+"\nseed : "+str(args.seed)+"\nsize : "+str(args.size)+"*"+str(args.size)+"\nsmooth : "+str(args.smooth))

	if args.test:
		#test whatever you want
		map = 0
		w = World(name, None, None, map)
		w.save()
	elif args.load:	
		try:
			w = World(name)
		except FileNotFoundError:
			print("FileNotFoundError: [Errno 2] No such file or directory: 'worlds/"+name+".png'; this world doses not exists")
	else:
		w = World(name, size, smooth)
		w.save()

main(args.name, args.size, args.smooth)





