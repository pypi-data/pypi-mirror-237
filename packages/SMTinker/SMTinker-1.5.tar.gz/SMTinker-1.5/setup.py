import os
import easyvenv as ev

project_dir = os.path.dirname(__file__)
publish = False

if not publish:
    ev.easyvenv(project_dir)