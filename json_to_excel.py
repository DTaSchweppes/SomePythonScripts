import json
import pandas as pd
import glob
import os

path = 'D:\\adb\\json'#путь к директории с json файлами

for filename in glob.glob(os.path.join(path, '*.json')): #используем os для открытия всех файлов в директории и glob для шаблона по расширению файла
    print(filename)
    data = json.load(open(filename,encoding='utf-8'))
    df1 = pd.DataFrame(data["ballots_config"])
    #df = pd.json_normalize(data)
    df1.to_excel(filename.replace(".json",".xlsx"))