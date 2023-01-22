import os
def check_links(domain):
    cwd = os.getcwd()
    os.chdir('shortlinkfromandrew/untitled1')
    output = os.popen(f'echo http://{domain} | ./shortlink').read()
    os.chdir('../..')
    try:
        if bool(int(output)): return True
    except ValueError as e:
        # print(f"ERROR: {e}")
        pass
    return False