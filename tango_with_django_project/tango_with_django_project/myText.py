import os
print __file__
# print os.path.join(os.path.dirname(__file__), '..')
# print os.path.dirname(os.path.realpath(__file__))
# print os.path.abspath(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print BASE_DIR
SETTINGS_DIR = os.path.dirname(__file__)
print SETTINGS_DIR
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
print PROJECT_PATH
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
print PROJECT_PATH