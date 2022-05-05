from enum import Enum, unique
import logging
import pdb

logging.basicConfig(level=logging.INFO)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun, Mon, = 0, 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def f00(s):
    n = int(s)
    # assert n != 0, 'n is zero!'
    logging.info('n = %d ' % n)
    pdb.set_trace()

    return 10/n


if __name__ == '__main__':
    # for name, member in Weekday.__members__.items():
    #     print(name, member, member.value)

    f00('0')