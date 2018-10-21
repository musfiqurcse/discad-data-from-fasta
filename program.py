# Discard Protein Sequence below 100
"""


"""

handle = open('input.fasta','r')
write_file = open('output.fasta','w+')
test_begin = False
test_close = False
output  = ""
main_content = ""
final_value = ""
for value in handle:
    if ">gi" in value:
        if test_begin == True:
            test_begin = True
            test_close = False
            main_content = main_content.replace(' ',"").replace('\n','')
            if len(main_content) > 99:
                #print(main_content)
                write_file.write(output[:])
                write_file.write(main_content[:])
                write_file.write('\n')
                # write_file.write('Total Character:  {0}'.format(str(len(main_content))))
                write_file.write('\n')
                #print(main_data)
            output = value
            main_content = ""
            # print(value)
        else:
            test_begin = True
            output = value
    else:
        main_content += str(value)
main_content = main_content.replace(' ',"").replace('\n','')
if len(main_content) > 99:
    write_file.write(output[:])
    write_file.write(main_content[:])
    write_file.write('\n')
    # write_file.write('Total Character:  {0}'.format(str(len(main_content))))
    # write_file.write('\n')
handle.close()
write_file.close()
