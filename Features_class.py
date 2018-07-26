class user_prefs:
	def __init__(self, name, rank, genre, score, preference):
		self.name = name
		self.rank = rank
		self.genre = genre
		self.score = score
		self.preference = preference

	def disp(self):
		print(self.name.decode('utf-8'), self.rank, self.score, self.genre, self.preference)


