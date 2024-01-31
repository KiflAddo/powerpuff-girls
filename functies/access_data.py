
def access_data(file_name):
    '''
    Function that opens a csv and reads the data into python
    '''

    data = []

    # open the file
    file = open(f'{file_name}', 'r')

    #remove the \n in every line
    true_file = (line.replace('\n', '') for line in file)

    #skip the first line
    for i in range(1):
        next(true_file)

    for line in true_file:
        data.append(line)

    return data
