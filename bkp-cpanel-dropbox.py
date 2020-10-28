# -*- coding: utf-8 -*-

import dropbox
import re
import sys
import glob
import os
from tqdm import tqdm


def upload(
    access_token,
    file_path,
    target_path,
    timeout=900,
    chunk_size=4*1024*1024
):
    dbx = dropbox.Dropbox(access_token, timeout=timeout)
    with open(file_path, "rb") as f:
        file_size = os.path.getsize(file_path)
        
        calc_percent = 0
        if file_size <= chunk_size:
            result_upload  = dbx.files_upload(f.read(), target_path)
            print("File '" + result_upload.name + "' uploaded 100%")
        else:
            with tqdm(total=file_size, desc="Uploading", unit_scale=True, unit_divisor=1024) as pbar:
                upload_session_start_result = dbx.files_upload_session_start(
                    f.read(chunk_size)
                )
                pbar.update(chunk_size)
                cursor = dropbox.files.UploadSessionCursor(
                    session_id=upload_session_start_result.session_id,
                    offset=f.tell(),
                )
                commit = dropbox.files.CommitInfo(path=target_path)
                while f.tell() < file_size:
                    if (file_size - f.tell()) <= chunk_size:
                        result_upload = dbx.files_upload_session_finish(
                                f.read(chunk_size), cursor, commit
                            )
                        print("File '" + result_upload.name + "' uploaded 100%")
                    else:
                        dbx.files_upload_session_append(
                            f.read(chunk_size),
                            cursor.session_id,
                            cursor.offset,
                        )
                        cursor.offset = f.tell()
                        
                    pbar.update(chunk_size)


access_token_dropbox = <ACCESS TOKEN>
chunk_size=300*1024*1024
timeout = 9999

fole_origin = sys.argv[1];
if fole_origin:
    file_name = os.path.basename(fole_origin)
    file_destiny = sys.argv[2];
    if not file_destiny:
        file_destiny = "/BKP-CPANEL/"+ file_name
    else:
        file_destiny = file_destiny + file_name

    upload(access_token_dropbox, fole_origin,file_destiny, timeout, chunk_size)
else:
    print('Invalid or not reported file')
