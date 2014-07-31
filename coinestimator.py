# intro to coin estimater
# function to weigh coins, also asks what type of coin, gives total,
# and wrappers needed
# Ask is more coins to weigh, if yes run function again,
# append to dictionary, if no give totals for all and exit. While loop.
# functions to call for each coin type, have it round up to
# the nearest integer

#possibly write to tell estimate of how much money you have?

# pennies  w: 2.5g   #/wrapper: 50
# nickels w:  5g  #/wrapper: 40
# dimes w:   2.268g #/wrapper: 50
# quarters w:  5.67g  #/wrapper: 40
# half-dollar w: 11.340g  #/wrapper: 20


from decimal import Decimal, ROUND_DOWN
more_coins = True
coin_types = {}
print("Welcome to the coin estimater.")

coin_list = []

class coin(object):

    def __init__(self, coin_type, weight, wrapper, coin_type_weight, value):
        self.coin_type = coin_type
        self.weight = weight
        self.wrapper = wrapper
        self.coin_type_weight = coin_type_weight
        self.value = value
        self.coin_type_wrappers = 0

    def total_number_coins(self):
        tnc = int(self.coin_type_weight / self.weight)
        return tnc
        
    def wrappers_needed(self):
        wn = int(self.total_number_coins() / self.wrapper)
        return wn

    def total_value(self):
         tv = Decimal(self.total_number_coins() * self.value).quantize(Decimal('.01'), rounding=ROUND_DOWN)
         return tv

    def results(self):
        self.coin_type_wrappers = self.wrappers_needed()
        print("Based on the weight of your coins, you have " + 
            str(self.total_number_coins()) + " coins. You would need " + 
            str(self.wrappers_needed()) + " wrappers, and would end up with $"
            + str(self.total_value()) + ".")


def ask_coins():
    ask_coin_input = raw_input("Do you have a weight of coins you would \
    like to get an estimate of? y or n? ")
    if ask_coin_input.lower() == "y":
        ask_type = raw_input("What type of coin would you \
            like to estimate? I can estimate pennies, nickels, \
            dimes, quarters, or half dollars. > ")
        if ask_type.lower() == "pennies" or ask_type.lower() == "penny":
            num = raw_input('How much do your pennies weigh?')
            penny = coin('penny', Decimal(2.5), 50, Decimal(num), Decimal(.01))
            coin_types["penny"] = penny
            coin_list.append(int(penny.total_value()))
            penny.results()
        elif ask_type.lower() == "nickels" or ask_type.lower() == "nickel":
            num = raw_input('How much do your nickels weigh?')
            nickel = coin('nickel', Decimal(5), 40, Decimal(num), Decimal(.05))
            coin_types["nickel"] = nickel
            coin_list.append(int(nickel.total_value()))
            nickel.results()
        elif ask_type.lower() == "dimes" or ask_type.lower() == "dime":
            num = raw_input('How much do your dimes weigh?')
            dime = coin('dime', Decimal(2.268), 40, Decimal(num), Decimal(.1))
            coin_types["dime"] = dime
            coin_list.append(int(dime.total_value()))
            dime.results()
        elif ask_type.lower() == "quarters" or ask_type.lower() == "quarter":
            num = raw_input('How much do your quarters weigh?')
            quarter = coin('quarter', Decimal(5.67), 40, Decimal(num), Decimal(.25))
            coin_types["quarter"] = quarter
            coin_list.append(int(quarter.total_value()))
            quarter.results()
        elif ask_type.lower() == "half dollars" or ask_type.lower() == "half dollar":
            num = raw_input('How much do your half dollars weigh?')
            half_dollar = coin('half_dollar', Decimal(11.340), 20, Decimal(num), Decimal(.5))
            coin_types["half dollar"] = half_dollar
            coin_list.append(int(half_dollar.total_value()))
            half_dollar.results()
        else:
            print('I do not know how to evaluate that type of coin.')
            ask_type
    else:
        print("You have $") + str(sum(coin_list)) + (".")

        for i in coin_types:
            print("You will need " + str(coin_types[i].coin_type_wrappers) + 
                " " + i + " wrappers.")

        print('Thank-you for using the coin estimater!')

        global more_coins
        more_coins = False


while more_coins is True:
    ask_coins()
    
