from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("My GUI")

# important label options
"""text - adds the Text
bd - background
fg - foreground
font - set the Font
padx - x padding
pady y padding
relief - border styling : - SUNKEN , RAISED, GROOVE, RIDGE"""
 
title_label = Label(text="""Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre
                     of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three
                     stumps.\n The batting side scores runs by striking the ball bowled at one of the wickets with the bat and then
                     running between the wickets, while the bowling and fielding side tries to prevent this (by preventing the ball
                     from leaving the field, and getting the ball to either wicket) and dismiss each batter (so they are "out").
                    \n Means of dismissal include being bowled, when the ball hits the stumps and dislodges the bails,\n and by the
                     fielding side either catching the ball after it is hit by the bat,\n but before it hits the ground, or hitting
                     a wicket with the ball before a batter can cross the crease in front of the wicket.\n When ten batters have
                     been dismissed, the innings ends and the teams swap roles.\n The game is adjudicated by two umpires, aided
                     by a third umpire and match referee in international matches.
                     They communicate with two off-field scorers who record the match's statistical information.\n
                    Forms of cricket range from Twenty20 (also known as T20), with each team batting for a single innings of
                     20 overs (each "over" being a set of 6 fair opportunities for the batting team to score) and the game
                     generally lasting three to four hours,\n to Test matches played over five days. Traditionally cricketers
                     play in all-white kit, but in limited overs cricket they wear club or team colours. In addition to the
                     basic kit,\n some players wear protective gear to prevent injury caused by the ball, which is a hard,
                     solid spheroid made of compressed leather with a slightly raised sewn seam enclosing a cork core layered
                     with tightly wound string.""" , bg='red' , fg='white',padx=44, pady=10 , font=("comicsanssms",9,"bold"),borderwidth=5,relief=SUNKEN)
# important pack options
"""
ANCHOR = 'nw'
side = bottom , top , right , left
fill = 
padx = 
pady = 
"""
title_label.pack(anchor='se',side = LEFT,fill=BOTH,padx=32,pady=30)
root.mainloop() 