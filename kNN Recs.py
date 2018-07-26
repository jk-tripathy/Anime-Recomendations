from sklearn import neighbors, svm
import numpy as np
from Features_class import user_prefs
import pandas as pd
from ast import literal_eval
import pickle
import csv
from sklearn.linear_model import LinearRegression


genres = ['Action', 'Adventure', 'Cars', 'Comedy', 
		'Demons', 'Drama', 'Ecchi', 'Fantasy',
		'Harem', 'Hentai', 'Historical', 'Horror'
		'Kids', 'Magic', 'Martial Arts', 'Mecha',
		'Music', 'Mystery', 'Parody', 'Police',
		'Romance', 'Samurai', 'School', 'Sci-Fi', 
		'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 
		'Space', 'Sports', 'Super Power', 'Supernatural', 
		'Trilller', 'Vampire', 'Yaoi', 'Yuri']

def run():
	df = pd.read_csv('preferences.csv')
	df.drop(['name'], 1, inplace=True)
	df.drop(['genre'], 1, inplace=True)
	X = np.array(df.drop(['preference'], 1))
	y = np.array(df['preference'])

	#clf = neighbors.KNeighborsClassifier()
	clf = svm.SVC()
	#clf = LinearRegression()
	clf.fit(X, y)

	'''
	with open('DB.file', 'rb') as f:
		animes = pickle.load(f)
		with open('DB.csv', 'w') as myfile:
			wr = csv.writer(myfile)
			for anime in animes:
				wr.writerow([anime.name, anime.rank, anime.genre, anime.score])'''
	
	DB = pd.read_csv('DB.csv')
	DB.drop(['name'], 1, inplace=True)
	DB.drop(['genre'], 1, inplace=True)	
	measures = np.array(DB)
	pred_col = clf.predict(measures)
	print(len(pred_col))
	cout = 1
	with open('DB.file', 'rb') as f:
		animes = pickle.load(f)
		for pred, anime in zip(pred_col, animes):
			if pred == 1:
				print(f'you will like {anime.name.decode("utf-8")}')
				cout += 1
	print(cout)

if __name__ == '__main__':
	run()