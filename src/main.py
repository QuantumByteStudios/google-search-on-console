import json
import subprocess
import platform
from duckpy import Client
import time

if (platform.system() == 'Windows'):
    subprocess.call("cls", shell=True)
else:
    subprocess.call("clear", shell=True)


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

UP = '\033[1A'
CLEAR = '\x1b[2K'

print(f'\n\t{google_text}')
query_search = input(f'\tSearch: {colors.CYAN}')
{colors.ENDC}

print(UP, end=CLEAR)
print(f'\t{colors.FAIL}Results for: {colors.CYAN}"{query_search}"{colors.ENDC}')

try:
    client = Client()
    searchStart = time.time()
    results = client.search(query_search)
    searchEnd = time.time()
    searchTime = searchEnd - searchStart

    searchTime = round(searchTime, 2)

    if (query_search == ':history'):
        history = open('search.history', 'r')
        print(f'\t{colors.FAIL}Search history:\n{colors.ENDC}')
        print(f'{colors.CYAN}')
        index = 1
        for line in history:
            print(f'\t{index}. {line}')
            index += 1
        print(f'{colors.ENDC}')
        history.close()
        garbage = input()
        exit()
    else:
        print(
            f'\t{colors.FAIL}About {len(results)} search results in {searchTime} seconds.{colors.ENDC}\n')
        history = open('search.history', 'a')
        history.write(f'{query_search}\n')
        history.close()
        results_length = len(results)
        for i in range(results_length):
            result_index = i + 1
            title = results[i].title
            url = results[i].url
            description = results[i].description
            print(
                f'{colors.CYAN}  {result_index}.{colors.ENDC}\t{colors.GREEN}{title}{colors.ENDC}')
            print(f'\t{colors.BLUE}{url}{colors.ENDC}')
            print(f'\t{description[0:100]}{colors.RED}...{colors.ENDC}')
            print('')
        garbage = input()
        exit()
except Exception as e:
    print(f'{colors.FAIL}No results available.{colors.ENDC}')
    garbage = input()
    exit()
