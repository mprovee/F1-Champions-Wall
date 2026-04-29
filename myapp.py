#Lines 3-5 written by me
#The following lines import necessary libraries for the project.
from tkinter import Tk
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

#Lines 9-226 written by me
#The following 'dictionary' lists the app profile for each F1 champion, each of which will be referenced later
champions = {
    "Giuseppe Farina": {
        "years": "1950", "Titles": 1, "Wins": 5, "Poles": 5,
        "teams": "Alfa Romeo",
        "image": "images/farina.jpg",
        "summary": "The winner of the first ever Formula 1 World Championship. Though he was later overshadowed by teammate Juan Manuel Fangio, Farina is considered F1's original pioneer."
    },
    "Juan Manuel Fangio": {
        "years": "1951, 1954-1957", "Titles": 5, "Wins": 24, "Poles": 29,
        "teams": "Alfa Romeo ('51), Maserati ('54, '57), Mercedez-Benz ('54, '55), Ferrari ('56)",
        "image": "images/fangio.jpg",
        "summary": "Known as El Maestro, Fangio was the original superstar of Formula 1. Winning 5 championships with 4 different manufacturers made him widely regarded to be one of the greatest drivers in history, even today."
    },
    "Alberto Ascari": {
        "years": "1952, 1953", "Titles": 2, "Wins": 13, "Poles": 14,
        "teams": "Ferrari",
        "image": "images/ascari.jpg",
        "summary": "Ascari was the first World Champion for the famed constructor Ferrari. He remains the only Italian driver to win the title while driving for Ferrari."
    },
    "Mike Hawthorn": {
        "years": "1958", "Titles": 1, "Wins": 3, "Poles": 4,
        "teams": "Ferrari",
        "image": "images/hawthorn.jpg",
        "summary": "Hawthorn became the first British Formula 1 World Champion, beating Stirling Moss by a single point. He quickly retired after his championship win and tragically died only 3 months later."
    },
    "Jack Brabham": {
        "years": "1959, 1960, 1966", "Titles": 3, "Wins": 14, "Poles": 13,
        "teams": "Cooper ('59, '60), Brabham ('66)",
        "image": "images/brabham.jpg",
        "summary": "Brabham's main contribution to the sport actually came in the garage. He developed the first mid-engine car, a style that remains even today. He later took that car, bearing his own name, to a World Championship."
    },
    "Phil Hill": {
        "years": "1961", "Titles": 1, "Wins": 3, "Poles": 6,
        "teams": "Ferrari",
        "image": "images/phill.jpg",
        "summary": "Phill Hill remains the only American-born driver to win the Formula 1 World Championship. He is also a master of endurance racing, having won 3 times at the 24 Hours of Le Mans."
    },
    "Graham Hill": {
        "years": "1962, 1968", "Titles": 2, "Wins": 14, "Poles": 13,
        "teams": "BRM ('62), Lotus ('68)",
        "image": "images/ghill.jpg",
        "summary": "Graham Hill is the only driver to win the Motorsport Triple Crown, taking victory in Formula 1, the Indianapolis 500, and the 24 Hours of Le Mans. He was known as Mr. Monaco in Formula 1 as he won the presitigious race in the principality 5 times."
    },
    "Jim Clark": {
        "years": "1963, 1965", "Titles": 2, "Wins": 25, "Poles": 33,
        "teams": "Lotus",
        "image": "images/clark.jpg",
        "summary": "A Scottish sheep farmer by trade, Clark possessed mechanical knowledge that allowed him to handily win races without wearing out his tires. He came close to winning the Motorsport Triple Crown, but failed to take victory at Le Mans."
    },
    "John Surtees": {
        "years": "1964", "Titles": 1, "Wins": 6, "Poles": 8,
        "teams": "Ferrari",
        "image": "images/surtees.jpg",
        "summary": "Surtees remains the only person to win World Championships on both two and four wheels, having secured seven motorcycle titles before entering Formula 1. His accomplishment with Ferrari has cemented his legacy as one of the most versatile drivers in history."
    },
    "Denis Hulme": {
        "years": "1967", "Titles": 1, "Wins": 8, "Poles": 1,
        "teams": "Brabham",
        "image": "images/hulme.jpg",
        "summary": "Hulme is the only New Zealander to ever win a Formula 1 World Championship. After securing his title, he became a foundational piece of the McLaren Formula 1 team that would come to dominate the sport for a period."
    },
    "Jackie Stewart": {
        "years": "1969, 1971, 1973", "Titles": 3, "Wins": 27, "Poles": 17,
        "teams": "Matra ('69), Tyrell ('71, '73)",
        "image": "images/stewart.jpg",
        "summary": "A clay pigeon shooter who narrowly missed the Olympics, Stewart translated his marksmanship into a clinically precise driving style. Beyond his three titles, he led the charge in pursuing safer conditions for Formula 1 drivers."
    },
    "Jochen Rindt": {
        "years": "1970", "Titles": 1, "Wins": 6, "Poles": 10,
        "teams": "Lotus",
        "image": "images/rindt.jpg",
        "summary": "Ridnt was a fearless competitor, but tragically died on track. He is the only driver to have the World Championship awarded posthumously, as his early season lead was impossible for other drivers to surmount even after his death."
    },
    "Emerson Fittipaldi": {
        "years": "1972, 1974", "Titles": 2, "Wins": 14, "Poles": 6,
        "teams": "Lotus ('72), McLaren ('74)",
        "image": "images/fittipaldi.jpg",
        "summary": "At the time, Fittipaldi became the youngest World Champion at just 25 years old. He brought McLaren their first driver's title and helped the sport grow in popularity, especially in his home country of Brazil."
    },
    "Niki Lauda": {
        "years": "1975, 1977, 1984", "Titles": 3, "Wins": 25, "Poles": 24,
        "teams": "Ferrari ('75, '77), McLaren ('84)",
        "image": "images/lauda.jpg",
        "summary": "Lauda most famously returned to the cockpit six weeks after nearly being killed in a fiery crash that left his face severely burned. He secured his last championship by only half a point, the smallest margin in F1 history."
    },
    "James Hunt": {
        "years": "1976", "Titles": 1, "Wins": 10, "Poles": 14,
        "teams": "McLaren",
        "image": "images/hunt.jpg",
        "summary": "Hunt, known for his early-career accidents and playboy lifestyle, was a global icon of the sport. He clinched his only title at rain-soaked Fuji, walking away shortly after to become a legendary broadcaster."
    },
    "Mario Andretti": {
        "years": "1978", "Titles": 1, "Wins": 12, "Poles": 18,
        "teams": "Lotus",
        "image": "images/andretti.jpg",
        "summary": "Andretti remains the last driver to win the Formula 1 Championship racing under the American flag. He later became a massive name in motorsports, owning and managing racing teams across categories and around the world."
    },
    "Jody Scheckter": {
        "years": "1979", "Titles": 1, "Wins": 10, "Poles": 3,
        "teams": "Ferrari",
        "image": "images/scheckter.jpg",
        "summary": "Scheckter is the only African driver to win the World Championship. His championship in 1979 began a 21 year drought for Ferrari, later ended by Michael Schumacher."
    },
    "Alan Jones": {
        "years": "1980", "Titles": 1, "Wins": 12, "Poles": 6,
        "teams": "Williams",
        "image": "images/jones.jpg",
        "summary": "Jones' aggressive driving style perfectly embodied the attitude of teamboss Frank Williams. His 1980 championship laid the groundwork that would allow Williams to seriously compete for much of the following two decades."
    },
    "Nelson Piquet": {
        "years": "1981, 1983, 1987", "Titles": 3, "Wins": 23, "Poles": 24,
        "teams": "Brabham ('81, '83), Williams ('87)",
        "image": "images/piquet.jpg",
        "summary": "Piquet was the first driver to win a world title using a turbocharged engine. He was a ruthless tactician who secured three championships across two iconic eras of the sport."
    },
    "Keke Rosberg": {
        "years": "1982", "Titles": 1, "Wins": 5, "Poles": 5,
        "teams": "Williams",
        "image": "images/krosberg.jpg",
        "summary": "Keke Rosberg famously clinched his 1982 title while only winning a single race all season. He eventually became a mentor to his son Nico, who also won a F1 World Championship, making them one of only two father-son duos to win Championships."
    },
    "Alain Prost": {
        "years": "1985-1986, 1989, 1993", "Titles": 4, "Wins": 51, "Poles": 33,
        "teams": "McLaren ('85, '86, '89'), Williams ('93')",
        "image": "images/prost.jpg",
        "summary": "Known as The Professor, Prost approached each race intellectually and strategically managed his race, often doing just enough to win. His career is often characterized by his bitter rivalry with the legendary Aytron Senna, a psychological and physical battle that produced some of the best moments in the history of the sport."
    },
    "Ayrton Senna": {
        "years": "1988, 1990-1991", "Titles": 3, "Wins": 41, "Poles": 65,
        "teams": "McLaren",
        "image": "images/senna.jpg",
        "summary": "Senna became known for his qualifying prowess and mastery of rain-soaked circuits, believing that each lap was a journey of self-discovery. His rivalry with Alain Prost and promising career was cut short as he was tragically killed at the 1994 San Marino Grand Prix, leaving many to wonder what may have happened if he were still alive."
    },
    "Nigel Mansell": {
        "years": "1992", "Titles": 1, "Wins": 31, "Poles": 32,
        "teams": "Williams",
        "image": "images/mansell.jpg",
        "summary": "In 1992, Mansell finally overcame years of heartbreak and near-misses to claim a World Championship for himself. His fearless and borderline aggressive overtaking style earned him the nickname The Lion from his loving Italian fans."
    },
    "Michael Schumacher": {
        "years": "1994-1995, 2000-2004", "Titles": 7, "Wins": 91, "Poles": 68,
        "teams": "Benetton ('94-'95), Ferrari ('00 - '04)",
        "image": "images/schumacher.jpg",
        "summary": "Schumacher brought a revolutionary level of physical fitness, technical mastery, and win-at-any-cost attitude to the sport. His 91 wins, 68 poles, and 7 driver's titles stood as sole records for a time, though his streak of 5 consecutive Championships still remains unequalled."
    },
    "Damon Hill": {
        "years": "1996", "Titles": 1, "Wins": 22, "Poles": 20,
        "teams": "Williams",
        "image": "images/dhill.jpg",
        "summary": "Damon Hill made history as the first son of an F1 World Champion (Graham Hill) to claim the crown for himself. His only title came after spending an entire seasoning battling the legendary Michael Schumacher."
    },
    "Jacques Villeneuve": {
        "years": "1997", "Titles": 1, "Wins": 11, "Poles": 13,
        "teams": "Williams",
        "image": "images/jacques.jpg",
        "summary": "Villeneuve achieved glory in just his second season after a controversial, season-long battle with Michael Schumacher. He remains the only Canadian to win the F1 Drivers Championship."
    },
    "Mika Häkkinen": {
        "years": "1998-1999", "Titles": 2, "Wins": 20, "Poles": 26,
        "teams": "McLaren",
        "image": "images/mika.jpg",
        "summary": "Mika famously spearheaded McLaren's return to the top of the order and ultimately became Michael Schumacher's greatest rival. He survived a near-fatal accident in 1995, subsequently becoming one of the most feared drivers on track, especially in his championship years."
    },
    "Fernando Alonso": {
        "years": "2005-2006", "Titles": 2, "Wins": 32, "Poles": 22,
        "teams": "Renault",
        "image": "images/alonso.jpg",
        "summary": "Fernando Alonso is the legendary Spanish driver who ended the Ferrari era of dominance by securing back-to-back titles. Known for his racecraft and longevity, he remains a competitor even today in the sport at 44 years old."
    },
    "Kimi Räikkönen": {
        "years": "2007", "Titles": 1, "Wins": 21, "Poles": 18,
        "teams": "Ferrari",
        "image": "images/kimi.jpg",
        "summary": "Nicknamed The Iceman for his blunt personality and precise driving style, Kimi snatched the 2007 title by only one point after a three-way season finale. He remains Ferrari's most recent Champion."
    },
    "Lewis Hamilton": {
        "years": "2008, 2014-2015, 2017-2020", "Titles": 7, "Wins": 105, "Poles": 104,
        "teams": "McLaren ('08), Mercedes ('14-'15, '17-'20)",
        "image": "images/hamilton.jpg",
        "summary": "Lewis Hamilton is statistically the most successful driver in history, holding records for all time wins, pole positions, and podium finishes. Beyond his success on track, he has used his global platform to advocate for social justice inside and outside of the motorsport industry."
    },
    "Jenson Button": {
        "years": "2009", "Titles": 1, "Wins": 15, "Poles": 8,
        "teams": "BrawnGP",
        "image": "images/button.jpg",
        "summary": "Button is best remembered for his fairytale 2009 season, where he led the newly formed Brawn GP team to a shock world title after the team was rescued from insolvency for only one dollar. Renowned for his smooth driving style and the team's double diffuser concept, Button held onto an early season lead for the most surprising title in history."
    },
    "Sebastian Vettel": {
        "years": "2010-2013", "Titles": 4, "Wins": 53, "Poles": 57,
        "teams": "Red Bull Racing",
        "image": "images/vettel.jpg",
        "summary": "Vettel was made the youngest champion in history during his four year title streak with Red Bull. After leaving Red Bull due to a disappointing 2014 season, Vettel joined Ferrari, though he failed to deliver a championship, later retiring as one of the most respected statesmen of the sport."
    },
    "Nico Rosberg": {
        "years": "2016", "Titles": 1, "Wins": 23, "Poles": 30,
        "teams": "Mercedes",
        "image": "images/nrosberg.jpg",
        "summary": "Rosberg's 2016 title was overshadowed by what was later deemed The Silver War, in which Mercedes teammates Hamilton and Rosberg, who were childhood friends, battled to the last lap of the season, with Rosberg emerging victorious. Their friendship fractured, Rosberg quickly retired and the two remain separated."
    },
    "Max Verstappen": {
        "years": "2021-2024", "Titles": 4, "Wins": 71, "Poles": 48,
        "teams": "Red Bull Racing",
        "image": "images/verstappen.jpg",
        "summary": "After perhaps the most significant title battle the sport has ever seen in 2021, Verstappen toppled Hamilton's reign and went on to win 4 consecutive championships. His record breaking 2023 season, in which he won 19 of 22 races (a record), and 10 races in a row (also a record), showcased his ruthless consistency on track and his ability to maintain peak performance over time."
    },
    "Lando Norris": {
        "years": "2025", "Titles": 1, "Wins": 17, "Poles": 11,
        "teams": "McLaren",
        "image": "images/norris.jpg",
        "summary": "Norris cemented his place in history in 2025 after clawing back a lost championship lead from teammate Oscar Piastri, securing the victory by two points in the season finale. Known for his personality and humor on and off-track, he led McLaren's resurgence in 2025 after previous disappointing years."
    },
    "?": {
        "years": "2026", "Titles": 0, "Wins": 0, "Poles": 0,
        "teams": "Unknown",
        "image": "images/question.jpg",
        "summary": "As the 2026 season rages on, fans are watching in anticipation. With plenty of challengers on the grid and a new set of regulations, who's to know who will come out on top?"
    }
}

#The following lines are the setup of the app 'window' where the user interacts with the code.
#Lines 230-232 written by me after some research from the following source https://docs.python.org/3/library/tkinter.html#module-tkinter
root = Tk() #Creates the window
root.title("F1 Champions Wall") #Window titles
root.configure(bg="#0a0a0a") #Window background color

#This section details the various fonts used for different elements of the app
#Lines 237-241 were written by me after some research from the following source https://docs.python.org/3/library/tkinter.font.html
title_font = font.Font(family="Georgia", size=9, weight="bold")
header_font = font.Font(family="Georgia", size=18, weight="bold")
small_font = font.Font(family="Georgia", size=10)
banner_font = font.Font(family="Georgia", size=26, weight="bold")
subtitle_font = font.Font(family="Georgia", size=11, slant="italic")

#This section provides the header and subtitle of the app when it is first opened
#The code in lines 245-246 was sourced from a variety of pages on https://www.tutorialkart.com/python/tkinter/how-to-set-background-color-for-label-in-tkinter-python/
tk.Label(root, text="F1 Champions Wall", font=banner_font, bg="#0a0a0a", fg="white").pack(pady=(15, 0)) #Creates label with appropriate font, sets background, foreground, and positions within window
tk.Label(root, text="Click on a champion to learn more about them", font=subtitle_font, bg="#0a0a0a", fg="#aaaaaa").pack(pady=(2, 8)) #Same as previous line but for the subtitle

#This section creates the frame and grid within the app in which each world champion is positioned
#Lines 250-255 sourced from a variety of Tkinter informational pages from https://www.geeksforgeeks.org/python/python-gui-tkinter/
main_frame = tk.Frame(root, bg="#0a0a0a") #creates frame
main_frame.pack(pady=5) #positions frame within app
grid_frame = tk.Frame(main_frame, bg="#0a0a0a") #creates a second frame
grid_frame.pack() #again, positions frame within first frame
COLS = 6 #number of columns in grid
photo_refs = [] #creates a list to hold images referenced from folder

#This section starts the creation of the informational cards
#Lines 259 and 264-267 were written by me while 268-309 sourced from a variety of Tkinter informational pages from https://www.geeksforgeeks.org/python/python-gui-tkinter/
panel = tk.Frame(root, bg="#111111", bd=2, relief="solid", width=350, height=450) #creates frame and sets dimensions or colors for the panels
panel.pack_propagate(False) #turns off automatic resizing

close_button = tk.Button( #creation of panel exit button
    panel,
    text="✕", #panel exit button text
    font=("Arial", 12, "bold"), #panel exit button font
    bg="#111111", #background of exit button
    fg="#666666", #foreground of exit button
    command=lambda: panel.place_forget() #uses lambda to avoid using parentheses? a new fun 'trick' i learned. this function hides the panel upon exit button click
)
close_button.place(x=320, y=5) #positions the exit button

panel_img = tk.Label(panel, bg="#111111") #champions image display
panel_img.pack(pady=10) #positioning and spacing for images

panel_name = tk.Label(panel, font=header_font, bg="#111111", fg="white", wraplength=300) #champions name
panel_name.pack() #adding name to panel

panel_info = tk.Label(panel, font=small_font, bg="#111111", fg="#aaaaaa") #used for stats summary (wins, poles, titles)
panel_info.pack(pady=5) #positioning for info

panel_extra = tk.Label(panel, font=small_font, bg="#111111", fg="#cccccc", wraplength=320) #label for other details (teams and years when championship was won)
panel_extra.pack() #positioning

panel_summary = tk.Label(panel, font=small_font, bg="#111111", fg="#888888", wraplength=320, justify="center") #label for the bio of the champion
panel_summary.pack(pady=15) #positioning

panel_photo_ref = None #holds image reference for each champion

def show_champion(name): #show panels with champions info
    global panel_photo_ref #show images of champions
    #the below lines allow for dynamic changing of champions in the app
    data = champions[name]
    panel_name.config(text=name)
    panel_info.config(text=f"{data['Titles']} Titles | {data['Wins']} Wins | {data['Poles']} Poles")
    panel_extra.config(text=f"Teams: {data['teams']}\nYears: {data['years']}")
    panel_summary.config(text=data["summary"])


    try: #used in case image loading fails
        img = Image.open(data["image"]).resize((150, 150)) #opens and resizes champion image
        panel_photo_ref = ImageTk.PhotoImage(img) #makes image Tkinter compatible
        panel_img.config(image=panel_photo_ref)
    except: #if image fails, use this block instead
        panel_img.config(image="", text="Image failed to load", fg="white") #sets label to display "No Image" if image is missing

    panel.place(relx=0.5, rely=0.5, anchor="center") #centers panel in window

#Building each grid panel/card
#Lines 313-315, 320-322, and 333-344 were written by me while lines 316-319, 324-331, and 345-353 were sourced from various Tkinter Frame pages from https://www.geeksforgeeks.org/python/python-gui-tkinter/
CARD_W = 140 #width of display card
CARD_H = 120   #height of display card
IMG_SIZE = 70  #size of image card
row = 0 #beginner row counter for grid layout
col = 0 #beginner column counter for grid layout

for name, data in champions.items(): #encapsulates all drivers in dictionary of champions
    card = tk.Frame(grid_frame, bg="#1a1a1a", width=CARD_W, height=CARD_H) #creates a frame for each champion card
    card.grid(row=row, column=col, padx=8, pady=5) #places the card within grid
    card.pack_propagate(False) #prevents resizing

    try:
        img = Image.open(data["image"]).resize((IMG_SIZE, IMG_SIZE)) #tries to open champion's image file
        photo = ImageTk.PhotoImage(img) #converts to Tkinter compatible image
    except:
        img = Image.new("RGB", (IMG_SIZE, IMG_SIZE), "#333333") #creates grey placeholder in grid if image fails
        photo = ImageTk.PhotoImage(img)

    photo_refs.append(photo) #retains reference to image

    img_label = tk.Label(card, image=photo, bg="#1a1a1a") #creates a label in the card to display image
    img_label.pack(pady=(4, 0)) #positions image within the card

    name_label = tk.Label( #this whole small section creates a label for the champions name and centers the text
        card,
        text=name,
        font=title_font,
        bg="#1a1a1a",
        fg="white",
        wraplength=CARD_W - 10,
        justify="center"
    )
    name_label.pack(pady=(2, 0)) #positions name within card

    for widget in [card, img_label, name_label]: #binds left click to interacting with panel
        widget.bind("<Button-1>", lambda e, n=name: show_champion(n))

    col += 1 #moves to next column in grid
    if col >= COLS: #if statement to say that if column count exceeds number of columns, reset and move to next row
        col = 0
        row += 1

root.mainloop() #Runs the app, written by me