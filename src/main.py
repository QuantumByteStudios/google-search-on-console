import json
import os

os.system("clear")


class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


google_text = f'{colors.BLUE}G{colors.ENDC}{colors.RED}o{colors.ENDC}{colors.YELLOW}o{colors.ENDC}{colors.BLUE}g{colors.ENDC}{colors.GREEN}l{colors.ENDC}{colors.RED}e{colors.ENDC}'
print(f'\n\t{google_text}\t')
query_search = input(f'\tenter your search query: ')

query_search = query_search.replace(' ', '+')

api_key = '6d513e41012e1a2cab4fcaa2071b863ed518afbf0fa58b197184a77d2ca1f136'

request_url = str(
    f'https://serpapi.com/search.json?engine=google&q={query_search}&api_key={api_key}')
# print(request_url)

os.system(f'curl -s "{request_url}" > result.json')

json_file = open('result.json', 'r', encoding="utf8")
json_data = json.load(json_file)

START = 0
END = len(json_data['organic_results'])
print_query = query_search.replace('+', ' ')
print(f'\t{colors.FAIL}Results for: {colors.CYAN}"{print_query}"\n{colors.ENDC}\n')

for i in range(START, END):
    try:
        title = json_data['organic_results'][i]['title']
        url = json_data['organic_results'][i]['link']
        description = json_data['organic_results'][i]['snippet']
        print(
            f'\t{i+1}) {colors.GREEN}{title}{colors.ENDC} | {colors.BLUE}{url}{colors.ENDC}')
        if(description == ''):
            description = 'No description available'
        else:
            print(f'\t{description[0:100]}{colors.RED}...{colors.ENDC}\n')
    except:
        pass

json_file.close()
