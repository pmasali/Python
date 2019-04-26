from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingBreakdown(MRJob):

	def steps(self):
		return [MRStep(mapper = self.ratingNumMapper,
				reducer = self.ratingCountReducer)
		]


	def ratingNumMapper(self, _, line):
		(id, movieid, rating, RatingTime) = line.split('\t')
		yield movieid, 1

	def ratingCountReducer(self, key, values):
		yield str(sum(values)).zfill(5), key

	def ratingSortReducer(self, count, movies):
		for movie in movies:
			yield movie, count

if __name__ == '__main__':
	RatingBreakdown.run()
