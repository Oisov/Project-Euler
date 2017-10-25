import os, sys
from shutil import copy2

PE_problem_folder = os.path.dirname(os.getcwd()) + '/Problems/'
for folder in os.listdir(PE_problem_folder):

    problem_path = PE_problem_folder + folder
    if not os.path.isdir(problem_path):
        continue

    readme = problem_path + '/README.md'
    if not os.path.isfile(readme):
        continue

    markdown_path = problem_path + '/Markdown'
    if os.path.isdir(markdown_path):
        continue
    else:
        os.makedirs(markdown_path)

    print("Copying readme in folder ", folder)

    new_readme = markdown_path+'/' + folder + '_problem.md'
    copy2(readme, new_readme)
