import datetime
import time
import pyttsx3
#------------------------- To-do list app ---------------------------

#------------------------------- wish fuction -----------------------------
def wishMe():
    hour = datetime.datetime.now().hour

    if hour <12:
        print("jay shree ram sir & mam,")
        speak("jay shree ram  sir & mam")
    elif hour<18:
        print("jay bajrangbali ki sir & mam,")
        speak(" jai bajrangbali ki sir & mam")
    else:
        print("jay mata di  sir  & mam ")
        speak("jay mata di sir & mam")

        print("welcome to owr do list app,/")
        speak("welcome to owr do list app,/ ")

#-------------------------------------speak fuction ------------------------
def speak(audio):
    """fuction convert text to specch"""
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150) # speak speed
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    time.sleep(1)#small pause for avoide overlap


#--------------------------  tasks list -------------------------
tasks = []
#-------------------------- add tasks -------------------------
def add_tasks():
    task = input("enter your tasks")
    tasks.append(task) # add new tasks in the empty list
    print("task add successfully/")
    speak("task add succesfully/")
#----------------------------- view tasks fuction -----------------------------------------
def view_task():
    if not tasks:
         print("no tasks availables/n")
         speak("no task available/")
    else:
        print("your tasks")
        speak("here your task")
        for i, task in enumerate(tasks,start=1): # here enumerate use for print number or task together
            print(f"{i}.{task}")
        print()

#------------------------------ remove tasks fuction ---------------------------------
def remove_tasks():
    view_task()
    if tasks:
        try:
            tasks_num = int(input("enter the tasks number for remove"))
            removed = tasks.pop(tasks_num - 1)  # here removed_tasks.pop used for 
            print(f'{removed} tasks removed succesfull')
            speak("your task removed sucessfully/")
        except (ValueError,IndexError):
            print("invalid tasks number")
            speak("ivalid task number")

#----------------------------------- loop apply -------------------------------------
wishMe()
while True: # yaha loop isliye lagya hai taki ye sab line wise print ho or user choose kar sake use kya karna hai ye loop har bar chale
    print(" welcome To do list app")
    speak(" welcome To do list app")
    print("1.add task") 
    speak("1.add task")
    print("2.view task")
    speak("2.view task")
    print("3.remove task")
    speak("3.remove task")
    print("4.exit")
    speak("4.exit")
    speak("enter your choice")
    choice = input("enter your choice")
    
 
#--------------------------------------- fuction call out ------------------------------
    if choice == '1':
        add_tasks()
    elif choice == '2':
        view_task()
    elif choice == '3':
        remove_tasks()
    elif choice == '4':
        print("alwida jai dada pashruam or jai maharanpartap ,exit")
        speak("alwida jai dada pashruam or jai maharanpartap,exit")
        break
    else:
        print("invalid number choice")
        speak("invalid number choice")
    

