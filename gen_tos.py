import os, fnmatch
import argparse

def getMdTitle(filename):
    for line in open(filename):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse folder and generate markdown file')
    parser.add_argument('folder', type=str, help='Folder to parse')
    parser.add_argument('--filename', type=str, default="index.md", help='Output filepath')
    args = parser.parse_args()

    res = "# Table of contents\n"
    listOfFiles = os.listdir(args.folder)  
    pattern = "*.md"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                res += "[{}]({})\n\n".format(getMdTitle(args.folder + "/" + entry), entry)
    f = open(args.folder + "/" + args.filename, "w+")
    f.write(res)
