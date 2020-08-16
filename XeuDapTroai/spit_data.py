from pymongo import MongoClient

client = MongoClient("mongodb+srv://17102591:Hao0215817@cluster0.bufis.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.NLP

client2 = MongoClient("mongodb+srv://firstData:firstdata10@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority")
db2 = client2.nlp
def clean_noise(s):
    noise = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "_",
             "=", "+", "-", "*", "/", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?"]
    list_str=[]
    for st in s:
        for c in noise:
            st_new = st.replace(c,"")
            st = st_new
        if(st.isalpha() == True):
            list_str.append(st)
    return list_str

def remove_Eng(s):
    Eng = ["F", "f", "J", "j", "Z", "z", "W", "w"]
    for st in s:
        for c in Eng:
            if(st.find(c) != -1):
                s.remove(st)
                break
    return s
def check_existDB(st):
    oj = db2.dics.find_one({"data": st})
    if (oj is not None):
        fr = int(oj["freq"])
        fr = fr + 1
        db2.dics.update_one({"data": st},{"$set": {"freq": fr}})
        print('ton tai ', fr)
    else:
        fr = 1
        dic = {"data": st, "freq": fr}
        db2.dics.insert_one(dic)
        print('them moi')
        
## main() 
for i in db.DATA.find(no_cursor_timeout=True):
    data = i["data"]
    state = i["state"]
    if(state == "No"):
        s = data.split()
        s_new1 = clean_noise(s)
        s_new2 = remove_Eng(s_new1)

        for st in s_new2:
            check_existDB(st)
        db.DATA.update_one({"data": data},{"$set": {"state": "Yes"}})
    else:
        print("Da xu ly!!")
