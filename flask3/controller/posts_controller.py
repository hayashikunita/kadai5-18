import logging
import re
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def name_check1(name):
    p = re.compile('[\u3041-\u309F\u30A1-\u30FF\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
    return p.fullmatch(name) is not None  # => True

def name_check2(name):
    namecheck2 = len(name)
    if namecheck2 < 16:
        logger.info(f'name<16')
        return True
    elif namecheck2 >= 16:
        logger.info(f'name>16')
        return False

def name_reverse(name):
    reverse_string = ""
    for a in name:
        reverse_string = a + reverse_string
    return reverse_string

def name_duplicate(name):
    duplicate_string = ""
    for a in name:
        duplicate_string += a + a 
    return duplicate_string











