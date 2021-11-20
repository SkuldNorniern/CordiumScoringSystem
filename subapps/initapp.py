import os
import sys
import typer
from core import configmod as cfm

def init(name, timeout, dtcnt, path):
    cfm.chkdirdt(name, path,1)
    cfm.chkpbdt(name,path,dtcnt,timeout)    
