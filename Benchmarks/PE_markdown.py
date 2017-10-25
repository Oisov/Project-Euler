import sys, os
import importlib
from PE_Benchmark import get_PE_dir, get_languages, LANGUAGES


def create_markdown(PE, create_all=False):
    path = get_PE_dir(PE)

    markdown_folderpath = path + "/Markdown"
    if not os.path.exists(markdown_folderpath):
        os.makedirs(markdown_folderpath)
        create_all = True

    if create_all:

        create_overview_markdown(PE, path)
        create_answer_markdown(PE, path)

        for language in get_languages(PE):
            create_language_markdown(PE, path, language)
    PE_name = 'PE_{:0>3}'.format(PE)
    first_three_files = [
        '{}/PE_{:0>3}_{}.md'.format(markdown_folderpath, PE, string)
        for string in ['problem', 'answer', 'overview']
    ]

    readme = path + '/README.md'
    if os.path.exists(readme):
        os.remove(readme)

    for filename in first_three_files:
        os.system('cat {} >> {}'.format(filename, readme))

    for files in os.listdir(markdown_folderpath):
        filepath = markdown_folderpath + '/' + files
        if filepath in first_three_files:
            continue
        print(filepath)
        os.system('cat {} >> {}'.format(filepath, readme))


def create_language_markdown(PE, path, language):
    name = 'PE_{:0>3}_'.format(PE) + language + '.md'
    filename = path + '/Markdown/' + name

    file = open(filename, "w")
    file.write("\n\n")
    file.write("### " + language.capitalize())
    file.write("\n\n")

    for filename in os.listdir(path + '/Images/'):
        if not filename.endswith(language + ".png"):
            continue
        file.write('<p align="center">\n')
        file.write("    <img src=Images/{}>\n".format(filename))
        file.write("</p>\n\n")
        file.write("----- ")

    return path


def create_overview_markdown(PE, path):
    filename = path + '/Markdown/PE_{:0>3}_overview.md'.format(PE)
    file = open(filename, "w")
    file.write("\n\n")
    file.write("### Overview")
    file.write("\n\n")

    for filename in os.listdir(path + '/Images/'):
        try:
            int(filename[-6:-4])
        except:
            continue
        file.write('<p align="center">\n')
        file.write("    <img src=Images/{}>\n".format(filename))
        file.write("</p>\n\n")
    file.write("----- ")


def create_answer_markdown(PE, path):
    filename = 'PE_{:0>3}'.format(PE)
    sys.path.insert(0, path + '/Python/')
    module = importlib.import_module(filename)
    function = getattr(module, filename)

    file = open(path + "/Markdown/" + filename + "_answer.md", "w")
    file.write("\n")
    file.write('<p align="center">\n')
    file.write("    {}\n".format(function()))
    file.write("</p>\n\n")
    file.write("----- ")
    file.close()


PE = 2
path = get_PE_dir(PE)
language = 'julia'
# create_answer(PE, path)
# create_overview_markdown(PE, path)
# create_language_markdown(PE, path, language)
create_markdown(PE, True)