import random
def generate_list():
    alist = [x for x in range(random.randint(1, 10))]
    assert (alist >=0)
    return alist

def printIt():
    print(generate_list())
    
def main():
    printIt()
    
if __name__ == '__main__':
    print("Test printIt() :")
    main()
    
    
    
    
    
     