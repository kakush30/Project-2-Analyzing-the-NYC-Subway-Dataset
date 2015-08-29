def create_master_turnstile_file(filenames, output_file):
    '''
    takes the files in the list filenames and consolidates them into one file
    located at output_file.
    '''
    
   
    header_string = 'C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n'
    with open(output_file, 'w') as master_file:
        master_file.write(header_string)
        for filename in filenames:
            with open('s.txt', 'r') as input_file:
                for line in input_file:
                    if line.strip() == header_string:
                        pass
                    else:
                        master_file.write(line)

if __name__ == '__main__':
    
    create_master_turnstile_file('s.txt','turnstile_data.csv') 