# CRAWLING_DATA

## Language, Framework and Plugins used :
- ### Python 3.6.9

## Connect Dictionaries MongoDB Atlas Database:
- Connect by shell: 
```sh
mongo "mongodb+srv://cluster-iukdn.mongodb.net/<dbname>" --username firstData
```
- Connect by application: 
```sh
uri = "mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority"
```
```sh
uri = "mongodb+srv://firstData:"+ password +"@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.dics
# collection: dics
```
- Connect by MongoDB Compass: 
```sh
mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/test
```
```sh
<password>  = "firstdata10"
<dbname>    = "nlp"
<collection> = "dics"
```

## Data Form
```sh
{
    "_id":ObjectId("5f33fad64d32a9233cbe6951"),
    "data":"string",                                // tu Tieng Viet
    "freq":int                                      // so lan xuat hien trong crawling data
}