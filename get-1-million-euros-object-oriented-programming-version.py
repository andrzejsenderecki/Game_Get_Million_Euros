import random, sys, tkinter
from tkinter import messagebox

gui = tkinter.Tk()

gui.geometry('910x450')

gui.title('GET 1 MILLION EUROS!')

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
        listQuestRandomEasy = [questionEasy1.fullQuestion, questionEasy2.fullQuestion, questionEasy3.fullQuestion, questionEasy4.fullQuestion, questionEasy5.fullQuestion, questionEasy6.fullQuestion, questionEasy7.fullQuestion, questionEasy8.fullQuestion]

    def createListQuestionMedium():
        global listQuestRandomMedium
        listQuestRandomMedium = [questionMedium1.fullQuestion, questionMedium2.fullQuestion, questionMedium3.fullQuestion, questionMedium4.fullQuestion, questionMedium5.fullQuestion, questionMedium6.fullQuestion, questionMedium7.fullQuestion, questionMedium8.fullQuestion]

    def createListQuestionHard():
        global listQuestRandomHard
        listQuestRandomHard = [questionHard1.fullQuestion, questionHard2.fullQuestion, questionHard3.fullQuestion, questionHard4.fullQuestion, questionHard5.fullQuestion, questionHard6.fullQuestion, questionHard7.fullQuestion, questionHard8.fullQuestion]

    def questionRandomEasy():
        global questRandomEasy
        questRandomEasy = random.choice(listQuestRandomEasy)

    def questionRandomMedium():
        global questRandomMedium
        questRandomMedium = random.choice(listQuestRandomMedium)

    def questionRandomHard():
        global questRandomHard
        questRandomHard = random.choice(listQuestRandomHard)

    def RemoveQuestionEasy():
        if questRandomEasy == questionEasy1.fullQuestion:
            listQuestRandomEasy.remove(questionEasy1.fullQuestion)
        elif questRandomEasy == questionEasy2.fullQuestion:
            listQuestRandomEasy.remove(questionEasy2.fullQuestion)
        elif questRandomEasy == questionEasy3.fullQuestion:
            listQuestRandomEasy.remove(questionEasy3.fullQuestion)
        elif questRandomEasy == questionEasy4.fullQuestion:
            listQuestRandomEasy.remove(questionEasy4.fullQuestion)
        elif questRandomEasy == questionEasy5.fullQuestion:
            listQuestRandomEasy.remove(questionEasy5.fullQuestion)
        elif questRandomEasy == questionEasy6.fullQuestion:
            listQuestRandomEasy.remove(questionEasy6.fullQuestion)
        elif questRandomEasy == questionEasy7.fullQuestion:
            listQuestRandomEasy.remove(questionEasy7.fullQuestion)
        elif questRandomEasy == questionEasy8.fullQuestion:
            listQuestRandomEasy.remove(questionEasy8.fullQuestion)

    def RemoveQuestionMedium():
        if questRandomMedium == questionMedium1.fullQuestion:
            listQuestRandomMedium.remove(questionMedium1.fullQuestion)
        elif questRandomMedium == questionMedium2.fullQuestion:
            listQuestRandomMedium.remove(questionMedium2.fullQuestion)
        elif questRandomMedium == questionMedium3.fullQuestion:
            listQuestRandomMedium.remove(questionMedium3.fullQuestion)
        elif questRandomMedium == questionMedium4.fullQuestion:
            listQuestRandomMedium.remove(questionMedium4.fullQuestion)
        elif questRandomMedium == questionMedium5.fullQuestion:
            listQuestRandomMedium.remove(questionMedium5.fullQuestion)
        elif questRandomMedium == questionMedium6.fullQuestion:
            listQuestRandomMedium.remove(questionMedium6.fullQuestion)
        elif questRandomMedium == questionMedium7.fullQuestion:
            listQuestRandomMedium.remove(questionMedium7.fullQuestion)
        elif questRandomMedium == questionMedium8.fullQuestion:
            listQuestRandomMedium.remove(questionMedium8.fullQuestion)

    def RemoveQuestionHard():
        if questRandomHard == questionHard1.fullQuestion:
            listQuestRandomHard.remove(questionHard1.fullQuestion)
        elif questRandomHard == questionHard2.fullQuestion:
            listQuestRandomHard.remove(questionHard2.fullQuestion)
        elif questRandomHard == questionHard3.fullQuestion:
            listQuestRandomHard.remove(questionHard3.fullQuestion)
        elif questRandomHard == questionHard4.fullQuestion:
            listQuestRandomHard.remove(questionHard4.fullQuestion)
        elif questRandomHard == questionHard5.fullQuestion:
            listQuestRandomHard.remove(questionHard5.fullQuestion)
        elif questRandomHard == questionHard6.fullQuestion:
            listQuestRandomHard.remove(questionHard6.fullQuestion)
        elif questRandomHard == questionHard7.fullQuestion:
            listQuestRandomHard.remove(questionHard7.fullQuestion)
        elif questRandomHard == questionHard8.fullQuestion:
            listQuestRandomHard.remove(questionHard8.fullQuestion)

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
        if score <= 3:
            if answerPlayer == questRandomEasy[5]:
                score += 1
                startScore = CheckAnswer
                startScore.score()
                printList.RemoveQuestionEasy()
                nextQuest = NextQuestion
                nextQuest.doYouWantToPlayNext()
            elif answerPlayer != questRandomEasy[5]:
                sys.exit()
            if lifebuoyState5050 == 1:
                gui_label_circle_1.config(text='Lifebuoy 50/50:     You do not have this lifebuoy!')
            if lifebuoyStatePhone == 1:
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     You do not have this lifebuoy!')
            if lifebuoyStateAudience == 1:
                gui_label_circle_3.config(text='Lifebuoy help of audience:     You do not have this lifebuoy!')
        elif score > 3 and score <= 7:
            if answerPlayer == questRandomMedium[5]:
                score += 1
                startScore = CheckAnswer
                startScore.score()
                printList.RemoveQuestionMedium()
                nextQuest = NextQuestion
                nextQuest.doYouWantToPlayNext()
            elif answerPlayer != questRandomEasy[5]:
                sys.exit()
        elif score > 7:
            if answerPlayer == questRandomHard[5]:
                score += 1
                startScore = CheckAnswer
                startScore.score()
                printList.RemoveQuestionHard()
                nextQuest = NextQuestion
                nextQuest.doYouWantToPlayNext()
            elif answerPlayer != questRandomEasy[5]:
                sys.exit()

    def score():
        global cash
        global guaranteedCash
        if score == 1:
            cash = 500
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 2:
            cash = 1000
            guaranteedCash = 1000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
            gui_label_exit_cash.config(text='You guaranteed win is: ' + str(guaranteedCash) + ' euro')
        elif score == 3:
            cash = 2000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 4:
            cash = 5000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 5:
            cash = 10000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 6:
            cash = 20000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 7:
            cash = 40000
            guaranteedCash = 40000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
            gui_label_exit_cash.config(text='You guaranteed win is: ' + str(guaranteedCash) + ' euro')
        elif score == 8:
            cash = 75000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 9:
            cash = 125000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 10:
            cash = 250000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 11:
            cash = 500000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
        elif score == 12:
            cash = 1000000
            guaranteedCash = 100000000
            gui_label_current_cash.config(text='You current win: ' + str(cash) + ' euro')
            gui_label_exit_cash.config(text='You guaranteed win is: ' + str(guaranteedCash) + ' euro')

class NextQuestion:
    def doYouWantToPlayNext():
        if score == 2 or score == 7:
            cashGuaranteed = messagebox._show(title='Good Answer!', message='You have guaranteed: ' + str(guaranteedCash) + ' euro! You can safely answer on next question!')
            game_end = 1
        else:
            game_end = messagebox.askyesno(title='Good Answer!', message='Good answer! Do you want to play next? You current win is: ' + str(cash) + ' euro!')
        if game_end == 0:
            game_end = messagebox._show(title='Thank you!', message='Thank you! You win: ' + str(cash) + ' euro!')
            sys.exit()
        elif game_end == 1 and score == 0 or score == 1 or score == 2 or score == 3:
            printList.questionRandomEasy()
            gui_label.config(text=questRandomEasy[0])
            gui_button_a.config(text=questRandomEasy[1])
            gui_button_b.config(text=questRandomEasy[2])
            gui_button_c.config(text=questRandomEasy[3])
            gui_button_d.config(text=questRandomEasy[4])
        elif game_end == 1 and score == 4 or score == 5 or score == 6 or score == 7:
            printList.questionRandomMedium()
            gui_label.config(text=questRandomMedium[0])
            gui_button_a.config(text=questRandomMedium[1])
            gui_button_b.config(text=questRandomMedium[2])
            gui_button_c.config(text=questRandomMedium[3])
            gui_button_d.config(text=questRandomMedium[4])
        elif game_end == 1 and score == 8 or score == 9 or score == 10 or score == 11:
            printList.questionRandomHard()
            gui_label.config(text=questRandomHard[0])
            gui_button_a.config(text=questRandomHard[1])
            gui_button_b.config(text=questRandomHard[2])
            gui_button_c.config(text=questRandomHard[3])
            gui_button_d.config(text=questRandomHard[4])

class Lifebuoy():
    def lifebuoyCrateVarible():
        global exitListFinal5050
        global exitValueFinalPhone
        global a
        global b
        global c
        global d
        global lifebuoyState5050
        global lifebuoyStatePhone
        global lifebuoyStateAudience
        exitListFinal5050 = 0
        exitValueFinalPhone = 0
        a = 0
        b = 0
        c = 0
        d = 0
        lifebuoyState5050 = 0
        lifebuoyStatePhone = 0
        lifebuoyStateAudience = 0

    def lifebuoy5050():
        global lifebuoy5050Value
        global exitPrint5050
        global lifebuoyState5050
        if score < 4:
            listFullQuestionEasy = questRandomEasy
            listLifebuoy5050 = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
        elif score > 3 and score < 9:
            listFullQuestionMedium = questRandomMedium
            listLifebuoy5050 = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
        elif score > 10:
            listFullQuestionHard = questRandomHard
            listLifebuoy5050 = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]

        if lifebuoyState5050 == 0:
            if listLifebuoy5050[4] == 'a':
                listFinal5050 = [listLifebuoy5050[1],listLifebuoy5050[2],listLifebuoy5050[3]]
                goodAnswer5050 = [listLifebuoy5050[0]]
                randomListFinal5050 = random.sample(listFinal5050, 1)
                exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
                exitPrint5050 = random.shuffle(exitListFinal5050)
                gui_label_circle_1.config(text='Lifebuoy 50/50:     One of these answers is good:    ' + str(exitListFinal5050))
                lifebuoyState5050 += 1

            elif listLifebuoy5050[4] == 'b':
                listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[2],listLifebuoy5050[3]]
                goodAnswer5050 = [listLifebuoy5050[1]]
                randomListFinal5050 = random.sample(listFinal5050, 1)
                exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
                exitPrint5050 = random.shuffle(exitListFinal5050)
                gui_label_circle_1.config(text='Lifebuoy 50/50:     One of these answers is good:    ' + str(exitListFinal5050))
                lifebuoyState5050 += 1

            elif listLifebuoy5050[4] == 'c':
                listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[1],listLifebuoy5050[3]]
                goodAnswer5050 = [listLifebuoy5050[2]]
                randomListFinal5050 = random.sample(listFinal5050, 1)
                exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
                exitPrint5050 = random.shuffle(exitListFinal5050)
                gui_label_circle_1.config(text = 'Lifebuoy 50/50:     One of these answers is good:    ' + str(exitListFinal5050))
                lifebuoyState5050 += 1

            elif listLifebuoy5050[4] == 'd':
                listFinal5050 = [listLifebuoy5050[0],listLifebuoy5050[1],listLifebuoy5050[2]]
                goodAnswer5050 = [listLifebuoy5050[3]]
                randomListFinal5050 = random.sample(listFinal5050, 1)
                exitListFinal5050 = [goodAnswer5050,randomListFinal5050]
                exitPrint5050 = random.shuffle(exitListFinal5050)
                gui_label_circle_1.config(text = 'Lifebuoy 50/50:     One of these answers is good:    ' + str(exitListFinal5050))
                lifebuoyState5050 += 1
        else:
            gui_label_circle_1.config(text='Lifebuoy 50/50:     You do not have this lifebuoy!')

    def lifebuoyPhone():
        global lifebuoyPhoneValue
        global lifebuoyStatePhone
        phoneVariantRandom = [1,2,3]
        phoneResultRandom = random.choice(phoneVariantRandom)
        if phoneResultRandom == 1 and lifebuoyStatePhone == 0:
            if score <= 4:
                listFullQuestionEasy = questRandomEasy
                listLifebuoyPhone = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
            elif score > 4 and score < 10:
                listFullQuestionMedium = questRandomMedium
                listLifebuoyPhone = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
            elif score > 10:
                listFullQuestionHard = questRandomHard
                listLifebuoyPhone = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]
            if listLifebuoyPhone[4] == 'a':
                listFinalPhone = [listLifebuoyPhone[1], listLifebuoyPhone[2], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[0]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                exitValueFinalPhone = exitListFinalPhone
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend thinks that one of these answers is good:     ' + str(exitValueFinalPhone))
            elif listLifebuoyPhone[4] == 'b':
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[2], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[1]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                exitValueFinalPhone = exitListFinalPhone
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend thinks that one of these answers is good:     ' + str(exitValueFinalPhone))
            elif listLifebuoyPhone[4] == 'c':
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[1], listLifebuoyPhone[3]]
                goodAnswerPhone = [listLifebuoyPhone[2]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                exitValueFinalPhone = exitListFinalPhone
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend thinks that one of these answers is good:     ' + str(exitValueFinalPhone))
            elif listLifebuoyPhone[4] == 'd':
                listFinalPhone = [listLifebuoyPhone[0], listLifebuoyPhone[1], listLifebuoyPhone[2]]
                goodAnswerPhone = [listLifebuoyPhone[3]]
                randomListFinalPhone = random.sample(listFinalPhone, 1)
                exitListFinalPhone = [goodAnswerPhone, randomListFinalPhone]
                exitPrintPhone = random.shuffle(exitListFinalPhone)
                exitValueFinalPhone = exitListFinalPhone
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend thinks that one of these answers is good:     ' + str(exitValueFinalPhone))
        elif phoneResultRandom == 2 and lifebuoyStatePhone == 0:
            gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend do not to know good answer!')
            lifebuoyStatePhone += 1
        elif phoneResultRandom == 3 and lifebuoyStatePhone == 0:
            if score <= 4:
                listFullQuestionEasy = questRandomEasy
                listLifebuoyPhone = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
                if listLifebuoyPhone[4] == 'a':
                    goodAnswer = [listFullQuestionEasy[1]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'b':
                    goodAnswer = [listFullQuestionEasy[2]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'c':
                    goodAnswer = [listFullQuestionEasy[3]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'd':
                    goodAnswer = [listFullQuestionEasy[4]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
            elif score > 4 and score < 10:
                listFullQuestionMedium = questRandomMedium
                listLifebuoyPhone = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
                if listLifebuoyPhone[4] == 'a':
                    goodAnswer = [listFullQuestionMedium[1]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'b':
                    goodAnswer = [listFullQuestionMedium[2]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'c':
                    goodAnswer = [listFullQuestionMedium[3]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'd':
                    goodAnswer = [listFullQuestionMedium[4]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
            elif score > 10:
                listFullQuestionHard = questRandomHard
                listLifebuoyPhone = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]
                if listLifebuoyPhone[4] == 'a':
                    goodAnswer = [listFullQuestionHard[1]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'b':
                    goodAnswer = [listFullQuestionHard[2]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'c':
                    goodAnswer = [listFullQuestionHard[3]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
                elif listLifebuoyPhone[4] == 'd':
                    goodAnswer = [listFullQuestionHard[4]]
                    exitValueFinalPhone = goodAnswer
                    gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(exitValueFinalPhone))
                    lifebuoyStatePhone += 1
    def lifebuoyAudience():
        global lifebuoyAudienceValue
        global lifebuoyStateAudience
        percent = 100
        a = 0
        b = 0
        c = 0
        d = 0
        if lifebuoyStateAudience == 0:
            if score <= 4:
                listFullQuestionEasy = questRandomEasy
                listLifebuoyAudience = [listFullQuestionEasy[1], listFullQuestionEasy[2], listFullQuestionEasy[3], listFullQuestionEasy[4], listFullQuestionEasy[5]]
            elif score > 4 and score < 10:
                listFullQuestionMedium = questRandomMedium
                listLifebuoyAudience = [listFullQuestionMedium[1], listFullQuestionMedium[2], listFullQuestionMedium[3], listFullQuestionMedium[4], listFullQuestionMedium[5]]
            elif score > 10:
                listFullQuestionHard = questRandomHard
                listLifebuoyAudience = [listFullQuestionHard[1], listFullQuestionHard[2], listFullQuestionHard[3], listFullQuestionHard[4], listFullQuestionHard[5]]
            if listLifebuoyAudience[4] == 'a':
                a += 30
                percent -= 30
            if listLifebuoyAudience[4] == 'b':
                b += 30
                percent -= 30
            if listLifebuoyAudience[4] == 'c':
                c += 30
                percent -= 30
            if listLifebuoyAudience[4] == 'd':
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
            gui_label_circle_3.config(text='Lifebuoy help of audience:     Result vote audience: ' + '    a - ' + str(a) + '%    ' + '    b - ' + str(b) + '%    ' '    c - ' + str(c) + '%    ' '    d - ' + str(d) + '%    ')
            lifebuoyStateAudience += 1
        else:
            gui_label_circle_3.config(text='Lifebuoy help of audience:     You do not have this lifebuoy!')

class ClickButton:
    def clickA():
        global answerPlayer
        answerPlayer = 'a'
        checkAnswer.checkPlayerAnswer()

    def clickB():
        global answerPlayer
        answerPlayer = 'b'
        checkAnswer.checkPlayerAnswer()

    def clickC():
        global answerPlayer
        answerPlayer = 'c'
        checkAnswer.checkPlayerAnswer()

    def clickD():
        global answerPlayer
        answerPlayer = 'd'
        checkAnswer.checkPlayerAnswer()

questionEasy1 = QuestionEasy('What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris', 'a')
questionEasy2 = QuestionEasy('What was the name of the Greek goddess of love?', 'a - Athena', 'b - Aphrodite', 'c - Euterpe', 'd - Hecate', 'b')
questionEasy3 = QuestionEasy('Where will the Mundial 2018?', 'a - Germany', 'b - France', 'c - Russia', 'd - England', 'c')
questionEasy4 = QuestionEasy('Which the sience is called queen every siences?', 'a - Biology', 'b - History', 'c - Physics', 'd - Maths', 'd')
questionEasy5 = QuestionEasy('What city is the capital of China:', 'a - Beijing', 'b - Berlin', 'c - Tokyo', 'd - Moscow', 'a')
questionEasy6 = QuestionEasy('The famous Polish computer game is:', 'a - Silent Hill',  'b - The Witcher', 'c - Fifa', 'd - Resident Evil', 'b')
questionEasy7 = QuestionEasy('Which ocean is the biggest?', 'a - Atlantic Ocean', 'b - Indian Ocean', 'c - Pacific Ocean', 'd - Arctic Ocean', 'c')
questionEasy8 = QuestionEasy('The famous movie which action was in the cosmos is:', 'a - The Predator', 'b - Rambo', 'c - The Terminator', 'd - The Star Wars', 'd')

questionMedium1 = QuestionMedium('Where is Albania?', 'a - Europe', 'b - Asia', 'c - Africa', 'd - South America', 'a')
questionMedium2 = QuestionMedium('The light on the North Pole?', 'a - Rainbow', 'b - Aurora borealis', 'c - Glow', 'd - Mirage', 'b')
questionMedium3 = QuestionMedium('What is the name of the power unit', 'a - Decibel', 'b - Volt', 'c - Watt', 'd - Boron', 'c')
questionMedium4 = QuestionMedium('What is the name the famous car with Italy?', 'a - BMW', 'b - Mercedes', 'c - Maseratti', 'd - Ferrari', 'd')
questionMedium5 = QuestionMedium('The games console made by Microsoft is:', 'a - Xbox', 'b - Pegasus', 'c - Playstation', 'd - Nintendo', 'a')
questionMedium6 = QuestionMedium('What is the name a fameous polish painter which painted darkness pictures?', 'a - Leonardo Davinci', 'b - Zdzisław Beksiński', 'c - Jan Matejko', 'd - Julian Tuwim', 'b')
questionMedium7 = QuestionMedium('How many people live on the world in 2017 year?', 'a - 6.5 billion', 'b - 7 billion', 'c - 7.5 billion', 'd - 8 billion', 'c')
questionMedium8 = QuestionMedium('What is the name the tallest building in the world?', 'a - Freedom Tower, ', 'b - Warsaw Spire', 'c - Empire State Building', 'd - Burdż Chalifa', 'd')

questionHard1 = QuestionHard('Wchich Superhero drew Bob Kane?', 'a - Batman', 'b - Spiderman', 'c - Captain America', 'd - Superman', 'a')
questionHard2 = QuestionHard('How years ago sank The Titanic?', 'a - 1911', 'b - 1912', 'c - 1913', 'd - 1914', 'b')
questionHard3 = QuestionHard('What animal is particulary treat in China?', 'a - Tiger', 'b - Elephant', 'c - Panda', 'd - Bear', 'c')
questionHard4 = QuestionHard('Which place on list the tallest peaks is peak Broad Peak?', 'a - First', 'b - Second', '3 - Fifth', 'd - Twelfth', 'd')
questionHard5 = QuestionHard('What is the marasaka?', 'a - Cherry', 'b - Apple', 'c - Fig', 'd - Pear', 'a')
questionHard6 = QuestionHard('The myrmecology is branch science about:', 'a - Butterflies', 'b - Ants', 'c - Frogs', 'd - Beetles', 'b')
questionHard7 = QuestionHard('Who is director movie "The Matador"?', 'a - Christopher Nolan ', 'b - Andrew Wajda', 'c - Pedro Almodóvar', 'd - Ron Howard', 'c')
questionHard8 = QuestionHard('How many people live in Japan?', 'a - 50 millions', 'b - 85 millions', 'c - 110 millions', 'd - 127 millions', 'd')

lifebuoyAll = Lifebuoy
lifebuoyVarible = Lifebuoy
printList = RandomQuestion
checkAnswer = CheckAnswer
clickButtons = ClickButton
lifebuoyVarible.lifebuoyCrateVarible()
checkAnswer.createVaribleScoreandCash()
printList.createListQuestionEasy()
printList.createListQuestionMedium()
printList.createListQuestionHard()

printList.questionRandomEasy()

gui_label_current_cash = tkinter.Label(gui, text='GET 1 MILLION EUROS!')
gui_label_current_cash.place(y=10, x=390)

gui_label_current_cash = tkinter.Label(gui, text='You current win is: ' + str(cash) + ' euro')
gui_label_current_cash.place(y=60, x=160)

gui_label_exit_cash = tkinter.Label(gui, text='You guaranteed win is: ' + str(guaranteedCash) + ' euro')
gui_label_exit_cash.place(y=60, x=470)

gui_label_quest_number = tkinter.Label(gui, text='Question:')
gui_label_quest_number.place(y=110, x=90)
gui_label = tkinter.Label(gui, text=questRandomEasy[0])
gui_label.place(y=130, x=90)

gui_button_a = tkinter.Button(gui, text=questRandomEasy[1], command=clickButtons.clickA, height = 1, width = 50)
gui_button_a.place(x=70, y=180)

gui_button_b = tkinter.Button(gui, text=questRandomEasy[2], command=clickButtons.clickB, height = 1, width = 50)
gui_button_b.place(x=470, y=180)

gui_button_c = tkinter.Button(gui, text=questRandomEasy[3], command=clickButtons.clickC, height = 1, width = 50)
gui_button_c.place(x=70, y=230)

gui_button_d = tkinter.Button(gui, text=questRandomEasy[4], command=clickButtons.clickD, height = 1, width = 50)
gui_button_d.place(x=470, y=230)

gui_label_circle_1 = tkinter.Label(gui, text='Lifebuoy 50/50:')
gui_label_circle_1.place(y=300, x=10)

gui_label_circle_2 = tkinter.Label(gui, text='Lifebuoy phone to friend:')
gui_label_circle_2.place(y=330, x=10)

gui_label_circle_3 = tkinter.Label(gui, text='Lifebuoy help of audience:')
gui_label_circle_3.place(y=360, x=10)

gui_circle5050 = tkinter.Button(gui, text='Lifebuoy 50/50:', command=lifebuoyAll.lifebuoy5050, height = 1, width = 40)
gui_circle5050.place(x=10, y=400)

gui_circle_audience = tkinter.Button(gui, text='Lifebuoy phone to friend', command=lifebuoyAll.lifebuoyPhone, height = 1, width = 40)
gui_circle_audience.place(x=310, y=400)

gui_circle_phone = tkinter.Button(gui, text='Lifebuoy help of audience', command=lifebuoyAll.lifebuoyAudience, height = 1, width = 40)
gui_circle_phone.place(x=610, y=400)

gui.mainloop()
