country = input().split(', ')
city = input().split(', ')
# country_dict = {country[index]: city[index] for index in range(len(country))}
country_dict = dict(zip(country, city))
for country, capital in country_dict.items():
    print(f"{country} -> {capital}")
