#!/usr/bin/env python3

# Aries - March 21 to April 19
# Taurus - April 20 - May 20
# Gemini - May 21 - June 21
# Cancer - June 21 - July 22
# Leo - July 23 -August 22
# Virgo - August 23 - September 22
# Libra - September 23 - October 22
# Scorpio - October 23 - November 21
# Sagittarius - November 22 - December 21
# Capricorn - December 22 - January 19
# Aquarius - January 20 - February 18
# Pisces - February 19- March 20
import datetime
from pyhoroscope import Horoscope

def check_zodiac(zodiac, birthday, name):
    """Prints Zodiac Signs"""
    zodiac_sign = 'not recognized'
    for sign in zodiac:
        if zodiac[sign][0] <= birthday <= zodiac[sign][1]: 
            zodiac_sign = sign
    # Display the result.
    print('{0} Your Zodiac Sign is {1}.'.format(name,zodiac_sign))
    return(zodiac_sign)

zodiac = {
    'Capricorn' : (12.22, 01.19),
    'Aquarius' : (01.20, 02.18),
    'Pisces' : (02.19, 03.20),
    'Aries' : (03.21, 04.19),
    'Taurus' : (04.20, 05.20),
    'Gemini' : (05.21, 06.21),
    'Cancer' : (06.22, 07.22),
    'Leo' : (07.23, 08.22),
    'Virgo' : (08.23, 09.22),
    'Libra' : (09.23, 10.22),
    'Scorpio' : (10.23, 11.21),
    'Sagitarius' : (11.22, 12.21) 
    }
        
# Ask for the name
name = input('What is your name? ')

# Ask for the birth date.
birthday = float(input('What is your Birthday? (MM.DD) '))

# Run function to check the date
zodiac_sign = check_zodiac(zodiac, birthday, name)

#your_horoscope = Horoscope.get_todays_horoscope(zodiac_sign)
#print(your_horoscope)
