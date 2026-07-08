import json
class Contact :
    # instantiating the objects
    def __init__(self,name, phone, email, id) :
        self.name = name
        self.phone = phone
        self.email = email
        self.__id =id
    # to display the contact information
    def display (self) :
        print (f"Name  : {self.name }")
        print (f"phone : {self.phone }")
        print (f"email : {self.email }")
        print (f" id   : {self.__id}")
    
    def get_id(self):
        return self.__id
        

# Store contacts in a list of Contact objects in memory.
contact_list = []

# menu-driven loop with operations

while True :
    print ("-- Operations --")
    print ("1. Add new contact")
    print ("2. View all contacts")
    print ("3. Search contact")
    print ("4. Update contact")
    print ("5. Delete contact")
    print ("6. Save and Exit")
    value = int(input( "Enter the operation you want to perform : "))
    match value :
        #  TO ADD NEW CONTACT
        case  1 :
            try:
                print (" to add new contact : ")
                name = input("Enter the name : ")
                number = int(input ( "Enter the number : "))
                email = input ("Enter the email : ")
                new_contact = Contact(name,number,email,len(contact_list)+1)
                contact_list.append(new_contact)
            except IOError :
                print ("Enter valid inputs")
            else:
                print (f"{name} contact is created ")
            
        
        # TO VIEW ALL THE CONTACTS
        case 2 :
            print ( " all contacts :")
            for cont in contact_list:
                print(f"Name  : {cont.name}")
                print(f"phone : {cont.phone}")
                print(f"email : {cont.email}")
                print(" id    :",cont.get_id())
            
        
        # TO SEARCH ANY CONTACT 
        case 3 :
            search_name = input("enter the name of the contact : ")
            for cont in contact_list:
                if search_name in cont.name :
                    flag =True
                else:
                    flag = False
            if flag :
                cont.display()
            else:
                print ("user not found")
            
        
        # TO UPDATE THE EXISTING CONTACT
        case 4 :
            search_name = input("enter the name of the contact :")
            for cont in contact_list:
                if search_name in cont.name :
                    flag =True
                else :
                    flag =False
            if flag:
                print("Choose what you want to update : ")
                print("1. Update name")
                print("2. Update number")
                print("3. Update email")
                num = int(input("Enter the number you want to update : "))
                if num == 1:
                    name = input("enter the new name : ")
                    cont.name = name
                    print(f"{cont.name} is updated successfully")
                elif num == 2:
                    number = int(input ("Enter the new number : "))
                    cont.phone = number
                    print(f"{cont.phone} is updated successfully")
                elif num == 3:
                    email = input("enter the new email : ")
                    cont.email = email
                    print(f"{cont.email} is updated successfully")
                else :
                    print ( "Enter the valid number to update : ")


            else:
                    print ("user not found")
            
        
        # TO DELETE SPECIFIC CONTACT
        case 5 :
            del_cont_name = input(" Enter the contact name you want to delete : ")
            for cont in contact_list:
                if del_cont_name in cont.name :
                    flag = True
                else:
                    flag = False
            if flag:
                contact_list.remove(cont)
                print(f"{cont.name} is deleted successfully")
            else:
                print ("user not found")
            
        
        # TO EXIT FROM THE LOOP 
        case 6 :
            data = {}
            with open ("contacts.json", 'w+') as f:

                for cont in contact_list:
                    contact_dict = {
                        cont.get_id() :[cont.name,cont.phone,cont.email]
                    }
                    json_data = json.dumps(contact_dict)
                    
                json.dump(json_data,f, indent = 4)
            

            print ("contacts are saved and you are exited successfully")
            break
        
        # TO ENSURE VALID OPERATION IN THE LOOP
        case _:
            print("Enter the valid number to perform specific operation")



            


                
           



   
