from bs4 import BeautifulSoup
import requests
import re
from tkinter import *
import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Web Scraper For Top Movies, Series")
window.geometry("900x330")
bg = PhotoImage(file= "C:/Users/sinch/python/IMDB/myreel.png")
my_label= Label(window, image=bg)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

label2=Label(window,text="Webscrapper to search Top Movies and TV series",fg = "blue",bg = "yellow",font = "Verdana 10 bold").pack()

def topengmovie():
    url = 'http://www.imdb.com/chart/top-english-movies'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

    imdb = []

    for index in range(0, 100):    
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index+1))-(len(movie))]
        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                }
        imdb.append(data)
    count = 1
    for item in imdb:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(item['place'],item['movie_title'],item['year'],item['star_cast']))
        count+=1
     
def toptv():
    url = 'http://www.imdb.com/chart/toptv'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    tvs = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    
    imdb = []
   
    for index in range(0, 100):
        tv_string = tvs[index].get_text()
        tv = (' '.join(tv_string.split()).replace('.', ''))
        tv_title = tv[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', tv_string).group(1)
        place = tv[:len(str(index+1))-(len(tv))]
        data = {"tv_title": tv_title,
                "year": year,
                "place": place,
                "star_cast": crew[index]
                }
        imdb.append(data)
    count = 1
    for item in imdb:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(item['place'],item['tv_title'],item['year'],item['star_cast']))
        count+=1
    
def  topmovie():
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')    
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    
    imdb = []

    for index in range(0, 100):
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index+1))-(len(movie))]
        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index]
               }
        imdb.append(data)

    count = 1
    for item in imdb:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(item['place'],item['movie_title'],item['year'],item['star_cast']))
        count+=1

def popmovie():
    url = 'http://www.imdb.com/chart/moviemeter'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

    imdb = []

    for index in range(0, 100):
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()))        
        movie_title = movie[0:-14].strip(' (20').replace('(', '').replace(')', '')
        year = re.search('\((.*?)\)', movie_string).group(1)   
        data = {"movie_title": movie_title,
                "year": year,                                
                "star_cast": crew[index]
                }
        imdb.append(data)
    i =1    
    count = 1
    for item in imdb:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(i,item['movie_title'],item['year'],item['star_cast']))
        count+=1
        i=i+1

def poptv():
    url = 'http://www.imdb.com/chart/tvmeter'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    tvs = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    imdb = []

    for index in range(0, 100):        
        tv_string = tvs[index].get_text()
        tv = (' '.join(tv_string.split()))
        tv_title = tv[0:-14].strip(' (20').replace('(', '').replace(')', '')
        year = re.search('\((.*?)\)', tv_string).group(1)    
        data = {"tv_title": tv_title,
                "year": year,                                
                "star_cast": crew[index]
                }
        imdb.append(data)

    i =1
    count = 1
    for item in imdb:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(i,item['tv_title'],item['year'],item['star_cast']))
        count+=1
        i=i+1

def cleartree():
    my_tree.delete(*my_tree.get_children())

def comboclick(event):    
    if myCombo.get() == 'Top English Movies':
        topengmovie()
    elif myCombo.get() == 'Top TV Series':
        toptv()
    elif myCombo.get() == 'Top Movies':
        topmovie()
    elif myCombo.get() == 'Popular Movies' :
        popmovie()
    elif myCombo.get() == 'Popular TV Series' :
        poptv()  
    
options=["Top English Movies","Top TV Series","Top Movies","Popular Movies","Popular TV Series"]
clicked=StringVar()
clicked.set(options[0])

myCombo=ttk.Combobox(window,value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>",comboclick)
myCombo.pack()

clear=Button(text="Clear",width=4,height=1,bg='Yellow',command=cleartree).pack()

my_tree = ttk.Treeview(window)
my_tree['columns'] = ("No","Movies","Year","Starring")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("No",anchor=CENTER,width=5)
my_tree.column("Movies",anchor=CENTER,width=200)
my_tree.column("Year",anchor=CENTER,width=10)
my_tree.column("Starring",anchor=CENTER,width=200)
my_tree.heading("No",text="Sl no",anchor=CENTER)
my_tree.heading("Movies",text="Movies/Show",anchor=CENTER)
my_tree.heading("Year",text="Year",anchor=CENTER)
my_tree.heading("Starring",text="Starring",anchor=CENTER)
my_tree.pack(pady=20,fill=tk.X)

window.mainloop()
