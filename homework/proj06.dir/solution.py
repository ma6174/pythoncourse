#!/usr/bin/env python
#coding=utf-8

def get_input_descriptor():
    while True:
        file_name = raw_input("Open what file:")
        try:
            file_object = open(file_name)
            return file_object
        except:
            print("Bad file name, try again")

def get_data_list(file_object,column_number):
    lines = file_object.readlines()
    data = []
    for line in lines[1:]:
        sp = line.strip().split(',')
        data.append((sp[0],sp[int(column_number)]))
    file_object.close()
    return data

def average_data(list_of_tuples):
    all = {}
    count = {}
    for li in list_of_tuples:
        sp = li[0].split('-')
        date = "%s-%s"%(sp[1],sp[0])
        if date in all:
            all[date] += float(li[1])
            count[date] += 1
        else:
            all[date] = float(li[1])
            count[date] = 1
    ave = []
    for key in all:
        ave.append((float("%.2f"%(all[key]/count[key])),key))
    sort_ave = sorted(ave)
    print("Lowest 6 for colum 6")
    for i in sort_ave[0:6]:
        print("Date:%s,Value: %s"%(i[1],i[0]))

    print("")
    print("Highest 6 for colum 6")
    for i in sort_ave[-6:][::-1]:
        print("Date:%s,Value: %s"%(i[1],i[0]))




def main():
    file_object = get_input_descriptor()
    column = raw_input("What column:")
    list_of_tuples = get_data_list(file_object,column)
    average_data(list_of_tuples)

if __name__=='__main__':
    main()
