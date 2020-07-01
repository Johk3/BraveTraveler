from time import strftime

LOG_INFO = lambda s : print(strftime("[%y%m%d-%H%M%S]") + f"\033[92m [INFO]\033[0m: {s}")
LOG_WARN = lambda s : print(strftime("[%y%m%d-%H%M%S]") + f"\033[93m [WARN]\033[0m: {s}")
LOG_FAIL = lambda s : print(strftime("[%y%m%d-%H%M%S]") + f"\033[91m [FAIL]\033[0m: {s}")
