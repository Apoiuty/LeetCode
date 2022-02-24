from typing import List


def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort()
    result = [0] * len(people)
    for item in people:
        # if pre_item == item[0]:
        #     pre_cnt += 1
        # else:
        #     pre_cnt = 0
        # people_num = item[1]
        # short_cnt = 0
        # for index in index_list:
        #     if result[index][0] == item[0]:
        #         people_num -= 1
        #     if people_num >= index - short_cnt:
        #         short_cnt += 1
        #     else:
        #         break
        # i = people_num + short_cnt
        # bisect.insort(index_list, i)
        # result[i] = item
        # pre_item = item[0]
        index = item[1]
        cnt = 0
        while index:
            if not result[cnt] or result[cnt][0] >= item[0]:
                index -= 1
            cnt += 1
        # 如果后一个有元素册跳过
        while result[cnt]:
            cnt += 1
        result[cnt] = item

    return result


print(reconstructQueue(0, [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
