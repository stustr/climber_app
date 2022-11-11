import pdb

from models.ascent import Ascent
import repositories.ascent_repository as ascent_repo

from models.climber import Climber
import repositories.climber_repository as climber_repo

from models.hill import Hill
import repositories.hill_repository as hill_repo

ascent_repo.delete_all()
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

print(climber_repo.select(1).id)

ascent_1 = Ascent("trial ascent", 12.12, "trial ascent desc", climber_1, hill_1)
ascent_repo.save(ascent_1)

for ascent in ascent_repo.select_all():
    print(ascent.__dict__)