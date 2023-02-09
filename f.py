from Factory import factory
from Player import player
import Database as ds

factory(player, 120)
print(ds.classes_generators["PL"])

#como pegar o valor de um gerador q esta referenciado dentro de um dict.