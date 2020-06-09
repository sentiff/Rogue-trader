# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 08:30:47 2020

@author: Marcin
"""

#proponowane klasy obiektów

class phenomena:
    kind = ''               #what kind of phenomena (solar flares, radiation burst etc)
    description = ''

class gas_giant:
    size = ''               #captain obvious
    moons = 0               #satellites - natural and artificial
    anomaly = False         #stellaris anomaly
    
class cloud:
    composition = ''
    resource = ''
    ammount = 0
    
class lesser_body:          #asteroidy,pola asteroid, mniejsze księżyce etc
    bodytype = ''           #asteroida / pas /etc
    composition = ''        #ice / carbon / rocky / crystalline
    resource1 = ''           #resource - RT book
    resource2 = ''
    ammount1 = 0             #ammount
    ammount2 = 0
    anomaly = False         #stellaris anomaly
        
class barren:               #lifeless planet
    bodytype = ''           #body type from RT (small & dense, etc)               
    gravity = ''            #gravity - warhammer standards (lower/ normal / higher)
    gs = 1                  #number of Gs 
    resource1 = ''
    resource2 = ''
    ammount1 = 0
    ammount2 = 0
    anomaly = False
    
class livingplanet:
    bodytype = ''
    gravity =''
    gs = 1
    resource1 = ''
    resource2 = ''
    resource3 = ''
    ammount1 = 0
    amomunt2 = 0
    ammount3 = 0
    anomaly = False
    
class strashipgraveyard:
    origin = ''
    ships = 0
    xenotech = 0            #ammount of xeno resources
    archeotech = 0          #archeo reseources

class hull:                 #hulls for graveyard
    faction = ''
    hullclass = ''
    condition = ''
    
class station:
    faction = ''
    role = ''               #observation, reaserch, military,fortress
    condition = ''
    xenotech = ''
    archeotech = ''

    