#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cxxfilt

print (' ----------------------------')
print (' \n Decoder of C++ symbols \n')
print (' \n Made by andrwgldmn \n') 
print (' ----------------------------')
		
symbol = raw_input(' Enter your symbol: ')
print(cxxfilt.demangle(symbol))
