# Visualisation de relations continues 
# Pour cette partie, nous utiliserons le dataset suivant : sales_predictions.csv que vous pouvez
#  trouver dans le dossier Data Sources.
 
# 1)Importez les librairies qu’il vous faut
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline

from google.colab import files
uploaded = files.upload()
import io
sales_predictions = pd.read_csv(io.BytesIO(uploaded['sales_predictions.csv']))
sales_predictions.head()

# 2)En utilisant relplot(), construisez un graphique qui va vous permettre de voir l’évolution
#  des prix par rapport au temps. Que pouvez vous voir ?  
sns.relplot(x=sales_predictions["item_price"],y=sales_predictions["date"],data=sales_predictions)


# 3)Corrigeons le problème de visualisation,
#  en utilisant la fonction .sample() de Pandas, prenez un échantillons de 50 éléments dans votre dataset 
 new_sp = sales_predictions.sample(50)
sns.relplot(x=new_sp["item_price"],y=new_sp["date"],data=new_sp)

#  4)Retentez de faire votre visualisation et créer une figure plus grande. Que voyez vous ? 
a4_dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=a4_dims)
sns.scatterplot(x=new_sp["item_price"],y=new_sp["date"],ax=ax,data=new_sp)

#  5)En utilisant la fonction pd.to_datetime(), convertissez votre colonne date en datetime
new_sp["date"] = pd.to_datetime(new_sp["date"])

# 6)Retentez une dernière fois votre visualisation.
sns.scatterplot(x="item_price",y="date",data=new_sp)

