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

# Download from accent database
url = 'http://accent.gmu.edu/soundtracks/' # this is the url for the accent database

# Imports
from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests
import os

try:
  os.mkdir('accents') # make accents folder
except:
  pass

"""html_page = urllib2.urlopen(url) # read HTML of database (containing all audio files)
soup = BeautifulSoup(html_page, features="html.parser") # instantiate soup object
for link in soup.findAll('a'): # iterate through each attribute in soup object
    myfile = requests.get(url + '/' + link.get('href')) # get the mp3 file name and get file url
    try:
      open('accents/' + link.get('href'), 'wb').write(myfile.content) # download file into accents
      print("Successfully downloaded " + link.get('href')) # print dl success
    except:
      print("Could not download " + link.get('href')) # print dl failure

# Clean-up data and group into accents
filenames = sorted(os.listdir('accents/.')) # get all file names
accentName = filenames[1][:-5] # get name of first accent (idx==1 to ignore .DS_store)
for file in filenames:
    try:
        if file[0:len(accentName)] != accentName: # if file is not the current accent name, you have reached a new accent file
            count = 1  # initialize at 1
            accentName = file[:-5] # all except 'n.mp3'
            os.mkdir('accents/' + accentName) # create folder for this new accent
            os.rename('accents/' + file, 'accents/' + accentName + '/' + file) # put first in there
        else: # if it's not the first of this accent we've seen...
            os.rename('accents/' + file, 'accents/' + accentName + '/' + accentName + str(count) + '.mp3') # put current file into its accent category
            count += 1 # add to counter (appended to file name within a folder)
    except:
        print('Could not move file ' + file)"""

os.system('python sendSMS.py') # send SMS to indicate the end
print('all done!')