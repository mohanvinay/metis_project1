#Function to take a date and create a season flag consisting of YYYYQ where Y = year and Q=Quarter

from collections import Counter
import pandas as pd
import operator

'''
def create_season_flag(df1, field):
    """
    Return season flag from date string

    Parameters
    ----------
    df1 : dataframe containing date field
    field : field containing date values
    
    Returns
    -------
    5-character string. 
    [0-3] - YYYY
    [4] - Quarter in the year YYYY

    """
    for i,value in enumerate(df1[field]):
        if int(df1.xs(i)[field])<=3:
            df1.xs(i)[field]=1
        else:
            pass
    return df1

        
    if (int(date[5:7])<=3):
        quarter=1
    elif (int(date[5:7])<=6):
        quarter=2
    elif (int(date[5:7])<=9):
        quarter=3
    else:
        quarter=4
    season_flag=str(year)+str(quarter)
    return season_flag'''


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
    data : dataframe containing data including 1 or more columns with categorical variable
    column : String indicating the name of the column with categorical variables
    top_n : integer indicating top n categories
    
    Returns
    -------
    Dataframe with dummy variables for categorical variable 'column'

    """
    top_field= data[column].value_counts().index[:top_n]
    top_df=data[data[column].isin(top_field)]
    dummies=pd.get_dummies(top_df[column])
    top_df= pd.concat([top_df,dummies],axis=1)
    return top_df   
        

if __name__=='__main__':
    data={'Gross':[2000,5000,5000,5500,2000,10000,500,7000],
    'Director':['James Bond','Steven Spielberg','Steven Spielberg','Steven Spielberg','James Bond','Steven Spielberg','James Bond','Martin S'],
    'Dates' : ['2008-03-05','2009-10-12','2011-11-12','2011-10-10','2008-01-01','2007-02-02','2006-02-02','2015-01-01']}
    df1=pd.DataFrame(data)
    column_name='Dates'
    df3=create_season_flag(df1,column_name)
    print df3
#    print season_flag
#    data={'Gross':[2000,5000,5000,5500,2000,10000,500,7000],
#    'Director':['James Bond','Steven Spielberg','Steven Spielberg','Steven Spielberg','James Bond','Steven Spielberg','James Bond','Martin S']}
#    df1=pd.DataFrame(data)
#    column_name='Director'
#    new_df=catg_to_dummy(df1,column_name,2)
#    print new_df

    
    
    