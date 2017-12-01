import random
class QuestionEasy:

    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        self.quest = quest
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.answerGood = answerGood
        self.fullGuestion = quest,answerA,answerB,answerC,answerD,answerGood

class RandomQuestion:
    def createListRandom():
        global questRandom
        listQuestRandom = [questionEasy1.fullGuestion,questionEasy2.fullGuestion,questionEasy3.fullGuestion]
        questRandom = random.choice(listQuestRandom)
        print(questRandom[0])
        print(questRandom[1])
        print(questRandom[2])
        print(questRandom[3])
        print(questRandom[4])

class Lifebuoy():

    def lifebuoy5050():
        listFullQuestion = questRandom
        listLifebuoy5050 = [listFullQuestion[1],listFullQuestion[2],listFullQuestion[3],listFullQuestion[4],listFullQuestion[5]]

        if listLifebuoy5050[0] == listLifebuoy5050[4]:
            listFinal5050 = [listLifebuoy5050[1],listLifebuoy5050[2],listLifebuoy5050[3]]
            goodAnswer5050 = [listLifebuoy5050[4]]
            randomListFinal5050 = random.sample(listFinal5050, 1)
            exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
            exitPrint5050 = random.shuffle(exitListFinal5050)
            print(exitListFinal5050)

        elif listLifebuoy5050[1] == listLifebuoy5050[4]:
            listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[2],listLifebuoy5050[3]]
            goodAnswer5050 = [listLifebuoy5050[4]]
            randomListFinal5050 = random.sample(listFinal5050, 1)
            exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
            exitPrint5050 = random.shuffle(exitListFinal5050)
            print(exitListFinal5050)

        elif listLifebuoy5050[2] == listLifebuoy5050[4]:
            listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[1],listLifebuoy5050[3]]
            goodAnswer5050 = [listLifebuoy5050[4]]
            randomListFinal5050 = random.sample(listFinal5050, 1)
            exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
            exitPrint5050 = random.shuffle(exitListFinal5050)
            print(exitListFinal5050)

        elif listLifebuoy5050[3] == listLifebuoy5050[4]:
            listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[1],listLifebuoy5050[2]]
            goodAnswer5050 = [listLifebuoy5050[4]]
            randomListFinal5050 = random.sample(listFinal5050, 1)
            exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
            exitPrint5050 = random.shuffle(exitListFinal5050)
            print(exitListFinal5050)

    def lifebuoyPhone():
        phoneVariantRandom = [1,2,3]

        phoneResultRandom = random.choice(phoneVariantRandom)

        if phoneResultRandom == 1:
            listFullQuestion = questRandom
            listLifebuoyPhone = [listFullQuestion[1], listFullQuestion[2], listFullQuestion[3], listFullQuestion[4],listFullQuestion[5]]

            if listLifebuoyPhone[0] == listLifebuoyPhone[4]:
                listFinalPhone = [listLifebuoyPhone[1], listLifebuoyPhone[2], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[4]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                print(exitListFinalPhone)

            elif listLifebuoyPhone[1] == listLifebuoyPhone[4]:
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[2], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[4]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                print(exitListFinalPhone)

            elif listLifebuoyPhone[2] == listLifebuoyPhone[4]:
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[1], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[4]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                print(exitListFinalPhone)

            elif listLifebuoyPhone[3] == listLifebuoyPhone[4]:
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[1], listLifebuoyPhone[2]]
                goodAnswerPhone = [listLifebuoyPhone[4]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                print(exitListFinalPhone)

        if phoneResultRandom == 2:
            print('Your friend do not to know good answer!')

        if phoneResultRandom == 3:
            listFullQuestion = questRandom
            goodAnswer = [listFullQuestion[5]]
            print('Your friend is certainly that good answer is: ' + str(goodAnswer))

    def lifebuoyAudience():
        percent = 100
        a = 0
        b = 0
        c = 0
        d = 0
        listFullQuestion = questRandom
        listLifebuoyAudience = [listFullQuestion[1], listFullQuestion[2], listFullQuestion[3], listFullQuestion[4],listFullQuestion[5]]
        if listLifebuoyAudience[0] == listLifebuoyAudience[4]:
            a += 30
            percent -= 30
        if listLifebuoyAudience[1] == listLifebuoyAudience[4]:
            b += 30
            percent -= 30
        if listLifebuoyAudience[2] == listLifebuoyAudience[4]:
            c += 30
            percent -= 30
        if listLifebuoyAudience[3] == listLifebuoyAudience[4]:
            d += 30
            percent -= 30
        percentA = random.randint(0, percent)
        a += percentA
        percent -= percentA
        percentB = random.randint(0, percent)
        b += percentB
        percent -= percentB
        percentC = random.randint(0, percent)
        c += percentC
        percent -= percentC
        percentD = percent
        d += percentD
        print('Odpowiedź a - ' + str(a) + '%')
        print('Odpowiedź b - ' + str(b) + '%')
        print('Odpowiedź c - ' + str(c) + '%')
        print('Odpowiedź d - ' + str(d) + '%')

questionEasy1 = QuestionEasy('What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris', 'a - London')
questionEasy2 = QuestionEasy('What was the name of the Greek goddess of love?', 'a - Athena', 'b - Aphrodite', 'c - Euterpe', 'd - Hecate', 'b - Aphrodite')
questionEasy3 = QuestionEasy('Where will the Mundial 2018?', 'a - Germany', 'b - France', 'c - Russia', 'd - England', 'c - Russia')
lifebuoyAll = Lifebuoy
printLIST = RandomQuestion
printLIST.createListRandom()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
lifebuoyAll.lifebuoy5050()
lifebuoyAll.lifebuoyPhone()
lifebuoyAll.lifebuoyAudience()
answerPlayer = input()
