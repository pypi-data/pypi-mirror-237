#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import pyzipper
# import shutil

def make_zip_v3(source_dir, output_filename,password):
    with pyzipper.AESZipFile(output_filename,'w',compression=pyzipper.ZIP_LZMA) as zf:
        zf.setpassword(password.encode('utf8'))
        zf.setencryption(pyzipper.WZ_AES, nbits=128)
        for path, _, filenames in os.walk(source_dir):
            fpath = path.replace(source_dir, '')
            for filename in filenames:
                zf.write(os.path.join(path, filename),os.path.join(fpath, filename))
    # try:
    #     shutil.rmtree(source_dir)
    # except:
    #     pass