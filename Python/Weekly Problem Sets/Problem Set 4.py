import string

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
        temp_fit = int(cat_list[2].strip().split(':')[1])
        temp_dep = cat_list[3].strip().split(':')[1] == 'deployed'
        rank_list.append(temp_rank)
        soldier_dict[temp_name] = Soldier(temp_name, temp_rank, temp_fit, temp_dep)
    return soldier_dict, set(rank_list)

def show_available(roster):
    name_list = []
    for key, value in roster.items():
        if value.deployed == False:
            name_list.append(key)
    name_sorted = sorted(name_list)
    for name in name_sorted:
        print(roster[name])

def dispatch(roster, name):
    if name.title() in roster:
        hold = roster[name.title()]
        if hold.deployed:
            print(f"{name.title()} is already deployed")
        else:
            hold.dispatch()
    else:
        print(f"{name.title()} not found in roster")

def fitness_report(roster):
    low_list = []
    med_list = []
    high_list = []
    for name, sol in roster.items():
        if sol.fitness >= 80:
            high_list.append(sol.name)
        elif sol.fitness >= 60:
            med_list.append(sol.name)
        else:
            low_list.append(sol.name)
    low_list.sort()
    med_list.sort()
    high_list.sort()
    new_dict = {
        'high': high_list,
        'medium': med_list,
        'low': low_list
    }
    return new_dict

#************************************* Prob 2 *********************************************************************
recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]

class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set):
        ing_set = set(self.ingredients)
        return ing_set == pantry_set.intersection(ing_set)

    def missing_ingredients(self, pantry_set):
        miss_list = []
        for item in self.ingredients:
            if item not in pantry_set:
                miss_list.append(item)
        miss_list.sort()
        return miss_list

class Pantry():
    def __init__(self, ingredients):
        self.ingredients = set(ingredients)

    def get_items(self):
        return(set(self.ingredients))

    def add_ingredients(self, extra_ingredients):
        self.ingredients = set(extra_ingredients).union(self.ingredients)

    def has(self, ingredient):
        return ingredient in self.ingredients

def create_recipes(recipe_data):
    rec_list = []
    for key, value in recipe_data.items():
        rec_list.append(Recipe(key, value))
    return rec_list

def check_recipes(recipes, pantry):
    print('=== RECIPE CHECKER ===')
    ing_set = set()
    for item in recipes:
        name = item.name
        status = 'CAN MAKE' if item.can_make(pantry.ingredients) else f'MISSING - {item.missing_ingredients(pantry.ingredients)}'
        print(f'{name}\t: {status}')
        ing_set = ing_set.union(set(item.ingredients))
    ing_list = list(ing_set)
    ing_list.sort()
    print()
    print(f'All unique ingredients ({len(ing_list)}): {ing_list}')

    
#************************************* Prob 3 *********************************************************************
lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""

stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}

class LyricAnalyzer():
    def __init__(self, lyrics):
        self.lyrics = lyrics
        lower_case = lyrics.lower()
        for char in lower_case:
            if char in string.punctuation:
                char = char.replace(char, '')
        self.words = lower_case.replace('\n', ' ').strip().split(' ')

    def filter_stopwords(self, stop_words):
        blank_list = []
        for word in self.words:
            if word not in stop_words:
                blank_list.append(word)
        self.words = blank_list

    def count_words(self):
        hold_dict = {}
        for word in self.words:
            if word in hold_dict:
                hold_dict[word] += 1
            else:
                hold_dict[word] = 1
        return hold_dict
    
    def unique_word_count(self):
        word_set = set(self.words)
        return len(word_set)

    def most_common_word(self):
        word_dict = self.count_words()
        temp_count = 0
        ret_item = tuple()
        for key, value in word_dict.items():
            if value > temp_count:
                temp_count = value
                ret_item = (key, value)
        return ret_item

    def print_report(self):
        print('== WORD COUNT ==')
        alph_list = sorted(list(set(self.words)))
        word_dict = self.count_words()
        for word in alph_list:
            print(f'{word}\t: {word_dict[word]}')
        print(f'Unique words: {self.unique_word_count()}')
        w, f = self.most_common_word()
        print(f'Most common word: "{w}" - {f} times')


    
#Testing
if __name__ == "__main__":
    def prob_1_test():
        sold_test = Soldier('pat', 'maj', '80', False)
        print(sold_test)
        sol_dict, rank_set = process_reports(reports)
        print(sol_dict)
        print(rank_set)
        show_available(sol_dict)
        dispatch(sol_dict, 'hickey')
        dispatch(sol_dict, 'Kowalski')
        dispatch(sol_dict, 'Santos')
        fit_dict = fitness_report(sol_dict)
        print(fit_dict)

    def prob_2_test():
        test_pant = Pantry(pantry_items)
        test_rec = create_recipes(recipe_data)
        check_recipes(test_rec, test_pant)
        user = input("Give me a comma separated list of ingredients")
        hold_list = user.split(',')
        new_list = [item.strip() for item in hold_list]
        test_pant.add_ingredients(new_list)
        check_recipes(test_rec, test_pant)

    def prob_3_test():
        test_lyr = LyricAnalyzer(lyrics)
        print(test_lyr.words)
        print(test_lyr.count_words())
        print(test_lyr.unique_word_count())
        print(test_lyr.most_common_word())
        test_lyr.print_report()
        test_lyr.filter_stopwords(stop_words)
        test_lyr.print_report()

    # prob_1_test()
    # prob_2_test()
    prob_3_test()