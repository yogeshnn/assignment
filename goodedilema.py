def minimumdifference(arr, z):

    # result=maximum value
    result = float('inf')

    # Length of the array
    n = len(arr)
    minIndex = 0
    
    # Sort the array
    arr.sort()
    
    # Find the minimum difference between the first and last element
    for i in range(n - z + 1):
        if (arr[i+z-1] - arr[i]) < result:
            result = arr[i+z-1] - arr[i]
            minIndex = i
  
    return result, minIndex

if __name__ == '__main__':
    price = dict()

    # Open the input file
    with open('sample_input1.txt', 'r') as f:

        # Number of employees be z
        z = int(f.readline().split(':')[1])

        # Store the price of goodies in a dictionary
        for line in f.readlines()[3:]:
            price[str(line.split(':')[0])] = int(line.split(':')[1])
    
    # Sort the dictionary
    price = dict(sorted(price.items(), key=lambda item: item[1]))
    
    # Get the result
    result, index = minimumdifference(list(price.values()), z)

    # Write the result to the output file and save it
    with open("output1.txt", 'w', encoding = 'utf-8') as f:
        f.write("The goodies selected for distribution are:\n\n")

        for i in range(z):
            f.write(list(price.keys())[index+i] + ": ")
            f.write(str(price[list(price.keys())[index+i]]) + "\n")
    
        f.write("\n The difference between the chosen goodie with highest price and the lowest price is " + str(result))
