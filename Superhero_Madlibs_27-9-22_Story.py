#Finished at 9/27/22
#With the help of Dayn!! Who helped with Tkinter.
#Mad libs Super hero story!!
from tkinter import *
root = Tk()
root.geometry("550x1000") 
Label(root, text= '"Super Hero" Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root,text="What is your name").pack()
name = Entry(root)
name.pack()
Label(root,text="How old will you be in 10 years ").pack()
age = Entry(root)
age.pack()
Label(root,text="What is your favorite animal").pack()
animal = Entry(root)
animal.pack()
Label(root,text="What is your favorite food? ").pack()
food = Entry(root)
food.pack()
Label(root,text="What is your favorite colour? ").pack()
colour = Entry(root)
colour.pack()
Label(root,text="where do you want to live? ").pack()
home = Entry(root)
home.pack()
Label(root,text="Who is your favorite superhero?  ").pack()
superhero = Entry(root)
superhero.pack()
Label(root,text="Who is your favorite supervillan ").pack()
villan = Entry(root)
villan.pack()
Label(root,text="Which is your favorite superhero team? ").pack()
team = Entry(root)
team.pack()
Label(root,text="What would you call you superhero move? ").pack()
hero_move = Entry(root)
hero_move.pack
Label(root,text="What would be you catchphrase? ")
catchphrase = Entry(root)
catchphrase.pack()
Label(root,text="What would you want to grow up to be?  ").pack()
profession = Entry(root)
profession.pack()
Label(root,text="What does this profession do? ").pack()
profession_do= Entry(root)
profession_do.pack()
Label(root,text="Where do you want to work? ").pack()
work= Entry(root)
work.pack()
def last():
    lasts = Toplevel()

    Label(lasts,text=f"your name is {name.get()} your are {age.get()} years old,you live in {home.get()}. You work at {work.get()} as a {profession.get()} and {profession_do.get()} all day.\n One day the {team.get()} calls you. {superhero.get()} It has retured, {villan.get()} Come fast!! \n You and {colour.get()} {animal.get()} come to fight it. {villan.get()} says' Hahaha You fool' and smashes into the ground. \n{superhero.get()} are thrown from the ground and get hurt really baddly.\n You get up and use your ultimate power called {hero_move.get()} and {villan.get()} dies.\n Everyone cheers and you say {catchphrase.get()}").pack()

    lasts.mainloop()
Button(root,text="Here is your story!",command= last).pack()
root.mainloop()






 