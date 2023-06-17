print("Grade Point Average")

score_table = {
      "A+":4.0
    , "A":4.0
    , "A-":3.7
    , "B+":3.3
    , "B":3.0
    , "B-":2.7
    , "C+":2.3
    , "C":2.0
    , "C-":1.7
    , "D+":1.3
    , "D":1.0
    , "F":0
}

score = []
while True:
# User inputs Letter Grade    
    grade = input("Grade:")
    if grade == "":
        break
    
    score.append(score_table[grade])
    
avg = sum(score) / len(score)
# Program will print Average based on score table
print("Average:", avg)
