import json
import os

sucess = {'status': 'Cleaned!'}
failed = {'status': 'Path not found! Switch your option.'}
arq = 'status.json'

def Sucess():
    with open(arq, 'w') as file:
        json.dump(sucess, file, indent=4)

def Failed():
    with open(arq, 'w') as file:
        json.dump(failed, file, indent=4)

def FileExists(arq):
    if os.path.isfile(arq):
        return True
    else:
        return False

def ReadStatus():
    if FileExists(arq):
        with open(arq, 'r') as file:
            json_data = json.loads(json.dumps(json.load(file), indent=4))
            return json_data
    else:
        ...