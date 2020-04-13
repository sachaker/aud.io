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

try:
  os.mkdir('accents') # make accents folder
except:
  pass
