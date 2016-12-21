import random

class MyDic:
    def __init__(self):

        self.dicBook = [[] for i in range(26)]
        f = open('words.txt','r')
        words = f.read().lower().split()
        words.sort()

        for i in range(0,len(words)):
            self.dicBook[ord(words[i][0]) - 97].append(words[i])
        f.close()

    def start(self):
        menu =0
        while(menu !=6):
            menu = self.showMenu()
            if menu == 1:
                word = input("찾을 단어를 입력 해주세요 : ")
                self.showSearchResult(self.search(word))
            elif menu == 2:
                word = input("추가할 단어를 입력 해주세요 : ")
                self.insert(word)
            elif menu == 3:
                word = input("삭제할 단어를 입력 해주세요 : ")
                self.deleteWord(word)
            elif menu == 4:
                self.saveDic()
            elif menu == 5:
                word = input("출력할 알파벳을 입력 해주세요 : ")
                self.selectPrint(word)
            elif menu == 6:
                return
            else:
                print("올바르지 않은 입력입니다 다시 입력해 주십시오.")


    def showMenu(self):
        print("1. Search 2. Insert 3. Delete 4. Save 5. select print 6. exit")
        return int(input("메뉴를 선택해 주세요 : "))

    def showSearchResult(self,result):
        if result == -1:
            print("단어를 찾지 못하였습니다")
            return
        print("{}단어를 찾았습니다".format(result))


    def search(self, getWord):
        index = ord(getWord[0])-97
        tempList = self.dicBook[index]

        for word in tempList:
            if word == getWord:
                return word
        return -1

    def insert(self , getWord):
        if(self.search(getWord)!=-1):
            print("원래 있는 단어입니다")
        else:
            index = ord(getWord[0])-97
            self.dicBook[index].append(getWord)
            self.dicBook[index].sort()
            print(self.dicBook[index])
            print("{} 단어 추가에 성공했습니다".format(getWord))

    def deleteWord(self,getWord):
        if(self.search(getWord)==-1):
            print("단어가 존재하지 않습니다")
        else:
            index = ord(getWord[0]) - 97
            tempList = self.dicBook[index]
            for wordInfo in enumerate(tempList):
                if wordInfo[1] == getWord:
                    del self.dicBook[index][wordInfo[0]]
                    print("{}번째 원소 삭제에 성공했습니다".format(wordInfo[0]))
                    print(self.dicBook[index])
                    break

    def saveDic(self):
        f = open("ResultList.txt","w")
        for i in range(26):
            f.write("{} : ".format(chr(i+97)))
            f.write(" ".join(self.dicBook[i]))
            f.write("\n\n")
        f.close()

        f = open("words.txt","w")
        for i in range(26):
            f.write(" ".join(self.dicBook[i]))

        f.close()

    def selectPrint(self,getCh):
        if(len(getCh)>1):
            print("올바르지 않은 입력입니다")
            return
        print("{} : ".format(getCh))
        tempList= self.dicBook[ord(getCh)-97]
        print(" ".join(tempList))
        print("\n\n")

temp = MyDic()
temp.start()