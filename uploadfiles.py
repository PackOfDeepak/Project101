
import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files, in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode("overwrite"))

def main():
    access_token = "EypI8EBAZeMAAAAAAAAAASPGT8tPXA2aPrrGh4Q7oJx-b4SvOClDy8heZvp3We4a"
    transferData = TransferData(access_token)

    file_from = input("Enter file to to transfer : ")
    file_to = input("Enter the full path to upload the file to, includint the file name: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()