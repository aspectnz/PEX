from pathlib import Path
downloads_path = str(Path.home() / "Downloads")
print(downloads_path)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    import shutil
    src = r'C:\wamp64\test.txt'
    dst = r'C:\test'
    shutil.copyfile(src, dst)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)