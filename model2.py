from script1 import catg_to_dummy,create_season_flag
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

if __name__=='__main__':
    data=pd.read_csv('/Users/jmx948/work/tech/repos/metis_project1/merged_data_v2.csv')
    #print data
    







#    date='2008-03-07'
#    season_flag=create_season_flag(date)
#    print season_flag
#    data={'Gross':[2000,5000,5000,5500,2000,10000,500,7000],
#    'Director':['James Bond','Steven Spielberg','Steven Spielberg','Steven Spielberg','James Bond','Steven Spielberg','James Bond','Martin S']}
#    df1=pd.DataFrame(data)
#    column_name='Director'
#    new_df=catg_to_dummy(df1,column_name,2)
#    print new_df