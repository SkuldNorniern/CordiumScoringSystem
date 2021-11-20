import os
import sys
import typer
import subprocess as sbp
from core import configmod as cfm
from core import miscfuncmod as mfm

compile_args={"Python":"python","Java":"java","C/C++":"gcc"}
plus_args={"Python":" ","Java":" ","C/C++":"a.exe"}

def compile(file,lang,name,user):
    typer.echo(f"{file}")
    path,tdpath,indtf,oudtf,dtcnt = cfm.calltd(name)
    state=True
    pt=100/dtcnt
    cpt=0
    for i in range (dtcnt):
        f = open((tdpath+"/"+indtf[i]))
        data = f.read()
        #print(data)
        process=sbp.Popen(f"{compile_args[lang]} {file}",shell=True,stdin=sbp.PIPE,stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
        if lang=="C/C++": 
            #print(f"{plus_args[lang]}")
            process=sbp.Popen(f"{plus_args[lang]}",stdin=sbp.PIPE,stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
            
        
        process.stdin.write(data)
        process.stdin.flush()
        f.close()
        
        out, cmd_err = process.communicate()
        
        f = open((tdpath+"/"+oudtf[i]))
        data = f.read()
        f.close()
        #print(data)
        #print(out)
        state=mfm.iscorrect(out.strip(),data.strip())
        if not(state): break
        cpt+=pt
        print(f"{cpt}%")
    if state: mfm.movefile(file,path)
    return state