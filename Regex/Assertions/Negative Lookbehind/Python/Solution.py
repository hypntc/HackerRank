Regex_Pattern = r'(?<![aeiouAEIOU]).'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())