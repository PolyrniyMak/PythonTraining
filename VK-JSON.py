# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df)



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.loc[:, 'city'])



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.head(5).drop('mobile_phone', axis=1))



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df[df.city=='Moscow'].drop('mobile_phone', axis=1).drop('music', axis=1).drop('can_access_closed', axis=1).drop('is_closed', axis=1).drop('json', axis=1))



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.loc[df.city=='Saint Petersburg', ['id', 'first_name', 'last_name', 'bdate', 'city']])



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.iloc[:, [1,2,3,6,7]])



# import pandas as pd
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.loc[df.last_name=='Borodin', ['id', 'first_name', 'last_name', 'bdate', 'city']])



from matplotlib import pyplot as plt
# x_values = [0, 1, 2, 3, 4]
# y_values = [0, 1, 4, 9, 16]
# plt.plot(x_values, y_values)
# plt.show()




# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# df_raw = pd.read_excel('tt.xlsx', header=0, sep='\t')
# df = df_raw.groupby('city').size()
# df.plot(kind='pie', figsize=(8,8), dpi=80)
# plt.title('Pie chart of people by city')
# plt.ylabel('')
# plt.show()
#print(df_raw.loc[:, ['city']])



# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# df1 = df.loc[:, ['city']]
# # plt.pie()
# # plt.show()
# print(df1)


from matplotlib import pyplot as plt

data_names = ['Петр', 'Саша', 'Антон', 'Наташа',
              'Егор', 'Аня', 'Женя', 'Ангелина',
              'Семен', 'Марина']
data_values = [1076, 979, 222, 189, 137, 134, 124, 124, 91, 79]

plt.figure(figsize=(9.2, 7))
plt.title('Распределение лаков и репостов на фотографиях (%)')

plt.pie(
    data_values, autopct='%d%%', radius = 1.1,
    explode = [0.07] + [0 for _ in range(len(data_names) - 1)] )
plt.axis('equal')
plt.legend(data_names, loc=2, borderaxespad=0)
plt.show()
plt.savefig('pie.png')