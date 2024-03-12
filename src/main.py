import subprocess
import platform
from duckduckgo_search import DDGS
import GoogleLogo as gl
import time

if (platform.system() == 'Windows'):
    subprocess.call("cls", shell=True)  # nosec B602, B607
else:
    subprocess.call("clear", shell=True)  # nosec B602, B607

google_text = gl.google_text

UP = '\033[1A'
CLEAR = '\x1b[2K'

print(google_text)
print(f'\t{gl.colors.FAIL}Type {gl.colors.CYAN}"{gl.colors.GREEN}:history{gl.colors.CYAN}"{gl.colors.FAIL} to see your search history.{gl.colors.ENDC}\n')

query_search = input(f'\tSearch: {gl.colors.CYAN}')
{gl.colors.ENDC}

print(UP, end=CLEAR)
print(f'\t{gl.colors.FAIL}Results for: {gl.colors.CYAN}"{query_search}"{gl.colors.ENDC}')

try:
    searchStart = time.time()
    results = DDGS().text(query_search, max_results=8)
    searchEnd = time.time()
    searchTime = searchEnd - searchStart

    searchTime = round(searchTime, 2)

    if (query_search == ':history'):
        history = open('search.history', 'r')
        print(f'\t{gl.colors.FAIL}Search history:\n{gl.colors.ENDC}')
        print(f'{gl.colors.CYAN}')
        index = 1
        for line in history:
            print(f'\t{index}. {line}')
            index += 1
        print(f'{gl.colors.ENDC}')
        history.close()
        garbage = input()
        exit()
    else:
        print(
            f'\t{gl.colors.FAIL}About {len(results)} search results in {searchTime} seconds.{gl.colors.ENDC}\n')
        history = open('search.history', 'a', encoding='utf_8')
        history.write(f'{query_search}\n')
        history.close()
        results_length = len(results)
        result_index = 1
        for result in results:
            title = result['title']
            url = result['href']
            description = result['body']
            print(
                f'{gl.colors.CYAN}  {result_index}.{gl.colors.ENDC}\t{gl.colors.GREEN}{title}{gl.colors.ENDC}')
            print(f'\t{gl.colors.BLUE}{url}{gl.colors.ENDC}')
            print(
                f'\t{description[0:100]}{gl.colors.RED}...{gl.colors.ENDC}')
            result_index += 1
            print('')
        garbage = input()
        exit()
except Exception as e:
    print(f'{gl.colors.FAIL}No results available.{gl.colors.ENDC}')
    garbage = input()
    exit()
