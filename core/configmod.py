import os
import typer
import pickle
import configparser
from core import loggermod as lgm
from core import miscfuncmod as mfm

#file_cfg = "config.dat"
file_pbdt = "problemdata.dat"
file_dirdt = "dirdt.dat"


# Check for files that is needed 

def chkdirdt(name,path):
    
    if os.path.exists(file_dirdt):
        typer.echo('Dirctory data detected loading problems.')
    else:
        typer.echo('Generating problem dirctory file.')
        gendirdt(name,path)
    
def chkpbdt(name,path,dtcnt):
    pbpath = path+"./"+file_pbdt
    if os.path.exists(pbpath):
        typer.echo('Problem data detected loading data.')
    else:
        typer.echo('Generating problem data.')
        genpbdt(name,path,pbpath,dtcnt)

# Generate files that is missing or need to be generated

def gendirdt(name,path):
    dirdt={'name':'path'}
    name = mfm.rmpathval(name)
    print(name)
    path="./"+mfm.rmpathval(path)
    print(path)
    dirdt[name]=path
    print(dirdt)
    with open(file_dirdt,'wb') as fw:
        pickle.dump(dirdt, fw)
    
def genpbdt(name, path, pbpath,dtcnt):
    with open(file_dirdt,'rb') as fr:
        dirdt = pickle.load(fr)
    print(dirdt)
    
    name = mfm.rmpathval(name)
    dirdt[name]=path
    print(dirdt)
    with open(file_dirdt,'wb') as fw:
        pickle.dump(dirdt, fw)
    print(name)
    path="./"+mfm.rmpathval(path)
    out=open(pbpath, 'w')
    out.close
    inittsdt(path,name,pbpath,dtcnt)

# Setting up database

def inittsdt(path,name,pbpath,dtcnt):
    pbdt={'name':name,name:(path+"/"+"testdata"),"testcasecnt":dtcnt}
    for i in range(1,dtcnt+1):
        inp=("input"+str(i)+".txt")
        oup=("output"+str(i)+".txt")
        if "input" in pbdt:
            pbdt["input"].append(inp)
        else:
            pbdt["input"] = [inp]
        if "output" in pbdt:
            pbdt["output"].append(oup)
        else:
            pbdt["output"]= [oup]
            
    print(pbdt)
    with open(pbpath,'wb') as fw:
        pickle.dump(pbdt, fw)

# Call problem test data

def calltd(name):
    with open(file_dirdt,'rb') as fr:
        dirdt = pickle.load(fr)

    path = dirdt[name]

    with open(path+"/"+file_pbdt,'rb') as fr:
        pbtd = pickle.load(fr)
    print(pbtd)
    tdpath=pbtd[name]
    indtf=pbtd["input"]
    oudtf=pbtd["output"]
    dtcnt=pbtd["testcasecnt"]
    return path,tdpath,indtf,oudtf,dtcnt