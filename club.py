import os,sys,shutil
extension = ['.pdf','.avi','.doc','.mp3','.mkv','.ppt','.m','.jpg','.png']
folder = [s.strip('.').upper() for s in extension]

def club(path):
    if sys.version_info < (3,5):
        print('Python version > 3.5 required!')
        return
    for entry in os.scandir(path):
        try:
            not_dir_and_acc = not entry.is_dir(follow_symlinks=False) and os.access(entry.path,os.R_OK)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if not_dir_and_acc :
            for e in range(len(extension)):
                if(entry.name.endswith( extension[e])):
                    rel_path = os.path.join(path,folder[e])
                    if(not os.path.isdir(rel_path)):
                        os.mkdir(rel_path)
                    shutil.move(entry.path,rel_path)
                    break

if __name__ == '__main__' :
    #TODO add suitable condition to print error message
    if(len(sys.argv)<2):
        print("Error: Provide enough arguments\nUsage : club.py  [directory] ") 
    elif(sys.argv[1] in ['-l' ,'-list']):
        print('Extensions Supported :'+ str(extension)) 
        #if(len(sys.argv)>=3 and os.path.exists(sys.argv[2])):
        #    club(sys.argv[1]) 
    elif(os.path.exists(sys.argv[1])):
        club(sys.argv[1])
    else:
        print("Error: Please provide a correct path\nUsage : club.py  [directory] ")
