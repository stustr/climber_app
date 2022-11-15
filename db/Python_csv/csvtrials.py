import csv
from repositories import hill_repository as hill_repo
from models.hill import Hill

f = open('List_of_Corbett_mountains_1.csv', encoding='UTF8')

csv_reader = csv.DictReader(f)

index = 1
for line in csv_reader:
    hill_repo.save(Hill(line['Name'], line['Height'], line['County']))
    
    
    # print(f"hill_{index} = Hill(\"{}\", {}, \"{}\")")
    # print(f"hill_repo.save(hill_{index})")
    # index += 1
    
