import subprocess

# Specify the full path to the MATLAB executable
# For me (Matteo Gristina, RedID: 825988404, this needed to include the .exe
matlab_executable = "C:/Program Files/MATLAB/R2023b/bin/matlab.exe"

# Set up MATLAB environment
#https://stackoverflow.com/a/6717782
# After reading this stakcoverflow, I derived this command which worked on my machine when I pasted into cmd.
#"C:/Program Files/MATLAB/R2023b/bin/matlab.exe" -nosplash -nodesktop -r  "run('task4.m'); exit;"

#https://stackoverflow.com/a/69411199
#CHANGELOG
#   -use -batch instead of other launch options
#   - use subprocess run instead of open

matlab_process = subprocess.run([matlab_executable, "-batch", "run('task4.m'); pause(2);"], capture_output=True) 


with open('input.txt', 'r') as file:
    line = file.readline()
    int_array = [int(value) for value in line.split()]
    
input_array = list(map(str, int_array))


### START OF C CODE ###
### START OF C CODE ###
### START OF C CODE ###


#https://stackoverflow.com/a/2381726
# This maximum argument size led me to partition the original array, into sizes that cmd could run

#size of partition
n = 256
#sum for debug
sum = 0

partition_list = [input_array[i:i + n] for i in range(0, len(input_array), n)]

#print(input_array)

with open('c_output.txt', 'w') as f:
        f.write('')

# Compile the C program (assuming it's saved as task1.c)
subprocess.run(["gcc", "task1.c", "-o", "task1"])

for i in partition_list:
    sum = sum + len(i)
    # Run the compiled C program with the PARTITIONED input array as arguments
    process = subprocess.run(["./task1"] + i, capture_output=True, text=True)
    
    # Store the output of the C program in a Python variable
    output_variable = process.stdout.strip()
    
    # Save the output_variable to a file
    
    with open('c_output.txt', 'a') as f:
        f.write(' ')
        f.write(output_variable)


### START OF HASKELL CODE ###
### START OF HASKELL CODE ###
### START OF HASKELL CODE ###

subprocess.run(['ghc', 'task2.hs'])

with open('haskell_output.txt', 'w') as f:
        f.write('')

for i in partition_list:
    sum = sum + len(i)
    # Run the compiled C program with the PARTITIONED input array as arguments
    process = subprocess.run(["./task2"] + i, capture_output=True, text=True)
    
    # Store the output of the C program in a Python variable
    output_variable = process.stdout.strip()
    
    # Save the output_variable to a file
    
    with open('haskell_output.txt', 'a') as f:
        f.write(' ')
        f.write(output_variable)


### START OF PROLOG CODE ###
### START OF PROLOG CODE ###
### START OF PROLOG CODE ###

input_quotes = []
for i in input_array:
### https://stackoverflow.com/a/58957893 ###
    input_quotes.append(f"\"{i.rstrip()}\"")

#a = '255'
#b = f"\"{a.rstrip()}\""

with open('prolog_output.txt', 'w') as f:
        f.write('')

partition_list_prolog = [input_quotes[i:i + n] for i in range(0, len(input_quotes), n)]

for i in partition_list_prolog:

    prolog_input = "[" + ",".join(map(str, i)) + "]."
    prolog = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'task3.pl'], input=prolog_input, capture_output=True, text=True)

    plresult = prolog.stdout.strip()
    
    
    ## REPLACE UNWANTED CHARS https://www.geeksforgeeks.org/python-string-replace/
    temp = plresult.replace("]", "")
    no_bracket = temp.replace("[", "")
    prolog_output = no_bracket.replace(",", " ")
    
    with open('prolog_output.txt', 'a') as f:
        f.write(' ')
        f.write(prolog_output)
        
#https://stackoverflow.com/a/69411199


matlab_process = subprocess.run([matlab_executable, "-batch", "run('task5.m'); pause(10);"], capture_output=True)