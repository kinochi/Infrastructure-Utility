import os
import sys
MB = 1<<20
files=[]
def get_files(path):
    """Returns all the files as well as total size of files in the subdirectory of specified path. If
    is_dir() or stat() fails, print an error message to stderr
    and assume zero size (for example, file has been deleted).
    """
    total=0;
    for entry in os.scandir(path):
        try:                                             # Don't follow sym_links and ignore if not a directory or need more permissions
            is_dir_and_acc = entry.is_dir(follow_symlinks=False) and os.access(entry.path,os.R_OK)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if is_dir_and_acc:  
            total += get_files(entry.path)               # Recursively get all files from subdirectories
        else:
            try:
                file_size = entry.stat(follow_symlinks=False).st_size   # Get file size
                file_path = entry.path                                  # Get path of the file
                files.append([file_path,file_size])
                total+=file_size

            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)
    return total

def main():
    if(len(sys.argv)>=3 and os.path.exists(sys.argv[2])):
        if(len(sys.argv)<4): k = int(sys.argv[2])
        else: k = 10
        total_size = get_files(sys.argv[1])/(MB); 
        print(str(total_size) + " MB")
        klargest = sorted(files, key=lambda x : x[1], reverse=True)[:k]
        print( '\n'.join(['{} : {} - {} MB'.format(i[0],i[1][0],round(i[1][1]/MB)) for i in enumerate(klargest,1)]) )
    else:
        print("Error: Please provide a correct path\nUsage : dir.py [directory] [num_result=10]")


if __name__ == '__main__':
    main()
