import os
import sys
import time
import typer
import subprocess as sbp
from core import configmod as cfm
from core import miscfuncmod as mfm
from core import datasetmod as dsm

compile_args={"Python":"python","Java":"java","C/C++":"gcc"}
plus_args={"Python":"","Java":"","C/C++":"a.exe"}
timebuff={"Python":1.5,"Java":1.5,"C/C++":1}

def compile(file,lang,name,user):
    
    typer.echo(f"-----------------------------------------------------------------")
    
    path,tdpath,indtf,oudtf,dtcnt,timelim = cfm.calltd(name)
    state=True
    dsm.init(path,dtcnt)
    times=[]
    #dsm.addname(user)
    #typer.echo("Adding name to scoreboard")
    i=0
    with typer.progressbar(range(dtcnt)) as progress:
        for i in (progress):
            f = open((tdpath+"/"+indtf[i]))
            data = f.read()
            #print(data)
            #print(len(plus_args["Python"]))
            timeStarted = time.time()
            try:
                process=sbp.Popen(f"{compile_args[lang]} {file}",shell=True,stdin=sbp.PIPE,
                                    stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
                if(len(plus_args[lang])!=0):
                    process.wait()
                    timeStarted = time.time()
                    process = sbp.Popen(f"{plus_args[lang]}", shell=True, stdin=sbp.PIPE, stdout=sbp.PIPE,
                                        stderr=sbp.STDOUT, universal_newlines=True)
                process.stdin.write(data)
                process.stdin.flush()
                f.close()
                out, cmd_err = process.communicate(
                    timeout=(timelim*timebuff[lang]))
                timeDelta = time.time() - timeStarted
            except Exception:
                process.kill()
                timeDelta=0
                process.wait()
                #print(str(e.output))
            
            
            f = open((tdpath+"/"+oudtf[i]))
            data = f.read()
            f.close()
            #print(data)
            #print(out)
            
            state=mfm.iscorrect(out.strip(),data.strip())
            if not(state):
                timeDelta = 0
                i-=1
                break
            times.append(round(timeDelta, 5))
    i+=1
    typer.echo(f"{i*(100/dtcnt)} 점")
    #dsm.addscore(user,name,i*(100/dtcnt))
    for j in range(i,dtcnt):
        times.append(0)
    dsm.addscore(path, dtcnt, user, times, i*(100/dtcnt))
    if state: mfm.movefile(file,path)
    return state
