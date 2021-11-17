import os
import sys
import typer
from core import configmod as cfm

def init(name, timeout, datacnt, path):
    cfm.chkdirdt(name, path)
