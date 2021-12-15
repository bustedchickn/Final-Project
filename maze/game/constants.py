import os

MAX_X = 50
MAX_Y = 35
FRAME_LENGTH = 0.001
PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 30
