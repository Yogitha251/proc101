import dropbox 
import os
from dropbox.files import WriteMode

class transferdata :
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfile (self,file_from,file_to) :
        db=dropbox.Dropbox(self.accesstoken)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    db.files_upload(f.read,dropbox_path,mode=WriteMode('overwrite'))


def main():
    token='sl.BHDU99ajC8GCGGZE3Fvz3Ck-B6AQeya_VJxq2hJlVsV16mhXxS87zgb7s5DTn82vVhUMbWgec45cSXRFnXBO4TJrRc1ldxAluathZvv8DF2R0pCxM0YTXeuCPNzZOm_JMJiZJe-EjJk0'
    tran=transferdata(token)
    file_from=input('enter the file to be transfered')
    file_to=input('enter the path where you want to transfer')
    tran.uploadfile(file_from,file_to)
    print('file has been moved!')
    
main()