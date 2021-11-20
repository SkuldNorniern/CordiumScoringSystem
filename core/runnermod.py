import os
import sys
import typer
import subprocess as sbp
from core import configmod as cfm
from core import miscfuncmod as mfm

compile_args={"Python":"python","Java":"java","C/C++":"gcc"}
plus_args={"Python":" ","Java":" ","C/C++":"&& a.exe"}
timebuff={"Python":1.5,"Java":1.5,"C/C++":1}

def compile(file,lang,name,user):
    typer.echo(f"-----------------------------------------------------------------")
    path,tdpath,indtf,oudtf,dtcnt,timelim = cfm.calltd(name)
    state=True
    with typer.progressbar(range(dtcnt)) as progress:
        for i in (progress):
            f = open((tdpath+"/"+indtf[i]))
            data = f.read()
            #print(data)
            process=sbp.Popen(f"{compile_args[lang]} {file} {plus_args[lang]}",shell=True,stdin=sbp.PIPE,stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
            process.stdin.write(data)
            process.stdin.flush()
            f.close()
            
            out, cmd_err = process.communicate(timeout=(timelim*timebuff[lang]))
            
            f = open((tdpath+"/"+oudtf[i]))
            data = f.read()
            f.close()
            #print(data)
            #print(out)
            state=mfm.iscorrect(out.strip(),data.strip())
            if not(state): break
        
    if state: mfm.movefile(file,path)
    return state