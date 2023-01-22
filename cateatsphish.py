import sys

import enumerate_domains
#import url_phishing_check
import check_ssl
import cookies_secure
import shortlink
import url_phishing_check
import websitedate
import pandas

domains_filename = sys.argv[1]

def scan(url):
    in_phishing_weight = 1
    similarity_weight = 1
    ssl_weight = 0.2
    date_weight = 0.2
    month_limit = 24
    cookies_weight = 0.05
    shortlink_weight = 0.05
    is_domain_in_phishing = enumerate_domains.find_domain(url.replace('https://', '').replace('http://', ''), enumerate_domains.PHISHING_URL_FILENAME)
    similarity = url_phishing_check.check_similarity(url.replace('https://', '').replace('http://', ''))
    has_ssl = check_ssl.has_ssl(url.replace('https://', '').replace('http://', ''))
    cookies = cookies_secure.get_cookies(url.replace('https://', '').replace('http://', ''))
    does_shortlink_exist = shortlink.check_links(url.replace('https://', '').replace('http://', ''))
    month_diff = websitedate.get_date(url.replace('https://', '').replace('http://', ''))

    # print("++++++++++++++CATEATSPHISH+++++++++++++")
    print(url)
    # print(is_domain_in_phishing, "IS DOMAIN IN PHISHING")
    # print(similarity, "IS SIMILAR")
    # print(has_ssl, "DOES DOMAIN HAS SSL CERT")
    # print(cookies, "COOKIES OF THE DOMAIN")
    # print(does_shortlink_exist, "EXISTS SHORTLINK")
    # print(month_diff, "months FROM CREATION")

    secured_cookies = [cookies[key]['secure'] for key in cookies]
    month_impact = 0.1
    try:
        month_impact = date_weight * ((month_limit - month_diff)/month_limit)
        if month_impact < 0: month_impact = 0
    except TypeError as e:
        # print(e)
        pass
    if is_domain_in_phishing: return (url, str(in_phishing_weight*100)+"%")
    result = round(similarity_weight * similarity + ssl_weight * (1-int(has_ssl)) + month_impact + (1-int(all(secured_cookies)))*cookies_weight + does_shortlink_exist * shortlink_weight)
    print("RESULT: ", str(result)+"%")
    if result > 100:
        result = 100
    elif result < 0:
        result = 0

    return (url, result)

if __name__ == "__main__":
    with open(domains_filename, "r") as file:
        data = []
        domains = file.readlines()
        i = 0
        for domain in domains:
            i+=1
            print(i)
            try:
                data.append(scan(domain.strip()))
            except:
                pass
        dataframe = pandas.DataFrame(data=data, columns=['url', 'result'])
        dataframe.to_csv('data.csv')
    print(dataframe)
