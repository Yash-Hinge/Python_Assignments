class BookStore :
    NoofBooks =0

    def __init__(self,Name,Author):
        self.Bookname=Name
        self.BookAuthor=Author
        BookStore.NoofBooks=BookStore.NoofBooks+1



    def Display(self):

        print(self.Bookname,"by",self.BookAuthor,". No.of books :",BookStore.NoofBooks)


    

def main():

    Book = input("Enter the Bookname :")

    Author = input("Enter the Author Name :")


    Bobj1 = BookStore(Book,Author) 

    Bobj1.Display()

    Bobj2 = BookStore(Book,Author) 

    Bobj2.Display()

    Bobj3 = BookStore(Book,Author) 

    Bobj3.Display()





if __name__ =="__main__":
    main()