

from pymongo import MongoClient


client= MongoClient("mongodb+srv://huylu:npf.huy8@cluster0.ua0vg.mongodb.net/<dbname>?retryWrites=true&w=majority")

db_nlp= client.nlp
db_link= client.data
db_content= client.Content







def Clean_Data(txt):
    wordList=[]
    data = txt.split(" ")
    rm = [',', '.', '?', ':', '!', '"', '@', '#', '(', ')', '$', '%', '^', '&', '/','~']
    for i in data:
        for r in rm:
            i = i.replace(r, '')
        if (i.isalpha() == True):
            wordList.append(i)
    return wordList
    
def find_word_Dics(txt):
    for i in txt:
        count = db_nlp.dics.count_documents({"data": i})
        if (count > 0):
            fre =db_nlp.dics.find({"data": i})
            for f in fre:
                t=f["freq"]+1
            db_nlp.dics.update_one({"data": i}, {"$set": {"freq": t}})
        else:
            count += 1
            data = {"data": i, "freq": count}
            db_nlp.dics.insert_one(data)
def Test():
    try:
        cursor= db_content.data.find({'state': False})
        for doc in cursor:
            txt = doc["data"]
            tx= Clean_Data(txt)
            find_word_Dics(tx)
            db_content.data.update_one({"_id": doc['_id']}, {"$set": {"state": True}})
    except:
        print("finish")
Test()