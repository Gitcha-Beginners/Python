# -*- coding: utf-8 -*-
import sys

class MyDic:
    def __init__(self):
        self.dicBook = {chr(alpa):[] for alpa in range(97,123)}
        try:
            f = open('words.txt','r')
        except Exception:
            print("파일을 열 수 없습니다")
            sys.exit(-1)

        words = f.read().lower().split()
        words.sort()
        f.close()

        for get in words:
            self.dicBook[get[0]].append(get)


    def start(self):
        menu =0
        while(menu !=6):
            menu = self.showMenu()
            if menu == 1:
                word = input("찾을 단어를 입력 해주세요 : ")
                self.search(word)
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

    def search(self, getWord):
        index = getWord[0]
        tempList = self.dicBook[index]

        if getWord in self.dicBook[index]:
            print("{}단어를 찾았습니다".format(getWord))
        else:
            print("단어를 찾지 못하였습니다")


    def insert(self , getWord):
        index = getWord[0]
        if getWord in self.dicBook[index]:
            print("원래 있는 단어입니다")
        else:
            self.dicBook[index].append(getWord)
            self.dicBook[index].sort()
            print(self.dicBook[index])
            print("{} 단어 추가에 성공했습니다".format(getWord))

    def deleteWord(self,getWord):
        index = getWord[0]
        if getWord not in self.dicBook[index]:
            print("단어가 존재하지 않습니다")
        else:
            self.dicBook.get(index).remove(getWord)
            print("{} 원소 삭제에 성공했습니다".format(getWord))

    def saveDic(self):
        f = open("ResultList.txt","w")
        for i in range(97, 123):
            f.write("{} : ".format(chr(i)))
            f.write(" ".join(self.dicBook[chr(i)]))
            f.write("\n\n")
        f.close()

        f = open("words.txt","w")
        for i in range(97, 123):
            f.write(" ".join(self.dicBook[chr(i)]))

        f.close()

    def selectPrint(self,getCh):
        if(len(getCh) > 1):
            print("올바르지 않은 입력입니다")
            return
        print("{} : ".format(getCh))
        tempList= self.dicBook[getCh]
        print(" ".join(tempList))
        print("\n\n")

temp = MyDic()
temp.start()