#!/bin/sh

ARG=$1
PATH='/goinfre/igarbuz/miniconda3'


if [[ $# -eq 0 ]] || [ $ARG == 'help' ] || [ $ARG == 'h' ]
then
	echo 'install-python - to (re)install'
	exit 0
elif [ $ARG == 'install-python' ]
then
	if [ ! -d $PATH ]
	then
		rsync -avu /sgoinfre/goinfre/Perso/igarbuz/miniconda3 /goinfre/igarbuz
		echo 'Python has been installed.'
	else
		echo 'Python is already installed, do you want to reinstall it ?'
		read -p '[yes|no]> ' -n 1 -r
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			rm -rf $PATH
			echo 'Python has been removed.'
			rsync -av /sgoinfre/goinfre/Perso/igarbuz/miniconda3 /goinfre/igarbuz
			echo 'Python has been installed.'
		else
			echo '\nexit.'
		fi
	fi
else
	echo 'uncknown argument.'
	exit 0
fi
