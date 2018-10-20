#encoding:utf8
__author__ = 'gold'

'''
401.
Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        numDic = {0: ['0'], 1: ['1', '2', '4', '8', '16', '32'], 2: ['3', '5', '6', '9', '10', '12', '17', '18', '20', '24', '33',
        '34', '36', '40', '48'], 3: ['7', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'],
        4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'], 5: ['31', '47', '55', '59']}

        results = []
        for i in range(num + 1):
            try:
                hour = numDic[i]
                min = numDic[num - i]
                for curHour in hour:
                    if int(curHour) > 11:
                        continue
                    for curMin in min:
                        if len(curMin) == 1:
                            results.append(curHour + ':0' + curMin)
                        else:
                            results.append(curHour + ':' + curMin)
            except KeyError as e:
                pass
        return results

if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
    print(Solution().readBinaryWatch(10))