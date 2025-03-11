questions = [
  [
    "Which language was used to create FaceBook?", "Python",
    "French","Javascript","Php","None", 4
  ],
  [
   "Which of the following countries is the world's largest producer of saffron?", "spain",
   "Iran", "India", "Greece", 2
  ],
  [
   "Which of the following countries is the world's largest producer of saffron?", "Money",
   "Apple", "Flower","Leaves", 1
  ],
  [
   "Which language was used to create FaceBook?", "Python",
     "French", "Javascript", "Php", "None", 4
  ],
  [
        "Which city is known as the Pink City of India?", "Banglore",
    "Mysore", "Kochi","Jaipur", 4
  ],
  [
      "Which language was used to create FaceBook?", "Python",
     "French","Javascript","Php","None", 4
  ],
  [
        "Which of the following countries is the world's largest producer of saffron?", "spain",
    "Iran", "India", "Greece", 2
  ],
  [
        "Which of the following countries is the world's largest producer of saffron?", "Money",
    "Apple", "Flower","Leaves", 1
  ],
  [
        "Which language was used to create FaceBook?", "Python",
     "French", "Javascript", "Php", "None", 4
  ],
  [
        "Which city is known as the Pink City of India?", "Banglore",
    "Mysore", "Kochi","Jaipur", 4
  ],
  [
      "Which language was used to create FaceBook?", "Python",
     "French","Javascript","Php","None", 4
  ],
  [
        "Which of the following countries is the world's largest producer of saffron?", "spain",
    "Iran", "India", "Greece", 2
  ],
  [
        "Which of the following countries is the world's largest producer of saffron?", "Money",
    "Apple", "Flower","Leaves", 1
  ],
  [
        "Which language was used to create FaceBook?", "Python",
     "French", "Javascript", "Php", "None", 4
  ],
  [
        "Which city is known as the Pink City of India?", "Banglore",
    "Mysore", "Kochi","Jaipur", 4
  ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000,
          80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rupees: {levels[i]}")
    print(f"a.{questions[1]}                     b.{questions[2]}")
    print(f"c.{questions[3]}                     d.{questions[4]}")
    reply = int(input("Enter your answer choice (1-4)"))
    if(reply == questions[-1]):
        print(f"Correct answer, you have won {levels[i]} Rupees")
        if (i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif (i == 14):
        money = 10000000
    else:
        print("Wrong answer!")
        break

