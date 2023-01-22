import os

start_dir = 'Similarity/out/production/Similarity'
jar_dir = '../../../jar_files/guava-31.1-jre.jar'

def count_numbers(url):
    numbers = sum(c.isdigit() for c in url)
    return numbers

def check_similarity(domain):
    initial_cwd = os.getcwd()
    os.chdir(start_dir)
    output = os.popen(f'echo {domain} | java -cp .:{jar_dir} Similarity').read()
    os.chdir(initial_cwd)
    return float(output)