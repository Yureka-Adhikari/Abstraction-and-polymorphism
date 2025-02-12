class Nepal:
    def capital(self):
        print("The capital of Nepal is Kathmandu")
    
    def language(self):
        print("The official languages of Nepal are English and Nepali")
        
    def type(self):
        print("Nepal is a developing country")

class USA:
    def capital(self):
        print("The capital of USA is Washington D.C")
    
    def language(self):
        print("The most widely spread language is English")
        
    def type(self):
        print("USA is a developed country")
        
nep= Nepal()
us = USA()

for country in (nep, us):
    country.capital()
    country.language()
    country.type()
    print()