Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the
number of times she breaks her season record for _most points_ and _least points_ in a game. Points scored in the first
game establish her record for the season, and she begins counting from there.

**Example**

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

Given the scores for a season, determine the number of times Maria breaks her records for _most_ and _least_ points
scored during the season.

**Function Description**

Complete the _breakingRecords_ function in the editor below.

breakingRecords has the following parameter(s):

- _int scores\[n\]:_ points scored per game

**Returns**

- _int\[2\]:_ An array with the numbers of times she broke her records. Index is for breaking _most points_ records, and
  index is for breaking _least points_ records.

**Input Format**

The first line contains an integer , the number of games.  
The second line contains space-separated integers describing the respective values of .

**Explanation 0**

The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

![image](https://s3.amazonaws.com/hr-assets/0/1487360234-6bca5c518d-breakingbest3.png)

She broke her best record twice (after games and ) and her worst record four times (after games , , , and ), so we
print `2 4` as our answer. Note that she _did not_ break her record for best score during game , as her score during
that game was _not_ strictly greater than her best record at the time.

**Sample Input 1**

10 3 4 21 36 10 28 35 5 24 42

**Explanation 1**

The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

![image](https://s3.amazonaws.com/hr-assets/0/1487360375-aee4388234-breakingbest5.png)

She broke her best record four times (after games 1, 2, 3, and 9) and her worst record zero times (no score during the
season was lower than the one she earned during her first game), so we print `4 0` as our answer.