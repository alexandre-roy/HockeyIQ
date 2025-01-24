from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect("HockeyIQ.db")
c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS quotes(author TEXT, quote TEXT)")

classements = requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5853&filters%5B%5D%5Bcategory_id%5D=5853&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1")
soup = BeautifulSoup(classements.text, "html.parser")

#quotes = soup.findAll("span", attrs={"class": "text"})
#authors = soup.findAll("small", attrs={"class": "author"})

#for i in range(len(quotes)):
    #c.execute("INSERT INTO quotes VALUES(?,?)", (authors[i].text, quotes[i].text))
    #con.commit()

#table = soup.find("table", class_ = "full_width data_table standings_table")

print(classements.json())
