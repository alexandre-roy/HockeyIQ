#pylint: disable = line-too-long

"""Modules"""
import re
import time
import threading
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from bd import sql

def run():
    """Ficher complet"""
    sql("DELETE FROM equipes")
    sql("DELETE FROM joueurs")

    equipes_b2 = extraire_classement(get_url("classement_b2_h2425").json())
    equipes_b3 = extraire_classement(get_url("classement_b3_h2425").json())

    statistiques_b2_result = []
    statistiques_b3_result = []
    calendrier_b2_result = []
    calendrier_b3_result = []

    statistiques_b2_thread = threading.Thread(target=lambda: statistiques_b2_result.append(extraire_joueurs('5852')))
    statistiques_b3_thread = threading.Thread(target=lambda: statistiques_b3_result.append(extraire_joueurs('5194')))
    calendrier_b2_thread = threading.Thread(target=lambda: calendrier_b2_result.append(extraire_calendrier('5852')))
    calendrier_b3_thread = threading.Thread(target=lambda: calendrier_b3_result.append(extraire_calendrier('5194')))

    statistiques_b2_thread.start()
    statistiques_b3_thread.start()
    calendrier_b2_thread.start()
    calendrier_b3_thread.start()

    statistiques_b2_thread.join()
    statistiques_b3_thread.join()
    calendrier_b2_thread.join()
    calendrier_b3_thread.join()

    inserer_classement("B2", "H2425", equipes_b2)
    inserer_classement("B3", "H2425", equipes_b3)
    inserer_joueurs("B2", "H2425", statistiques_b2_result[0])
    inserer_joueurs("B3", "H2425", statistiques_b3_result[0])
    inserer_calendrier("B2", "H2425", calendrier_b2_result[0])
    inserer_calendrier("B3", "H2425", calendrier_b3_result[0])

    i = 0
    while i < 100:
        print("La base de données est maintenant à jour !")
        time.sleep(5)
        i += 1


def extraire_classement(url):
    """Etxtrait le classement à partir d'un url"""
    stats_equipes = []

    for cle, valeur in url.items():
        if cle.isdigit():
            equipe_valeurs = valeur['values']
            nom_equipe = ""

            for item in equipe_valeurs:
                if item["key"] == "override":
                    debut = item["val"].find("<a")
                    debut = item["val"].find(">", debut) + 1
                    fin = item["val"].find("</a>", debut)
                    nom_equipe = item["val"][debut:fin].strip()

            dictionnaire_stats = {}

            for stat in equipe_valeurs:
                if stat["key"] != "override":
                    dictionnaire_stats[stat["key"]] = stat["val"]

            stats_equipes.append({"equipe": nom_equipe, "stats": dictionnaire_stats})

    return stats_equipes

def inserer_classement(categorie, saison,  equipes):
    """Insère le classement équipes dans la base de données"""
    position = 1

    for equipe in equipes:
        equipe_dictionnaire = {
            "nom_equipe" : equipe["equipe"],
            "categorie" : categorie,
            "saison" : saison,
            "position" : position,
            "matchs_joues" : equipe["stats"]["gp"],
            "points" : equipe["stats"]["pts"],
            "victoires_total" : equipe["stats"]["wins_tot"],
            "victoires_temps_regulier" : equipe["stats"]["wins_tot"],
            "victoires_fusillades" : equipe["stats"]["so_wins"],
            "defaites" : equipe["stats"]["losses"],
            "defaites_fusillades" : equipe["stats"]["so_loss"],
            "nulles" : equipe["stats"]["ot"],
            "buts_pour" : equipe["stats"]["gf"],
            "buts_contre" : equipe["stats"]["ga"],
            "differentiel" : equipe["stats"]["diff"],
            "points_periode" : equipe["stats"]["pts_period"],
            "points_partie" : equipe["stats"]["pts_game"],
            "points_penalites" : equipe["stats"]["pts_penalty"],
            "points_par_match" : equipe["stats"]["pts_gp"]
        }

        sql("INSERT INTO equipes (id_equipe, nom_equipe, categorie, saison, position, "
            "matchs_joues, points, victoires_total, victoires_temps_regulier, "
            "victoires_fusillades, defaites, defaites_fusillades, nulles, buts_pour, "
            "buts_contre, differentiel, points_periode, "
            "points_partie, points_penalites, points_par_match) "
            "VALUES(NULL, %(nom_equipe)s, %(categorie)s, %(saison)s, %(position)s, "
            "%(matchs_joues)s, %(points)s, %(victoires_total)s, %(victoires_temps_regulier)s, "
            "%(victoires_fusillades)s, %(defaites)s, %(defaites_fusillades)s, "
            "%(nulles)s, %(buts_pour)s, %(buts_contre)s, %(differentiel)s, %(points_periode)s, "
            "%(points_partie)s, %(points_penalites)s, %(points_par_match)s)"
            , equipe_dictionnaire)

        position += 1

def extraire_joueurs(categorie):
    """Extrait les statistiques du site"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)

    url = 'https://www.ddlc.ca/ligues/statistiques/'
    driver.get(url)

    WebDriverWait(driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(( By.TAG_NAME, 'iframe')))

    button_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='dropdownMenuButtonCategories']")))
    button_categories.click()

    button_my_categorie = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[data-value='{categorie}']")))
    button_my_categorie.click()
    time.sleep(1)

    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-target='players']")))
    button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#nbhpa_table_players > div > table")))

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    player_table = soup.select_one('#nbhpa_table_players > div > table')

    if player_table:
        stats_joueurs = []

        rows = player_table.find_all('tr')

        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]

        for row in rows[1:]:
            cols = row.find_all('td')

            if cols:
                joueur_stats = {}

                for i, col in enumerate(cols):
                    valeur = col.get_text(strip=True)

                    if valeur == "-":
                        valeur = "0"

                    joueur_stats[headers[i]] = valeur

                stats_joueurs.append(joueur_stats)

        for joueur in stats_joueurs:
            joueur['Joueur'] = re.sub(r'^[^A-Z]+|[A-Z]\d+[a-z]*', '', joueur['Joueur'])

    else:
        print("Table des joueurs non trouvée.")

    driver.quit()

    return stats_joueurs

def inserer_joueurs(categorie, saison,  joueurs):
    """Insère les joueurs dans la base de données"""
    position = 1

    for joueur in joueurs:
        joueurs_dictionnaire = {
            "nom" : joueur['Joueur'],
            "categorie" : categorie,
            "saison" : saison,
            "position" : position,
            "equipe" : joueur["Équipe"],
            "matchs_joues" : joueur["MJ"],
            "buts" : joueur["B"],
            "passes" : joueur["A"],
            "points" : joueur["P"],
            "minutes_penalite" : joueur["PUN"],
            "points_par_match" : joueur["P/P"],
            "buts_avantage_numerique" : joueur["BAN"],
            "points_avantage_numerique" : joueur["PAN"],
            "buts_inferiorite_numerique" : joueur["BIN"],
            "points_inferiorite_numerique" : joueur["PIN"],
            "buts_gagnants" : joueur["BG"]
        }
        sql("INSERT INTO joueurs (id_joueur, nom, categorie, saison, position, equipe, matchs_joues, "
            "buts, passes, points, minutes_penalite, points_par_match, buts_avantage_numerique, "
            "points_avantage_numerique, buts_inferiorite_numerique, points_inferiorite_numerique, buts_gagnants) "
            "VALUES (NULL, %(nom)s, %(categorie)s, %(saison)s, %(position)s, %(equipe)s, %(matchs_joues)s, "
            "%(buts)s, %(passes)s, %(points)s, %(minutes_penalite)s, %(points_par_match)s, "
            "%(buts_avantage_numerique)s, %(points_avantage_numerique)s, %(buts_inferiorite_numerique)s, "
            "%(points_inferiorite_numerique)s, %(buts_gagnants)s)",
            joueurs_dictionnaire)

        position += 1

def extraire_calendrier(categorie):
    """Extrait les calendriers du site"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.ddlc.ca/ligues/calendrier/")

    WebDriverWait(driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

    button_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='dropdownMenuButtonCategories']")))
    button_categories.click()
    time.sleep(1)

    button_my_categorie = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[data-value='{categorie}']")))
    button_my_categorie.click()
    time.sleep(1)

    labels = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "label.list_view.btn.btn-dark"))
        )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", labels[0])
    time.sleep(1)

    labels[1].click()

    time.sleep(3)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    calendrier = soup.find('table')

    if calendrier:
        parties = []

        for row in soup.find_all("tr", class_="position-relative schedule_container border"):

            equipes = row.find_all("div", class_="team_name")
            equipe_visiteur = equipes[0].find("a").text.strip()
            equipe_locale = equipes[1].find("a").text.strip()

            date_partie = row.find_all("div", class_="game_date")

            raw_date = date_partie[0].text.strip()
            date = raw_date.split("\n")[-1].strip()

            heure = date_partie[1].text.strip()

            scores = row.find_all("span", class_="score")

            if len(scores) > 0:
                score_visiteur = re.search(r"\d+", scores[0].text).group()
            else:
                score_visiteur = None

            if len(scores) > 1:
                score_local = re.search(r"\d+", scores[1].text).group()
            else:
                score_local = None

            fusillades = None
            if score_visiteur and score_local:
                tds = row.find_all('td', class_='text-nowrap')
                third_td = tds[2]
                fusillades = 'FUS' in third_td.text

            partie_info = {
                "partie": {
                    "equipe_visiteur": equipe_visiteur,
                    "equipe_locale": equipe_locale,
                    "date": date,
                    "heure": heure,
                    "score_visiteur": score_visiteur,
                    "score_local": score_local,
                    "fusillades": fusillades
                }
            }

            parties.append(partie_info)

        return parties

    driver.quit()

def inserer_calendrier(categorie, saison, calendrier):
    """Insère les calendriers dans la base de données"""
    for partie in calendrier:
        partie_info = partie["partie"]

        calendrier_dictionnaire = {
            "categorie": categorie,
            "saison": saison,
            "equipe_visiteur": partie_info['equipe_visiteur'],
            "equipe_locale": partie_info['equipe_locale'],
            "date": partie_info['date'],
            "heure": partie_info['heure'],
            "score_visiteur": partie_info['score_visiteur'],
            "score_local": partie_info['score_local'],
            "fusillades": partie_info['fusillades']
        }
        sql("""
            INSERT INTO parties (categorie, saison, equipe_local, equipe_visiteur, date, heure, score_local, score_visiteur, fusillades)
            VALUES (%(categorie)s, %(saison)s, %(equipe_locale)s, %(equipe_visiteur)s, %(date)s, %(heure)s, %(score_local)s, %(score_visiteur)s, %(fusillades)s)
            ON DUPLICATE KEY UPDATE
                score_local = VALUES(score_local),
                score_visiteur = VALUES(score_visiteur),
                fusillades = VALUES(fusillades),
                date = VALUES(date),
                heure = VALUES(heure)
        """, calendrier_dictionnaire)

def get_url(url):
    """Retourne le contenu d'un fichier basé sur un url"""
    if url == "classement_b2_h2425":
        return requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5852&filters%5B%5D%5Bcategory_id%5D=5852&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1", timeout = 10)

    if url == "classement_b3_h2425":
        return requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5194&filters%5B%5D%5Bcategory_id%5D=5194&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1", timeout = 10)

    return 1

if __name__ == "__main__":
    run()
