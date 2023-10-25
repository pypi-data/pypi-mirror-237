import os


def get_dirs(path):
    """ Return list of directories in folder """
    directories = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            directories.append(os.path.join(root, d))
    return directories

def get_files(dir):
    """ Return list of files in folder """
    files = []
    for p in os.listdir(dir):
        fullpath = os.path.join(dir, p)
        # Check if current path is a file
        if os.path.isfile(fullpath):
            files.append(fullpath)
    return files
