import os 
from Book import Book 
from common import input_int 
from common import tryinput_int 
class Application: 
    def __init__(self): 
        self.genres= list() 
        self.books = list() 
    def Run(self): 
        self.Load() 
        while True: 
            key = self.SelectMenu() 
            if key == '0': 
                break 
            elif key == '1': 
                self.AddGenre() 
            elif key =='2': 
                self.AddBook() 
            elif key == '3': 
                self.RemoveBook() 
            elif key == '4': 
                self.FindBook() 
            elif key == '5': 
                self.CorrectBook() 
            elif key =='6': 
                self.ViewAll() 
            else: 
                print("잘못 선택하였습니다.") 
            input("엔터 키를 누르세요.") 
        self.Save() 
    def Load(self): 
        print("===Load===") 
        try: 
            self.LoadGenres() 
            self.LoadBooks() 
        except: 
            print("환영합니다.") 
        input("엔터 키를 누르세요.")  
    def SelectMenu(self): 
        os.system("cls") 
        print("== 도서 관리 프로그램 ==") 
        f = open("C:/Users/dlqqj/OneDrive/바탕 화면/eon_7/input.txt", 'r',encoding ='UTF-8')
        data = f.read()
        print(data)
        f.close()
        print("1:장르 추가") 
        print("2:도서 추가") 
        print("3:도서 삭제") 
        print("4:도서 검색") 
        print("5:도서 수정") 
        print("6:전체 보기")
        return input("\n메뉴 입력 ◀:") 
    def AddGenre(self): 
        print("===장르 추가===") 
        self.ViewGenres() 
        genre = input("추가할 장르 명:") 
        self.genres.append(genre) 
    def ViewGenres(self): 
        sz = len(self.genres) 
        for i in range(0,sz): 
            print("{0}:{1}".format(i+1, self.genres[i]),end=' ') 
        print() 
    def AddBook(self): 
        print("===도서 추가===")
        gn = self.SelectGenre()#장르를 선택한다. 
        if gn == 0:#잘못 선택하였을 때 
            print("잘못 선택하였습니다.") 
            return 
        title = input("title:")#title을 입력받는다. 
        sbook = self.Find(title)#title으로 도서를 검색한다. 
        if sbook != None:#검색한 도서가 존재하면 
            print("이미 존재하는 title입니다.") 
            return 
        book = self.MakeBook(title,gn)#도서 개체를 만든다. 
        self.books.append(book)#도서 컬렉션에 추가한다. 
    def SelectGenre(self): 
        self.ViewGenres() 
        gn = input_int("선택할 장르 번호:") 
        if gn>0 and gn<=len(self.genres):
            return gn 
        return 0 
    def Find(self,title): 
        for book in self.books: 
            if book.title == title: 
                return book 
        return None 
    def MakeBook(self,title,gn): 
        year = input("출판연도:") 
        author = input("저자:") 
        publisher = input("출판사:")  
        return Book(title,year,gn,author,publisher) 
    def RemoveBook(self): 
        print("===도서 삭제===") 
        year = input("year:") 
        book =self.Find(year) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.books.remove(book) 
        del book #메모리에서 제거 
        print("삭제하였습니다.") 
    def FindBook(self): 
        print("===도서 검색===") 
        year = input("year:") 
        book =self.Find(year) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.ViewBook(book) 
    def CorrectBook(self):
        print("===도서 수정===")
        
    def ViewAll(self): 
        print("===전체 보기===") 
        f = open("C:/Users/dlqqj/OneDrive/바탕 화면/eon_7/input.txt", 'r',encoding ='UTF-8')
        data = f.read()
        print(data)
        f.close()   
        self.ViewGenres() 
        self.ViewBooks() 
    def ViewBooks(self): 
        print("===추가도서 목록:{0}권".format(len(self.books))) 
        for book in self.books: 
            self.ViewBook(book) 
    def ViewBook(self,book): 
        print("{0}:{1}".format(book.title,book.year)) 
        print("\t장르 번호:",book.gn) 
        print("\t저자:",book.author) 
        print("\t출판사:",book.publisher) 

