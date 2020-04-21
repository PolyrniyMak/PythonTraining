import pandas as pd
df = pd.read_html('https://www.cbr.ru/currency_base/daily/', header=0)
print(df)