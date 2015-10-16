
import pandas as pd
import statsmodels.api as sm
import math
import script1
from sklearn.cluster import KMeans
import numpy as np
import seaborn
import pprint


data = pd.read_csv('merged_data.v2.csv')

data['release_date_wide'] = pd.to_datetime(data['release_date_wide'])
data['release_year_qtr'] = data['release_date_wide'].apply(lambda x: x.year*100+x.quarter)
data['release_qtr'] = data['release_date_wide'].apply(lambda x: x.quarter)

data['sqrt_prodcost']=[math.sqrt(x) for x in data.production_budget]

data.sqrt_prodcost.hist()

dat = data.dropna()

dir_data=dat.groupby('director_x')
dir_production=dir_data['production_budget'].mean()

dir_production.describe()

dir_1=dir_production[dir_production<=1.7E7].index
dir_2=dir_production[(dir_production>1.7E7) & (dir_production<=3.65E7)].index
dir_3=dir_production[(dir_production>3.65E7) & (dir_production<=6.5E7)].index
dir_4=dir_production[dir_production>6.5E7].index

dat['dir_cat'] = np.nan
dat['dir_cat'][dat.director_x.isin(dir_1)] = "DIR 1"
dat['dir_cat'][dat.director_x.isin(dir_2)] = "DIR 2"
dat['dir_cat'][dat.director_x.isin(dir_3)] = "DIR 3"
dat['dir_cat'][dat.director_x.isin(dir_4)] = "DIR 4"

studio_data=dat.groupby('studio')
studio_production=studio_data['production_budget'].mean()

studio_production.describe()

studio_1=studio_production[studio_production<=1.3E7].index
studio_2=studio_production[(studio_production>1.3E7) & (studio_production<=2.8E7)].index
studio_3=studio_production[(studio_production>2.8E7) & (studio_production<=5.51E7)].index
studio_4=studio_production[studio_production>5.51E7].index

dat['studio_cat'] = np.nan
dat['studio_cat'][dat.studio.isin(studio_1)] = "Studio 1"
dat['studio_cat'][dat.studio.isin(studio_2)] = "Studio 2"
dat['studio_cat'][dat.studio.isin(studio_3)] = "Studio 3"
dat['studio_cat'][dat.studio.isin(studio_4)] = "Studio 4"

st_cat=pd.get_dummies(dat['studio_cat'])
d_cat=pd.get_dummies(dat['dir_cat'])

X_data=st_cat.ix[:,0:3].join(d_cat.ix[:,0:3])

#pd.get_dummies(dat['genre'])

Y = dat.sqrt_prodcost
X=sm.add_constant(X_data)

fit1 = sm.OLS(Y,X)
fit1 = fit1.fit()
fit1.summary()

#%matplotlib inline
seaborn.boxplot(x='studio_cat',y='production_budget',data=dat)

seaborn.boxplot(x='dir_cat',y='production_budget',data=dat)

print(dir_1)
