unit = {
    'Hickey' : {'rank': 'MAJ', 'years_of_service': 16},
    'Stuck' : {'rank': 'LTC', 'years_of_service': 25},
    'Taylor' : {'rank': 'CPT', 'years_of_service': 8},
    'Herndon' : {'rank': 'MSG', 'years_of_service': 18},
    'Johnson' : {'rank': 'CSM', 'years_of_service': 22}
}

def lookup_soldier(dict, name):
    # print(f'{dict.get(name, "Soldier doesn't exist")['rank']}')
    if name in dict:
        record = dict[name]
        print(f'Rank is {record['rank']}, {record['years_of_service']} years of service')
    else:
        print("The Soldier does not exist")

lookup_soldier(unit, "Johnson")