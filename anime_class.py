class anime_details:
	def __init__(self, name, score, synopsis, genre, user_recs, rank):
		self.name = name
		self.score = score
		self.synopsis = synopsis
		self.genre = genre
		self.user_recs = user_recs
		self.rank = rank
		
	def disp_data(self):
		print( "- -"*50)
		print (self.name.decode('utf-8'), self.rank, self.score, 
			self.synopsis, self.genre, self.user_recs)
