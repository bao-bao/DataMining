"""
    A sample for GSP algorithm
    ===============================================================    
    :param:
    *** dataset: dictionary of transactions with time sequence     eg: {name: list(list(str(items), ...), ...)), ...}
    *** minSupport: minimum support number rather than percentage
    
    :return:
    *** freqItems: frequent itemsets in dataset restricted by minSupport
"""
import itertools
import datetime


def freq1(data, frequent_num):
    f1 = []
    appear_freq_ele = []
    for key, value in data.items():
        appear = []
        for j in range(len(data[key])):
            for k in range(len(data[key][j])):
                appear += data[key][j][k]
        appear_freq_ele += list(set(appear))
    # print(appear_ele)
    appear_ele2 = list(set(appear_freq_ele))
    # print(appear_ele2)
    for item in appear_ele2:
        itm = appear_freq_ele.count(item)
        if itm >= frequent_num:
            f1.append(item)
    return f1


def freq_more(data, f1):
    queue = []
    queue_new = []
    top = 0
    times = 3
    while True:

        if not queue_new:
            for i in range(len(f1)):
                for j in range(i + 1, len(f1)):
                    item = f1[i] + f1[j]
                    queue.append(item)
            for i in range(len(f1)):
                for j in range(len(f1)):
                    if j != i:
                        item = f1[i] + '->' + f1[j]
                        queue.append(item)
            for i in range(len(queue)):
                freq_item = isFreq(queue[i], data)
                if freq_item != 0:
                    queue_new.append(freq_item)
            queue = []

        if queue_new:
            if top == len(queue_new):
                return queue_new
            else:
                demo_list = []
                for i in range(top, len(queue_new)):
                    if '->' not in queue_new[i]:
                        demo_list.append(queue_new[i])
                demo_string = List_to_String(demo_list)
                demo_ele = "".join(set(demo_string))
                if len(demo_ele) >= times:
                    if len(demo_ele) == times:
                        queue.append(demo_ele)
                        times += 1
                    else:
                        combin = Combinations(demo_ele, times)
                        for i in range(len(combin)):
                            queue.append(combin[i])
                        times += 1

                queue = Make_time_queue(top, f1, queue, queue_new)

                top = len(queue_new)

                for i in range(len(queue)):
                    freq_item = isFreq(queue[i], data)
                    if freq_item != 0:
                        queue_new.append(freq_item)
                queue = []


def List_to_String(li):
    demo_string = ''

    for i in range(len(li)):
        demo_string = demo_string + li[i]
    return demo_string


def Combinations(item, times):
    demo_list = []
    combin = []
    element = ''

    for i in range(1, len(item) + 1):
        ite = itertools.combinations(item, i)
        demo_list.append(list(ite))
    demo_combin = demo_list[times - 1]
    for i in range(len(demo_combin)):
        for j in range(len(demo_combin[0])):
            element += demo_combin[i][j]
        combin.append(element)
        element = ''
    return combin


def isFreq(item, data):
    num = 0

    if '->' not in item:
        for key, value in data.items():
            for i in range(len(value)):
                if isIn_Item(item, data, key, i) != 0:
                    num += 1
        if num >= 2:
            return item
        else:
            return 0
    else:
        item0 = item.split('->')

        for key, value in data.items():
            array = 0
            i = 0
            while True:
                if array == len(item0) or i == len(value):
                    break
                if len(item0[array]) >= 2:
                    if isIn_Item(item0[array], data, key, i) == 1:
                        array += 1
                        i += 1
                    else:
                        i += 1
                else:
                    if item0[array] in value[i]:
                        array += 1
                        i += 1
                    else:
                        i += 1
            if array == len(item0):
                num += 1
        if num >= 2:
            return item
        else:
            return 0


def isIn_Item(item, data, key, i):
    demo_num = 0

    for k in range(len(item)):
        if item[k] in data[key][i]:
            demo_num += 1
    if demo_num == len(item):
        return 1
    else:
        return 0


def isIn_Time(item0, data, key, i):
    num = 0

    item0_lenth = len(item0)
    if item0_lenth == 2:
        for m in range(i + 1, len(data[key])):
            if item0[1] in data[i][m]:
                num += 1
    else:
        if item0[item0_lenth - 2] in data[key][i]:
            for m in range(i + 1, len(data[key])):
                if item0[item0_lenth - 1] in data[key][m]:
                    num += 1
                    break
    return num


def Make_time_queue(top, f1, queue, queue_new):
    for i in range(top, len(queue_new)):
        #           for j in range(len(f1)):
        if '->' not in queue_new[i]:
            difference = Difference(queue_new[i], f1)
            for j in range(len(difference)):
                queue.append(difference[j] + '->' + queue_new[i])
                queue.append(queue_new[i] + '->' + difference[j])
        else:
            difference = Difference(queue_new[i], f1)
            for j in range(len(difference)):
                queue.append(queue_new[i] + '->' + difference[j])
    return queue


def Difference(item, f1):
    demo_list = []

    if '->' not in item:
        for i in range(len(f1)):
            if f1[i] not in item:
                demo_list.append(f1[i])
    else:
        demo_item = item.split('->')
        demo_item_string = List_to_String(demo_item)
        for i in range(len(f1)):
            if f1[i] not in demo_item_string:
                demo_list.append(f1[i])
    return demo_list


def gsp(dataSet, minsupport=1):
    print "GSP Running..."
    frequent = freq1(dataSet, minsupport)
    frequent.extend(freq_more(dataSet, frequent))
    return frequent


if __name__ == '__main__':
    dataset = {100: [['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'F'], ['A', 'C', 'D', 'F']],
               200: [['A', 'B', 'F'], ['E']],
               300: [['A', 'B', 'F']],
               400: [['D', 'G', 'H'], ['B', 'F'], ['A', 'G', 'H']]}

    testdata = {
        100: [['1'], ['3', '4']],
        200: [['2'], ['3'], ['5']],
        300: [['1'], ['2', '3'], ['5']],
        400: [['2', '5']]}

    starttime = datetime.datetime.now()
    freq1 = freq1(dataset, 2)
    freq_more(dataset, freq1)
    endtime = datetime.datetime.now()
    print(endtime - starttime)
