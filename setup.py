''' Setup the program.
Start by adding the directory to the system path.
Check the environment conditions.
Install any requirements that need it.
Run a check for all systems:
    network connectivity
    database connection
    access to external storage
    verify python version
Add a verification file to report log.
'''


import os
import sys


# Add this directory to the system PATH
current_dir = os.path.abspath('.')
sys.path.append(current_dir)

# Check the python version
'''
A tuple containing the five components of the version number: major, minor,
micro, releaselevel, and serial. All values except releaselevel are integers;
the release level is 'alpha', 'beta', 'candidate', or 'final'. The components
can also be accessed by name.
'''
version_info = sys.version_info
if version_info[0] < 3:
    print('python version must be greater than 2 \n Just quit now....')
elif version_info[1] < 7:
    print('python version must be 3.7 or greater. \n Just quit now...')


# Check requirements and install any that are not already installed.
#os.system('cd caster; pip install -r requirements.txt')

