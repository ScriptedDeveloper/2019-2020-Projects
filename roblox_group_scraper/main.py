try:
    import random
    import time
    import string
    from requests import Session
    from colorama import Fore, init
    init(autoreset=True)
except ModuleNotFoundError:
    from os import system
    system('cmd /k "pip3 install random"')
    system('cmd /k "pip3 install colorama"')
    system('cmd /k "pip3 install requests"')


req = Session()

class main():
    def __init__(self):
        pass

    def finder(self):
        print('Running.. This might take a while! Results will be posted here.')
        while True:
            id = ''.join(random.choice(string.digits) for i in range(8))
            group = req.get('https://groups.roblox.com/v1/groups/' + id)
            if group.status_code == 200:
                if group.json()['owner'] == None and group.json()['publicEntryAllowed'] == True:
                    print(Fore.GREEN + "https://www.roblox.com/groups/" + str(id))

                else:
                    pass

            elif group.status_code == 400:
                pass

            else:
                pass


        



if __name__ == '__main__':
    main().finder()
