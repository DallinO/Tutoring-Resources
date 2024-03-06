# life_expectancies = []
# count = 0

# max = -1
# min = 99999
# country_max = ''
# country_min = ''
# year_max = 0
# year_min = 0

# year_of_interest = int(input("Enter the year of interest: "))
# print()
# with open('life-expectancy.csv') as dataset:
#     next(dataset)
#     for line in dataset:
#         data = line.split()
#         country = int(line[0])
#         year = int(line[1])
#         life_expectancies = int(line[3])

#         if life_expectancies > max:
#             max > life_expectancies
#             country_max > country
#             year_max > year
#         if life_expectancies < min:
#             min > life_expectancies
#             country_min > country
#             year_min > year
            
# Initialize variables
overall_max_life_expect = float(-1)
overall_min_life_expect = float(9999999)
overall_max_country = ""
overall_min_country = ""
overall_max_year = ""
overall_min_year = ""

target_year_max_life = float(-1)
target_year_min_life = float(9999999)
target_year_max_country = ""
target_year_min_country = ""
target_year_avg = 0
target_year = 0
sum_life_expectancy = 0
total_countries = 0

# Read data from a CSV file (assuming 'life-expectancy.csv' exists in the same directory)
target_year = int(input('Enter the year of interest: '))
with open("life-expectancy.csv") as dataset:
    next(dataset)
    for line in dataset:
        data = line.split(',')
        country = data[0]
        year = int(data[2]) 
        life_expectancy = float(data[3])

        # Update overall max and min life expectancy
        if life_expectancy > overall_max_life_expect:
            overall_max_life_expect = life_expectancy
            overall_max_country = country
            overall_max_year = year

        if life_expectancy < overall_min_life_expect:
            overall_min_life_expect = life_expectancy
            overall_min_country = country
            overall_min_year = year

        # Update target year max and min life expectancy
        if year == target_year:
            if life_expectancy > target_year_max_life:
                target_year_max_life = life_expectancy
                target_year_max_country = country

            if life_expectancy < target_year_min_life:
                target_year_min_life = life_expectancy
                target_year_min_country = country

            sum_life_expectancy += life_expectancy
            total_countries += 1

# Calculate average life expectancy for the target year
if total_countries > 0:
    target_year_avg = sum_life_expectancy / total_countries

# Print the results
print(f"The overall max life expectancy is: {overall_max_life_expect:.2f} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min_life_expect:.2f} from {overall_min_country} in {overall_min_year}")
print(f"For the year {target_year}:")
print(f"The average life expectancy across all countries was: {target_year_avg:.2f}")
print(f"The max life expectancy was in {target_year_max_country} with {target_year_max_life:.2f}")
print(f"The min life expectancy was in {target_year_min_country} with {target_year_min_life:.2f}")

      

