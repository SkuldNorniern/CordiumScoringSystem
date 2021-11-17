import os
import typer
import pickle
import configparser
from core import loggermod as lgm

#file_cfg = "config.dat"
file_pbdt = "problemdata.dat"
file_dirdt = "dirdt.dat"

def chkdirdt(name,path):
    
    if os.path.exists(file_dirdt):
        typer.echo('Dirctory data detected loading problems.')
    else:
        typer.echo('Generating problem dirctory file.')
        gendirdt()
    chkpbdt(name,path)
    

def chkpbdt(name,path):
    pbpath = path+"./"+file_pbdt
    if os.path.exists(pbpath):
        typer.echo('Problem data detected loading data.')
    else:
        typer.echo('Generating problem data.')
        genpbdt(name,path,pbpath)
    
def gendirdt():
    dirdt={'name':'path'}
    with open(file_dirdt,'wb') as fw:
        pickle.dump(dirdt, fw)
    
def genpbdt(name, path, pbpath):
    with open(file_dirdt,'rb') as fr:
        dirdt = pickle.load(fr)
    print(dirdt)
    dirdt[name]=path
    with open(file_dirdt,'wb') as fw:
        pickle.dump(dirdt, fw)
    out=open(pbpath, 'w')
    out.close

def init():
    lgm.logmsg('Start Initialing config module','debug')
