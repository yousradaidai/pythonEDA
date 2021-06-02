#  Visualisation d’un nuage de points et exploration des variables Pour cette partie, nous allons
#  utiliser le dataset suivante : house_pricing.csv que vous pouvez trouver dans le dossier Data Sources.
#  Nous allons tenter de comprendre un peu mieux ce dataset par la visualisation

# 1)Importez les librairies qu’il nous faut (pandas, seaborn, matplotlib, numpy)
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline

from google.colab import files
uploaded = files.upload()
import io
df2 = pd.read_csv(io.BytesIO(uploaded['house_pricing.csv']))

# 2)Donnez la liste des variables présentes dans ce dataset ainsi que leur nature 
# (sont elles qualitatives (the others/caltplot), quantitatives(int and float/), discrète etc...) et leur type (float, int, str etc...) 
sns.scatterplot(data=df2, x="LotArea", y="SalePrice")

# 3)En créant un nuage de points, regardez comment se comporte la colonne LotArea par rapport au SalesPrices
filter_tab = df2[(df2['LotArea'] <= 20000) & (df2['SalePrice'] <= 500000)]
sns.scatterplot(data=filter_tab, x="LotArea", y="SalePrice")

# 4)Affinez votre visualisation en ne gardant uniquement les maisons qui ont un LotAreainférieur à 20 000 
# pieds carrés et un prix inférieur à 500 000$ 5)En créant un nuage de points, regardez la relation entre le 
# LotFrontage et le LotArea
test = sns.scatterplot(data=filter_tab, x="LotFrontage", y="LotArea")

# 6)De la même manière, affinez votre visualisation en ne gardant uniquement les maisons qui ont un LotFrontage
#  inférieur à 200 pieds carrés et un LotArea inférieur à 100000 pieds carré

filter_tab2 = df2[(df2['LotFrontage'] <= 200) & (df2['LotArea'] <= 100000)]
test = sns.scatterplot(data=filter_tab2, x="LotFrontage", y="LotArea")