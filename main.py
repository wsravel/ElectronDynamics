import requests
import base64
import json
import uuid
import datetime
import os

ext = ""

#從文件夾下,讀取文件
def read_dir():
    global ext
    path = "C:\Users\yu.tien\Projects\宇庭練習\ElectronDynamics" #指定的文件夾目錄
    files = os.listdir(path) #得到文件下的所有文件名稱
    
    for file in files:    #歷變
        