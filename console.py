import pdb

from models.activity import Activity
import repositories.activity_repository as activity_repo

from models.climber import Climber
import repositories.climber_repository as climber_repo

from models.hill import Hill
import repositories.hill_repository as hill_repo

activity_repo.delete_all()
climber_repo.delete_all()
hill_repo.delete_all()

climber_1 = Climber("Fin")
climber_2 = Climber("Kit")
climber_3 = Climber("Sky")

climber_repo.save(climber_1)
climber_repo.save(climber_2)
climber_repo.save(climber_3)

hill_1 = Hill("Beinn a' Chlaidheimh", 913.96, "Highlands")
hill_2 = Hill("Beinn Bhreac", 912.44, "Perth & Kinross")
hill_3 = Hill("Meall Buidhe", 908.2, "Argyll & Bute")

hill_repo.save(hill_1)
hill_repo.save(hill_2)
hill_repo.save(hill_3)


