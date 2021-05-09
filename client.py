from socket import *
from hashlib import md5
import sys
from time import sleep
import json

host = '192.168.3.224'
port = 8000

def new():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))

def signin(id, password):
    new()
    lkdpsw = md5(password.encode('GBK')).hexdigest()
    msg = f'signin {id} {lkdpsw}'
    s.sendall(msg.encode())
    sleep(1)
    reply = s.recv(1024).decode()
    data = json.loads(reply)
    return data

def register(name, password):
    new()
    lkdpsw = md5(password.encode('GBK')).hexdigest()
    msg = f'register {name} {lkdpsw}'
    s.sendall(msg.encode())
    sleep(1)
    reply = s.recv(1024).decode()
    data = json.loads(reply)
    return data