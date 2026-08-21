
import pandas as pd
from inicio import *

# Entidad de games 
games = df[["appid", "name", "developer","publisher"]].reset_index(drop=True)
games["id_game"] = games.index + 1
games = games[["id_game","appid", "name", "developer","publisher"]]


games.to_csv('games.csv',index=False)


# Entidad de estadisticas de los juegos 
stats_games = df[["positive","negative","price","initialprice","discount","ccu","owners_min","owners_max"]].reset_index(drop=True)
stats_games["id_stats_game"] = stats_games.index + 1
stats_games = stats_games[["id_stats_game","positive","negative","price","initialprice","discount","ccu","owners_min","owners_max"]]


stats_games.to_csv('stats_games.csv',index=False)

#--------------------------- Seguimos normalizando la entidad de games 

name_games = games[["name"]].drop_duplicates(subset=["name"]).reset_index(drop=True)
name_games["id_name"] = name_games.index + 1
name_games = name_games[["id_name","name"]]
name_games.to_csv('nombress.csv',index=False)

developer_games = games[["developer"]].drop_duplicates(subset=["developer"]).reset_index(drop=True)
developer_games["id_developer"] = developer_games.index + 1
developer_games = developer_games[["id_developer","developer"]]
developer_games.to_csv('developoerss.csv',index=False)

publisher_games = games[["publisher"]].drop_duplicates(subset=["publisher"]).reset_index(drop=True)
publisher_games["id_publisher"] = publisher_games.index + 1
publisher_games = publisher_games[["id_publisher","publisher"]]


publisher_games.to_csv('publisherss.csv',index=False)


# ------------------------------ MERGE
print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n")


print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n")
print(games.columns.to_list())



games = games.merge(
    name_games[["id_name", "name"]],
    on="name",
    how="left"
)

games = games.merge(
    developer_games[["id_developer", "developer"]],
    on="developer",
    how="left"
)

games = games.merge(
    publisher_games[["id_publisher", "publisher"]],
    on="publisher",
    how="left"
)

print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n")


print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \n")
print(games.columns.to_list())

