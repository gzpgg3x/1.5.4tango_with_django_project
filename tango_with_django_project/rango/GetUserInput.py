from sys import version_info

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
  response = input("Please enter your name: ")
else:
  response = raw_input("Please enter your name: ")