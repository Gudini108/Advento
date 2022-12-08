import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    files_and_directories = f.read().split('\n')
    

filesystem_copy = files_and_directories.copy()

system_dict = {}

system_path_checker = ['/']


for file in filesystem_copy:
    
    file = file.split(' ')
    
    last_dir = system_path_checker[-1]
    
    if file[1] == 'cd':
        directory = file[2]
        
        if directory == '..':
            system_path_checker.pop()
            continue
        
        elif directory == '/':
            system_dict[directory] = {'subdirs': [], 'filesize': 0, 'dirsize': 0}
            continue
        
        else: # if we have cd with a name
            system_path_checker.append(directory)
            pathway = '-'.join(system_path_checker)
            system_dict[pathway] = {'subdirs': [], 'filesize': 0, 'dirsize': 0}
        continue
            
    
    if file[1] == 'ls':
        continue
    
    if file[0] == 'dir':
        pathway = '-'.join(system_path_checker)
        system_dict[pathway]['subdirs'].append(pathway + '-' + file[1])
        continue
        
    if int(file[0]):
        pathway = '-'.join(system_path_checker)
        system_dict[pathway]['filesize'] += int(file[0])
        system_dict[pathway]['dirsize'] += int(file[0])
        continue
            


def weight_calcualte(key):
    directory = system_dict[key] # system_dict = {key: {subdirs: [], filesize: 0, dirsize: 0}}
    subdir = directory['subdirs']
    filesize = directory['filesize']
    
    if len(subdir) == 0:
        return filesize
    
    else:
        directory_weight = filesize
        
        for dir in subdir:
            directory_weight += weight_calcualte(dir)
    
    return directory_weight


counter = 0
dir_to_del = []
for key in system_dict:
    system_dict[key]['dirsize'] = weight_calcualte(key)

    if system_dict[key]['dirsize'] <= 100000:
        counter += system_dict[key]['dirsize']
    
    if system_dict[key]['dirsize'] >= (30000000 - (70000000 - system_dict['/']['dirsize'])):
        if len(dir_to_del) == 0:
            dir_to_del.append(system_dict[key]['dirsize'])
            
        else:
            if dir_to_del[0] > system_dict[key]['dirsize']:
                dir_to_del.pop()
                dir_to_del.append(system_dict[key]['dirsize'])
            continue
                

print(counter)
print(system_dict['/']['dirsize'], dir_to_del)