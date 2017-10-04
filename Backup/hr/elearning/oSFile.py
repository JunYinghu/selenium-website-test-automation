import datetime
import os
import shutil
from os import path
from zipfile import ZipFile

def main():
    print os.name
    print "does the path exist " + str(path.exists("textfile.txt"))
    print "it is a file " + str(path.isfile("textfile.txt"))
    print "is it a folder " + str(path.isdir("textfile.txt"))
    print str(path.realpath("textfile.txt"))
    print str(path.split(path.realpath("textfile.txt")))
    # get modification datetime of file
    # t = time.ctime(path.getmtime("textfile.txt"))
    # print t
    print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

    # get how long the file was modificed
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print  str(td)
    print str(td.total_seconds())

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        head, tail = path.split(src)
        print head
        print tail
        # make a backup
        dst = src + ".bak"
        shutil.copy(src, dst)
        # copy permission and modificaton time and other info
        shutil.copystat(src, dst)

        os.rename("textfile.txt", "newtextfile.txt")
        src = path.realpath("newtextfile.txt")
        # archive everything into a zip
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newtextfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == '__main__':
    main()
