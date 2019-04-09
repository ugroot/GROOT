import logging

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

def driveAuthorization():
    """Authorizes access to the Google Drive"""
    
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    drive = GoogleDrive(gauth)
    return drive

def getGrootFolderId(drive):
    """Shows the Folder Id of Groot Folder in your Google Drive"""

    fileFolderList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for GrootFolder in fileFolderList:
        if GrootFolder['title'] == 'Groot':       
            print ('title: %s, id: %s' % (GrootFolder['title'], GrootFolder['id']))
            return GrootFolder['id']

def getFileList(drive):
    """Gives the file list inside of the Groot Folder"""
    
    file_list = drive.ListFile({'q': "'11--DsLz-mGaNvL0nOzhUeQ7RmMcV-BZC' in parents and trashed=false"}).GetList()
    filedict = {}
    for file1 in file_list:
        #print ('title: %s, id: %s' % (file1['title'], file1['id']))
        filedict[file1['title']]= file1['id']
    return filedict

def createFile(filename,fileContent):
    """Creates file in the Groot Directory:
    fileName: "Name of the file(.txt added later)" 
    fileContent = "Content of file"
    """
    drive = driveAuthorization()
    fid = getGrootFolderId(drive)
    fileList = getFileList(drive)
    if fid:
        print("Groot Folder Found and Fid Created")
    else:
        return "Fid not found please create folder named Groot in your Google Drive"

    title = str(filename)+".txt"

    if title in fileList.keys():
        return "Name Already Exists Please Choose Another Name"
    
    f = drive.CreateFile({"title" : title ,"parents": [{"kind": "Groot/", "id": fid}]})
    f.SetContentString(fileContent)
    f.Upload()
    return "Successful"


def getGrootFolderContent():
    drive = driveAuthorization()
    f = getFileList(drive)
    fileDict = {}
    for key,value in f.items():
        file1 = drive.CreateFile({'id': value})
        content = file1.GetContentString()
        fileDict[key] = content
    
    return fileDict
        

val = getGrootFolderContent()
print(val)