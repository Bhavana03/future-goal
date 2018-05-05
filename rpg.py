def display(place , items , position,score):
    print("----------------------")
    print(place)
    print("Inventory : ",items)
    pos = position.split()
    if pos[2] == "contain":
        print("----------------------")
    else:
        print(position)
    print("Your score is" , score)
    print("----------------------")
def stop1():
    import sys
    sys.exit("You won the game")
def stop2():
    import sys
    sys.exit("Monster caught you...You lost the game")
def check(item,score):
    if item == "monster":
        print("Your final score is",score)
        stop2()
    else:
        return item 
def check_place(place,score):
    if  place == "garden" and "key" in items and "potion" in items:
        print("Your final score is",score)
        stop1()
def item_present(place,score,item):
    for a, b in house.items():
        if a == place:
            for key in b:
                if "item" in b:
                    if b["item"] in items:
                        return "contain"
                    else:
                        p = check(b["item"],score)
                        return p
                else:
                    return "nothing"
def pla_modify(lists,string,score):
        for a,b in house.items(): 
            if a == string:
                for key in b:
                    if lists[1] in b:
                        score = score + 10
                        print("----------------------")
                        print("Your score is increased by 10")
                        return b[lists[1]] ,score
                    else:
                        print("----------------------")
                        print("You can't go that way")
                        print("Your score is decreased by 10")
                        score = score - 10
                        return string , score
def stat_modify(lists,pos_list):
    if pos_list[2] in items:
        print("-----------------")
    elif lists[1]  ==  pos_list[2]:
        items.append(lists[1])
    else:
        print("----------------------")
        print("You can't get that")
def intro_display():
    print(''' RBG Maze Game
            --------------------
            --------------------
            Reach the garden with key and portion to win
            Stay away from monsters!!
            
            Commands to be given:
                 go  [any direction]
                 get [item(if you find any)] ''')
                 
house = {"library" : {"south" : "balcony"},
                   "balcony":{"north" : "library" , "west" : "hall"},
                   "hall" : {"north" : "diningroom" , "east" : "balcony" , "south" : "garden" , "west" : "guestroom"},
                   "diningroom" : {"south" : "hall" , "west" : "kitchen" , "item" : "key"},
                   "kitchen" : {"east" : "diningroom" , "south":"guestroom" , "item" : "potion"},
                   "guestroom" : {"north" : "kitchen" , "east" : "hall" , "item" : "monster"}, 
                   "garden" : {"north" : "hall"}
                   }
intro_display()
place = "You are in library"
items = []
status = "You see nothing"
score = 0
display(place , items , status,score)
pla_list = place.split()
stat_list = status.split()
while 1:
    inputs = input(">>>" )
    inp_list = inputs.split()
    if inp_list[0] == "go" :
        pre_place , score= pla_modify(inp_list,pla_list[3],score)
        place = place.replace(pla_list[3],pre_place)
        pla_list[3]  = pre_place
        pre_item = item_present(pla_list[3],score,items)
        status = status.replace(stat_list[2] , pre_item)
        stat_list[2] = pre_item
        check_place(pla_list[3],score)
        display(place , items , status,score)
    elif inp_list[0] == "get":
       stat_modify(inp_list , stat_list)
       display(place , items , status,score)
    else :
        display(place , items , status,score)
