import os

MAX_X = 49
MAX_Y = 36
FRAME_LENGTH = 0.001
PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 30
