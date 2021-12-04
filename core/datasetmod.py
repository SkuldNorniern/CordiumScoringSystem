import csv
import typer
import os.path
import pandas as pd
from datetime import datetime
#from core import configmod as cfm
#from core import loggermod as lgm

file_svr = 'saved_report.csv'

def init(pbpath,dtcnt):
    filepath = pbpath + "/" + file_svr
    if not(os.path.exists(filepath)):
        clm = {'date': [], 'user': []}
        for i in range(dtcnt):
            clm["data "+(str(i+1))] = []
        clm["score"] = []
        filedt = pd.DataFrame(clm)
        filedt.to_csv(filepath, index=False, encoding='utf-8-sig')
        

def addscore(pbpath, dtcnt ,user, exectimes, score):
    filepath = pbpath + "/" + file_svr
    date = datetime.today().strftime('%Y-%m-%d-%H:%M')
    filedt = pd.read_csv(filepath)
    dic = {'date': date, 'user': user}
    for i in range(dtcnt):
        dic["data "+(str(i+1))]=exectimes[i]
    
    dic["score"]=score
    print(dic)
    filedt=filedt.append(dic, ignore_index=True)
    print(filedt)
    filedt.to_csv(filepath, index=False, encoding='utf-8-sig')







#def addproblem(name):
#    filedt=pd.read_csv(file_svr)
#    filedt[name]=0
#    filedt.to_csv(file_svr,index=False)
#    print(filedt)

#def addscore(user,name,score):
#    filedt = pd.read_csv(file_svr)
#    filedt.loc[filedt['name'] == user, name] = score
#    print(filedt)

#def addname(user):
#    filedt = pd.read_csv(file_svr)
#    print(filedt)
#    print(filedt.loc[filedt['name'==user]])
#    if(filedt.empty or not(filedt.name.isin([user]).all('name'))):
#        print(filedt)
#        filedt = filedt.append({'name': user},ignore_index=True)
#    filedt.to_csv(file_svr, index=False)
#df = pd.DataFrame(columns=['name', 'age', 'job'])
#df['salary'] = 0
#print(df)
