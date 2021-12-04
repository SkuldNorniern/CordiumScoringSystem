import os
import typer
import pickle
from core import loggermod as lgm
from core import miscfuncmod as mfm
file_pbdt = "problemdata.dat"
file_dirdt = "dirdt.dat"


# Check for files that is needed 

def chkdirdt(name,path="./",state=0):
    
    if os.path.exists(file_dirdt):
        if(not(state)): typer.echo('Dirctory data detected loading problems.')
        if(not(state)): return True
    elif(state):
        typer.echo('Generating problem dirctory file.')
        gendirdt(name,path)
    if(not(state)): return False
    
def chkpbdt(name,path,dtcnt,timeout):
    pbpath = path+"./"+file_pbdt
    if os.path.exists(pbpath):
        typer.echo('Problem data detected loading data.')
    else:
        typer.echo('Generating problem data.')
        genpbdt(name,path,pbpath,dtcnt,timeout)

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
    
def genpbdt(name, path, pbpath,dtcnt,timeout):
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
    inittsdt(path,name,pbpath,dtcnt,timeout)

# Setting up database

def inittsdt(path,name,pbpath,dtcnt,timeout):
    pbdt={'name':name,name:(path+"/"+"testdata"),"testcasecnt":dtcnt,"timeout":timeout}
    for i in range(1,dtcnt+1):
        inp=("input"+str(i)+".txt")
        oup=("output"+str(i)+".txt")
        
        # Migration & Correct some bad test data placement
        if os.path.exists(path+"/"+inp):
            if not(os.path.exists(path+"/"+"testdata")):
                mfm.mkdir(path+"/"+"testdata")
            mfm.movefile((path+"/"+inp),(path+"/"+"testdata"+"/"+inp))
            mfm.movefile((path+"/"+oup),(path+"/"+"testdata"+"/"+oup))
        
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

def calldirdt(name):
    with open(file_dirdt,'rb') as fr:
        dirdt = pickle.load(fr)
    return dirdt[name]
    
def calltd(name):
    path = calldirdt(name)

    with open(path+"/"+file_pbdt,'rb') as fr:
        pbtd = pickle.load(fr)
    #print(pbtd)
    tdpath=pbtd[name]
    indtf=pbtd["input"]
    oudtf=pbtd["output"]
    dtcnt=pbtd["testcasecnt"]
    timeout=pbtd["timeout"]
    return path,tdpath,indtf,oudtf,dtcnt,timeout

