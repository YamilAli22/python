import pandas as pd
import matplotlib.pyplot as mtp
import seaborn as sns

df = pd.read_csv("/home/yamil/Escritorio/python/graficos/pe2.csv")
print(df)
#creando el grafico
sns.lineplot(x="fecha", y="pedos",data=df)

#creando un punto en el momento mas alto
mtp.plot("01-06", 16, "o")

#mostrando el grafico
mtp.show()