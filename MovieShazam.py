# imports for Google searching, getting URLs, and getting HTMLs
from bs4 import BeautifulSoup as bs
from googlesearch import search
import requests

# imports for NER
import spacy

# imports for GUI
import customtkinter as ctkr

# NER and GUI setup
NER = spacy.load("en_core_web_sm")

ctkr.set_appearance_mode("System")
ctkr.set_default_color_theme("dark-blue")

root = ctkr.CTk()
root.geometry("800 x 500")

# gets the movie name using Google searches and NER
def movieGetter():

    numHtmls = 10  # number of google searches
    query = entry1.get()  # gets the entered quote from the GUI
    print(query)
    urls = search(query + "movie dialogue", lang="co.in", num_results=numHtmls, timeout=2)  # gets an array of URLS from Google search
    
    # declares and initializes arrays to store raw HTMLs of search results, cleaned HTMLs of search results, and possible movie titles
    htmls = [None] * numHtmls
    texts = [None] * numHtmls
    movieTitles = ["Placeholder"]
    # populates the HTML array by getting HTMLs from URL array using BeautifulSoup
    i = 0
    for j in urls:
        htmls[i] = bs(requests.get(j).text, features="html.parser")
        i += 1
    # populates the texts array by cleaning up the HTML to allow for more consistent NER
    l = 0
    movie_keywords = ["movie", "film", "series"]  # Keywords indicating movie titles
    for k in htmls:
        for script in k(["script", "style"]):
            script.extract()

        texts[l] = k.get_text(separator = '\n', strip=True)
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in texts[l].splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        texts[l] = '\n'.join(chunk for chunk in chunks if chunk)

        # NER on texts array
        texts[l] = NER(texts[l])

        # populates movieTitles array with possible movie titles (if NER recognizes a phrase as a Work of Art)
        for word in texts[l].ents:
            if word.label_==("WORK_OF_ART"):
                movieTitles.append(word.text)

        l += 1

    # sorts movieTitles array
    movieTitles.sort()
    mainmovie = movieTitles[1]

    # finds most recurring movie title as identified by NER
    totalCount = 1
    individualCount = 1
    
    for m in range(1, len(movieTitles)):
        if movieTitles[m] == movieTitles[m - 1] and movieTitles[m] != "Valheim":
            individualCount += 1
        
        if individualCount > totalCount:
            totalCount = individualCount
            individualCount = 1
            mainMovie = movieTitles[m]

    return mainMovie

# prints movie result in the GUI
def printer():
    movie = movieGetter()
    print(movie)
    movieName.configure(text=movie)

def switch_event(): 
    if (switch_var.get() == "off"):
        ctkr.set_appearance_mode('light')
    else:
        ctkr.set_appearance_mode('dark')
    

# GUI framework
frame = ctkr.CTkFrame(master=root)
frame.pack(pady=40, padx=120, fill="both", expand=True)


label = ctkr.CTkLabel(master=frame, text="Shazam for Movies", font=("calibri", 40))
label.pack(pady=24, padx=20)

intro = ctkr.CTkLabel(master=frame, text="Please enter a movie dialogue, and we'll guess the possible movies it could be from")
intro.pack(pady=24, padx=20)

entry1 = ctkr.CTkEntry(master=frame, placeholder_text="Enter Your Quote", font=("sans-bold", 12))
entry1.pack(pady=24, padx=20)

movieName = ctkr.CTkLabel(master=frame, text="", font=("calibri", 20))
movieName.pack(pady=24, padx=20)

button = ctkr.CTkButton(master=frame, text="Submit", command=printer, fg_color="#1a0dd1", border_color="black", hover_color="blue", font=("calibri", 25))
button.pack(pady=10, padx=20)
switch_var = ctkr.StringVar(value="on")
switch = ctkr.CTkSwitch(master = root, text="Change light mode", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off", fg_color="blue", 
                                 switch_height=20, switch_width=50)
switch.place(relx=0.5, rely=0.12, anchor = "center")
# runs GUI
root.mainloop()