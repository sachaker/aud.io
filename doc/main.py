# INSTALLATIONS
# ---------------
# Enable pip install
import subprocess
def install(name):
    subprocess.call(['pip', 'install', name])

# Install dependencies via pip
install('-r requirements.txt')

# DATA COLLECTION
# -----------------

# Imports
import os
import helpers

try:
    os.mkdir('accents') # make accents folder if it doesn't exist
    helpers.getAudioFiles() # download from database
    helpers.cleanupAudioFiles() # organize by accent
    helpers.getSpeakerGender() # create txt file of all genders (ordered)

except:
  print('Audio files already downloaded! Moving on...')


# MODEL TRAINING
# --------------

print('Need to figure out what to do next...')