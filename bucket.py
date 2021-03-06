from builtins import input
import sys

# data for 100 rolls for 6 dice
x = [[4, 6, 3, 8, 1, 1], [6, 3, 2, 6, 4, 9], [3, 2, 8, 9, 4, 5], [4, 3, 1, 2, 7, 8], [6, 5, 9, 7, 1, 7], [5, 7, 4, 4, 4, 7], [9, 7, 6, 7, 2, 9], [4, 9, 3, 2, 5, 9], [7, 3, 2, 5, 8, 8], [3, 3, 1, 7, 4, 9], [5, 7, 3, 9, 9, 4], [9, 6, 5, 4, 9, 5], [1, 7, 8, 1, 1, 1], [9, 6, 3, 6, 8, 4], [3, 5, 2, 6, 5, 5], [4, 2, 5, 2, 2, 5], [3, 2, 2, 1, 5, 1], [1, 2, 7, 5, 9, 5], [5, 6, 2, 6, 6, 9], [3, 8, 3, 4, 8, 1], [7, 5, 7, 1, 9, 9], [7, 1, 2, 8, 3, 8], [7, 6, 3, 1, 3, 6], [2, 2, 5, 7, 2, 8], [7, 3, 5, 3, 4, 8], [9, 3, 5, 5, 8, 4], [8, 1, 3, 2, 1, 3], [3, 2, 5, 9, 4, 7], [8, 5, 8, 5, 2, 8], [7, 7, 4, 6, 5, 7], [9, 4, 4, 3, 6, 9], [2, 5, 2, 2, 1, 4], [3, 7, 7, 9, 7, 5], [7, 2, 7, 6, 6, 1], [1, 7, 3, 9, 9, 7], [7, 1, 1, 1, 4, 8], [6, 9, 6, 6, 4, 6], [9, 8, 9, 2, 5, 8], [8, 8, 8, 9, 6, 8], [8, 1, 9, 2, 4, 6], [5, 8, 2, 2, 4, 9], [8, 9, 8, 3, 7, 1], [7, 1, 5, 1, 6, 8], [8, 9, 9, 4, 8, 1], [9, 3, 4, 4, 2, 6], [2, 6, 8, 9, 6, 2], [5, 9, 3, 1, 9, 4], [9, 2, 7, 4, 7, 3], [1, 7, 8, 2, 7, 8], [8, 4, 4, 4, 6, 2], [3, 4, 8, 6, 8, 4], [6, 6, 9, 3, 9, 6], [1, 1, 4, 6, 6, 2], [6, 4, 4, 5, 7, 4], [4, 2, 1, 2, 3, 1], [8, 9, 5, 3, 4, 6], [3, 3, 5, 8, 2, 5], [9, 7, 3, 8, 7, 3], [9, 3, 6, 5, 7, 1], [7, 7, 2, 9, 1, 9], [6, 8, 7, 4, 5, 4], [5, 8, 5, 4, 2, 4], [7, 3, 4, 5, 9, 4], [4, 4, 9, 1, 8, 3], [5, 3, 9, 1, 3, 1], [1, 9, 6, 1, 1, 1], [1, 3, 1, 2, 9, 7], [5, 7, 2, 9, 7, 6], [2, 5, 1, 8, 9, 5], [5, 1, 8, 4, 1, 4], [4, 5, 1, 2, 5, 3], [1, 6, 3, 4, 3, 6], [5, 8, 4, 5, 7, 5], [7, 5, 5, 7, 2, 4], [6, 7, 1, 6, 8, 7], [3, 3, 6, 3, 1, 6], [7, 6, 8, 9, 6, 9], [2, 4, 5, 7, 1, 4], [1, 8, 4, 8, 2, 5], [7, 5, 6, 9, 9, 8], [8, 8, 1, 8, 9, 5], [5, 2, 8, 4, 5, 1], [9, 8, 1, 6, 8, 9], [1, 8, 9, 3, 6, 3], [3, 4, 5, 6, 2, 8], [8, 5, 9, 5, 3, 2], [7, 6, 5, 9, 6, 5], [7, 2, 7, 8, 7, 8], [5, 7, 6, 6, 9, 2], [5, 7, 2, 6, 2, 5], [4, 1, 6, 9, 4, 9], [1, 3, 4, 7, 4, 5], [5, 8, 9, 7, 4, 1], [1, 3, 8, 4, 8, 9], [2, 8, 7, 4, 8, 3], [7, 3, 5, 2, 2, 8], [1, 6, 5, 4, 1, 1], [1, 2, 6, 9, 6, 9], [8, 5, 2, 7, 3, 8], [2, 1, 2, 4, 1, 2]]
sum = 0

bucket = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
        "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
        "31": 0, "32": 0, "33": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0, "40": 0,
        "41": 0, "42": 0, "43": 0, "44": 0, "45": 0, "46": 0, "47": 0, "48": 0, "49": 0}

# get input m for bucket capacity
m = int(input())

consume = 0
overflow = 0
total = 0
# Check constraints
if m <= 0 or m > 50:
    sys.exit()

total = m*49
for i in range(len(x)):
    sum = 0
    for j in range(len(x[i])):
        sum += x[i][j]

    if sum < m or sum == m:
        if bucket[str(sum)] != 0:
            if bucket[str(sum)] == m:
                overflow += sum
            else:
                temp = bucket[str(sum)]
                space = (m-temp)
                if sum > space or sum == space:
                    bucket.update({str(sum): m})
                    consume += space
                    overflow += sum-space
                else:
                    tochange = temp+sum
                    bucket.update({str(sum): tochange})
                    consume += sum
        else:
            bucket.update({str(sum): sum})
            consume += sum


    else:
        if bucket[str(sum)] != 0:
            if bucket[str(sum)] == m:
                overflow += sum
        else:
            bucket.update({str(sum): m})
            consume += m
            overflow += (sum-m)
    


print(consume)
print(overflow)
print(total-consume)





