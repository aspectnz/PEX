try:
    import getpass
except:
    import pip
    pip.main(['install', 'getpass'])
    import getpass

usera=getpass.getuser()
passa=getpass.getpass()

print(passa)