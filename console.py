from classes.Player import player, players
from classes.Party import party, parties
from classes.Weapon import weapon, weapons
from functionality_classes.Factory import factory

factory(player, 5)
player.objects_storage["PL_A000"].name = "Macaco"
player.objects_storage["PL_A001"].name = "Saiko"
player.objects_storage["PL_A002"].name = "Gemapls"
player.objects_storage["PL_A003"].name = "Davajones"
player.objects_storage["PL_A004"].name = "caco"

factory(party, 3)
parties["PT_A000"].name = "Articmankeys"
parties["PT_A001"].name = "Gorilazz"
parties["PT_A002"].name = "Tropadoarrancadiu"

factory(weapon, 3)
weapons["WP_A000"].carrier = "Macaco"