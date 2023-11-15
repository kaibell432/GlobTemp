import matplotlib.pyplot as plt
import pandas as pd

def plot_relevant(df):
    for col in range(2,df.shape[1],2):
        df.iloc[:,[col,col+1]].plot(subplots=True, figsize=(15,16))
    plt.show()

df = pd.read_csv('data\Global Temperature.csv')
df.columns = df.columns.map(lambda name: name.strip())
df[df.columns[2:]] = df[df.columns[2:]].applymap(lambda string:float(string))
df2 = df.copy()
df2['Date'] = pd.to_datetime(df2[['Year', 'Month']].assign(day=1))
df2.set_index('Date', inplace=True)

df2.index = df2.index.strftime('%Y-%m')
plot_relevant(df2)
print(df2.head(2))