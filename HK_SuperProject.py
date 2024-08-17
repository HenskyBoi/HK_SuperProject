#--------------------------------------------------------------------------------------------------
# HK_SuperProject.py
#--------------------------------------------------------------------------------------------------
# Author: Henry King
# Version 1.0
# Release Date: 8/16/2024
#--------------------------------------------------------------------------------------------------

print('Select your project')
# This is the list of projects so that the user can find them easily
print('0 = Hello World Script')
print('1 = Unamed Project')
# This is just added to add extra spacing
print()

# This sets the input to the variable "project_ID"
project_ID = input()
# This is just added to add extra spacing
print()

# Hello World Script
if project_ID == '0':
    print('Hello world!')

# Copy and paste the bellow code after the elif script but before the else script to duplicate, and then update the project_ID and the list of projects accordingly.

# Unamed Project
elif project_ID == '1':
    print('This project currently has no code.')

# Copy and paste on the line above me. :)

# This runs if the project_ID isn't valid
else:
    print('That is not a valid project ID. Please restart the super project.')