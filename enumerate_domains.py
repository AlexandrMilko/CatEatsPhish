PHISHING_URL_FILENAME = 'phishing_domains.txt'

def find_domain(domain, PHISHING_URL_FILENAME):
    with open(PHISHING_URL_FILENAME, "r") as phishing_url_file:
        phishing_urls = [url.strip() for url in phishing_url_file.readlines()]
        formatted_domain = domain.replace("http://", "")
        if formatted_domain in phishing_urls:
            return True
        return False

# if __name__ == "__main__":
#     find_domains(links_filename, PHISHING_URL_FILENAMENAME))
