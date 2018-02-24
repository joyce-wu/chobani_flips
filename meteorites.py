'''
Joyce Wu & Queenie Xiang
Softdev2 pd7 
K05 -- Import/Export Bank
2018-02-26
'''

'''
Dataset: Record of Earth Meteorite Landings
Description: Contains information about location, date, name, mass, and unique id of each meteorite
Download hyperlink: https://data.nasa.gov/resource/y77d-th95.json
Import: We opened the url to retrieve data and imported as json. write_json writes the json object into meteorites.json file
'''

from pymongo import MongoClient
import urllib2, json

data = {} 
c = MongoClient('lisa.stuy.edu')
mfDB = c.chobani_flips
collie = mfDB.meteorites

def import_info():
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    resp = urllib2.urlopen(url)
    data = json.loads(resp.read())
    return data

def write_json(data):
    f = open("meteorites.json", "w+")
    f.write(str(data))
    f.close()

#retrieve data and insert into database and imported into json file
#data = import_info()
#write_json(data)
#collie.insert_many(data)

#retrieves all meteorite landings with mass less than n  
def mass(n):

#retrieves all meteorite landings with that recclass
def recclass(recclass):
 
#retrieves all meteorite landings with names that start with 'letter'
#and have a mass less than 'mass' 
def name_mass(letter, mass):

#retrieves meteorite landings with mass between mass1 and mass2
def between_masses(mass1, mass2):

#retrieces meteorite landings with year, month, date, range of days)
def date_range(y, m, d, range): 
