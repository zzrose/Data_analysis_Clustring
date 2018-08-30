_auther_ = 'Harry'
_date_ = '5/4/2018 11:36 AM'

import sys

if __name__ == '__main__':

    productList = ["chips","olive oil","biscuits","cheese","orange juise","fullcream milk","whole chiken","hand soap","water bottle","Harry"]
    d1 = {}

    for product in productList:
        f = open("./inventory.txt")
        line = f.readline()
        while line:
            if product == line.replace('\n',''):
                print(line)
                num = f.readline()
                d1.update({line.replace('\n',''):num.replace('\n','')})
                line = f.readline()

            else:
                line = f.readline()

        f.close()
    print(d1)


    command = ' '
    while command == "yes" or ' ':
        print("plese input product you want:")
        product_name = input()

        try:
            d1[product_name]
            if product_name in d1.keys():
                number = d1.get(product_name)
                print("the number of " + product_name + " is " + number)
                print("do you want to continue to search? (yes/no)")
                command = input()
                if command == "yes":
                    continue
                elif command == "no":
                    break
                else:
                    print("please input yes or no!")
                    command = input()
                    if command == 'no':
                        break


        except Exception as e:
            print("the name of product you search not correct, try another product name")




