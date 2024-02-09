#!/usr/bin/python3

"""
Learning about dictionaries in python
"""
#this indentation is conventional it makes your code readable
phone_no = {
    'lolo': 1234, 
    'sasa': 5678, 
    'mohan': 91011
    #Dublicate keys are not advisable/ allowed if duplicate keys are there
    #it will only take the last value
}

#method two of creating dicts
#student_n0=dict([
#    'lolo':3456
#    'georam': 8923
 #   'stacy': 8935
#])

#method 3 of creating dicts
#color_no=dict([('red': 6788), ('purple':8925),('pink':6712)])
#keys shoud be immutable but the values can be any type and is mutable
#nested dicts: a dict within a dict
print(phone_no['mohan'])
phone_no['martha'] = {222, 1111, 4444}
phone_no['stephen'] = {'stephanie': 3333, 'silvia': 8888}
#accessing using get methods
#print(phone_no.get('martha'))
del phone_no('lolo')