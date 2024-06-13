# Script to read a text file containing words, 
# clean and print them, 
# and finally save them into an output file

filename = 'tags-orderer/tags.txt'
output_filename = 'tags-orderer/tags-output.txt'
separator = ';'

with open(filename, 'r') as file:
    tags = list(set(file.read().split(separator)))

tags = [tag.lower() for tag in tags]
tags.sort()

tags_final = [tag.replace('-', ' ').title() for tag in tags if tag != '']

for tag in tags_final:
    print(tag)

tags_output = [tag.lower().replace(' ', '-') for tag in tags_final]

with open(output_filename, 'w') as file:
    file.write(';'.join(tags_output))
