''' Assignment: Pizza Crust
    Created on 17 april 2016
    @author: Mylene Martodihardjo'''

from decimal import Decimal

r, c = [Decimal(x) for x in raw_input().split(' ')]
cheeseProcent = (1 - ((r**2 - (r-c)**2)/r**2))*100
print "%.6f" % cheeseProcent