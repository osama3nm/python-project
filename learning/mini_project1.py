# Library : view / add / delete / search
library = [                                           # list of dict 
    {"Title":"White Nights", "Author":"A1"},
    {"Title":"The End", "Author":"A2"}
]

# Show All Books Info
def show(books):
    c=1
    for i in books:
        for key,value in i.items():
            print(f"{key} of Book {c} {value}")
        c+=1        



#Search
booktitle = "osama"
def search(book):
    for i in library:
        for key , value in i.items():
            # print(key , value)
            if book == value:
                print( f"The book {value} is founded")
                return True
    print(f"{booktitle} is not founded")
    return False
            
                
# show(library)
# delete(b)
# show(library)   

def delete(bookname):
    if search(bookname):
        for i in library:
            for k,v in i.items():
                if v==bookname:
                    library.remove(i)
                    print(f"{bookname} deleted Successfully")  
                    return       
    else:
        print(f"No book name {bookname} was founded to delete")            
# search(booktitle)
show(library)
search(booktitle)
delete(booktitle)