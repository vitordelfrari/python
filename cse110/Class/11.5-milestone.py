with open("life-expectancy.csv") as info:

    output = []

    for line in info:
        clean_line = line.strip()
        data = clean_line.split(",")

        entity = data[0]
        code = data[1]
        year = data[2]
        expectancy = float(data[3])
      
        ## Append to the list
        output.append([entity, code, year, expectancy])

max_life = max(output, key=lambda x: x[3])
min_life = min(output, key=lambda x: x[3])

print(f'The overall max life expectancy is {max_life[3]} from {max_life[0]} in {max_life[2]}')    
print(f'The overall min life expectancy is {min_life[3]} from {min_life[0]} in {min_life[2]}')
