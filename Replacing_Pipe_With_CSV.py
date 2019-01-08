
def pipe_to_CSV (source,dest):
    import csv
    #filename = 'Cars_Original.csv'
    #filename1 = 'Cars.csv'

    with open(source,'r+') as file:
        reader = csv.reader(file)
        lines = file.readlines()
        print(lines)
        for line in lines:
            line=line.replace('|',',')
            print(line)
            with open(dest,'a')as file1:
                file1.writelines(line)


pipe_to_CSV('Cars_Original.csv','Cars.csv')