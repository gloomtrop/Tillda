from pythonds.basic import Stack

class Patient:

    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = int(ålder)

    def __str__(self):
        return self.namn + " " + str(self.ålder) + " år"

class Stack:

    def __init__(self):
        self.top = None
    
    def push(self, x):
        """Lägger x överst på stacken"""
        ny = Node(x)
        ny.next = self.top
        self.top = ny
    
    def pop(self):
        """Plockar ut och returnerar det översta 
        elementet"""
        x = self.top.data
        self.top = self.top.next
        return x
    
    def isEmpty(self):
        """Returnerar True om stacken är tom, False
        annars"""
        if self.top == None:
            return True
        else:
            return False

class Node:

    def __init__(self, x, next = None):
        self.data = x
        self.next = next

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self,x):
        """Stoppar in x sist i kön"""
        ny = Node(x)
        if self.first == None: """Om kön är tom blir
            det på ett sätt...
            ... som du får tänka ut själv."""
        else: """Annars blir det på ett annat sätt...
            ... som du också får klura ut själv."""

    def dequeue(self):
        """Plockar ut och returnerar det som står
        först i kön"""

    def isEmpty(self):
        """Returnerar True om kön är tom, False 
        annars"""
        
def main():
    korridor = Stack()
    with open("patienter.txt", encoding = "utf8") as register:
        for rad in register:
            lista = rad.split()
            namn = lista[0]
            ålder = lista[1]
            p = Patient(namn, ålder)
            if p.ålder < 65:
                korridor.push(p)
            else:
                print("Vaccinerar:", p)
    print("Om vi ginner tar vi också: ")
    while not korridor.isEmpty():
        p = korridor.pop()
        print("\t", p)
main()

