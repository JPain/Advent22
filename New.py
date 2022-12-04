#!/usr/bin/env python3
import os
import os.path
import shutil

'''
    New.py creates new files for Advent of Code for each run.
    Define a template in the User Configuarion, using XX for day numbers.
'''

# START User configuration
pyTemplateName = 'Day-XX.py'
txtTemplateName = 'Day-XX-input.txt'
debug = False
# END User configuration

# Start script run
def makeNewDay():

    # Require file in pyTemplateName exists
    if not os.path.exists(pyTemplateName):
        print('Cannot find {0}. Exiting'.format(pyTemplateName))
        return

    # Require file in txtTemplateName exists
    if not os.path.exists (txtTemplateName):
        print('Cannot find {0}. Exiting'.format(txtTemplateName))
        return

    logDebug('Found template files')

    # Advent of Code runs for 25 days.
    # From 01 to 25, check if files exist for each day.
    for x in range(25):
        day = x + 1
        dayPyFile = pyTemplateName.replace('XX', '{:02}'.format(day))
        dayTxtFile = txtTemplateName.replace('XX', '{:02}'.format(day))
        logDebug('Looking for {0}'.format(dayPyFile))

        # If py file doesn't exist, create it from template
        if not os.path.exists(dayPyFile):
            print('Creating {0}'.format(dayPyFile))
            shutil.copyfile(pyTemplateName, dayPyFile)
            logDebug('Looking for {0}'.format(dayTxtFile))

            # If txt file doesn't exist, create it from template
            if not os.path.exists(dayTxtFile):
                print('Creating {0}'.format(dayTxtFile))
                shutil.copyfile(txtTemplateName, dayTxtFile)
            else:
                print('Skipping {0}.'.format(dayTxtFile))
            break
        else:
            logDebug('Found. Continuing')

# Output message if debug is True
def logDebug(logMessage):
    if debug == True:
        print(logMessage)

if __name__ == "__main__":
    makeNewDay()
