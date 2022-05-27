from typing import List
import datetime
from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for i in [1, 2, 4, 8]:
            times.append(datetime.timedelta(hours=i))

        for i in [1, 2, 4, 8, 16, 32]:
            times.append(datetime.timedelta(minutes=i))

        if turnedOn > len(times):
            return []

        result = []
        for t in combinations(times, turnedOn):
            minute = datetime.timedelta()
            hour = datetime.timedelta()
            for t_ in t:
                if t_.seconds % 3600 == 0:
                    hour += t_
                else:
                    minute += t_

            if minute.seconds >= 3600:
                continue
            if hour.seconds > 11 * 3600:
                continue
            result.append(str(hour + minute)[:-3])

        return result


s = Solution()
print(s.readBinaryWatch(9))
