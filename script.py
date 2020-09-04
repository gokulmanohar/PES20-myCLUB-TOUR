# IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import webbrowser
import script_helper

# GETTING THE RELEVANT TOUR DICTIONARY
tour, dict_filename = script_helper.get_working_dict()

# OPENING & READING THE TXT FILE
line_count = 0
index_nos = 0
no_of_goals_lists = []
file_name = input("Enter the Filename: ")
try:
    with open('Files/' + file_name + ".txt", mode="r", encoding="utf-8") as file:
        no_of_goals_lists.clear()
        data = file.readlines()
        for line in data:
            line_count = line_count + 1
            words = line.split()
            no_of_goals_lists.append(int(words[-1]))
except FileNotFoundError:
    print("There is no such file in the directory\n")
    exit()
except IndexError:
    print("Error in the file syntax\n")
    exit()

if len(no_of_goals_lists) != line_count:
    print("An error occured!\n")
    exit()

# CALCULATING THE SUM OF GOALS
sum_of_goals = sum(no_of_goals_lists)
if(line_count == len(no_of_goals_lists)):
    print("\nGoals scored in the Tour Event = ", sum_of_goals)
else:
    print("Inviad format")

# FINDING THE GOLDEN BOOT WINNER
no_of_goals_lists.sort(reverse=True)
max_goal = no_of_goals_lists[0]
try:
    with open('Files/' + file_name + ".txt", mode="r", encoding="utf-8") as file:
        data = file.readlines()
        for line in data:
            words = line.split()
            str_words = str(words[-1])
            if int(str_words) == max_goal:
                line_highest_scorer = line
except FileNotFoundError:
    print("There is no such file in the directory\n")
    exit()
except IndexError:
    print("Error in the file syntax\n")
    exit()
list_highest_scorer = line_highest_scorer.split()
golden_boot_winner = " ".join(list_highest_scorer)
golden_boot_winner = golden_boot_winner[3:golden_boot_winner.rfind(" - ")]
print("GOLDEN BOOT:", golden_boot_winner.upper(), "with", max_goal, "goals", "\n")

# EDITING THE OPERATING FILE WITH NEW KEY AND VALUE
str_new_key = (file_name[0:3] + " " + file_name[3:]).title()
str_new_value = str(sum_of_goals)
year_suffix = script_helper.get_year_suffix()
refactored_string = '\t' + '"' + year_suffix + '-' + str_new_key + '"' + ': ' + str_new_value + ','
operating_filename = dict_filename + ".py"
itte = 0
try:
    with open(operating_filename, mode="r") as inpt:
        with open("operating_file_copy.py", mode="w") as oupt:
            for line in inpt:
                if line.strip("\n") != "}":
                    oupt.write(line)
                    itte += 1
                    if itte == len(tour.values())+1:
                        oupt.write(refactored_string)
                        oupt.write("\n}")
except SyntaxError:
    print("SyntaxError in " + operating_filename)
    exit()
except FileNotFoundError:
    print(operating_filename + " not found")
    exit()

# UPDATING THE KEY & VALUE PAIRS IN MEMORY
key_with_suffix = year_suffix + '-' + str_new_key
tour.update({key_with_suffix: sum_of_goals})

# SHOWING THE GRAPH
key_lists = []
value_lists = []
for key, value in tour.items():
    key_lists.append(key)
    value_lists.append(value)
plt.rcdefaults()
x_pos = np.arange(len(key_lists))
y_pos = value_lists
plt.bar(x_pos, y_pos, align='center', alpha=0.5)
plt.xticks(x_pos, key_lists)
plt_title = script_helper.get_year() + " " + script_helper.checkQuarter()
plt.title(plt_title)
plt.ylabel('Number of goals')
plt.xlabel('Tour event')
for i, v in enumerate(y_pos):
    plt.text(x=i, y=v+1, s=str(v))
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt_graph_filepath = "statistics/" + plt_title + ".jpg"
plt.savefig(plt_graph_filepath, format='JPEG')
plt.show()

# REMOVING & RENAMING tourdictionary
try:
    os.remove(operating_filename)
    os.rename(r'operating_file_copy.py', operating_filename)
except:
    print("\nError in removing or renaming the file")

# REMOVING DUPLICATE DICTIONARY ITEMS
with open(file="tourdictionaryDupeFixed.py", mode="w", encoding="utf8") as tourdictionaryfixdupe:
    tourdictionaryfixdupe.write(dict_filename + " = {\n")
    for key, val in tour.items():
        dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
        tourdictionaryfixdupe.write(dictline)
    tourdictionaryfixdupe.write("}")
os.remove(operating_filename)
os.rename(r'tourdictionaryDupeFixed.py', operating_filename)

# OPENING WEB-BROWSER
time.sleep(0.5)
try:
    url = "https://www.google.com.tr/search?q={}".format(golden_boot_winner)
    webbrowser.open_new_tab(url)
except:
    print("\nError in opening the webbrowser")

# CREATING `tour_complete.py` AS A BACKUP
script_helper.edit_tour_complete()

# FUTURE PLANS
"""
    1. Copy to clipboard
    2. Image resizing with OPENCV
    3. --Github Readme.md updation-- [complete]

"""