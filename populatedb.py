import pymongo
from xml.etree import ElementTree
client = pymongo.MongoClient("mongodb://localhost:27017/") 

mydb = client["DBLP"]
col = mydb['DATA']

tree = ElementTree.iterparse("dblp.xml",events=('start','end'))

for event,elem in tree:
    dic = {}
    if event == 'end':
        for item in elem:
            dic["Category"] = elem.tag
            dic[item.tag] = item.text
        
        if len(dic) != 0:
            col.insert_one(dic)

    del dic