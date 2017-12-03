import random, sys

class QuestionEasy:
    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        self.quest = quest
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.answerGood = answerGood
        self.fullQuestion = quest,answerA,answerB,answerC,answerD,answerGood

class QuestionMedium(QuestionEasy):
    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        super().__init__(quest,answerA,answerB,answerC,answerD,answerGood)

class QuestionHard(QuestionEasy):
    def __init__(self,quest,answerA,answerB,answerC,answerD,answerGood):
        super().__init__(quest,answerA,answerB,answerC,answerD,answerGood)

class RandomQuestion:
    def createListQuestionEasy():
        global listQuestRandomEasy
        listQuestRandomEasy = [questionEasy1.fullQuestion, questionEasy2.fullQuestion, questionEasy3.fullQuestion]

    def createListQuestionMedium():
        global listQuestRandomMedium
        listQuestRandomMedium = [questionMedium1.fullQuestion, questionMedium2.fullQuestion, questionMedium3.fullQuestion]

    def createListQuestionHard():
        global listQuestRandomHard
        listQuestRandomHard = [questionHard1.fullQuestion, questionHard2.fullQuestion, questionHard3.fullQuestion]

    def questionRandomEasy():
        global questRandomEasy
        questRandomEasy = random.choice(listQuestRandomEasy)
        print(questRandomEasy[0])
        print(questRandomEasy[1])
        print(questRandomEasy[2])
        print(questRandomEasy[3])
        print(questRandomEasy[4])

    def questionRandomMedium():
        global questRandomMedium
        questRandomMedium = random.choice(listQuestRandomMedium)
        print(questRandomMedium[0])
        print(questRandomMedium[1])
        print(questRandomMedium[2])
        print(questRandomMedium[3])
        print(questRandomMedium[4])

    def questionRandomHard():
        global questRandomHard
        questRandomHard = random.choice(listQuestRandomHard)
        print(questRandomHard[0])
        print(questRandomHard[1])
        print(questRandomHard[2])
        print(questRandomHard[3])
        print(questRandomHard[4])

    def RemoveQuestionEasy():
        if questRandomEasy == questionEasy1.fullQuestion:
            listQuestRandomEasy.remove(questionEasy1.fullQuestion)
            print(listQuestRandomEasy)
        elif questRandomEasy == questionEasy2.fullQuestion:
            listQuestRandomEasy.remove(questionEasy2.fullQuestion)
            print(listQuestRandomEasy)
        elif questRandomEasy == questionEasy3.fullQuestion:
            listQuestRandomEasy.remove(questionEasy3.fullQuestion)
            print(listQuestRandomEasy)

    def RemoveQuestionMedium():
        if questRandomMedium == questionMedium1.fullQuestion:
            listQuestRandomMedium.remove(questionMedium1.fullQuestion)
            print(listQuestRandomMedium)
        elif questRandomMedium == questionMedium2.fullQuestion:
            listQuestRandomMedium.remove(questionMedium2.fullQuestion)
            print(listQuestRandomMedium)
        elif questRandomMedium == questionMedium3.fullQuestion:
            listQuestRandomMedium.remove(questionMedium3.fullQuestion)
            print(listQuestRandomMedium)

    def RemoveQuestionHard():
        if questRandomHard == questionHard1.fullQuestion:
            listQuestRandomHard.remove(questionHard1.fullQuestion)
            print(listQuestRandomHard)
        elif questRandomHard == questionHard2.fullQuestion:
            listQuestRandomHard.remove(questionHard2.fullQuestion)
            print(listQuestRandomHard)
        elif questRandomHard == questionHard3.fullQuestion:
            listQuestRandomHard.remove(questionHard3.fullQuestion)
            print(listQuestRandomHard)

class CheckAnswer:
    def createVaribleScoreandCash():
        global score
        global cash
        global guaranteedCash
        score = 0
        cash = 0
        guaranteedCash = 0

    def checkPlayerAnswer():
        global score
        global cash
        global guaranteedCash
        guaranteedcash = 0
        if answerPlayer == questRandomEasy[5]:
            print('Good answer!')
            score += 1
            startScore = CheckAnswer
            startScore.score()
            nextQuest = NextQuestion
            nextQuest.doYouWantToPlayNext()
        elif answerPlayer != questRandomEasy[5]:
            print('Bad answer! Game Over! You win ' + str(guaranteedcash))
            sys.exit()
        elif answerPlayer == questRandomMedium[5]:
            print('Good answer!')
            score += 1
            startScore = CheckAnswer
            startScore.score()
        elif answerPlayer != questRandomEasy[5]:
            print('Bad answer! Game Over! You win ' + str(guaranteedcash))
            sys.exit()
        elif answerPlayer == questRandomHard[5]:
            print('Good answer!')
            score += 1
            startScore = CheckAnswer
            startScore.score()
        elif answerPlayer != questRandomEasy[5]:
            print('Bad answer! Game Over! You win ' + str(guaranteedcash))
            sys.exit()

    def score():
        global cash
        global guaranteedcash
        if score == 1:
            cash = 500
            guaranteedcash = 0
            print('You have 500 Euros!')
            print(cash)
            print(guaranteedcash)
        elif score == 2:
            cash = 1000
            guaranteedcash = 1000
            print('You Have 1000 Euros!')
            print(cash)
            print(guaranteedcash)

class NextQuestion:
    def doYouWantToPlayNext():
        print('Do you want to play next? You current win is: ' + str(cash) + ' euro!')
        playerNextQuestion = input()
        if playerNextQuestion == 't':
            print('Good decision! You are play next!')
        if playerNextQuestion == 'n':
            print('Thak you! You win: ' + str(cash) + ' euro!')
            sys.exit()

class Lifebuoy():
    def chooseLifebuoy():
        global lifebuoy5050Value
        global lifebuoyPhoneValue
        global lifebuoyAudienceValue
        lifebuoy5050Value = 0
        lifebuoyPhoneValue = 0
        lifebuoyAudienceValue = 0
        while lifebuoy5050Value == 0 or lifebuoyPhoneValue == 0 or lifebuoyAudienceValue == 0:
            print('Do you want use the lifebouy?')
            useLifebuoy = input()
            if useLifebuoy == '1':
                lifebuoyAll.lifebuoy5050()
            if useLifebuoy == '2':
                lifebuoyAll.lifebuoyPhone()
            if useLifebuoy == '3':
                lifebuoyAll.lifebuoyAudience()
            else:
                print('Odpowiedz na pytanie.')

    def lifebuoy5050():
        global lifebuoy5050Value
        if score <= 4:
            listFullQuestionEasy = questRandomEasy
            listLifebuoy5050 = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
        elif score > 4 and score < 10:
            listFullQuestionMedium = questRandomMedium
            listLifebuoy5050 = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
        elif score > 10:
            listFullQuestionHard = questRandomHard
            listLifebuoy5050 = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]

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

        lifebuoy5050Value += 1

    def lifebuoyPhone():
        global lifebuoyPhoneValue
        phoneVariantRandom = [1,2,3]
        phoneResultRandom = random.choice(phoneVariantRandom)

        if phoneResultRandom == 1:
            if score <= 4:
                listFullQuestionEasy = questRandomEasy
                listLifebuoyPhone = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
            elif score > 4 and score < 10:
                listFullQuestionMedium = questRandomMedium
                listLifebuoyPhone = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
            elif score > 10:
                listFullQuestionHard = questRandomHard
                listLifebuoyPhone = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]

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
            if score <= 4:
                listFullQuestionEasy = questRandomEasy
                listLifebuoyPhone = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
                goodAnswer = [listFullQuestionEasy[5]]
            elif score > 4 and score < 10:
                listFullQuestionMedium = questRandomMedium
                listLifebuoyPhone = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
                goodAnswer = [listFullQuestionMedium[5]]
            elif score > 10:
                listFullQuestionHard = questRandomHard
                listLifebuoyPhone = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]
                goodAnswer = [listFullQuestionHard[5]]
            goodAnswer = [listFullQuestion[5]]
            print('Your friend is certainly that good answer is: ' + str(goodAnswer))

        lifebuoyPhoneValue += 0

    def lifebuoyAudience():
        global lifebuoyAudienceValue
        percent = 100
        a = 0
        b = 0
        c = 0
        d = 0

        if score <= 4:
            listFullQuestionEasy = questRandomEasy
            listLifebuoyAudience = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
        elif score > 4 and score < 10:
            listFullQuestionMedium = questRandomMedium
            listLifebuoyAudience = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
        elif score > 10:
            listFullQuestionHard = questRandomHard
            listLifebuoyAudience = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]

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

        lifebuoyAudienceValue += 1

questionEasy1 = QuestionEasy('What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris', 'a - London')
questionEasy2 = QuestionEasy('What was the name of the Greek goddess of love?', 'a - Athena', 'b - Aphrodite', 'c - Euterpe', 'd - Hecate', 'b - Aphrodite')
questionEasy3 = QuestionEasy('Where will the Mundial 2018?', 'a - Germany', 'b - France', 'c - Russia', 'd - England', 'c - Russia')

questionMedium1 = QuestionMedium('Where is Albania?', 'a - Europe', 'b - Asia', 'c - Africa', 'd - South America', 'a - Europe')
questionMedium2 = QuestionMedium('The light on the North Pole?', 'a - Rainbow', 'b - Aurora borealis', 'c - Glow', 'd - Mirage', 'b - Aurora borealis')
questionMedium3 = QuestionMedium('What is the name of the power unit', 'a - Decibel', 'b - Volt', 'c - Watt', 'd - Boron', 'c - Watt')

questionHard1 = QuestionHard('Wchich Superhero drew Bob Kane?', 'a - Batman', 'b - Spiderman', 'c - Captain America', 'd - Superman', 'a - Batman')
questionHard2 = QuestionHard('How years ago sank The Titanic?', 'a - 1911', 'b - 1912', 'c - 1913', 'd - 1914', 'b - 1912')
questionHard3 = QuestionHard('What animal is particulary treat in China?', 'a - Tiger', 'b - Elephant', 'c - Panda', 'd - Bear', 'c - Panda')

lifebuoyAll = Lifebuoy
printList = RandomQuestion
checkAnswer = CheckAnswer
checkAnswer.createVaribleScoreandCash()
printList.createListQuestionEasy()
printList.createListQuestionMedium()
printList.createListQuestionHard()

printList.questionRandomEasy()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
lifebuoyAll.chooseLifebuoy()
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionEasy()

printList.questionRandomEasy()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionEasy()

printList.questionRandomMedium()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionMedium()

printList.questionRandomMedium()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionMedium()

printList.questionRandomHard()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionHard()

printList.questionRandomHard()
print('You write good answer: a, b, c or d')
print('Do you want use lifebuoy?')
answerPlayer = input()
checkAnswer.checkPlayerAnswer()
printList.RemoveQuestionHard()
