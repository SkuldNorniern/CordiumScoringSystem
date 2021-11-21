import csv
import typer
import os.path
import pandas as pd
#from core import configmod as cfm
#from core import loggermod as lgm

file_svr = 'saved_report.csv'

def init():
    if os.path.exists(file_svr):
        typer.echo("Found file")
        #lgm.logmsg('Dataset Detected Continue to boot.', 'info')
    else:
        filedt=pd.DataFrame(columns=['name'])
        filedt.to_csv(file_svr,index=False)

def addproblem(name):
    filedt=pd.read_csv(file_svr)
    filedt[name]=0
    filedt.to_csv(file_svr,index=False)
    print(filedt)

def addscore(user,name,score):
    filedt = pd.read_csv(file_svr)
    filedt.loc[filedt['name'] == user, name] = score
    print(filedt)

def addname(user):
    filedt = pd.read_csv(file_svr)
    print(filedt)
    print(filedt.loc[filedt['name'==user]])
    if(filedt.empty or not(filedt.name.isin([user]).all('name'))):
        filedt = filedt.append({'name': user},ignore_index=True)
        print(filedt)
    filedt.to_csv(file_svr, index=False)
#df = pd.DataFrame(columns=['name', 'age', 'job'])
#df['salary'] = 0
#print(df)
