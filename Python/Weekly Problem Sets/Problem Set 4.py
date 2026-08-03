#Problem 1
reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]

class Soldier():
    def __init__(self, name, rank, fitness, deployed):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def __str__(self):
        return (f'{self.name}: ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})')

    def dispatch(self):
        self.deployed = True

def process_reports(list):
    soldier_dict = {}
    rank_list = []
    for entry in list:
        cat_list = entry.split('|')
        temp_name = cat_list[0].strip().title()
        temp_rank = cat_list[1].strip().upper()
        temp_fit = cat_list[2].strip().split(':')[1]
        temp_dep = cat_list[3].strip().split(':')[1] == 'deployed'
        rank_list.append(temp_rank)
        soldier_dict[temp_name] = Soldier(temp_name, temp_rank, temp_fit, temp_dep)
    return soldier_dict, set(rank_list)

def show_availabe(roster):
    name_list = []
    for key, value in roster.items():
        if value.deployed == False:
            name_list.append(key)
    name_sorted = sorted(name_list)
    for name in name_sorted:
        print(roster[name])

def dispatch(roster, name):
    if name in roster:
        hold = roster[name]
        if hold.deployed:
            print(f"{name} is already deployed")
        else:
            hold.dispatch()
    else:
        print(f"{name} not found in roster")

#Testing
if __name__ == "__main__":
    sold_test = Soldier('pat', 'maj', '80', False)
    print(sold_test)
    sol_dict, rank_set = process_reports(reports)
    print(sol_dict)
    print(rank_set)
    show_availabe(sol_dict)
    dispatch(sol_dict, 'hickey')
    dispatch(sol_dict, 'Kowalski')
    dispatch(sol_dict, 'Santos')
