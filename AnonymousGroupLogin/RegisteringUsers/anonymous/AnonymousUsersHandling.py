'''
Created on 21 Nov 2011

@author: GIC
'''

class users():
    
    def __init__(self):
        
        self.text_name = "users.txt"
        
        text = open(self.text_name,"r")
        lines  = text.readlines()
        text.close()
        
        self.admins = []
        for line in lines:
            line = line.replace("\n","")
            self.admins.append(line)
            
        #print self.admins
        
    
    def addUser(self, what=None):
        
        if what==None:
            print "There is nothing to save"
            return 0
        users = open(self.text_name,"r")
        temp = users.readlines()
        users.close()
        if (what in temp) or(what+"\n" in temp):
            return 0
        else:
            what =  "\n"+what
            temp.append(what)
            users = open(self.text_name,"w")
            for line in temp:
                users.write(line)
            users.close()
        
    
    
    def removeUser(self):
        
        return 1
    
    def load(self, Person=None):
        
        if Person==None:
            print "There is nothing to load"
            return 0
        
        users = open("users.txt","r")
        lines = users.readlines()
        users.close()
        i = 0
        while i<len(lines):
            if (Person.lower() in lines[i]) or (Person in lines[i]):
                key = lines[i+1]
                secret = lines[i+2]
                break
            i = i + 1
        key = key.replace("\n","")
        secret = secret.replace("\n","")
        return "key=%sPAUSEsecret=%s"%(key,secret)
        
    
    def search_for_user(self, Person=None):
        
        if Person==None:
            print "There is nothing to search"
            return 0
        
        users = open(self.text_name,"r")
        temp = users.readlines()
        users.close()
        
        for line in temp:
            if (Person in line) or (Person.lower() in line):
                return 1
        return 0
        
        
        
        
users = users()
#print admin.search_for_admin(Person="koukouroukou3")
users.addUser(what="koukouroukou3")