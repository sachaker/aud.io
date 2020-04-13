# INSTALLATIONS
# ---------------
# Enable pip install
import subprocess
def install(name):
    subprocess.call(['pip', 'install', name])

# Install via pip
install('requests')
install('beautifulsoup4')
install('twilio')


# DATA COLLECTION
# -----------------

# Imports
import os
import helpers

try:
    os.mkdir('accents') # make accents folder if it doesn't exist
    helpers.getAudioFiles() # download from database
    helpers.cleanupAudioFiles() # organize by accent

except:
  print('Audio files already downloaded! Moving on...')


# MODEL TRAINING
# --------------
