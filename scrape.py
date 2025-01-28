import requests
from connection import sql

def extraire_stats(url):
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

classement_b2_h2425_url = requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5852&filters%5B%5D%5Bcategory_id%5D=5852&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1")
equipes_b2 = extraire_stats(classement_b2_h2425_url.json())

sql("TRUNCATE TABLE equipes")

for equipe in equipes_b2:

    equipe_dictionnaire = {
        "nom_equipe" : equipe["equipe"],
        "categorie" : "B2",
        "saison" : "H2425",
        "position" : 1,
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
        + "matchs_joues, points, victoires_total, victoires_temps_regulier, "
        + "victoires_fusillades, defaites, defaites_fusillades, nulles, buts_pour, "
        + "buts_contre, differentiel, points_periode, points_partie, points_penalites, points_par_match) "
        + "VALUES(NULL, %(nom_equipe)s, %(categorie)s, %(saison)s, %(position)s, "
        + "%(matchs_joues)s, %(points)s, %(victoires_total)s, %(victoires_temps_regulier)s, "
        + "%(victoires_fusillades)s, %(defaites)s, %(defaites_fusillades)s, %(nulles)s, %(buts_pour)s, "
        + "%(buts_contre)s, %(differentiel)s, %(points_periode)s, %(points_partie)s, %(points_penalites)s, %(points_par_match)s)"
        , equipe_dictionnaire)

classement_b3_h2425_url = requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5194&filters%5B%5D%5Bcategory_id%5D=5194&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1")
equipes_b3 = extraire_stats(classement_b3_h2425_url.json())








