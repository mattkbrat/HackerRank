"""
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored
during the season.
"""


def breakingRecords(scores):
    least_point_records = [scores[0], 0]  # Record, Times Broken
    most_point_records = [scores[0], 0]  # Record, Times Broken

    for n in scores[1:]:
        if n < least_point_records[0]:
            least_point_records[1] = least_point_records[1] + 1
            least_point_records[0] = n
        if n > most_point_records[0]:
            most_point_records[1] = most_point_records[1] + 1
            most_point_records[0] = n
    result = [most_point_records[1], least_point_records[1]]
    return result


if __name__ == '__main__':
    a = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
    print(a)
