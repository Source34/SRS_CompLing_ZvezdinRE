from pymongo import MongoClient

class Database:
    client = MongoClient("")
    #client = MongoClient('mongodb://localhost:27017/')
    db = client["parser"]
    collectionNews = db["news"]
    collectionPhrases = db["phrases"]

    # ��������/�������� ������ � �� (�������)
    def addNews(self, data):
        self.collectionNews.find_one_and_update(
            {
            "name": data['name'],
            "date": data['date'],
            "href": data['href']
            },
            {
                "$set": data
            },
            upsert=True
        )

    # �������� ��� ������ �� ��
    def getAllNews(self):
        data = self.collectionNews.find({})
        return list(data)

    # ��������� (�������)
    def getPaginationNews(self, pageNum, pageSize):
        skips = int(pageSize) * (int(pageNum) - 1)
        data = self.collectionNews.find({}).skip(skips).limit(pageSize)
        return list(data)

    # �������� ������ � �� (����� - ����������� � �������)
    def addPhrase(self, data):
        self.collectionPhrases.insert_one({
            "sentence": data['sentence'],
            "facts": data['facts'],  # [{ 'type': '' 'name': '' }, { 'type': '' 'name': '' }],
            }
        )

     # �������� ��� ������ �� �� (����� - ����������� � �������)
    def getAllPhrases(self):
        data = self.collectionPhrases.find({})
        return list(data)

    # ��������� (����� - ����������� � �������)
    def getPaginationPhrases(self, pageNum, pageSize):
        skips = int(pageSize) * (int(pageNum) - 1)
        data = self.collectionPhrases.find({}).skip(skips).limit(pageSize)
        return list(data)
