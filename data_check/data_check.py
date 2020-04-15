#1
import pandas as pd
import json
df = pd.read_csv('foo294file0.txt', sep=";", names=['data_check'])
df.info(memory_usage='deep')
with open(r"foo294file0.txt", "r", encoding="utf8") as f:
    data = json.load(f)
    df = pd.DataFrame(data)
df.columns = ['three', 'four', 'five', 'six']
df1 = df.four[df.four == 0]
print(df1.count)




#2
import pandas as pd
import json
df = pd.read_csv('foo294file0.txt', sep=";", names=['data_check'])
df.info(memory_usage='deep')
with open(r"foo294file0.txt", "r", encoding="utf8") as f:
    data = json.load(f)
    df = pd.DataFrame(data)
df.columns = ['three', 'four', 'five', 'six']
df1 = df.four[df.four != 0]
print(df1.count)




#3
import pandas as pd
import json
df = pd.read_csv('foo294file0.txt', sep=";", names=['data_check'])
df.info(memory_usage='deep')
with open(r"foo294file0.txt", "r", encoding="utf8") as f:
    data = json.load(f)
    df = pd.DataFrame(data)
df.columns = ['three', 'four', 'five', 'six']
df1 = df[(((df.five != 0) & (df.six !=0)) | ((df.five != 0) | (df.six !=0))) & ((df.four == 0) | (df.four != 0))]
print(df1)