import random
def generate_list(): 
     alist=[x for x in range(random.randint(-10,10))]
     return alist
     
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
if __name__ == 'main':
    print("Test printIt():")
    main()
    
    
     