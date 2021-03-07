import random
import string

lower = "abcdefghijklmnñopqrstuvwxyzёйцукенгшщзхъфывапролджэячсмитьбюθωερτψυιοπασδφγηςκλζχξωβνμ"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮΘΩΕΡΤΨΥΙΟΠΑΣΔΦΓΗςΚΛΖΧΞΩΒΝΜ"
numbers = "0123456789"
symbols = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

all = lower + upper + numbers + symbols
print('Type 1 for mixed diccionary, 2 for standard character set.')
op = int(input('--Option:'))
if op == 1:
    length = int(input('--Desired-password-length(196max):'))
    passwd = "".join(random.sample(all, length))
    print('Here is your password:')
    print(passwd)

if op == 2:
    length = int(input('--Desired-password-length(96max):'))
    passwd = "".join(random.sample(string.printable, length))
    print('Here is your password:')
    print(passwd)