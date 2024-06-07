overall_max_life_expect = 0
overall_min_life_expect = 9999
overall_max_country = ''
overall_min_country = ''
overall_max_year = 0
overall_min_year = 0

# Represent index positions of data in the line
COUNTRY = 0
YEAR = 2
LIFE = 3

with open('life-expectancy.csv', 'r') as file:
    for line in file:
        data = line.split(",")
        print(data[COUNTRY])









# with open('life-expectancy.csv', 'r') as file:
#     next(file)
#     for line in file:
#         data = line.split(',')
#         country = data[0]
#         year = int(data[2])
#         life_expectancy = float(data[3])

#         if life_expectancy > overall_max_life_expect:
#             overall_max_life_expect = life_expectancy
#             overall_max_country = country
#             overall_max_year = year

#         if life_expectancy < overall_min_life_expect:
#             overall_min_life_expect = life_expectancy
#             overall_min_country = country
#             overall_min_year = year

# print(f'The overall max life expectancy is: {overall_max_life_expect} from {overall_max_country} in {overall_max_year}')
# print(f'The overall min life expectancy is: {overall_min_life_expect} from {overall_min_country} in {overall_min_year}')