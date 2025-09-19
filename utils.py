
from typing import List, Union, TextIO
import re


def get_query(cmd: str, value: str, file: Union[str, List, TextIO]) -> Union[str, List]:
    if cmd == 'filter':
        return list(filter(lambda x: value in x, file))

    if cmd == 'map':
        return '\n'.join([x.split()[int(value)] for x in file])

    if cmd == 'unique':
        return list(set(file))

    if cmd == 'sort':
        reverse = value == 'desc'
        return sorted(file, reverse=reverse)

    if cmd == 'limit':
        return list(file)[:int(value)]

    if cmd == 'regex':
        reg = re.compile(value)
        result = list(filter(lambda x: reg.findall(x), file))

    return result
