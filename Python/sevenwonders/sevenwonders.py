''' Assignment: Seven Wonders
    Created on 20th of October 2016
    @author: Mylene Martodihardjo'''

sevenWondersCards       = raw_input()
numberOfTabletCards     = sevenWondersCards.count("T")
numberOfCompassCards    = sevenWondersCards.count("C")
numberOfGearCards       = sevenWondersCards.count("G")

minSetCards = min(numberOfTabletCards,
                  min(numberOfCompassCards,numberOfGearCards))
bonus = 7 * minSetCards
    
print(numberOfTabletCards**2 + numberOfCompassCards**2 + numberOfGearCards**2 + bonus)