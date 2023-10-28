from os import listdir
from os.path import isfile, join
from os import walk
import openai
import fileinput

class ErrorLog:

    def __init__(self):
        self.files = []
        self.omittedDirs = []

    def giveCode(self, dirs, omittedDirs=[]):
        '''
        Retrieve all files from all dirs, set omitted dirs (optionally, a user can omit subdirectories)
        '''
        self.omittedDirs = omittedDirs
        for dir in dirs:
            self.getAllFiles(dir)

    def debuglog(self, err, brief=True):
        '''
        Logs the solution to the error, which is manually typed by the user or caught as an exception
        err: the error message
        brief (optional): decides whether the response should be brief or not.
        '''
        if len(self.files) == 0:
            print("ERR: Please provide the files or directories for the code.")
            return -1

        msg = self.constructPrompt(self.files, err, brief)
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg},
        ])
        print(response['choices'][0]['message']['content'])

    def constructPrompt(self, files, err, brief):
        '''
        err: the inputted error message
        '''
        msg = ['The code I have for each file is as follows:\n']
        for file in files:
            f = open(file, mode='rb')
            codeFromFile = "1 " + f.read().decode('utf-8')
            lines = codeFromFile.split('\n')
            codeString = ''
            for i, line in enumerate(lines):
                codeString += f"{line}\n{i + 2} "
            msg += [f'The code for {file}, starting at --- and ending at ---:\n---\n', codeString, '\n---\n\n']
            f.close()
        if brief:
            msg.append(''.join(['Do not mention indentations, and answering specific to the above code, and limiting to 200 characters, and mentioning which file, solve this bug I have:, starting at --- and ending at ---?:', '\n---\n', err, '\n---']))
        else:
            msg.append(''.join(['Do not mention indentations, and answering specific to the above code, and mentioning which file, solve this bug I have:, starting at --- and ending at ---?:', '\n---\n', err, '\n---']))

        return ''.join(msg)

    def getAllFiles(self, curDir):
        '''
        curDir: the current working directory

        Recursively retrieves all files within a directory
        Ensures file is not in omittedDirs
        '''

        for (dirpath, dirnames, filenames) in walk(curDir):
            for file in filenames:
                self.files.append(''.join([dirpath, '/', file]))
            for dir in dirnames:
                if dir not in self.omittedDirs:
                    self.getAllFiles(''.join([dirpath, '/', dir]))
            break
