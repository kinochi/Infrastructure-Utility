import os,sys,shutil
extension = ['.pdf','.avi','.doc','.mp3','.mkv','.ppt','.m','.jpg','.png']
folder = [s.strip('.').upper() for s in extension]

def club(path):
    if sys.version_info < (3,5):                        # os.scandir need python version 3.5 at least
        print('Python version > 3.5 required!')
        return

    # os.scandir is substitute for os.walk as its slower due to unnessecary calls to os.listdir
    for entry in os.scandir(path):                      
        try:
            #TODO os.access does not works properly with windows access permission checking 
            #checks if its not a directory and accessible
            not_dir_and_acc = not entry.is_dir(follow_symlinks=False) and os.access(entry.path,os.R_OK)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if not_dir_and_acc :
            # for all the files that end with any of these extension make the path for directory
            # And if it does not exists make the directory and move the file to that directory
            for e in range(len(extension)):
                if(entry.name.endswith( extension[e])):
                    rel_path = os.path.join(path,folder[e])
                    if(not os.path.isdir(rel_path)):
                        os.mkdir(rel_path)
                    shutil.move(entry.path,rel_path)
                    break

if __name__ == '__main__' :
    if(len(sys.argv)<2):
        print("Error: Provide enough arguments\nUsage : club.py  [directory] ") 
    # For seeing supported extensions
    elif(sys.argv[1] in ['-l' ,'-list']):
        print('Extensions Supported :'+ str(extension)) 
    elif(os.path.exists(sys.argv[1])):
        club(sys.argv[1])
    else:
        print("Error: Please provide a correct path\nUsage : club.py  [directory] ")
