class todo_list:
    def __init__(self, name):
        self.name=name
        self.lst=[]  
    
    def add(self):
        while True:
            add=input("Enter the task in the todo list otherwise press n for termination: ")
            if add=="n":
                break
            else:
                self.lst+=[add]    
    
    def update(self):
        todo_list.view(self)
        todo_list.add(self)
            
    
    def view(self):
        for i in range(1,1+len(self.lst)):
            print(i,") ",self.lst[i-1],sep="", end="\n")


while True: 
    print("Select:-\n1) create \n2) update \n3) view \n4) exit")
    u_input=int(input('Enter the number according to your choice: '))
    if u_input==1:
            name=input("Enter the name for the todo list: ")
            my_list=todo_list(name)
            my_list.add()              

    elif u_input==2:
            print("Add task to todo list: ")
            my_list.update()


    elif u_input==3 :
            print()
            my_list.view()
            print()

    elif u_input==4:
        break

    else:
        print("Invalid choice! Please select a valid option.")