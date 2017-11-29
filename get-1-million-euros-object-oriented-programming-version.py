import random
class QuestionEasy:

    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        self.quest = quest
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.answerGood = answerGood
        self.fullGuestion = quest,answerA,answerB,answerC,answerD

    # def printQuestion(self):
    #     print(self.quest)
    #     print(self.answerA)
    #     print(self.answerB)
    #     print(self.answerC)
    #     print(self.answerD)

class RandomQuestion:
    def createListRandom():
        list = [questionEasy1.fullGuestion,questionEasy2.fullGuestion,questionEasy3.fullGuestion]
        questRandom = random.choice(list)
        print(questRandom[0])
        print(questRandom[1])
        print(questRandom[2])
        print(questRandom[3])
        print(questRandom[4])

# class CheckAnswer:
#
#     def checkAnswer():
#         if answerPlayer == questionEasy1.answerGood:
#             print('Good answer!')
#         else:
#             print('Bad answer!')

questionEasy1 = QuestionEasy('What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris','a')
questionEasy2 = QuestionEasy('What was the name of the Greek goddess of love?', 'a - Athena', 'b - Aphrodite', 'c - Euterpe', 'd - Hecate', 'b')
questionEasy3 = QuestionEasy('Where will the Mundial 2018?', 'a - Germany', 'b - France', 'c - Russia', 'd - England', 'c')

printLIST = RandomQuestion
printLIST.createListRandom()

# checkAnswer = CheckAnswer()
# print('You write good answer: a, b, c or d')
# answerPlayer = input()
# checkAnswer.checkAnswer()
