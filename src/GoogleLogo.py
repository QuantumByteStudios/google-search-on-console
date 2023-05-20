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


google = '''
█▀▀▀ █▀▀█ █▀▀█ █▀▀▀ █░░ █▀▀ 
█░▀█ █░░█ █░░█ █░▀█ █░░ █▀▀ 
▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 
'''

google_text_line_one = \
    colors.BLUE + "█▀▀▀ " + colors.ENDC + \
    colors.RED + "█▀▀█ " + colors.ENDC + \
    colors.YELLOW + "█▀▀█ " + colors.ENDC + \
    colors.BLUE + "█▀▀▀ " + colors.ENDC + \
    colors.GREEN + "█   " + colors.ENDC + \
    colors.RED + "█▀▀ " + colors.ENDC

google_text_line_two = \
    colors.BLUE + "█ ▀█ " + colors.ENDC + \
    colors.RED + "█  █ " + colors.ENDC + \
    colors.YELLOW + "█  █ " + colors.ENDC + \
    colors.BLUE + "█ ▀█ " + colors.ENDC + \
    colors.GREEN + "█   " + colors.ENDC + \
    colors.RED + "█▀▀ " + colors.ENDC

google_text_line_three = \
    colors.BLUE + "▀▀▀▀ " + colors.ENDC + \
    colors.RED + "▀▀▀▀ " + colors.ENDC + \
    colors.YELLOW + "▀▀▀▀ " + colors.ENDC + \
    colors.BLUE + "▀▀▀▀ " + colors.ENDC + \
    colors.GREEN + "▀▀▀ " + colors.ENDC + \
    colors.RED + "▀▀▀" + colors.ENDC


google_text = f'\n\t{google_text_line_one}\n\t{google_text_line_two}\n\t{google_text_line_three}'

# print(google_text)
