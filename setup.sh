#!/bin/sh
##############################
# OpenMDQ setup script       #
# checks for dependencies etc#
##############################

# os name for user
os="$(. /etc/os-release | grep PRETTY_NAME | cut -d "=" -f 2)"

######################
# simple about dialog#
######################
about(){
dialog  --msgbox "OpenMDQ install shell script. \n \
# OpenMDQ - Small shell script (sh) for installing MDQ \n \
# Copyright (C) 2019 Luis Kress, Sarah Kreutzke, Fabian Krill, Johannes Hausmann \n \
# \n \
# This program is free software; you can redistribute it and/or modify \n \
# it under the terms of the GNU General Public License as published by \n \
# the Free Software Foundation; either version 3 of the License, or \n \
# (at your option) any later version. \n \
# \n \
# This program is distributed in the hope that it will be useful, \n \
# but WITHOUT ANY WARRANTY; without even the implied warranty of \n \
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the \n \
# GNU General Public License for more details. \n \
# \n \
# You should have received a copy of the GNU General Public License along \n \
# with this program; if not, write to the Free Software Foundation, Inc., \n \
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. \n \
# \n \
\n \
\
2019 Johannes Hausmann <johannes.hausmann@stud.th-bingen.de>" 40 100
}
#

##################################
# install → set up dirs & flask  #
##################################

installmdq(){
workdir="${HOME}/bin"

pip3 install -q -U --user flask

[ ! -d "$workdir" ] && mkdir -p "$workdir"

cd "$workdir" || exit 1

git clone https://github.com/jack-the-dvdripper/MedizinischeInformatik.git > /dev/null

ln -s MedizinischeInformatik/flaskMain.py main.py 

nohup python3 main.py &

dialog --msgbox "OpenMDQ successfully installed and started. Check localhost:5000" 10 20


}

###################################################
#remove function → removes dirs and python modules#
###################################################

removemdq(){

[ ! -d "$workdir" ] && mkdir -p "$workdir"

cd "$workdir" || exit 1

rm -r MedizinischeInformatik

pip3 uninstall -q flask

dialog --msgbox "Removed OpenMDQ and the python dependencies from your system" 10 20

}

###########################################
# script needs dialog for user interaction#
###########################################

! command -v dialog && echo "Install dialog to use script" && exit 1

#dependencies
deps=("python3" "git" "nano" "pip3")
pythondeps="flask"




if ! command -v "${deps[@]}" > /dev/null; then
	dialog --title "Dependencie error" --msgbox "Please install  dependencies from requirements.txt \
			 You should check with you distrobution $os package manager" 20 30
	exit 1
else
	choice=`dialog --menu "OpenMDQ setup script" 0 0 0 \
               "Install" "Install MDQ from git" "Remove" "Remove MDQ from your system" \
               "About" "" 3>&1 1>&2 2>&3`

	case $choice in
		"Install") installmdq;;
		"Remove") removemdq;;
		"About") about;;
	esac
fi



