import json
import os

def getroad():
    file_path = os.path.dirname(os.getcwd())+"\\dataset\\allways.json"
    file = open(file_path, 'r', encoding='utf-8')
    for line in file.readlines():
        dic = json.loads(line)
        print(dic)

if __name__ == "__main__":
    getroad()