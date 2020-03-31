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



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# df = pd.read_excel('tt.xlsx', header=0, sep='\t')
# print(df.loc[:, ['city']])