import os

from datetime import date
today = date.today()
today_month = today.strftime("%m")
today_year = today.strftime("%Y")

def get_date(domain):
    creation_line = ''
    output = os.popen(f'whois {domain}').read()
    lines = output.split('\n')
    try:
        creation_line = [line for line in lines if "Creation" in line][-1].split(" ")[2]
        # print(creation_line, domain)
        site_year = creation_line[:4]
        site_month = creation_line[5:7]
        # print(site_year, site_month)
        diff_months = ((int(today_year)-int(site_year))*12+(int(today_month)-int(site_month)))
    except:
        return None
    return diff_months