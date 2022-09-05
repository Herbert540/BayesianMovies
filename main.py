import csv


def read_breed_data(path_to_csv):
    '''
    Open a CSV file at the given path, read in the lines, and return a list of lists
    representing a

        Parameters:
            path_to_csv (str): a relative path to the breed information csv file
        Returns:
            (list): a list of lists of str [["Affenpinscher","","Toy"], ...[more breed data]]
    '''

    file = open(path_to_csv)
    reader = csv.reader(file, delimiter=',')

    return list(reader)

path_to_breed_characteristics = "IMDB Dataset.csv"

breeds = read_breed_data(path_to_breed_characteristics)

count = 0
for ii in breeds:
    count+=1

print(count)