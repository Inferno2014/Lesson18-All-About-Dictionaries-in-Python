dict1 = {'india' : '0091', 'australia' : '0025', 'nepal' : '00977'}
country = input('For which country do you want the pin-code?: ').lower()
print(dict1.get(country,'Country not found!'))