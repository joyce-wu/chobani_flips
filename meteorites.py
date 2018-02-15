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


#data = import_info()
#collie.insert_many(data)

