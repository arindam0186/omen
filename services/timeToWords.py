from util.nums import nums

def printTime(h, m):
    if (m == 0):
        time = nums[h], "o' clock";

    elif (m == 1):
        time = "one minute past", nums[h];

    elif (m == 59):
        time = "one minute to", nums[(h % 12) + 1];

    elif (m == 15):
        time = "quarter past", nums[h];

    elif (m == 30):
        time = "half past", nums[h];

    elif (m == 45):
        time = "quarter to", (nums[(h % 12) + 1]);

    elif (m <= 30):
        time = nums[m], "minutes past", nums[h];

    elif (m > 30):
        time = nums[60 - m], "minutes to", nums[(h % 12) + 1];

    return time
