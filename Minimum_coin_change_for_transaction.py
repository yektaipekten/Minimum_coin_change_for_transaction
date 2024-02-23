# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 02:52:06 2023

@author: yekta
"""

import tkinter as tk                                                # Call tkinter library a simple algorithm development library
                                                                    # tk is short name we appointed that
# tk._test()


window = tk.Tk()

hasPound = tk.BooleanVar()                                          # Declaring the Boolean  variable for pound
has50p = tk.BooleanVar()                                            # Declaring the Boolean  variable for 50p
has20p = tk.BooleanVar()                                            # Declaring the Boolean  variable for 20p
has10p = tk.BooleanVar()                                            # Declaring the Boolean  variable for 10p
has5p = tk.BooleanVar()                                             # Declaring the Boolean  variable for 5p
has2p = tk.BooleanVar()                                             # Declaring the Boolean  variable for 2p
has1p = tk.BooleanVar()                                             # Declaring the Boolean  variable for 1p

window.title("Change Calculator")                                   # window name
window.iconbitmap("icon4.png")                                      # window icon
window.configure(background='red')                                  # window background
window.geometry("750x500")                                          # window size



coins = {100,50,20,10,5,2,1}                                        # coin identification
rCoins = set()                                                      # the set() function creates a set object

######################################################################

def exitApp():                                                     # when we press Quit, console gonna write "Ending App!"
                                                  
    print("Ending App!")
    window.destroy()
    
######################################################################

def change():                                                      # when we click to boxes it gonna change coins 
    print("Updated ")
    print(f"{lblCoinEntry.get()}")
    
    l_coins = list(coins)
    l_coins.sort(reverse=True)
    value = int(lblCoinEntry.get())
    result = {}
    
    for i in l_coins:
        result[i] = value // i
        value = value % i
    v=""
    
    for i in result:
        if result.get(i) != 0:
            v+= f'{i} : {result[i]}\n'
       
    lblResult.configure(text= f"{v}")
    
######################################################################
    
def exclude(n):                                                    # def exclude variables for if it catch same character 
   
    global coins                                                    # it won't write that character to output
    global rCoins
    c ={100:hasPound.get(),                                         
         50:has50p.get(),
         20:has20p.get(),
         10:has10p.get(),
         5:has5p.get(),
         2:has2p.get(),
         1:has1p.get()
     }.get(n)
    print(f"{n}: {c}")
    if  c:
        print('>>')
        coins = coins - {n}
    else:
        print('<<')
        coins.add(n)
    print(f"Coins available {coins}") 







######################################################################

# Title
lblMachine =tk.Label(text="Change Machine",                          # change machine label's printing type and location
                   font=('Arial Black', 24,'bold'),
                   bg ='red',
                   fg='white') 
lblMachine.grid(row=0,column=2,columnspan=3,pady=(3,10))

######################################################################

#Entry
lblRequired =tk.Label(text="Change Required: ",                      # change required label's printing type and location
                   font=('Arial Black', 12,'bold'),                 
                   bg ='blue',
                   fg='white') 
lblRequired.grid(row=1,column=0, sticky=tk.E, padx=(5,5))

lblCoinEntry =tk.Entry(text="Change Machine",                        # this label's printing type and location
                   font=('Arial Black', 12,'bold') ) 
lblCoinEntry.grid(row=1,column=1, columnspan=6,pady=(5,5) )

######################################################################

#Coin Availability
lblCoins =tk.Label(text="Coins NOT Available:",                      # this label for if coins not Available
                   font=('Arial Black', 12,'bold'),                  # printing type and location
                   bg ='blue',
                   fg='white') 
lblCoins.grid(row=2,column=0,pady=(5,2) )

#####################################################################

# Coins check buttons

cbPound = tk.Checkbutton(window, text="1£", variable=hasPound,       # pound's check button printing type and location
                         font=('Arial', 12,'bold'),                  # printing type and location
                         bg ='yellow',
                         fg='black',
                         command= lambda: exclude(100))
cbPound.grid(row=3, column=1)


cb50p = tk.Checkbutton(window, text="50p", variable=has50p,          # 50P check button printing type and location
                       font=('Arial', 12,'bold'),                    # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(50)) 
cb50p.grid(row=3, column=2)


cb20p = tk.Checkbutton(window, text="20p", variable=has20p,          # 20P check button printing type and location
                       font=('Arial', 12,'bold'),                    # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(20))
cb20p.grid(row=3, column=3)


cb10p = tk.Checkbutton(window, text="10p", variable=has10p,           # 10P check button printing type and location
                       font=('Arial', 12,'bold'),                     # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(10))
cb10p.grid(row=3, column=4)


cb5p = tk.Checkbutton(window, text="5p", variable=has5p,               # 5P check button printing type and location
                       font=('Arial', 12,'bold'),                      # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(5))
cb5p.grid(row=3, column=5)


cb2p = tk.Checkbutton(window, text="2p", variable=has2p,               # 2P check button printing type and location
                       font=('Arial', 12,'bold'),                      # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(2))
cb2p.grid(row=3, column=7)


cb1p = tk.Checkbutton(window, text="1p", variable=has1p,                # 1P check button printing type and location
                       font=('Arial', 12,'bold'),                       # printing type and location
                       bg ='yellow',
                       fg='black',
                       command= lambda: exclude(1))
cb1p.grid(row=3, column=8)

######################################################################

#Result
lblCoins = tk.Label(text="Coin break down:",                            # break down coin label's
                   font=('Georgia Pro Black', 12,'bold'),               # printing type and location
                   bg ='blue',
                   fg='white') 
lblCoins.grid(row=4,column=0)



lblResult = tk.Label(text='Result gonna shown here', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='green',
                   fg='white') 
lblResult.grid(row=5,column=0)


######################################################################



# Exec button
btnExe = tk.Button(text="Exec", command=change,                        # this button for upload number to system
                   font= ('Georgia', 14,'bold'),                       # printing type and location
                   bg = 'green',
                   fg = 'white',
                   width=5,height=2)
btnExe.grid(row=6,column=4)



btnQuit = tk.Button(text="Quit", command=exitApp,                      # this button for exit from the system
                    font= ('Georgia', 14,'bold'),                      # printing type and location
                    bg = 'red',
                    fg = 'white',
                    width=5,height=2)
btnQuit.grid(row=6,column=5)



window.mainloop()                                                      # main loop for run all of them


