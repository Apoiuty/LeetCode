from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def back_trace(ip, sub_str, n):
            # 剪枝
            if len(sub_str) > n * 3 or len(sub_str) < n:
                return
            if n == 0 and sub_str == '':
                ans.append(ip[1:])

            for i in range(1, len(sub_str) + 1):
                next_ip = sub_str[0:i]
                if 0 <= int(next_ip) <= 255 and not (len(next_ip) > 1 and next_ip.startswith('0')):
                    back_trace(f'{ip}.{next_ip}', sub_str[i:], n - 1)

        back_trace('', s, 4)
        return ans


s = Solution()
print(s.restoreIpAddresses("101023"))
