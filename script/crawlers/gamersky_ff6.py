#! /usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# gamersky_ff6.py - 
#
# Created by skywind on 2024/05/26
# Last Modified: 2024/05/26 04:52:25
#
#======================================================================
import sys
import time

import crawler


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
def main ():
    url = 'http://www.gamersky.com/ent/202405/1481985.shtml'
    c = crawler.Crawler()
    c.fetch(url)
    print(c.title)
    print(c.content)
    return 0


#----------------------------------------------------------------------
# testing suit
#----------------------------------------------------------------------
if __name__ == '__main__':
    def test1():
        
        return 0
    test1()


