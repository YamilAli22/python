import pandas as pd
import matplotlib.pyplot as mtp
import seaborn as sns

df = pd.read_csv("/home/yamil/Escritorio/python/graficos/boxplot.csv")
print(df)
#creando el grafico
sns.boxplot(x="categoria", y="valor",data=df)

#mostrando el grafico
mtp.show()