from tkinter import *
from anime_class import anime_details
from Features_class import user_prefs
import pickle
import random
import csv

genres = ['Action', 'Adventure', 'Cars', 'Comedy', 
		'Demons', 'Drama', 'Ecchi', 'Fantasy',
		'Harem', 'Hentai', 'Historical', 'Horror'
		'Kids', 'Magic', 'Martial Arts', 'Mecha',
		'Music', 'Mystery', 'Parody', 'Police',
		'Romance', 'Samurai', 'School', 'Sci-Fi', 
		'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 
		'Space', 'Sports', 'Super Power', 'Supernatural', 
		'Thriller', 'Vampire', 'Yaoi', 'Yuri']


def gui(choices):
	root = Tk()
	root.title('Anime Selector')
	root.geometry('500x500')

	myframe = Frame(root, width=500, height=450)
	myframe.pack()

	canvas=Canvas(myframe)
	frame=Frame(canvas)
	myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
	canvas.configure(yscrollcommand=myscrollbar.set)
	
	variables = [IntVar() for i in range(50)]
	for i, anime in zip(range(50), choices):
		Checkbutton(frame, text='', variable=variables[i]).grid(row=i, column=1, sticky=W)
		Label(frame, text=anime.name).grid(row=i, column=2, sticky=W)
	
	frame.pack()
	myscrollbar.pack(side="right",fill="y")
	canvas.pack(side="left")
	canvas.create_window((0,0),window=frame,anchor='nw')

	def myfunction(event):
		canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=450)

	frame.bind("<Configure>",myfunction)
	btn = Button(root, text='Done', command=root.destroy)
	btn.pack()
	root.mainloop()

	user_likes = []
	user_dislikes = []
	flag = 0
	for i, anime in zip(range(50), choices):
		genre_normalised = []
		for genre in genres:
			for g in anime.genre:
				if g == genre:
					flag = 1
			genre_normalised.append(flag)
			flag = 0
		if variables[i].get() == 1:
			print(anime.name)
			feature = user_prefs(anime.name, anime.rank, genre_normalised, anime.score, 1)
			user_likes.append(feature)
		elif variables[i].get() == 0:
			feature = user_prefs(anime.name, anime.rank, genre_normalised, anime.score, 0)
			user_dislikes.append(feature)
	
	with open('preferences.csv', 'w') as myfile:
	    wr = csv.writer(myfile)
	    for like in user_likes:
	    	wr.writerow([like.name, like.rank, like.genre, like.score, like.preference])
	    for like in user_dislikes:
	    	wr.writerow([like.name, like.rank, like.genre, like.score, like.preference])
	
def run():
	choices = []
	with open("DB.file", "rb") as f:
		animes = pickle.load(f)

	var = random.sample(range(100), 20)
	for num in var:
		for anime in animes:
			if num == anime.rank:
				choices.append(anime)

	
	gui(choices)

if __name__ == '__main__':
	run()
