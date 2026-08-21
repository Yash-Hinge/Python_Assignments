def ChkVowel(Char):
    if(Char=='a'or Char=='e'or Char=='i' or Char=='o' or Char=='u'or Char=='O'or Char=='A' or Char=='E' or Char=='I' or Char=='U'):
        return True
    
    else:
        return False
    




def main():
    char=str(input("Enter the character:"))

    ret = ChkVowel(char)

    if(ret ==True):
        print("The entered character is vowel.")


    else:
        print("the entered character is consonant.")





if(__name__)=="__main__":
    main()