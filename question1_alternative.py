def get_max_profit(numbers):
    # find also the index_max and index_min
    max_profit, current_min_value, index_max, index_min, list_index_min = 0, numbers[0], len(numbers), 0, []
    for i, price in enumerate(numbers[1:]):
        if current_min_value > price:
            current_min_value = price
            list_index_min.append(i)
        
        profit = price - current_min_value 

        if max_profit < profit:
            max_profit = profit
            index_max = i+1   
    
    for index in list_index_min:
        if index < index_max:
            index_min = index+1
            
    return max_profit, index_max, index_min


# get data from txt
numbers = []
with open('gistfile1.txt') as fp:
    for line in fp:
        numbers.extend(  # append the list of numbers to the result array
            [int(item)  # convert each number to an integer
             for item in line.split()  # split each line of whitespace
             ])

# list of possible testcase
# numbers = [5,4,3,2,1]
# numbers = [3,2,1,5,6,4]
# numbers = [3,2,1,5,6,6,4] # duplicate max value
# numbers = [5,5,5,5,5,5] # all are max value
# numbers = [8,9,2,5,4,7] # best profit is after the max value
max_profit, index_max, index_min = get_max_profit(numbers)

print("the maximum profit Jacky can make is: $" + str(max_profit) 
        + ", he will buy at hour " + str(index_min+1) + " and sell at hour " + str(index_max+1))

print(numbers[11788], numbers[19089])