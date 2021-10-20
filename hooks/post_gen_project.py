import os
import shutil
from subprocess import Popen

print(os.getcwd()) 

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", ":cookie: Initial Commit :rocket:"],
        ["git", "branch", "-m", "master", "main"]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()



# Remove unused files
create_pytest = '{{cookiecutter.use_pytest}}' == 'y'
create_pylint = '{{cookiecutter.use_pylint}}' == 'y'
create_github_actions = '{{cookiecutter.use_github_actions}}' == 'y'

if not create_pytest:
    remove('{{cookiecutter.project_slug}}/test_main.py')

if not create_pylint:
    remove('{{cookiecutter.project_slug}}/.pylintrc')

if not create_github_actions:
    remove('.github')

# Initialize Git (should be run after all file have been modified or deleted)
if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove(".gitignore")
    remove('.github')
