"""Script qui scrape les données et statistuqies de la ligue de hockey"""
import requests
from bd import sql

def run():
    """Ficher complet"""
    sql("DELETE FROM equipes")

    equipes_b2 = extraire_stats(get_url("classement_b2_h2425").json())
    inserer_classement("B2", "H2425", equipes_b2)

    equipes_b3 = extraire_stats(get_url("classement_b3_h2425").json())
    inserer_classement("B3", "H2425", equipes_b3)

def extraire_stats(url):
    """Etxtrait les statistiques à partir d'un url"""
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

def get_url(url):
    """Retourne le contenu d'un fichier basé sur un url"""
    #pylint: disable = line-too-long
    if url == "classement_b2_h2425":
        return requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5852&filters%5B%5D%5Bcategory_id%5D=5852&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1", timeout = 10)
    if url == "classement_b3_h2425":
        return requests.get("https://admin.nbhpa.com/table_data.php?order=pts_tiebreak%20DESC&group=team_id&league_id=29&filters%5B%5D%5Bleague_id%5D=29&filters%5B%5D%5Bseason_id%5D=2858&category_id=5194&filters%5B%5D%5Bcategory_id%5D=5194&public_site=1&class=Standings&fields%5B%5D=override%3A%3Cdiv%20class%3D%27team_name_container%20relative%27%3E%3Cdiv%20class%3D%27center_vertical%20full_width%20d-flex%20align-items-center%27%3E%3Cdiv%20class%3D%27photo_container%20relative%20white_background%27%3E%3Cimg%20data-test%3D%27a%27%20class%3D%27team_photo%27%20src%3D%27https%3A%2F%2Fadmin.nbhpa.com%2F%7Bteam_pic%7D%27%3E%3C%2Fimg%3E%3C%2Fdiv%3E%7Bposition%7D.%20%26nbsp%3B%3Ca%20href%3D%27https%3A%2F%2Fwww.ddlc.ca%2Fequipes%2F%7Bteam_id%7D%27%20target%3D%27_parent%27%20class%3D%27flex-fill%20team_name%27%3E%7Bqualified%7D%7Bteam_name%7D%3C%2Fa%3E%7Blogoinvite%7D%3C%2Fdiv%3E%3C%2Fdiv%3E~~ultra_light_grey_background%20headcol%20py-0%20border-bottom&fields%5B%5D=gp~~text-right&fields%5B%5D=wins_tot~~text-right&fields%5B%5D=wins~~text-right&fields%5B%5D=so_wins~~text-right&fields%5B%5D=losses~~text-right&fields%5B%5D=so_loss~~text-right&fields%5B%5D=ot~~text-right&fields%5B%5D=pts~~text-right&fields%5B%5D=gf~~text-right&fields%5B%5D=ga~~text-right&fields%5B%5D=diff~~text-right&fields%5B%5D=pts_period~~text-right&fields%5B%5D=pts_game~~text-right&fields%5B%5D=pts_penalty~~text-right&fields%5B%5D=pts_gp~~text-right&page=1", timeout = 10)

    return 1

if __name__ == "__main__":
    run()
