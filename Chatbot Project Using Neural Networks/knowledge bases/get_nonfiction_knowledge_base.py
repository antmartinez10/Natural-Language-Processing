'''
This file is for creating the two knowledge bases for fiction and non-fiction books
'''
import pickle


non_fiction_generes = ['advertising', 'archeology', 'autobiographies', 'black history', 'energy', 'environmental',
                       'jazz/jazz history', 'kites', 'negotiation', 'popular-physics', 'psychedelics', 'self help',
                       'skepticism', 'world war 2', 'books written by CEOs']

non_fiction_knowledge_base = {}

# set genre title as key in dictionary
for genre in non_fiction_generes:
    non_fiction_knowledge_base[genre] = []

# insert book titles into their respective titles
file = open("../non-fiction/advertising.txt", "r", encoding='utf-8')
advertising_titles = file.readlines()
non_fiction_knowledge_base['advertising'] = advertising_titles
file.close()


file = open("../non-fiction/archeology.txt", "r", encoding='utf-8')
archeology_titles = file.readlines()
# stip newlines
for i in range(0,len(archeology_titles)):
    archeology_titles[i] = archeology_titles[i].strip()
non_fiction_knowledge_base['archeology'] = archeology_titles
file.close()

# set authobigoraphy books
file = open("../non-fiction/autobiography.txt", "r", encoding='utf-8')
autobiography_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(autobiography_titles)):
    autobiography_titles[i] = autobiography_titles[i].split()
    autobiography_titles[i] = ' '.join(autobiography_titles[i])
non_fiction_knowledge_base['autobiographies'] = autobiography_titles
file.close()

# set black history books
file = open("../non-fiction/black_history.txt", "r", encoding='utf-8')
black_history_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(black_history_titles)):
    black_history_titles[i] = black_history_titles[i].split()
    black_history_titles[i] = ' '.join(black_history_titles[i])
non_fiction_knowledge_base['black history'] = black_history_titles
file.close()

# set energy books
file = open("../non-fiction/energy.txt", "r", encoding='utf-8')
energy_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(energy_titles)):
    energy_titles[i] = energy_titles[i].split()
    energy_titles[i] = ' '.join(energy_titles[i])
non_fiction_knowledge_base['energy'] = energy_titles
file.close()

# set energy books
file = open("../non-fiction/enviromental.txt", "r", encoding='utf-8')
enviromental_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(enviromental_titles)):
    enviromental_titles[i] = enviromental_titles[i].split()
    enviromental_titles[i] = ' '.join(enviromental_titles[i])
non_fiction_knowledge_base['environmental'] = enviromental_titles
file.close()


# set jazz books
file = open("../non-fiction/jazz.txt", "r", encoding='utf-8')
jazz_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(jazz_titles)):
    jazz_titles[i] = jazz_titles[i].split()
    jazz_titles[i] = ' '.join(jazz_titles[i])
non_fiction_knowledge_base['jazz/jazz history'] = jazz_titles
file.close()


# set kites books
file = open("../non-fiction/kites.txt", "r", encoding='utf-8')
kites_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(jazz_titles)):
    kites_titles[i] = kites_titles[i].split()
    kites_titles[i] = ' '.join(kites_titles[i])
non_fiction_knowledge_base['kites'] = kites_titles
file.close()


# set negotiation books
file = open("../non-fiction/negotiation.txt", "r", encoding='utf-8')
negotiation_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(negotiation_titles)):
    negotiation_titles[i] = negotiation_titles[i].split()
    negotiation_titles[i] = ' '.join(negotiation_titles[i])
non_fiction_knowledge_base['negotiation'] = negotiation_titles
file.close()


# set popular physics books
file = open("../non-fiction/popularphysics.txt", "r", encoding='utf-8')
popularphysics_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(popularphysics_titles)):
    popularphysics_titles[i] = popularphysics_titles[i].split()
    popularphysics_titles[i] = ' '.join(popularphysics_titles[i])
non_fiction_knowledge_base['popular-physics'] = popularphysics_titles
file.close()



# set  psychedlics books
file = open("../non-fiction/psychedelics.txt", "r", encoding='utf-8')
psychedelics_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(psychedelics_titles)):
    psychedelics_titles[i] = psychedelics_titles[i].split()
    psychedelics_titles[i] = ' '.join(psychedelics_titles[i])
non_fiction_knowledge_base['psychedelics'] = psychedelics_titles
file.close()


# set self help books
file = open("../non-fiction/self_help.txt", "r", encoding='utf-8')
self_help_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(self_help_titles)):
    self_help_titles[i] = self_help_titles[i].split()
    self_help_titles[i] = ' '.join(self_help_titles[i])
non_fiction_knowledge_base['self help'] = self_help_titles
file.close()


# set skepticism books
file = open("../non-fiction/skepticism.txt", "r", encoding='utf-8')
skepticism_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(skepticism_titles)):
    skepticism_titles[i] = skepticism_titles[i].split()
    skepticism_titles[i] = ' '.join(skepticism_titles[i])
non_fiction_knowledge_base['skepticism'] = skepticism_titles
file.close()


# set world war 2 books
file = open("../non-fiction/world_war_2.txt", "r", encoding='utf-8')
ww2_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(ww2_titles)):
    ww2_titles[i] = ww2_titles[i].split()
    ww2_titles[i] = ' '.join(ww2_titles[i])
non_fiction_knowledge_base['world war 2'] = ww2_titles
file.close()


# set written by ceo books
file = open("../non-fiction/written_by_ceos.txt", "r", encoding='utf-8')
written_by_ceos_titles = file.readlines()
# stip newlines and tabs
for i in range(0,len(written_by_ceos_titles)):
    written_by_ceos_titles[i] = written_by_ceos_titles[i].split()
    written_by_ceos_titles[i] = ' '.join(written_by_ceos_titles[i])
non_fiction_knowledge_base['books written by CEOs'] = written_by_ceos_titles
file.close()


# pickle the knowledge base of non-fiction books
with open('non_fiction_knowledge_base.pickle', 'wb') as handle:
    pickle.dump(non_fiction_knowledge_base, handle)







