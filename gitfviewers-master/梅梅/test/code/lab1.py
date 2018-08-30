_auther_ = 'Harry'
_date_ = '5/4/2018 8:05 AM'

from datetime import datetime, date


def main():
    L1 = [3, 'word', 4.5, (3, 4, 5), [(1, 'x'), 2, (3, 'y')], 'Windsor', 'B', 75, 'Toronto']
    L2 = ['sky', 'tree', 20, 5.00, 'grass', 'green']
    del L2[-3]

    # s1 = "Python is a very easy language to learn!"
    # s2 = 'Why we need to learn web development in Django?'
    # print(s1+" "+s2)


    # L3 = []
    # for x in range(100,500):
    #     if x%7==0:
    #         if x%5 != 0:
    #             L3.append(x)
    # print(L3)

    d1 = {"name": "John", "age": 25, (3, 'm'): ['a', 'b', 'c'], 5: "Ontario", 20: 96, 12: 27}
    d2 = dict([("name", "Alice"), ('age', 24), ((1, 2), ['u', 'v', 'w']), (0, 'blue'), (86, 20)])
    d3 = dict(id=123, name='Willis', siblings=['Alex', 'Bob', 'Cindy'])
    d4 = dict(zip(("id", "name", "quantity"), (1234, "Disk Drive", 3)))

    #d2.update(d3)
    # d1.get((1, 2))
    # print(d1)
    # for key in d2.keys():
    #     print(d2[key])


    # print(datetime.now().year)
    # print(datetime.now().month)
    # print(datetime.now().day)

    today = date.today()
    endday = date(today.year,12,31)
    time_to_endday = abs(endday - today)
    print(time_to_endday.days)

if __name__ =="__main__":
        main()