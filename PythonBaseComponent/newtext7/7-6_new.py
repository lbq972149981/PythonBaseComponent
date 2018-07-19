# -*- coding: utf-8 -*-                                                                            #0
"""                                                                                                #1
Created on Thu Oct 26 22:11:41 2017                                                                #2
                                                                                                   #3
@author: Administrator                                                                             #4
"""                                                                                                #5
                                                                                                   #6
filename = '7-6.py'                                                                                #7
with open(filename,'r') as fp:                                                                     #8
    lines = fp.readlines()                                                                         #9
lines = [line.rstrip() + ' '*(100-len(line)) + '#' + str(index) + '\n' for index,line in enumerate(lines)]#10
with open(filename[:-3] + '_new.py','w') as fp:                                                    #11
    fp.writelines(lines)                                                                           #12
