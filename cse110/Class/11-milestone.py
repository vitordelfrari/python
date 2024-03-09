interest = input("Enter the year of interest: ")
country = input("Enter the country of interest: ")

with open("life-expectancy.csv") as info:

    avr = []
    avr2 = []

    max_year = ""
    max_entity = ""
    max_expectancy = -1

    min_year = ""
    min_entity = ""
    min_expectancy = 9999

    int_max_year = ""
    int_max_entity = ""
    int_max_expectancy = -1

    int_min_year = ""
    int_min_entity = ""
    int_min_expectancy = 9999

    con_max_year = ""
    con_max_entity = ""
    con_max_expectancy = -1

    con_min_year = ""
    con_min_entity = ""
    con_min_expectancy = 9999


    for line in info:
        clean_line = line.strip()
        data = clean_line.split(",")

        entity = data[0]
        code = data[1]
        year = data[2]
        expectancy = float(data[3])

        if expectancy > max_expectancy:
            max_year = year
            max_entity = entity
            max_expectancy = expectancy

        if expectancy < min_expectancy:
            min_year = year
            min_entity = entity
            min_expectancy = expectancy

        if year == interest:
                avr.append(expectancy)

                if expectancy > int_max_expectancy:
                    int_max_year = year
                    int_max_entity = entity
                    int_max_expectancy = expectancy

                if expectancy < int_min_expectancy:
                    int_min_year = year
                    int_min_entity = entity
                    int_min_expectancy = expectancy

        if entity.lower() == country.lower():
                avr2.append(expectancy)

                if expectancy > con_max_expectancy:
                    con_max_year = year
                    con_max_entity = entity
                    con_max_expectancy = expectancy

                if expectancy < int_min_expectancy:
                    con_min_year = year
                    con_min_entity = entity
                    con_min_expectancy = expectancy

    print(f'The overall max life expectancy is {max_expectancy} from {max_entity} in {max_year}') 
    print(f'The overall max life expectancy is {min_expectancy} from {min_entity} in {min_year}')
    print("")
    print(f"The average life expectancy across all countries was", "{:.3f}".format(sum(avr)/len(avr)))
    print(f"The max life expectancy was in {int_max_entity} with {int_max_expectancy}")
    print(f"The min life expectancy was in {int_min_entity} with {int_min_expectancy}")
    print("")
    print(f"The average life expectancy across {con_max_entity} was", "{:.3f}".format(sum(avr2)/len(avr2)))
    print(f"The max life expectancy in {con_max_entity} was {con_max_expectancy}")
    print(f"The min life expectancy in {con_min_entity} was {con_min_expectancy}")
