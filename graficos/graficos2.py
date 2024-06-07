import pandas as pd
import matplotlib.pyplot as mtp
import seaborn as sns

df = pd.read_csv("/home/yamil/Escritorio/python/graficos/datos.csv")
print(df)
#creando el grafico
sns.scatterplot(x="tiempo", y="dinero",data=df)

#mostrando el grafico
mtp.show()