#!/usr/bin/env python3

# import only what we need
from platform import linux_distribution
from os import geteuid,system,remove
from sys import exit
from shutil import rmtree
from os.path import realpath
#from os.path import exists

# initial distro check
if linux_distribution()[0] != 'debian':
	print ('This installer only works on Debian')
	exit ()

# initial
if geteuid() != 0:
	print ('Only for root')
	exit ()

# update system first
#system('apt-get -qq update')

if system('systemctl get-default >/dev/null') != 'multi-user.target':
	system('systemctl set-default multi-user.target')

#trgt = '/lib/systemd/system/multi-user.target'
#if realpath('/etc/systemd/system/default.target') != trgt:
#	system('systemctl set-default multi-user.target')

# delete useless folders if exists
try:
	rmtree('/var/log/puppetlabs/')
except OSError:
	pass

# delete useless files if exists
try:
	remove('/var/log/alternatives.log')
	remove('/var/log/bootstrap.log')
except OSError:
        pass
