import os
import pickle

folder = os.path.dirname(__file__)
fileName = 'data.txt'
dataFilePath = os.path.join(folder, fileName)

with open(dataFilePath, 'rb') as dataFile:
	data = pickle.load(dataFile)
