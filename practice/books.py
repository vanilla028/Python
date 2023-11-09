# 도서 관리 프로그램

class Book:
    def __init__(self, title, author, available=True): # 초기 설정 True(대출 가능)
        self.title = title
        self.author = author
        self.available = available
    
class Library:
    def __init__(self):
        self.books =[]
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book) # books 리스트에 book 추가
        print(f"도서 '{title}'이(가) 추가되었습니다.")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"도서 '{title}'이(가) 삭제되었습니다.")
                return
        print(f"도서 '{title}'을(를) 찾을 수 없습니다.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"도서 정보 - 제목: {book.title}, 저자: {book.author}, 대출 가능 여부: {'대출 가능' if book.available else '대출 불가'}")
                return
        print("찾으시는 도서가 없습니다.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                try:
                    if book.available:
                        book.available=False
                        print(f"도서 '{title}'이(가) 대출되었습니다.")
                    else:
                        print(f"도서 '{title}'은(는) 현재 대출 중입니다.")
                    return
                except AttributeError as e:
                    print(f"에러 발생: {e}")
        print(f"도서 '{title}'을(를) 찾을 수 없습니다.")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"도서 '{title}'이(가) 반납되었습니다.")
                else:
                    print(f"도서 '{title}'은(는) 이미 반납 완료되었습니다.")
                return
        print("대출된 이력이 없거나, 소장 도서가 아닙니다. 관리자에게 문의하세요.")

# 이제 테스트 해보자.
library = Library()
library.add_book("정의란 무엇인가", "마이클 샌델")
library.search_book("정의란 무엇인가")    
        