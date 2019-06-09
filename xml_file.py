#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
#  xml_file.py
#
#  Copyright 2019 Jo Hausmann <johannes.hausmann@stud.th-bingen.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from lxml import etree
import time
import os
import sys

########################################################################
# simple create function                                               #
# unique key for filename --> combination of name and insurance number #
# key should be unique --> needs testing                               #
########################################################################

def create(name, kknummer):
    gkey = generate_key(name,kknummer)
    root = etree.Element(gkey)
    my_tree = etree.ElementTree(root)
    write(my_tree,gkey)


########################################################################
# add function --> arguments data = dir(), key = name + insurance      #
# open file                                                            #
# create child nodes based on keys in parsed dictionary                #
########################################################################

def add(data,name,kknummer):
    gkey = generate_key(name,kknummer)
    try:
        tree= etree.parse(gkey + ".xml")#Parse an existing XML Sheet
        root = tree.getroot()
    except etree.XMLSyntaxError:
        print ("File doesn't have root node")
    except IOError:
        print("File doesn't exist in the directory")

    try:
        if isinstance(data, dict):
            for x,y in data.items():
                child = etree.SubElement(root, str(x),value=str(y))

            my_tree = etree.ElementTree(root)
            write(my_tree,gkey)
    except AttributeError:
        print("Data structure ist not a dict")


########################################################################
# get function --> returns a dictionary                                #
# dict is based on xml file                                            #
########################################################################

def get(name,kknummer):
    gkey = generate_key(name,kknummer)
    try:
        data = dict()
        tree= etree.parse(gkey + ".xml")
        root= tree.getroot()
        for child in root:
            x=str(child.tag)
            y=str(child.get("value"))
            data[x]=y
        return (data)

    except etree.XMLSyntaxError:
        print ("File doesn't have root node")
    except IOError:
        print("File doesn't exist in the directory")


#########################################################
# write function                                        #
# check whether given tree is instance of etree class   #
# write tree as xml file --> pretty_print               #
#########################################################

def write(my_tree,gkey):
	if isinstance(my_tree,etree._ElementTree):
		f = open(gkey + ".xml", "wb")
		f.write(etree.tostring(my_tree, pretty_print=True))
		f.close()
	else:
		os.error("Given argument is not object of class etree")
#########################################################
# key method                                            #
#########################################################

def generate_key(name, kknummer):
    return (name + "_" + kknummer)
