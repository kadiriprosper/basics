import json
import os
import shutil
import re


os.system('cls')
desktop_path = os.path.expanduser("~")


def organizeFiles(filePattern):
    # fileMode = 'a'
    # file_path = f'{desktop_path}/.data.json'
    # if (not os.path.exists(file_path)):
    #     fileMode = 'w'
    # with open(file_path, fileMode) as file_ref:
    print("Creating Folders")
    print("---------------------------------------------------------------------------------")
    for folder_name in filePattern:
        folder_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    print("Folders Created\n")
    print("Organizing Files")
    print("---------------------------------------------------------------------------------")
    
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)
        if os.path.isfile(file_path):
            for folder_name, extensions in filePattern.items():
                for extension in extensions:
                    if file_name.endswith(extension):
                        destination_folder =os.path.join(desktop_path, folder_name)
                        shutil.move(file_path, destination_folder)

    print("Files organized")
    print("---------------------------------------------------------------------------------")
        
    

def getFilePattern():
    print('Loading file patterns.....')
    try:
        file_path = open(f'{desktop_path}/.data.json', 'r')
        _filePattern = file_path.read()
        filePattern = json.loads(_filePattern)
        print((re.sub(r'{|}', '\n', (str(filePattern).replace('],', ']\n')))).replace(' ', ''))

        file_path.close()
        print('\n')
        print("---------------------------------------------------------------------------------")
        return filePattern
    except:
        print("File Pattern does not exist. Creating one now")
        try:
            folders = {
            "Images" : ['.svg', '.jpeg', '.gif', '.png', '.jpg', '.jfif'],
            "Documents": ['.doc', '.docx', '.pdf', '.txt', '.csv', '.pptx', '.xlsx'],
            "Archives" : ['.zip', '.rar', '.apk', '.iso'],
            'Applications': ['.exe','.msi']
            }   


            file_path = open(f'{desktop_path}/.data.json', 'w')
            file_path.write(json.dumps(folders))
            file_path.close()
            getFilePattern()
            print("File Pattern Successfully Created")
        except:
            print("Error getting file pattern")
    print("---------------------------------------------------------------------------------")
    return {}


runApp = True
firstRun = True

while (runApp):
    os.system('cls')
    print('--------------------------------------------------------------------------------')
    print('Welcome to File Organizer 0.5 (alpha)')
    if firstRun:
        path = input(f'Please input the directory you want to organize: {desktop_path}\\')
        if (input):
            desktop_path = f'{desktop_path}\\{path}'
            if (not os.path.isdir(desktop_path)):
                print('Cannot find directory. Exiting app')
                input('Press any key to exit...')
                runApp = False
                exit()
        else:
            print("File not specified. Exiting app")
            input('Press any key to exit...')
            runApp = False
            exit()
        firstRun = False

    print('Input an option index to continue')
    print('1. Organize Files')
    print('2. View file pattern dictionary')
    print('3. Exit')
    userSelection = input()
    try:
        userSelection = int(userSelection)
        if (userSelection == 1):
            #organize files
            os.system('cls')
            print('Your selection is 1. Organize File')
            print('--------------------------------------------------------------------------------------')
            print('We are currntly going to use the following file patterns:')
            print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            filePattern = getFilePattern()
            organizeFiles(filePattern)
            input('Press any key to continue...')
            
        elif (userSelection == 2):
            os.system('cls')
            print('Current File Pattern:')
            getFilePattern()
            input('Press any key to continue...')
        elif(userSelection == 3):
            print('.'  * 20)
            print("File Organizer (0.5 alpha)")
            print('.'  * 20)
            runApp = False
        else:
            print('Please input a valid option')
    except:
        print(f'{userSelection} is invalid. Please select from the options')

