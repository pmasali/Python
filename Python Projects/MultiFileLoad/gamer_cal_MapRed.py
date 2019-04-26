from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class calculateScore(MRJob):
	
	def steps(self):
		return [MRStep(mapper = self.recordCreatorMapper,
				reducer = self.recordSumScore)
		]

	def recordCreatorMapper(self, _, line):
		import os
		path = '/Users/prateekmasali/Desktop/Git/Python/Python Projects/MultiFileLoad/data/'
		filelist = os.listdir(path)
		for file in filelist:
			with open(path+file,'r') as f:
				for fline in f:
					(gamerid, score, city, country) = fline.strip().split('\t')
					if gamerid != 'gamerid':
						yield gamerid, int(score)

	def recordHighestReducer(self, key, values):
		yield key, max(values)

	def recordSumScore(self, key, values):
		yield key, sum(values)
	
	def recordCountScore(self, key, values):
		yield key, count(int(values))

if __name__ == '__main__':
	calculateScore.run()
