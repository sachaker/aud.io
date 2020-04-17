def getSpeakerGender():

    import requests
    import os
    import re
    import pickle

    try:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
    except:
        pass

    path = '/Users/Guest/PycharmProjects/aud.io/data/audio/wav/accents'
    accents = os.listdir(path) # get list of all accent names


    for accent in accents:
        try:
            count = 1 # initialize
            genders = []

            url = 'https://accent.gmu.edu/browse_language.php?function=find&language='+accent  # this is the url for info for speakers
            response = requests.get(url)
            html = response.content.decode("utf-8") # html content as string
            I = [m.start() for m in re.finditer(accent, html)] # indices of all occurences of accent on page of speaker info

            for idx in I:
                genders.append(html[idx+len(accent)+len(str(count))+6]) # first letter of listed gender (yes it's ugly, just trust)
                count += 1

            with open(path + '/' + accent + '/genders', "w") as outfile:
                outfile.write("\n".join(genders)) # dump genders into text file
            print('Successfully added info for ' + accent + ' speakers!')
            print(genders)
        except:
            print('Error retrieving speaker info for: ' + accent)
            continue
    return None


# Downloads accent audio files from database
def getAudioFiles():
    from bs4 import BeautifulSoup
    import urllib.request as urllib2
    import requests

    url = 'http://accent.gmu.edu/soundtracks/'  # this is the url for the accent database

    html_page = urllib2.urlopen(url)  # read HTML of database (containing all audio files)
    soup = BeautifulSoup(html_page, features="html.parser")  # instantiate soup object
    for link in soup.findAll('a'):  # iterate through each attribute in soup object
        myfile = requests.get(url + '/' + link.get('href'))  # get the mp3 file name and get file url
        try:
            open('accents/' + link.get('href'), 'wb').write(myfile.content)  # download file into accents
            print("Successfully downloaded " + link.get('href'))  # print dl success
        except:
            print("Could not download " + link.get('href'))  # print dl failure


# Clean-up data and group into accents
def cleanupAudioFiles():
    import os

    filenames = sorted(os.listdir('accents/.'))  # get all file names
    accentName = filenames[1][:-5]  # get name of first accent (idx==1 to ignore .DS_store)
    for file in filenames:
        try:
            if file[0:len(accentName)] != accentName:  # if file is not the current accent name, you have reached a new accent file
                count = 1  # initialize at 1
                accentName = file[:-5]  # all except 'n.mp3'
                os.mkdir('accents/' + accentName)  # create folder for this new accent
                os.rename('accents/' + file, 'accents/' + accentName + '/' + file)  # put first in there
            else:  # if it's not the first of this accent we've seen...
                os.rename('accents/' + file, 'accents/' + accentName + '/' + accentName + str(count) + '.mp3')  # put current file into its accent category
                count += 1  # add to counter (appended to file name within a folder)
        except:
            print('Could not move file ' + file)

    sendSMS('Your code has finished running!')  # send SMS to indicate completion

def sendSMS(msg):
    from twilio.rest import Client
    import config

    client = Client(config.accountSID_twilio, config.authToken_twilio)

    client.messages.create(from_=config.sendNum,
                           to=config.myNum,
                           body=msg)