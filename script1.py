#Function to take a date and create a season flag consisting of YYYYQ where Y = year and Q=Quarter

from collections import Counter
import pandas as pd
import operator

def create_season_flag(date):
    """
    Return season flag from date string

    Parameters
    ----------
    date : date string in format 'YYYY-MM'DD
    
    Returns
    -------
    5-character string. 
    [0-3] - YYYY
    [4] - Quarter in the year YYYY

    """
    if not isinstance(date,string):
        raise TypeError('date variable must be a string')
        
    year=date[:4]
    if (int(date[5:7])<=3):
        quarter=1
    elif (int(date[5:7])<=6):
        quarter=2
    elif (int(date[5:7])<=9):
        quarter=3
    else:
        quarter=4
    season_flag=str(year)+str(quarter)
    return season_flag


#Please ignore function below
'''def catg_to_dummy_manual(data,column,top_n):
    list=data[column].tolist()    
    dict_counts=Counter(list);
    sorted_dict_counts = sorted(dict_counts.items(), key=operator.itemgetter(1),reverse=True)
    list_top=[]
    for i,value in enumerate(sorted_dict_counts):
            if(i<top_n):
                list_top.append(value[0])
    for i,value in enumerate(list_top):
        name= 'Is' + str(list_top[i])
        data[name]=0
        print data       
    for i,value in enumerate(list_top):
        name= 'Is' + str(list_top[i])
        data[(data[column]==list_top[i])][name] = 1
#        data[name]=data[column].map(list_top[i]:'1')
        print data 
        '''
    
def catg_to_dummy(data,column,top_n):
    """
    Returns a dataframe with dummy variables for categorical variables

    Parameters
    ----------
    data : dataframe containing data including column with categorical variable
    column : Categorical Column [1-n]
    top_n : integer indicating top n categories
    
    Returns
    -------
    Dataframe with dummy variables for categorical variable indicated by 'column'

    """
    top_field= data[column].value_counts().index[:top_n]
    top_df=data[data[column].isin(top_field)]
    dummies=pd.get_dummies(top_df[column])
    top_df= pd.concat([top_df,dummies],axis=1)
    return top_df   
        

if __name__=='__main__':
#    date='2008-03-07'
#    season_flag=create_season_flag(date)
#    print season_flag
    data={'Gross':[2000,5000,5000,5500,2000,10000,500,7000],
    'Director':['James Bond','Steven Spielberg','Steven Spielberg','Steven Spielberg','James Bond','Steven Spielberg','James Bond','Martin S']}
    df1=pd.DataFrame(data)
    column_name='Director'
    new_df=catg_to_dummy(df1,column_name,2)
    print new_df
    
    
    
    
    
    
    
    