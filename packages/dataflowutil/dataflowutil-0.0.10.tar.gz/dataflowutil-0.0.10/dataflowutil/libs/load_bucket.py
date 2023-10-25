import os
from google.cloud import storage
import dataflowutil.config.extra_var as extra_v
import sys
import pandas as pd
from datetime import datetime

class LoadBucket:
    def __init__(self,connection,spreadsheets,config_data):
        self.cn = connection
        self.spreadsheets = spreadsheets
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(extra_v.PATH_CREDENTIALS, self.cn.credentials_path) 
        self.storage_client = storage.Client()
        self.name_bucket = self.cn.bucket_name
       # self.data_config = spreadsheets.load_spreadsheets(self.cn.id_spread_sheets,self.cn.page_sheet_local_to_bucket)
        self.data_config = config_data.get_data()

    def get_list_blobs(self,only_excel=False):
        list_blobs = []
        for VarFile in self.storage_client.list_blobs(self.name_bucket):
            name_file = VarFile.name
            if only_excel:
                if ".xlsx" in name_file or ".csv" in name_file:
                    list_blobs.append(name_file)
            else:
                list_blobs.append(name_file)
        return list_blobs
    
    def upload_files_bucket(self):
        try:
            index = 0
            for data_strct_key,row in self.data_config.items():
                
                index += 1

                tag_name = row["path_local"]
                path_data = row["path_bucket"]
                update_status = int(row["update_bucket"])

                if update_status == extra_v.STATUS_UPDATE["UPDATE"] or update_status == extra_v.STATUS_UPDATE["NO_LOAD"]:
                    continue

                upload = os.path.join(extra_v.PATH_UPLOAD_BUCKET, tag_name)
                bucket = self.storage_client.bucket(self.name_bucket)
                blob = bucket.blob(path_data+tag_name)
                blob.upload_from_filename(upload,timeout=300)

                print(f"[SUCCEFULL UPLOAD BUCKET] : Index: {index} // Name_Bucket: {self.name_bucket} // Db_Name: {tag_name} // Destination: {path_data}")

                self.spreadsheets.update_spreadsheets(self.cn.id_spread_sheets,self.cn.page_sheet_config_data,f"H{index+1}",str(datetime.now()))
                self.spreadsheets.update_spreadsheets(self.cn.id_spread_sheets,self.cn.page_sheet_config_data,f"F{index+1}",extra_v.STATUS_UPDATE["UPDATE"])

                

        except:
            tipo_excepcion, valor_excepcion, traceback = sys.exc_info()
            print("Tipo de excepción:", tipo_excepcion)
            print("Valor de excepción:", valor_excepcion)
            print("Traceback:", traceback)

