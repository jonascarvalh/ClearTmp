import getpass
import os
import shutil
from src import status

def GetDisks():
    # Disks Avaiable in System
    all_disks = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    disks_avaiable = []

    os.system('cls')

    for d in all_disks:
        if os.path.exists('%s:' % d):
            disks_avaiable.append('%s' % d) 
    
    return disks_avaiable

def ClearTemp(disco):
    disco = f'{disco}:\\'

    # Acessing path %temp%
    usuario = getpass.getuser()
    if os.path.isdir(os.path.join(disco, 'users')):
        caminho = os.path.join(disco, 'users', usuario, 'appdata', 'local', 'temp')
        status.Sucess()
    elif os.path.isdir(os.path.join(disco, 'usuários')):
        caminho = os.path.join(disco, 'usuários', usuario, 'appdata', 'local', 'temp')
        status.Sucess()
    else:
        status.Failed()
        return

    # Listing files and dirs
    files = []
    dirs  = []

    for (dirpath, dirnames, filenames) in os.walk(caminho):
        files.extend(filenames)
        dirs.extend(dirnames)
        break

    # Deleting dirs
    for dir in dirs:
        try:
            shutil.rmtree(os.path.join(caminho, dir))
        except:
            ...

    # Deleting files
    for file in files:
        try:
            os.remove(os.path.join(caminho, file))
        except:
            ...

    # Acessing path temp
    caminho = os.path.join(disco, 'windows', 'temp')

    # Listing files and dirs
    files = []
    dirs  = []

    for (dirpath, dirnames, filenames) in os.walk(caminho):
        files.extend(filenames)
        dirs.extend(dirnames)
        break

    # Deleting dirs
    for dir in dirs:
        try:
            shutil.rmtree(os.path.join(caminho, dir))
        except:
            ...

    # Deleting files
    for file in files:
        try:
            os.remove(os.path.join(caminho, file))
        except:
            ...