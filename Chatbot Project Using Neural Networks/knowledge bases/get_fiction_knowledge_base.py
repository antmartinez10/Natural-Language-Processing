'''
This file is for creating the fiction knowledge bases for fiction books and generes
'''
import pickle

fiction_generes = ['choose your own adventure', 'christmas books', 'gothic fiction', 'inspiring novels',
                       'longest fiction novels', 'mystery novels', 'crime novels', 'poetry', 'science fiction', 'world war 1 novels'
                       , 'zombie novels']

fiction_knowledge_base = {}

# set genre title as key in dictionary
for genre in fiction_generes:
    fiction_knowledge_base[genre] = []


# set choose your own adventure books
file = open("../fiction/choose_your_own_adventure.txt", "r", encoding='utf-8')
choose_your_own_adventure_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(choose_your_own_adventure_titles)):
    choose_your_own_adventure_titles[i] = choose_your_own_adventure_titles[i].split()
    choose_your_own_adventure_titles[i] = ' '.join(choose_your_own_adventure_titles[i])
fiction_knowledge_base['choose your own adventure'] = choose_your_own_adventure_titles
file.close()


# set christmas books
file = open("../fiction/christmas.txt", "r", encoding='utf-8')
christmas_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(christmas_titles)):
    christmas_titles[i] = christmas_titles[i].split()
    christmas_titles[i] = ' '.join(christmas_titles[i])
fiction_knowledge_base['christmas books'] = christmas_titles
file.close()


# set crime novles
file = open("../fiction/crime.txt", "r", encoding='utf-8')
crime_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(crime_titles)):
    crime_titles[i] = crime_titles[i].split()
    crime_titles[i] = ' '.join(crime_titles[i])
fiction_knowledge_base['crime novels'] = crime_titles
file.close()


# set gothic novels
file = open("../fiction/gothic.txt", "r", encoding='utf-8')
gothic_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(gothic_titles)):
    gothic_titles[i] = gothic_titles[i].split()
    gothic_titles[i] = ' '.join(gothic_titles[i])
fiction_knowledge_base['gothic fiction'] = gothic_titles
file.close()


# set insipiring novels
file = open("../fiction/inspiring.txt", "r", encoding='utf-8')
inspiring_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(inspiring_titles)):
    inspiring_titles[i] = inspiring_titles[i].split()
    inspiring_titles[i] = ' '.join(inspiring_titles[i])
fiction_knowledge_base['inspiring novels'] = inspiring_titles
file.close()



# set longest novels
file = open("../fiction/longest_fiction.txt", "r", encoding='utf-8')
longest_fiction_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(longest_fiction_titles)):
    longest_fiction_titles[i] = longest_fiction_titles[i].split()
    longest_fiction_titles[i] = ' '.join(longest_fiction_titles[i])
fiction_knowledge_base['longest fiction novels'] = longest_fiction_titles
file.close()


# set mystery novels
file = open("../fiction/mystery.txt", "r", encoding='utf-8')
mystery_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(mystery_titles)):
    mystery_titles[i] = mystery_titles[i].split()
    mystery_titles[i] = ' '.join(mystery_titles[i])
fiction_knowledge_base['mystery titles'] = mystery_titles
file.close()



# set poetry titles
file = open("../fiction/poetry.txt", "r", encoding='utf-8')
poetry_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(poetry_titles)):
    poetry_titles[i] = poetry_titles[i].split()
    poetry_titles[i] = ' '.join(poetry_titles[i])
fiction_knowledge_base['poetry'] = poetry_titles
file.close()


# set science fiction titles
file = open("../fiction/science_fiction.txt", "r", encoding='utf-8')
sci_fi_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(sci_fi_titles)):
    sci_fi_titles[i] = sci_fi_titles[i].split()
    sci_fi_titles[i] = ' '.join(sci_fi_titles[i])
fiction_knowledge_base['science fiction'] = sci_fi_titles
file.close()


# set world war 1 novels
file = open("../fiction/world_war_one.txt", "r", encoding='utf-8')
ww1_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(ww1_titles)):
    ww1_titles[i] = ww1_titles[i].split()
    ww1_titles[i] = ' '.join(ww1_titles[i])
fiction_knowledge_base['world war 1 novels'] = ww1_titles
file.close()


# set zombie novels
file = open("../fiction/zombies.txt", "r", encoding='utf-8')
zombie_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(zombie_titles)):
    zombie_titles[i] = zombie_titles[i].split()
    zombie_titles[i] = ' '.join(zombie_titles[i])
fiction_knowledge_base['zombie novels'] = zombie_titles
file.close()

# pickle the knowledge base of fiction books
with open('fiction_knowledge_base.pickle', 'wb') as handle:
    pickle.dump(fiction_knowledge_base, handle)

print(fiction_knowledge_base)











