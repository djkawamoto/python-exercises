# !usr/local/bin/python2
# The Tech Academy
# Python Course step 68 of 79
# File Transfer Script drill by Daniel Kawamoto

import shutil
import os
import time

class FileCheckerCopier():

    def ck_cpy_mod_files():
        srcFiles = os.listdir("/Users/danielkawamoto/Desktop/FileCheckerCopier/SourceFolder/")
        src = "/Users/danielkawamoto/Desktop/FileCheckerCopier/SourceFolder/"
        dst = "/Users/danielkawamoto/Desktop/FileCheckerCopier/DestinationFolder/"
        now = int(time.time())
        fileCount = 0

        for _file in srcFiles:
            if int(os.stat(os.path.abspath(src+'%s' % _file)).st_mtime) > (now - 86400):
                shutil.copy2(src+'%s' % _file, dst+'%s' % _file)
                fileCount += 1
        print fileCount, " files copied."

    ck_cpy_mod_files()

if __name__ == "__main__":
    FileCheckerCopier()
