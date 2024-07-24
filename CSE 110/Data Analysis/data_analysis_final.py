overall_max_life_expect = 0
overall_min_life_expect = 9999
overall_max_country = ''
overall_min_country = ''
overall_max_year = 0
overall_min_year = 0

target_year_max_life = 0
target_year_min_life = 9999
target_year_max_country = ''
target_year_min_country = ''
target_year_avg = 0
sum = 0
total = 0

target_year = int(input('Enter the year of interest: '))
with open('life-expectancy.csv', 'r') as file:
    next(file)
    for line in file:
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        life_expectancy = float(data[3])

        if life_expectancy > overall_max_life_expect:
            overall_max_life_expect = life_expectancy
            overall_max_country = country
            overall_max_year = year

        if life_expectancy < overall_min_life_expect:
            overall_min_life_expect = life_expectancy
            overall_min_country = country
            overall_min_year = year

        if year == target_year:
            if life_expectancy > target_year_max_life:
                target_year_max_life = life_expectancy
                target_year_max_country = country

            if life_expectancy < target_year_min_life:
                target_year_min_life = life_expectancy
                target_year_min_country = country

            sum += life_expectancy
            total += 1
target_year_avg = sum / total

print(f'\nThe overall max life expectancy is: {overall_max_life_expect} from {overall_max_country} in {overall_max_year}')
print(f'The overall min life expectancy is: {overall_min_life_expect} from {overall_min_country} in {overall_min_year}')
print(f'\nFor the year {target_year}:')
print(f'The average life expectancy across all countries was {target_year_avg}')
print(f'The max life expectancy was in {target_year_max_country} with {target_year_max_life}')
print(f'The max life expectancy was in {target_year_min_country} with {target_year_min_life}')