
#open the salmonella sequence
with open('data/salmonella_spi1_region.fna', 'r') as f:
    counter = 0

    #skip the first two lines of the file
    while counter < 2:
        f.readline()
        counter += 1
    f_list = f.readlines()
    print('In the with block, is the file closed?', f.closed)


print('Out of the with block, is the file closed?', f.closed)

#convert f_list from a list into a string
for line in range(len(f_list)):
    f_list[line] = f_list[line].rstrip()

f_str = ''.join(f_list)

print(f_str[:100])
