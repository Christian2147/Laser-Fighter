# Copyright (C) [2021] [Christian Marinkovich]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Created By: CMarink(aka Christian2147) This is the code for Machine War I.
# This code is currently very messy and needs a lot of cleanup.
# This is game version 1.0.0 released on 12/27/21

import random
import time
import turtle
import winsound

delay = 0.05

# The variables and what they mean:
# score = used for the players score
# death_animation = this is used for when the player dies
# update = these are used for when an enemy gets killed by the player
# dc(num) = used for the death count of each enemy
# moving = used for when the enemies move across the screen
# health_bar = used for the health bars of stronger enemies
# hit_delay = used to delay how often certain enemies can be hit
# god_mode = used for the secret god mode feature

score = 0
death_animation = 0
update_player = 0
update1 = 0
update2 = 0
update3 = 0
update4 = 0
update5 = 0
update6 = 0
update7 = 0
update8 = 0
update9 = 0
update10 = 0
update11 = 0
update12 = 0
update13 = 0
update14 = 0
update15 = 0
update_boss = 0
dc1 = 0
moving1 = 1
dc2 = 0
moving2 = 1
dc3 = 0
moving3 = 1
dc4 = 0
moving4 = 1
dc5 = 0
moving5 = 1
dc6 = 0
moving6 = 1
dc7 = 0
moving7 = 1
dc8 = 0
moving8 = 1
dc9 = 0
moving9 = 1
dc10 = 0
moving10 = 1
dc11 = 0
moving11 = 1
health_bar11 = 2
hit_delay11 = 0
dc12 = 0
moving12 = 1
health_bar12 = 2
hit_delay12 = 0
dc13 = 0
moving13 = 1
health_bar13 = 2
hit_delay13 = 0
dc14 = 0
moving14 = 1
health_bar14 = 2
hit_delay14 = 0
dc15 = 0
moving15 = 1
health_bar15 = 2
hit_delay15 = 0
dc_boss = 0
moving_boss = 1
health_bar_boss = 10
hit_delay_boss = 0
hit_delay_boss2 = 0
hit_delay_boss3 = 0
hit_delay_boss4 = 0
hit_delay_boss5 = 0
hit_delay_boss6 = 0
hit_delay_boss7 = 0
hit_delay_boss8 = 0
hit_delay_boss9 = 0
god_mode = 0

# Used to check if god mode has been set to true or false
file = open("Cheat_Code.txt", "r")
f = file.readlines()
file.close()
file2 = open("Machine War I.txt", "r")
f2 = file2.readlines()
file2.close()
if f == f2:
    god_mode = 1
else:
    god_mode = 0

# Used to check whether sound was previously set to on or off
soundfile = open("Sound.txt", "r")
sound_number = soundfile.readlines()
soundfile.close()
soundfile2 = open("Machine War I #2.txt", "r")
sound_number2 = soundfile2.readlines()
soundfile2.close()
if sound_number == sound_number2:
    sound = 1
else:
    sound = 0

# Used to disable the high score when god mode is on and to set the high_score to what it previously was
if god_mode == 0:
    score_file = open("High_Score.txt", "r")
    high_score_list = score_file.readlines()
    score_file.close()
    high_score_temp = high_score_list[0]
    high_score = int(high_score_temp)
else:
    high_score = "N/A"

# Used to create the windows for the game and to add all the textures that are needed in it
wn = turtle.Screen()
wn.title("Machine War I")
wn.bgpic("Shooting_Game_Background.gif")
wn.setup(width=1280, height=720)
wn.tracer(0)
wn.addshape("Player.gif")
wn.addshape("Player_Laser.gif")
wn.addshape("Enemy(1-5).gif")
wn.addshape("Enemy(1-5)_Laser.gif")
wn.addshape("Enemy(6-10).gif")
wn.addshape("Enemy(6-10)_Laser.gif")
wn.addshape("Enemy(11-15).gif")
wn.addshape("Enemy(11-15)_Laser.gif")
wn.addshape("Boss.gif")
wn.addshape("Boss_Laser.gif")
wn.addshape("Enemy(11-15)_HealthBar_Full.gif")
wn.addshape("Enemy(11-15)_HealthBar_Half.gif")
wn.addshape("Boss_Health10.gif")
wn.addshape("Boss_Health9.gif")
wn.addshape("Boss_Health8.gif")
wn.addshape("Boss_Health7.gif")
wn.addshape("Boss_Health6.gif")
wn.addshape("Boss_Health5.gif")
wn.addshape("Boss_Health4.gif")
wn.addshape("Boss_Health3.gif")
wn.addshape("Boss_Health2.gif")
wn.addshape("Boss_Health1.gif")
wn.addshape("Explosion1.gif")
wn.addshape("Explosion2.gif")

# Lines 162 - 590 is where all the different sprites(turtles) that are needed are created
player = turtle.Turtle()
player.speed(0)
player.shape("Player.gif")
player.color("gray")
player.shapesize(5, 2)
player.penup()
player.goto(0, -300)
player.direction = "stop"
player.showturtle()

laser = turtle.Turtle()
laser.color("green")
laser.shape("Player_Laser.gif")
laser.penup()
laser.speed(0)
laser.shapesize(1, 1)
laser.direction = "down"
laser.left(90)
laser.hideturtle()

score_box = turtle.Turtle()
score_box.speed(0)
score_box.shape("square")
score_box.color("white")
score_box.penup()
score_box.hideturtle()
score_box.goto(0, 320)

god_mode_indicator = turtle.Turtle()
god_mode_indicator.speed(0)
god_mode_indicator.shape("square")
god_mode_indicator.color("white")
god_mode_indicator.penup()
god_mode_indicator.hideturtle()
god_mode_indicator.goto(630, 320)
if god_mode == 1:
    god_mode_indicator.write("God Mode is On!", align="right", font=("Courier", 24, "normal"))
else:
    god_mode_indicator.clear()

sound_text = turtle.Turtle()
sound_text.speed(0)
sound_text.shape("square")
sound_text.color("white")
sound_text.penup()
sound_text.hideturtle()
sound_text.goto(-630, 320)
sound_text.write("Sound: ", align="left", font=("Courier", 24, "normal"))

sound_indicator = turtle.Turtle()
sound_indicator.speed(0)
sound_indicator.shape("square")
sound_indicator.penup()
sound_indicator.hideturtle()
sound_indicator.goto(-515, 320)

enemy1 = turtle.Turtle()
enemy1.color("gray")
enemy1.shape("Enemy(1-5).gif")
enemy1.penup()
enemy1.speed(0)
enemy1.shapesize(2, 2)
enemy1.goto(-200, 220)
enemy1.direction = "down"

enemy2 = turtle.Turtle()
enemy2.color("gray")
enemy2.shape("Enemy(1-5).gif")
enemy2.penup()
enemy2.speed(0)
enemy2.shapesize(2, 2)
enemy2.goto(200, 220)
enemy2.direction = "down"

enemy3 = turtle.Turtle()
enemy3.color("gray")
enemy3.shape("Enemy(1-5).gif")
enemy3.penup()
enemy3.speed(0)
enemy3.shapesize(2, 2)
enemy3.goto(500, 220)
enemy3.direction = "down"

enemy4 = turtle.Turtle()
enemy4.color("gray")
enemy4.shape("Enemy(1-5).gif")
enemy4.penup()
enemy4.speed(0)
enemy4.shapesize(2, 2)
enemy4.goto(-500, 220)
enemy4.direction = "down"
enemy4.hideturtle()

enemy5 = turtle.Turtle()
enemy5.color("gray")
enemy5.shape("Enemy(1-5).gif")
enemy5.penup()
enemy5.speed(0)
enemy5.shapesize(2, 2)
enemy5.goto(-400, 220)
enemy5.direction = "down"
enemy5.hideturtle()

enemy6 = turtle.Turtle()
enemy6.color("gray")
enemy6.shape("Enemy(6-10).gif")
enemy6.penup()
enemy6.speed(0)
enemy6.shapesize(2, 2)
enemy6.goto(-300, 220)
enemy6.direction = "down"
enemy6.hideturtle()

enemy7 = turtle.Turtle()
enemy7.color("gray")
enemy7.shape("Enemy(6-10).gif")
enemy7.penup()
enemy7.speed(0)
enemy7.shapesize(2, 2)
enemy7.goto(-250, 220)
enemy7.direction = "down"
enemy7.hideturtle()

enemy8 = turtle.Turtle()
enemy8.color("gray")
enemy8.shape("Enemy(6-10).gif")
enemy8.penup()
enemy8.speed(0)
enemy8.shapesize(2, 2)
enemy8.goto(250, 220)
enemy8.direction = "down"
enemy8.hideturtle()

enemy9 = turtle.Turtle()
enemy9.color("gray")
enemy9.shape("Enemy(6-10).gif")
enemy9.penup()
enemy9.speed(0)
enemy9.shapesize(2, 2)
enemy9.goto(-350, 220)
enemy9.direction = "down"
enemy9.hideturtle()

enemy10 = turtle.Turtle()
enemy10.color("gray")
enemy10.shape("Enemy(6-10).gif")
enemy10.penup()
enemy10.speed(0)
enemy10.shapesize(2, 2)
enemy10.goto(350, 220)
enemy10.direction = "down"
enemy10.hideturtle()

enemy11 = turtle.Turtle()
enemy11.color("gray")
enemy11.shape("Enemy(11-15).gif")
enemy11.penup()
enemy11.speed(0)
enemy11.shapesize(2, 2)
enemy11.goto(375, 220)
enemy11.direction = "down"
enemy11.hideturtle()

enemy12 = turtle.Turtle()
enemy12.color("gray")
enemy12.shape("Enemy(11-15).gif")
enemy12.penup()
enemy12.speed(0)
enemy12.shapesize(2, 2)
enemy12.goto(-375, 220)
enemy12.direction = "down"
enemy12.hideturtle()

enemy13 = turtle.Turtle()
enemy13.color("gray")
enemy13.shape("Enemy(11-15).gif")
enemy13.penup()
enemy13.speed(0)
enemy13.shapesize(2, 2)
enemy13.goto(325, 220)
enemy13.direction = "down"
enemy13.hideturtle()

enemy14 = turtle.Turtle()
enemy14.color("gray")
enemy14.shape("Enemy(11-15).gif")
enemy14.penup()
enemy14.speed(0)
enemy14.shapesize(2, 2)
enemy14.goto(-325, 220)
enemy14.direction = "down"
enemy14.hideturtle()

enemy15 = turtle.Turtle()
enemy15.color("gray")
enemy15.shape("Enemy(11-15).gif")
enemy15.penup()
enemy15.speed(0)
enemy15.shapesize(2, 2)
enemy15.goto(275, 220)
enemy15.direction = "down"
enemy15.hideturtle()

boss = turtle.Turtle()
boss.color("gray")
boss.shape("Boss.gif")
boss.penup()
boss.speed(0)
boss.shapesize(2, 2)
boss.goto(175, 220)
boss.direction = "down"
boss.hideturtle()

enemy1_laser = turtle.Turtle()
enemy1_laser.color("blue")
enemy1_laser.shape("Enemy(1-5)_Laser.gif")
enemy1_laser.penup()
enemy1_laser.speed(0)
enemy1_laser.shapesize(2.25, 0.5)
enemy1_laser.direction = "down"
enemy1_laser.goto(-200, 140)

enemy2_laser = turtle.Turtle()
enemy2_laser.color("blue")
enemy2_laser.shape("Enemy(1-5)_Laser.gif")
enemy2_laser.penup()
enemy2_laser.speed(0)
enemy2_laser.shapesize(2.25, 0.5)
enemy2_laser.direction = "down"
enemy2_laser.goto(200, 140)

enemy3_laser = turtle.Turtle()
enemy3_laser.color("blue")
enemy3_laser.shape("Enemy(1-5)_Laser.gif")
enemy3_laser.penup()
enemy3_laser.speed(0)
enemy3_laser.shapesize(2.25, 0.5)
enemy3_laser.direction = "down"
enemy3_laser.goto(500, 140)

enemy4_laser = turtle.Turtle()
enemy4_laser.color("blue")
enemy4_laser.shape("Enemy(1-5)_Laser.gif")
enemy4_laser.penup()
enemy4_laser.speed(0)
enemy4_laser.shapesize(2.25, 0.5)
enemy4_laser.direction = "down"
enemy4_laser.goto(-500, 140)
enemy4_laser.hideturtle()

enemy5_laser = turtle.Turtle()
enemy5_laser.color("blue")
enemy5_laser.shape("Enemy(1-5)_Laser.gif")
enemy5_laser.penup()
enemy5_laser.speed(0)
enemy5_laser.shapesize(2.25, 0.5)
enemy5_laser.direction = "down"
enemy5_laser.goto(-400, 140)
enemy5_laser.hideturtle()

enemy6_laser = turtle.Turtle()
enemy6_laser.color("yellow")
enemy6_laser.shape("Enemy(6-10)_Laser.gif")
enemy6_laser.penup()
enemy6_laser.speed(0)
enemy6_laser.shapesize(2.25, 0.5)
enemy6_laser.direction = "down"
enemy6_laser.goto(-300, 140)
enemy6_laser.hideturtle()

enemy7_laser = turtle.Turtle()
enemy7_laser.color("yellow")
enemy7_laser.shape("Enemy(6-10)_Laser.gif")
enemy7_laser.penup()
enemy7_laser.speed(0)
enemy7_laser.shapesize(2.25, 0.5)
enemy7_laser.direction = "down"
enemy7_laser.goto(-250, 140)
enemy7_laser.hideturtle()

enemy8_laser = turtle.Turtle()
enemy8_laser.color("yellow")
enemy8_laser.shape("Enemy(6-10)_Laser.gif")
enemy8_laser.penup()
enemy8_laser.speed(0)
enemy8_laser.shapesize(2.25, 0.5)
enemy8_laser.direction = "down"
enemy8_laser.goto(250, 140)
enemy8_laser.hideturtle()

enemy9_laser = turtle.Turtle()
enemy9_laser.color("yellow")
enemy9_laser.shape("Enemy(6-10)_Laser.gif")
enemy9_laser.penup()
enemy9_laser.speed(0)
enemy9_laser.shapesize(2.25, 0.5)
enemy9_laser.direction = "down"
enemy9_laser.goto(-350, 140)
enemy9_laser.hideturtle()

enemy10_laser = turtle.Turtle()
enemy10_laser.color("yellow")
enemy10_laser.shape("Enemy(6-10)_Laser.gif")
enemy10_laser.penup()
enemy10_laser.speed(0)
enemy10_laser.shapesize(2.25, 0.5)
enemy10_laser.direction = "down"
enemy10_laser.goto(350, 140)
enemy10_laser.hideturtle()

enemy11_laser = turtle.Turtle()
enemy11_laser.color("red")
enemy11_laser.shape("Enemy(11-15)_Laser.gif")
enemy11_laser.penup()
enemy11_laser.speed(0)
enemy11_laser.shapesize(2.25, 0.5)
enemy11_laser.direction = "down"
enemy11_laser.goto(375, 140)
enemy11_laser.hideturtle()

enemy12_laser = turtle.Turtle()
enemy12_laser.color("red")
enemy12_laser.shape("Enemy(11-15)_Laser.gif")
enemy12_laser.penup()
enemy12_laser.speed(0)
enemy12_laser.shapesize(2.25, 0.5)
enemy12_laser.direction = "down"
enemy12_laser.goto(-375, 140)
enemy12_laser.hideturtle()

enemy13_laser = turtle.Turtle()
enemy13_laser.color("red")
enemy13_laser.shape("Enemy(11-15)_Laser.gif")
enemy13_laser.penup()
enemy13_laser.speed(0)
enemy13_laser.shapesize(2.25, 0.5)
enemy13_laser.direction = "down"
enemy13_laser.goto(325, 140)
enemy13_laser.hideturtle()

enemy14_laser = turtle.Turtle()
enemy14_laser.color("red")
enemy14_laser.shape("Enemy(11-15)_Laser.gif")
enemy14_laser.penup()
enemy14_laser.speed(0)
enemy14_laser.shapesize(2.25, 0.5)
enemy14_laser.direction = "down"
enemy14_laser.goto(-325, 140)
enemy14_laser.hideturtle()

enemy15_laser = turtle.Turtle()
enemy15_laser.color("red")
enemy15_laser.shape("Enemy(11-15)_Laser.gif")
enemy15_laser.penup()
enemy15_laser.speed(0)
enemy15_laser.shapesize(2.25, 0.5)
enemy15_laser.direction = "down"
enemy15_laser.goto(275, 140)
enemy15_laser.hideturtle()

boss_laser = turtle.Turtle()
boss_laser.color("pink")
boss_laser.shape("Boss_Laser.gif")
boss_laser.penup()
boss_laser.speed(0)
boss_laser.shapesize(2.25, 0.5)
boss_laser.direction = "down"
boss_laser.goto(175, 140)
boss_laser.hideturtle()

enemy11_health_bar = turtle.Turtle()
enemy11_health_bar.color("green")
enemy11_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
enemy11_health_bar.penup()
enemy11_health_bar.speed(0)
enemy11_health_bar.shapesize(1, 1)
enemy11_health_bar.direction = "down"
enemy11_health_bar.goto(375, 290)
enemy11_health_bar.hideturtle()

enemy12_health_bar = turtle.Turtle()
enemy12_health_bar.color("green")
enemy12_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
enemy12_health_bar.penup()
enemy12_health_bar.speed(0)
enemy12_health_bar.shapesize(1, 1)
enemy12_health_bar.direction = "down"
enemy12_health_bar.goto(-375, 290)
enemy12_health_bar.hideturtle()

enemy13_health_bar = turtle.Turtle()
enemy13_health_bar.color("green")
enemy13_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
enemy13_health_bar.penup()
enemy13_health_bar.speed(0)
enemy13_health_bar.shapesize(1, 1)
enemy13_health_bar.direction = "down"
enemy13_health_bar.goto(325, 290)
enemy13_health_bar.hideturtle()

enemy14_health_bar = turtle.Turtle()
enemy14_health_bar.color("green")
enemy14_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
enemy14_health_bar.penup()
enemy14_health_bar.speed(0)
enemy14_health_bar.shapesize(1, 1)
enemy14_health_bar.direction = "down"
enemy14_health_bar.goto(-325, 290)
enemy14_health_bar.hideturtle()

enemy15_health_bar = turtle.Turtle()
enemy15_health_bar.color("green")
enemy15_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
enemy15_health_bar.penup()
enemy15_health_bar.speed(0)
enemy15_health_bar.shapesize(1, 1)
enemy15_health_bar.direction = "down"
enemy15_health_bar.goto(275, 290)
enemy15_health_bar.hideturtle()

boss_health_bar = turtle.Turtle()
boss_health_bar.color("green")
boss_health_bar.shape("Boss_Health10.gif")
boss_health_bar.penup()
boss_health_bar.speed(0)
boss_health_bar.shapesize(1, 1)
boss_health_bar.direction = "down"
boss_health_bar.goto(175, 290)
boss_health_bar.hideturtle()

# These are all the functions that are used for all the different controls in the game

def go_right():
    player.direction = "right"
    move()

def go_left():
    player.direction = "left"
    move()

def move():
    if player.direction == "left" and player.xcor() > -620 and death_animation == 0:
        x = player.xcor()
        player.setx(x - 30)

    if player.direction == "right" and player.xcor() < 620 and death_animation == 0:
        x = player.xcor()
        player.setx(x + 30)

def shoot():
    if laser.ycor() > 359 and death_animation == 0:
        laser.showturtle()
        if sound == 1:
            winsound.PlaySound("Gun_Sound.wav", winsound.SND_ASYNC)
        x = player.xcor()
        y = player.ycor()
        laser.setx(x)
        laser.sety(y + 100)

def toggle_sound():
    soundfile = open("Sound.txt", "r")
    sound = soundfile.readlines()
    soundfile.close()
    soundfile2 = open("Machine War I #2.txt", "r")
    sound2 = soundfile2.readlines()
    soundfile2.close()
    if sound == sound2:
        soundupdate = open("Sound.txt", "w")
        soundupdate.writelines("Sound = 0")
        soundupdate.close()
    else:
        soundupdate = open("Sound.txt", "w")
        soundupdate.writelines("Sound = 1")
        soundupdate.close()

wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(shoot, "space")
wn.onkeypress(toggle_sound, "v")

# The code inside this loop is everything that needs to be checked at every delay tick, which is set to 0.05
while True:
    wn.update()

    # This is used for when the player fires his laser. If it reaches the edge of the screen, it goes back to him
    if laser.ycor() < 360:
        laser.direction = "up"
        laser.forward(30)
    else:
        laser.hideturtle()

    # Lines 655 - 992 is used for updating the lasers of all the enemies in the game
    if enemy1_laser.ycor() > -360:
        enemy1_laser.direction = "down"
        YL = enemy1_laser.ycor()
        enemy1_laser.sety(YL - 20)
    else:
        x = enemy1.xcor()
        y = enemy1.ycor()
        enemy1_laser.setx(x)
        enemy1_laser.sety(y - 80)

    if enemy2_laser.ycor() > -360:
        enemy2_laser.direction = "down"
        YL = enemy2_laser.ycor()
        enemy2_laser.sety(YL - 20)
    else:
        x = enemy2.xcor()
        y = enemy2.ycor()
        enemy2_laser.setx(x)
        enemy2_laser.sety(y - 80)

    if enemy3_laser.ycor() > -360:
        enemy3_laser.direction = "down"
        YL = enemy3_laser.ycor()
        enemy3_laser.sety(YL - 20)
    else:
        x = enemy3.xcor()
        y = enemy3.ycor()
        enemy3_laser.setx(x)
        enemy3_laser.sety(y - 80)

    if score >= 5:
        enemy4.showturtle()
        enemy4_laser.showturtle()
        if enemy4_laser.ycor() > -360:
            enemy4_laser.direction = "down"
            YL = enemy4_laser.ycor()
            enemy4_laser.sety(YL - 20)
        else:
            x = enemy4.xcor()
            y = enemy4.ycor()
            enemy4_laser.setx(x)
            enemy4_laser.sety(y - 80)
    else:
        enemy4.hideturtle()
        enemy4_laser.hideturtle()
        x = enemy4.xcor()
        y = enemy4.ycor()
        enemy4_laser.setx(x)
        enemy4_laser.sety(y - 80)

    if score >= 10:
        enemy5.showturtle()
        enemy5_laser.showturtle()
        if enemy5_laser.ycor() > -360:
            enemy5_laser.direction = "down"
            YL = enemy5_laser.ycor()
            enemy5_laser.sety(YL - 20)
        else:
            x = enemy5.xcor()
            y = enemy5.ycor()
            enemy5_laser.setx(x)
            enemy5_laser.sety(y - 80)
    else:
        enemy5.hideturtle()
        enemy5_laser.hideturtle()
        x = enemy5.xcor()
        y = enemy5.ycor()
        enemy5_laser.setx(x)
        enemy5_laser.sety(y - 80)

    if score >= 15:
        enemy6.showturtle()
        enemy6_laser.showturtle()
        if enemy6_laser.ycor() > -360:
            enemy6_laser.direction = "down"
            YL = enemy6_laser.ycor()
            enemy6_laser.sety(YL - 30)
        else:
            x = enemy6.xcor()
            y = enemy6.ycor()
            enemy6_laser.setx(x)
            enemy6_laser.sety(y - 80)
    else:
        enemy6.hideturtle()
        enemy6_laser.hideturtle()
        x = enemy6.xcor()
        y = enemy6.ycor()
        enemy6_laser.setx(x)
        enemy6_laser.sety(y - 80)

    if score >= 20:
        enemy7.showturtle()
        enemy7_laser.showturtle()
        if enemy7_laser.ycor() > -360:
            enemy7_laser.direction = "down"
            YL = enemy7_laser.ycor()
            enemy7_laser.sety(YL - 30)
        else:
            x = enemy7.xcor()
            y = enemy7.ycor()
            enemy7_laser.setx(x)
            enemy7_laser.sety(y - 80)
    else:
        enemy7.hideturtle()
        enemy7_laser.hideturtle()
        x = enemy7.xcor()
        y = enemy7.ycor()
        enemy7_laser.setx(x)
        enemy7_laser.sety(y - 80)

    if score >= 25:
        enemy8.showturtle()
        enemy8_laser.showturtle()
        if enemy8_laser.ycor() > -360:
            enemy8_laser.direction = "down"
            YL = enemy8_laser.ycor()
            enemy8_laser.sety(YL - 30)
        else:
            x = enemy8.xcor()
            y = enemy8.ycor()
            enemy8_laser.setx(x)
            enemy8_laser.sety(y - 80)
    else:
        enemy8.hideturtle()
        enemy8_laser.hideturtle()
        x = enemy8.xcor()
        y = enemy8.ycor()
        enemy8_laser.setx(x)
        enemy8_laser.sety(y - 80)

    if score >= 30:
        enemy9.showturtle()
        enemy9_laser.showturtle()
        if enemy9_laser.ycor() > -360:
            enemy9_laser.direction = "down"
            YL = enemy9_laser.ycor()
            enemy9_laser.sety(YL - 30)
        else:
            x = enemy9.xcor()
            y = enemy9.ycor()
            enemy9_laser.setx(x)
            enemy9_laser.sety(y - 80)
    else:
        enemy9.hideturtle()
        enemy9_laser.hideturtle()
        x = enemy9.xcor()
        y = enemy9.ycor()
        enemy9_laser.setx(x)
        enemy9_laser.sety(y - 80)

    if score >= 35:
        enemy10.showturtle()
        enemy10_laser.showturtle()
        if enemy10_laser.ycor() > -360:
            enemy10_laser.direction = "down"
            YL = enemy10_laser.ycor()
            enemy10_laser.sety(YL - 30)
        else:
            x = enemy10.xcor()
            y = enemy10.ycor()
            enemy10_laser.setx(x)
            enemy10_laser.sety(y - 80)
    else:
        enemy10.hideturtle()
        enemy10_laser.hideturtle()
        x = enemy10.xcor()
        y = enemy10.ycor()
        enemy10_laser.setx(x)
        enemy10_laser.sety(y - 80)

    if score >= 40:
        if update11 == 0:
            enemy11.showturtle()
            enemy11_laser.showturtle()
            enemy11_health_bar.showturtle()
        if enemy11_laser.ycor() > -360:
            enemy11_laser.direction = "down"
            YL = enemy11_laser.ycor()
            enemy11_laser.sety(YL - 40)
        else:
            x = enemy11.xcor()
            y = enemy11.ycor()
            enemy11_laser.setx(x)
            enemy11_laser.sety(y - 80)
    else:
        if update11 == 0:
            enemy11.hideturtle()
            enemy11_laser.hideturtle()
            enemy11_health_bar.hideturtle()
            enemy11_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
            health_bar11 = 2
            x = enemy11.xcor()
            y = enemy11.ycor()
            enemy11_laser.setx(x)
            enemy11_laser.sety(y - 80)

    if score >= 50:
        if update12 == 0:
            enemy12.showturtle()
            enemy12_laser.showturtle()
            enemy12_health_bar.showturtle()
        if enemy12_laser.ycor() > -360:
            enemy12_laser.direction = "down"
            YL = enemy12_laser.ycor()
            enemy12_laser.sety(YL - 40)
        else:
            x = enemy12.xcor()
            y = enemy12.ycor()
            enemy12_laser.setx(x)
            enemy12_laser.sety(y - 80)
    else:
        if update12 == 0:
            enemy12.hideturtle()
            enemy12_laser.hideturtle()
            enemy12_health_bar.hideturtle()
            enemy12_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
            health_bar12 = 2
            x = enemy12.xcor()
            y = enemy12.ycor()
            enemy12_laser.setx(x)
            enemy12_laser.sety(y - 80)

    if score >= 60:
        if update13 == 0:
            enemy13.showturtle()
            enemy13_laser.showturtle()
            enemy13_health_bar.showturtle()
        if enemy13_laser.ycor() > -360:
            enemy13_laser.direction = "down"
            YL = enemy13_laser.ycor()
            enemy13_laser.sety(YL - 40)
        else:
            x = enemy13.xcor()
            y = enemy13.ycor()
            enemy13_laser.setx(x)
            enemy13_laser.sety(y - 80)
    else:
        if update13 == 0:
            enemy13.hideturtle()
            enemy13_laser.hideturtle()
            enemy13_health_bar.hideturtle()
            enemy13_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
            health_bar13 = 2
            x = enemy13.xcor()
            y = enemy13.ycor()
            enemy13_laser.setx(x)
            enemy13_laser.sety(y - 80)

    if score >= 70:
        if update14 == 0:
            enemy14.showturtle()
            enemy14_laser.showturtle()
            enemy14_health_bar.showturtle()
        if enemy14_laser.ycor() > -360:
            enemy14_laser.direction = "down"
            YL = enemy14_laser.ycor()
            enemy14_laser.sety(YL - 40)
        else:
            x = enemy14.xcor()
            y = enemy14.ycor()
            enemy14_laser.setx(x)
            enemy14_laser.sety(y - 80)
    else:
        if update14 == 0:
            enemy14.hideturtle()
            enemy14_laser.hideturtle()
            enemy14_health_bar.hideturtle()
            enemy14_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
            health_bar14 = 2
            x = enemy14.xcor()
            y = enemy14.ycor()
            enemy14_laser.setx(x)
            enemy14_laser.sety(y - 80)

    if score >= 80:
        if update15 == 0:
            enemy15.showturtle()
            enemy15_laser.showturtle()
            enemy15_health_bar.showturtle()
        if enemy15_laser.ycor() > -360:
            enemy15_laser.direction = "down"
            YL = enemy15_laser.ycor()
            enemy15_laser.sety(YL - 40)
        else:
            x = enemy15.xcor()
            y = enemy15.ycor()
            enemy15_laser.setx(x)
            enemy15_laser.sety(y - 80)
    else:
        if update15 == 0:
            enemy15.hideturtle()
            enemy15_laser.hideturtle()
            enemy15_health_bar.hideturtle()
            enemy15_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
            health_bar15 = 2
            x = enemy15.xcor()
            y = enemy15.ycor()
            enemy15_laser.setx(x)
            enemy15_laser.sety(y - 80)

    if score >= 100:
        if update_boss == 0:
            boss.showturtle()
            boss_laser.showturtle()
            boss_health_bar.showturtle()
        if boss_laser.ycor() > -360:
            boss_laser.direction = "down"
            if 10 >= health_bar_boss > 8:
                YL = boss_laser.ycor()
                boss_laser.sety(YL - 35)
            if 8 >= health_bar_boss > 6:
                YL = boss_laser.ycor()
                boss_laser.sety(YL - 40)
            if 6 >= health_bar_boss > 4:
                YL = boss_laser.ycor()
                boss_laser.sety(YL - 45)
            if 4 >= health_bar_boss > 2:
                YL = boss_laser.ycor()
                boss_laser.sety(YL - 50)
            if 2 >= health_bar_boss > -1:
                YL = boss_laser.ycor()
                boss_laser.sety(YL - 55)
        else:
            x = boss.xcor()
            y = boss.ycor()
            boss_laser.setx(x)
            boss_laser.sety(y - 80)
    else:
        if update_boss == 0:
            boss.hideturtle()
            boss_laser.hideturtle()
            boss_health_bar.hideturtle()
            boss_health_bar.shape("Boss_Health10.gif")
            health_bar_boss = 10
            x = boss.xcor()
            y = boss.ycor()
            boss_laser.setx(x)
            boss_laser.sety(y - 80)

    # Lines 995 - 1815 is for what happens when the enemies die
    if update1 == 6:
        enemy1.showturtle()
        update1 = 0

    if update1 == 5:
        update1 = 6

    if update1 == 4:
        update1 = 5

    if update1 == 3:
        enemy1.hideturtle()
        enemy1.shape("Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy1.goto(x, 220)
        update1 = 4

    if update1 == 2:
        update1 = 3

    if update1 == 1:
        enemy1.shape("Explosion2.gif")
        update1 = 2

    if laser.distance(enemy1) < 55:
        if update1 == 0:
            score = score + 1
            dc1 = dc1 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy1.shape("Explosion1.gif")
        update1 = 1

    if update2 == 6:
        enemy2.showturtle()
        update2 = 0

    if update2 == 5:
        update2 = 6

    if update2 == 4:
        update2 = 5

    if update2 == 3:
        enemy2.hideturtle()
        enemy2.shape("Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy2.goto(x, 220)
        update2 = 4

    if update2 == 2:
        update2 = 3

    if update2 == 1:
        enemy2.shape("Explosion2.gif")
        update2 = 2

    if laser.distance(enemy2) < 55:
        if update2 == 0:
            score = score + 1
            dc2 = dc2 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy2.shape("Explosion1.gif")
        update2 = 1

    if update3 == 6:
        enemy3.showturtle()
        update3 = 0

    if update3 == 5:
        update3 = 6

    if update3 == 4:
        update3 = 5

    if update3 == 3:
        enemy3.hideturtle()
        enemy3.shape("Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy3.goto(x, 220)
        update3 = 4

    if update3 == 2:
        update3 = 3

    if update3 == 1:
        enemy3.shape("Explosion2.gif")
        update3 = 2

    if laser.distance(enemy3) < 55:
        if update3 == 0:
            score = score + 1
            dc3 = dc3 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy3.shape("Explosion1.gif")
        update3 = 1

    if update4 == 6:
        enemy4.showturtle()
        update4 = 0

    if update4 == 5:
        update4 = 6

    if update4 == 4:
        update4 = 5

    if update4 == 3:
        enemy4.hideturtle()
        enemy4.shape("Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy4.goto(x, 220)
        update4 = 4

    if update4 == 2:
        update4 = 3

    if update4 == 1:
        enemy4.shape("Explosion2.gif")
        update4 = 2

    if enemy4.isvisible() and laser.distance(enemy4) < 55:
        if update4 == 0:
            score = score + 1
            dc4 = dc4 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy4.shape("Explosion1.gif")
        update4 = 1

    if update5 == 6:
        enemy5.showturtle()
        update5 = 0

    if update5 == 5:
        update5 = 6

    if update5 == 4:
        update5 = 5

    if update5 == 3:
        enemy5.hideturtle()
        enemy5.shape("Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy5.goto(x, 220)
        update5 = 4

    if update5 == 2:
        update5 = 3

    if update5 == 1:
        enemy5.shape("Explosion2.gif")
        update5 = 2

    if enemy5.isvisible() and laser.distance(enemy5) < 55:
        if update5 == 0:
            score = score + 1
            dc5 = dc5 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy5.shape("Explosion1.gif")
        update5 = 1

    if update6 == 6:
        enemy6.showturtle()
        update6 = 0

    if update6 == 5:
        update6 = 6

    if update6 == 4:
        update6 = 5

    if update6 == 3:
        enemy6.hideturtle()
        enemy6.shape("Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy6.goto(x, 220)
        update6 = 4

    if update6 == 2:
        update6 = 3

    if update6 == 1:
        enemy6.shape("Explosion2.gif")
        update6 = 2

    if enemy6.isvisible() and laser.distance(enemy6) < 55:
        if update6 == 0:
            score = score + 2
            dc6 = dc6 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy6.shape("Explosion1.gif")
        update6 = 1

    if update7 == 6:
        enemy7.showturtle()
        update7 = 0

    if update7 == 5:
        update7 = 6

    if update7 == 4:
        update7 = 5

    if update7 == 3:
        enemy7.hideturtle()
        enemy7.shape("Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy7.goto(x, 220)
        update7 = 4

    if update7 == 2:
        update7 = 3

    if update7 == 1:
        enemy7.shape("Explosion2.gif")
        update7 = 2

    if enemy7.isvisible() and laser.distance(enemy7) < 55:
        if update7 == 0:
            score = score + 2
            dc7 = dc7 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy7.shape("Explosion1.gif")
        update7 = 1

    if update8 == 6:
        enemy8.showturtle()
        update8 = 0

    if update8 == 5:
        update8 = 6

    if update8 == 4:
        update8 = 5

    if update8 == 3:
        enemy8.hideturtle()
        enemy8.shape("Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy8.goto(x, 220)
        update8 = 4

    if update8 == 2:
        update8 = 3

    if update8 == 1:
        enemy8.shape("Explosion2.gif")
        update8 = 2

    if enemy8.isvisible() and laser.distance(enemy8) < 55:
        if update8 == 0:
            score = score + 2
            dc8 = dc8 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy8.shape("Explosion1.gif")
        update8 = 1

    if update9 == 6:
        enemy9.showturtle()
        update9 = 0

    if update9 == 5:
        update9 = 6

    if update9 == 4:
        update9 = 5

    if update9 == 3:
        enemy9.hideturtle()
        enemy9.shape("Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy9.goto(x, 220)
        update9 = 4

    if update9 == 2:
        update9 = 3

    if update9 == 1:
        enemy9.shape("Explosion2.gif")
        update9 = 2

    if enemy9.isvisible() and laser.distance(enemy9) < 55:
        if update9 == 0:
            score = score + 2
            dc9 = dc9 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy9.shape("Explosion1.gif")
        update9 = 1

    if update10 == 6:
        enemy10.showturtle()
        update10 = 0

    if update10 == 5:
        update10 = 6

    if update10 == 4:
        update10 = 5

    if update10 == 3:
        enemy10.hideturtle()
        enemy10.shape("Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy10.goto(x, 220)
        update10 = 4

    if update10 == 2:
        update10 = 3

    if update10 == 1:
        enemy10.shape("Explosion2.gif")
        update10 = 2

    if enemy10.isvisible() and laser.distance(enemy10) < 55:
        if update10 == 0:
            score = score + 2
            dc10 = dc10 + 1
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        enemy10.shape("Explosion1.gif")
        update10 = 1

    if update11 == 6:
        enemy11.showturtle()
        enemy11_health_bar.showturtle()
        update11 = 0

    if update11 == 5:
        update11 = 6

    if update11 == 4:
        x = enemy11.xcor()
        enemy11_health_bar.goto(x, 290)
        enemy11_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
        health_bar11 = 2
        update11 = 5

    if update11 == 3:
        enemy11.hideturtle()
        enemy11.shape("Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy11.goto(x, 220)
        update11 = 4

    if update11 == 2:
        update11 = 3

    if update11 == 1:
        enemy11.shape("Explosion2.gif")
        update11 = 2

    if enemy11.isvisible() and laser.distance(enemy11) < 55 and health_bar11 == 1 and hit_delay11 == 0:
        if update11 == 0:
            score = score + 5
            dc11 = dc11 + 1
            health_bar11 = 0
            enemy11_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            enemy11.shape("Explosion1.gif")
            update11 = 1

    if hit_delay11 == 3:
        hit_delay11 = 0

    if hit_delay11 == 2:
        hit_delay11 = 3

    if hit_delay11 == 1:
        hit_delay11 = 2

    if enemy11.isvisible() and laser.distance(enemy11) < 55 and health_bar11 == 2:
        if update11 == 0:
            score = score + 1
            enemy11_health_bar.shape("Enemy(11-15)_HealthBar_Half.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar11 = 1
            hit_delay11 = 1

    if update12 == 6:
        enemy12.showturtle()
        enemy12_health_bar.showturtle()
        update12 = 0

    if update12 == 5:
        update12 = 6

    if update12 == 4:
        x = enemy12.xcor()
        enemy12_health_bar.goto(x, 290)
        enemy12_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
        health_bar12 = 2
        update12 = 5

    if update12 == 3:
        enemy12.hideturtle()
        enemy12.shape("Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy12.goto(x, 220)
        update12 = 4

    if update12 == 2:
        update12 = 3

    if update12 == 1:
        enemy12.shape("Explosion2.gif")
        update12 = 2

    if enemy12.isvisible() and laser.distance(enemy12) < 55 and health_bar12 == 1 and hit_delay12 == 0:
        if update12 == 0:
            score = score + 5
            dc12 = dc12 + 1
            health_bar12 = 0
            enemy12_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            enemy12.shape("Explosion1.gif")
            update12 = 1

    if hit_delay12 == 3:
        hit_delay12 = 0

    if hit_delay12 == 2:
        hit_delay12 = 3

    if hit_delay12 == 1:
        hit_delay12 = 2

    if enemy12.isvisible() and laser.distance(enemy12) < 55 and health_bar12 == 2:
        if update12 == 0:
            score = score + 1
            enemy12_health_bar.shape("Enemy(11-15)_HealthBar_Half.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar12 = 1
            hit_delay12 = 1

    if update13 == 6:
        enemy13.showturtle()
        enemy13_health_bar.showturtle()
        update13 = 0

    if update13 == 5:
        update13 = 6

    if update13 == 4:
        x = enemy13.xcor()
        enemy13_health_bar.goto(x, 290)
        enemy13_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
        health_bar13 = 2
        update13 = 5

    if update13 == 3:
        enemy13.hideturtle()
        enemy13.shape("Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy13.goto(x, 220)
        update13 = 4

    if update13 == 2:
        update13 = 3

    if update13 == 1:
        enemy13.shape("Explosion2.gif")
        update13 = 2

    if enemy13.isvisible() and laser.distance(enemy13) < 55 and health_bar13 == 1 and hit_delay13 == 0:
        if update13 == 0:
            score = score + 5
            dc13 = dc13 + 1
            health_bar13 = 0
            enemy13_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            enemy13.shape("Explosion1.gif")
            update13 = 1

    if hit_delay13 == 3:
        hit_delay13 = 0

    if hit_delay13 == 2:
        hit_delay13 = 3

    if hit_delay13 == 1:
        hit_delay13 = 2

    if enemy13.isvisible() and laser.distance(enemy13) < 55 and health_bar13 == 2:
        if update13 == 0:
            score = score + 1
            enemy13_health_bar.shape("Enemy(11-15)_HealthBar_Half.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar13 = 1
            hit_delay13 = 1

    if update14 == 6:
        enemy14.showturtle()
        enemy14_health_bar.showturtle()
        update14 = 0

    if update14 == 5:
        update14 = 6

    if update14 == 4:
        x = enemy14.xcor()
        enemy14_health_bar.goto(x, 290)
        enemy14_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
        health_bar14 = 2
        update14 = 5

    if update14 == 3:
        enemy14.hideturtle()
        enemy14.shape("Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy14.goto(x, 220)
        update14 = 4

    if update14 == 2:
        update14 = 3

    if update14 == 1:
        enemy14.shape("Explosion2.gif")
        update14 = 2

    if enemy14.isvisible() and laser.distance(enemy14) < 55 and health_bar14 == 1 and hit_delay14 == 0:
        if update14 == 0:
            score = score + 5
            dc14 = dc14 + 1
            health_bar14 = 0
            enemy14_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            enemy14.shape("Explosion1.gif")
            update14 = 1

    if hit_delay14 == 3:
        hit_delay14 = 0

    if hit_delay14 == 2:
        hit_delay14 = 3

    if hit_delay14 == 1:
        hit_delay14 = 2

    if enemy14.isvisible() and laser.distance(enemy14) < 55 and health_bar14 == 2:
        if update14 == 0:
            score = score + 1
            enemy14_health_bar.shape("Enemy(11-15)_HealthBar_Half.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar14 = 1
            hit_delay14 = 1

    if update15 == 6:
        enemy15.showturtle()
        enemy15_health_bar.showturtle()
        update15 = 0

    if update15 == 5:
        update15 = 6

    if update15 == 4:
        x = enemy15.xcor()
        enemy15_health_bar.goto(x, 290)
        enemy15_health_bar.shape("Enemy(11-15)_HealthBar_Full.gif")
        health_bar15 = 2
        update15 = 5

    if update15 == 3:
        enemy15.hideturtle()
        enemy15.shape("Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy15.goto(x, 220)
        update15 = 4

    if update15 == 2:
        update15 = 3

    if update15 == 1:
        enemy15.shape("Explosion2.gif")
        update15 = 2

    if enemy15.isvisible() and laser.distance(enemy15) < 55 and health_bar15 == 1 and hit_delay15 == 0:
        if update15 == 0:
            score = score + 5
            dc15 = dc15 + 1
            health_bar15 = 0
            enemy15_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            enemy15.shape("Explosion1.gif")
            update15 = 1

    if hit_delay15 == 3:
        hit_delay15 = 0

    if hit_delay15 == 2:
        hit_delay15 = 3

    if hit_delay15 == 1:
        hit_delay15 = 2

    if enemy15.isvisible() and laser.distance(enemy15) < 55 and health_bar15 == 2:
        if update15 == 0:
            score = score + 1
            enemy15_health_bar.shape("Enemy(11-15)_HealthBar_Half.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar15 = 1
            hit_delay15 = 1

    if update_boss == 6:
        boss.showturtle()
        boss_health_bar.showturtle()
        update_boss = 0

    if update_boss == 5:
        update_boss = 6

    if update_boss == 4:
        x = boss.xcor()
        boss_health_bar.goto(x, 290)
        boss_health_bar.shape("Boss_Health10.gif")
        health_bar_boss = 10
        update_boss = 5

    if update_boss == 3:
        boss.hideturtle()
        boss.shape("Boss.gif")
        x = random.randint(-640, 640)
        boss.goto(x, 220)
        update_boss = 4

    if update_boss == 2:
        update_boss = 3

    if update_boss == 1:
        boss.shape("Explosion2.gif")
        update_boss = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 1 and hit_delay_boss9 == 0:
        if update_boss == 0:
            score = score + 50
            dc_boss = dc_boss + 1
            health_bar_boss = 0
            boss_health_bar.hideturtle()
            if sound == 1:
                winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
            boss.shape("Explosion1.gif")
            update_boss = 1

    if hit_delay_boss9 == 3:
        hit_delay_boss9 = 0

    if hit_delay_boss9 == 2:
        hit_delay_boss9 = 3

    if hit_delay_boss9 == 1:
        hit_delay_boss9 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 2 and hit_delay_boss8 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health1.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 1
            hit_delay_boss9 = 1

    if hit_delay_boss8 == 3:
        hit_delay_boss8 = 0

    if hit_delay_boss8 == 2:
        hit_delay_boss8 = 3

    if hit_delay_boss8 == 1:
        hit_delay_boss8 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 3 and hit_delay_boss7 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health2.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 2
            hit_delay_boss8 = 1

    if hit_delay_boss7 == 3:
        hit_delay_boss7 = 0

    if hit_delay_boss7 == 2:
        hit_delay_boss7 = 3

    if hit_delay_boss7 == 1:
        hit_delay_boss7 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 4 and hit_delay_boss6 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health3.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 3
            hit_delay_boss7 = 1

    if hit_delay_boss6 == 3:
        hit_delay_boss6 = 0

    if hit_delay_boss6 == 2:
        hit_delay_boss6 = 3

    if hit_delay_boss6 == 1:
        hit_delay_boss6 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 5 and hit_delay_boss5 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health4.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 4
            hit_delay_boss6 = 1

    if hit_delay_boss5 == 3:
        hit_delay_boss5 = 0

    if hit_delay_boss5 == 2:
        hit_delay_boss5 = 3

    if hit_delay_boss5 == 1:
        hit_delay_boss5 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 6 and hit_delay_boss4 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health5.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 5
            hit_delay_boss5 = 1

    if hit_delay_boss4 == 3:
        hit_delay_boss4 = 0

    if hit_delay_boss4 == 2:
        hit_delay_boss4 = 3

    if hit_delay_boss4 == 1:
        hit_delay_boss4 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 7 and hit_delay_boss3 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health6.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 6
            hit_delay_boss4 = 1

    if hit_delay_boss3 == 3:
        hit_delay_boss3 = 0

    if hit_delay_boss3 == 2:
        hit_delay_boss3 = 3

    if hit_delay_boss3 == 1:
        hit_delay_boss3 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 8 and hit_delay_boss2 == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health7.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 7
            hit_delay_boss3 = 1

    if hit_delay_boss2 == 3:
        hit_delay_boss2 = 0

    if hit_delay_boss2 == 2:
        hit_delay_boss2 = 3

    if hit_delay_boss2 == 1:
        hit_delay_boss2 = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 9 and hit_delay_boss == 0:
        if update_boss == 0:
            score = score + 1
            boss_health_bar.shape("Boss_Health8.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 8
            hit_delay_boss2 = 1

    if hit_delay_boss == 3:
        hit_delay_boss = 0

    if hit_delay_boss == 2:
        hit_delay_boss = 3

    if hit_delay_boss == 1:
        hit_delay_boss = 2

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 10:
        if update_boss == 0:
            score = score + 2
            boss_health_bar.shape("Boss_Health9.gif")
            if sound == 1:
                winsound.PlaySound("Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 9
            hit_delay_boss = 1

    # Lines 1818 - 2000 are for what happens when the player gets hit and dies
    if update_player == 6:
        player.showturtle()
        update_player = 0
        death_animation = 0

    if update_player == 5:
        update_player = 6

    if update_player == 4:
        update_player = 5

    if update_player == 3:
        player.hideturtle()
        player.shape("Player.gif")
        player.goto(0, -300)
        update_player = 4

    if update_player == 2:
        update_player = 3

    if update_player == 1:
        player.shape("Explosion2.gif")
        dc1 = 0
        dc2 = 0
        dc3 = 0
        dc4 = 0
        dc5 = 0
        dc6 = 0
        dc7 = 0
        dc8 = 0
        dc9 = 0
        dc10 = 0
        dc11 = 0
        dc12 = 0
        dc13 = 0
        dc14 = 0
        dc15 = 0
        dc_boss = 0
        update_player = 2

    if enemy1_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy1_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy2_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy2_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy3_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy3_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy4_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy4_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy5_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy5_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy6_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy6_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy7_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy7_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy8_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy8_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy9_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy9_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy10_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy10_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy11_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy11_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy12_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy12_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy13_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy13_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy14_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy14_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if enemy15_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (enemy15_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    if boss_laser.distance(player) < 125 and death_animation == 0 and god_mode == 0:
        if -30 < (boss_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if sound == 1:
                winsound.PlaySound("Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Explosion1.gif")
            score = 0
            update_player = 1

    # Lines 2003 - 2669 are for the movement of all the enemies. The more times they each die, the faster they move
    if dc1 >= 4 and death_animation == 0 and update1 == 0:
        if 600 < enemy1.xcor() < 650:
            moving1 = -1
        if -600 > enemy1.xcor() > -650:
            moving1 = 1
        if moving1 == 1:
            if 4 <= dc1 < 7:
                x = enemy1.xcor()
                enemy1.setx(x + 5)
            if 7 <= dc1 < 10:
                x = enemy1.xcor()
                enemy1.setx(x + 10)
            if 10 <= dc1 < 13:
                x = enemy1.xcor()
                enemy1.setx(x + 15)
            if 13 <= dc1 < 16:
                x = enemy1.xcor()
                enemy1.setx(x + 20)
            if 16 <= dc1:
                x = enemy1.xcor()
                enemy1.setx(x + 25)
        if moving1 == -1:
            if 4 <= dc1 < 7:
                x = enemy1.xcor()
                enemy1.setx(x - 5)
            if 7 <= dc1 < 10:
                x = enemy1.xcor()
                enemy1.setx(x - 10)
            if 10 <= dc1 < 13:
                x = enemy1.xcor()
                enemy1.setx(x - 15)
            if 13 <= dc1 < 16:
                x = enemy1.xcor()
                enemy1.setx(x - 20)
            if 16 <= dc1:
                x = enemy1.xcor()
                enemy1.setx(x - 25)

    if dc2 >= 4 and death_animation == 0 and update2 == 0:
        if 600 < enemy2.xcor() < 650:
            moving2 = -1
        if -600 > enemy2.xcor() > -650:
            moving2 = 1
        if moving2 == 1:
            if 4 <= dc2 < 7:
                x = enemy2.xcor()
                enemy2.setx(x + 5)
            if 7 <= dc2 < 10:
                x = enemy2.xcor()
                enemy2.setx(x + 10)
            if 10 <= dc2 < 13:
                x = enemy2.xcor()
                enemy2.setx(x + 15)
            if 13 <= dc2 < 16:
                x = enemy2.xcor()
                enemy2.setx(x + 20)
            if 16 <= dc2:
                x = enemy2.xcor()
                enemy2.setx(x + 25)
        if moving2 == -1:
            if 4 <= dc2 < 7:
                x = enemy2.xcor()
                enemy2.setx(x - 5)
            if 7 <= dc2 < 10:
                x = enemy2.xcor()
                enemy2.setx(x - 10)
            if 10 <= dc2 < 13:
                x = enemy2.xcor()
                enemy2.setx(x - 15)
            if 13 <= dc2 < 16:
                x = enemy2.xcor()
                enemy2.setx(x - 20)
            if 16 <= dc2:
                x = enemy2.xcor()
                enemy2.setx(x - 25)

    if dc3 >= 4 and death_animation == 0 and update3 == 0:
        if 600 < enemy3.xcor() < 650:
            moving3 = -1
        if -600 > enemy3.xcor() > -650:
            moving3 = 1
        if moving3 == 1:
            if 4 <= dc3 < 7:
                x = enemy3.xcor()
                enemy3.setx(x + 5)
            if 7 <= dc3 < 10:
                x = enemy3.xcor()
                enemy3.setx(x + 10)
            if 10 <= dc3 < 13:
                x = enemy3.xcor()
                enemy3.setx(x + 15)
            if 13 <= dc3 < 16:
                x = enemy3.xcor()
                enemy3.setx(x + 20)
            if 16 <= dc3:
                x = enemy3.xcor()
                enemy3.setx(x + 25)
        if moving3 == -1:
            if 4 <= dc3 < 7:
                x = enemy3.xcor()
                enemy3.setx(x - 5)
            if 7 <= dc3 < 10:
                x = enemy3.xcor()
                enemy3.setx(x - 10)
            if 10 <= dc3 < 13:
                x = enemy3.xcor()
                enemy3.setx(x - 15)
            if 13 <= dc3 < 16:
                x = enemy3.xcor()
                enemy3.setx(x - 20)
            if 16 <= dc3:
                x = enemy3.xcor()
                enemy3.setx(x - 25)

    if dc4 >= 4 and death_animation == 0 and update4 == 0:
        if 600 < enemy4.xcor() < 650:
            moving4 = -1
        if -600 > enemy4.xcor() > -650:
            moving4 = 1
        if moving4 == 1:
            if 4 <= dc4 < 7:
                x = enemy4.xcor()
                enemy4.setx(x + 5)
            if 7 <= dc4 < 10:
                x = enemy4.xcor()
                enemy4.setx(x + 10)
            if 10 <= dc4 < 13:
                x = enemy4.xcor()
                enemy4.setx(x + 15)
            if 13 <= dc4 < 16:
                x = enemy4.xcor()
                enemy4.setx(x + 20)
            if 16 <= dc4:
                x = enemy4.xcor()
                enemy4.setx(x + 25)
        if moving4 == -1:
            if 4 <= dc4 < 7:
                x = enemy4.xcor()
                enemy4.setx(x - 5)
            if 7 <= dc4 < 10:
                x = enemy4.xcor()
                enemy4.setx(x - 10)
            if 10 <= dc4 < 13:
                x = enemy4.xcor()
                enemy4.setx(x - 15)
            if 13 <= dc4 < 16:
                x = enemy4.xcor()
                enemy4.setx(x - 20)
            if 16 <= dc4:
                x = enemy4.xcor()
                enemy4.setx(x - 25)

    if dc5 >= 4 and death_animation == 0 and update5 == 0:
        if 600 < enemy5.xcor() < 650:
            moving5 = -1
        if -600 > enemy5.xcor() > -650:
            moving5 = 1
        if moving5 == 1:
            if 4 <= dc5 < 7:
                x = enemy5.xcor()
                enemy5.setx(x + 5)
            if 7 <= dc5 < 10:
                x = enemy5.xcor()
                enemy5.setx(x + 10)
            if 10 <= dc5 < 13:
                x = enemy5.xcor()
                enemy5.setx(x + 15)
            if 13 <= dc5 < 16:
                x = enemy5.xcor()
                enemy5.setx(x + 20)
            if 16 <= dc5:
                x = enemy5.xcor()
                enemy5.setx(x + 25)
        if moving5 == -1:
            if 4 <= dc5 < 7:
                x = enemy5.xcor()
                enemy5.setx(x - 5)
            if 7 <= dc5 < 10:
                x = enemy5.xcor()
                enemy5.setx(x - 10)
            if 10 <= dc5 < 13:
                x = enemy5.xcor()
                enemy5.setx(x - 15)
            if 13 <= dc5 < 16:
                x = enemy5.xcor()
                enemy5.setx(x - 20)
            if 16 <= dc5:
                x = enemy5.xcor()
                enemy5.setx(x - 25)

    if dc6 >= 4 and death_animation == 0 and update6 == 0:
        if 600 < enemy6.xcor() < 650:
            moving6 = -1
        if -600 > enemy6.xcor() > -650:
            moving6 = 1
        if moving6 == 1:
            if 4 <= dc6 < 7:
                x = enemy6.xcor()
                enemy6.setx(x + 5)
            if 7 <= dc6 < 10:
                x = enemy6.xcor()
                enemy6.setx(x + 10)
            if 10 <= dc6 < 13:
                x = enemy6.xcor()
                enemy6.setx(x + 15)
            if 13 <= dc6 < 16:
                x = enemy6.xcor()
                enemy6.setx(x + 20)
            if 16 <= dc6:
                x = enemy6.xcor()
                enemy6.setx(x + 25)
        if moving6 == -1:
            if 4 <= dc6 < 7:
                x = enemy6.xcor()
                enemy6.setx(x - 5)
            if 7 <= dc6 < 10:
                x = enemy6.xcor()
                enemy6.setx(x - 10)
            if 10 <= dc6 < 13:
                x = enemy6.xcor()
                enemy6.setx(x - 15)
            if 13 <= dc6 < 16:
                x = enemy6.xcor()
                enemy6.setx(x - 20)
            if 16 <= dc6:
                x = enemy6.xcor()
                enemy6.setx(x - 25)

    if dc7 >= 4 and death_animation == 0 and update7 == 0:
        if 600 < enemy7.xcor() < 650:
            moving7 = -1
        if -600 > enemy7.xcor() > -650:
            moving7 = 1
        if moving7 == 1:
            if 4 <= dc7 < 7:
                x = enemy7.xcor()
                enemy7.setx(x + 5)
            if 7 <= dc7 < 10:
                x = enemy7.xcor()
                enemy7.setx(x + 10)
            if 10 <= dc7 < 13:
                x = enemy7.xcor()
                enemy7.setx(x + 15)
            if 13 <= dc7 < 16:
                x = enemy7.xcor()
                enemy7.setx(x + 20)
            if 16 <= dc7:
                x = enemy7.xcor()
                enemy7.setx(x + 25)
        if moving7 == -1:
            if 4 <= dc7 < 7:
                x = enemy7.xcor()
                enemy7.setx(x - 5)
            if 7 <= dc7 < 10:
                x = enemy7.xcor()
                enemy7.setx(x - 10)
            if 10 <= dc7 < 13:
                x = enemy7.xcor()
                enemy7.setx(x - 15)
            if 13 <= dc7 < 16:
                x = enemy7.xcor()
                enemy7.setx(x - 20)
            if 16 <= dc7:
                x = enemy7.xcor()
                enemy7.setx(x - 25)

    if dc8 >= 4 and death_animation == 0 and update8 == 0:
        if 600 < enemy8.xcor() < 650:
            moving8 = -1
        if -600 > enemy8.xcor() > -650:
            moving8 = 1
        if moving8 == 1:
            if 4 <= dc8 < 7:
                x = enemy8.xcor()
                enemy8.setx(x + 5)
            if 7 <= dc8 < 10:
                x = enemy8.xcor()
                enemy8.setx(x + 10)
            if 10 <= dc8 < 13:
                x = enemy8.xcor()
                enemy8.setx(x + 15)
            if 13 <= dc8 < 16:
                x = enemy8.xcor()
                enemy8.setx(x + 20)
            if 16 <= dc8:
                x = enemy8.xcor()
                enemy8.setx(x + 25)
        if moving8 == -1:
            if 4 <= dc8 < 7:
                x = enemy8.xcor()
                enemy8.setx(x - 5)
            if 7 <= dc8 < 10:
                x = enemy8.xcor()
                enemy8.setx(x - 10)
            if 10 <= dc8 < 13:
                x = enemy8.xcor()
                enemy8.setx(x - 15)
            if 13 <= dc8 < 16:
                x = enemy8.xcor()
                enemy8.setx(x - 20)
            if 16 <= dc8:
                x = enemy8.xcor()
                enemy8.setx(x - 25)

    if dc9 >= 4 and death_animation == 0 and update9 == 0:
        if 600 < enemy9.xcor() < 650:
            moving9 = -1
        if -600 > enemy9.xcor() > -650:
            moving9 = 1
        if moving9 == 1:
            if 4 <= dc9 < 7:
                x = enemy9.xcor()
                enemy9.setx(x + 5)
            if 7 <= dc9 < 10:
                x = enemy9.xcor()
                enemy9.setx(x + 10)
            if 10 <= dc9 < 13:
                x = enemy9.xcor()
                enemy9.setx(x + 15)
            if 13 <= dc9 < 16:
                x = enemy9.xcor()
                enemy9.setx(x + 20)
            if 16 <= dc9:
                x = enemy9.xcor()
                enemy9.setx(x + 25)
        if moving9 == -1:
            if 4 <= dc9 < 7:
                x = enemy9.xcor()
                enemy9.setx(x - 5)
            if 7 <= dc9 < 10:
                x = enemy9.xcor()
                enemy9.setx(x - 10)
            if 10 <= dc9 < 13:
                x = enemy9.xcor()
                enemy9.setx(x - 15)
            if 13 <= dc9 < 16:
                x = enemy9.xcor()
                enemy9.setx(x - 20)
            if 16 <= dc9:
                x = enemy9.xcor()
                enemy9.setx(x - 25)

    if dc10 >= 4 and death_animation == 0 and update10 == 0:
        if 600 < enemy10.xcor() < 650:
            moving10 = -1
        if -600 > enemy10.xcor() > -650:
            moving10 = 1
        if moving10 == 1:
            if 4 <= dc10 < 7:
                x = enemy10.xcor()
                enemy10.setx(x + 5)
            if 7 <= dc10 < 10:
                x = enemy10.xcor()
                enemy10.setx(x + 10)
            if 10 <= dc10 < 13:
                x = enemy10.xcor()
                enemy10.setx(x + 15)
            if 13 <= dc10 < 16:
                x = enemy10.xcor()
                enemy10.setx(x + 20)
            if 16 <= dc10:
                x = enemy10.xcor()
                enemy10.setx(x + 25)
        if moving10 == -1:
            if 4 <= dc10 < 7:
                x = enemy10.xcor()
                enemy10.setx(x - 5)
            if 7 <= dc10 < 10:
                x = enemy10.xcor()
                enemy10.setx(x - 10)
            if 10 <= dc10 < 13:
                x = enemy10.xcor()
                enemy10.setx(x - 15)
            if 13 <= dc10 < 16:
                x = enemy10.xcor()
                enemy10.setx(x - 20)
            if 16 <= dc10:
                x = enemy10.xcor()
                enemy10.setx(x - 25)

    if dc11 >= 4 and death_animation == 0 and update11 == 0:
        if 600 < enemy11.xcor() < 650:
            moving11 = -1
        if -600 > enemy11.xcor() > -650:
            moving11 = 1
        if moving11 == 1:
            if 4 <= dc11 < 7:
                x = enemy11.xcor()
                enemy11.setx(x + 5)
                enemy11_health_bar.goto(x + 5, 290)
            if 7 <= dc11 < 10:
                x = enemy11.xcor()
                enemy11.setx(x + 10)
                enemy11_health_bar.goto(x + 10, 290)
            if 10 <= dc11 < 13:
                x = enemy11.xcor()
                enemy11.setx(x + 15)
                enemy11_health_bar.goto(x + 15, 290)
            if 13 <= dc11 < 16:
                x = enemy11.xcor()
                enemy11.setx(x + 20)
                enemy11_health_bar.goto(x + 20, 290)
            if 16 <= dc11:
                x = enemy11.xcor()
                enemy11.setx(x + 25)
                enemy11_health_bar.goto(x + 25, 290)
        if moving11 == -1:
            if 4 <= dc11 < 7:
                x = enemy11.xcor()
                enemy11.setx(x - 5)
                enemy11_health_bar.goto(x - 5, 290)
            if 7 <= dc11 < 10:
                x = enemy11.xcor()
                enemy11.setx(x - 10)
                enemy11_health_bar.goto(x - 10, 290)
            if 10 <= dc11 < 13:
                x = enemy11.xcor()
                enemy11.setx(x - 15)
                enemy11_health_bar.goto(x - 15, 290)
            if 13 <= dc11 < 16:
                x = enemy11.xcor()
                enemy11.setx(x - 20)
                enemy11_health_bar.goto(x - 20, 290)
            if 16 <= dc11:
                x = enemy11.xcor()
                enemy11.setx(x - 25)
                enemy11_health_bar.goto(x - 25, 290)

    if dc12 >= 4 and death_animation == 0 and update12 == 0:
        if 600 < enemy12.xcor() < 650:
            moving12 = -1
        if -600 > enemy12.xcor() > -650:
            moving12 = 1
        if moving12 == 1:
            if 4 <= dc12 < 7:
                x = enemy12.xcor()
                enemy12.setx(x + 5)
                enemy12_health_bar.goto(x + 5, 290)
            if 7 <= dc12 < 10:
                x = enemy12.xcor()
                enemy12.setx(x + 10)
                enemy12_health_bar.goto(x + 10, 290)
            if 10 <= dc12 < 13:
                x = enemy12.xcor()
                enemy12.setx(x + 15)
                enemy12_health_bar.goto(x + 15, 290)
            if 13 <= dc12 < 16:
                x = enemy12.xcor()
                enemy12.setx(x + 20)
                enemy12_health_bar.goto(x + 20, 290)
            if 16 <= dc12:
                x = enemy12.xcor()
                enemy12.setx(x + 25)
                enemy12_health_bar.goto(x + 25, 290)
        if moving12 == -1:
            if 4 <= dc12 < 7:
                x = enemy12.xcor()
                enemy12.setx(x - 5)
                enemy12_health_bar.goto(x - 5, 290)
            if 7 <= dc12 < 10:
                x = enemy12.xcor()
                enemy12.setx(x - 10)
                enemy12_health_bar.goto(x - 10, 290)
            if 10 <= dc12 < 13:
                x = enemy12.xcor()
                enemy12.setx(x - 15)
                enemy12_health_bar.goto(x - 15, 290)
            if 13 <= dc12 < 16:
                x = enemy12.xcor()
                enemy12.setx(x - 20)
                enemy12_health_bar.goto(x - 20, 290)
            if 16 <= dc12:
                x = enemy12.xcor()
                enemy12.setx(x - 25)
                enemy12_health_bar.goto(x - 25, 290)

    if dc13 >= 4 and death_animation == 0 and update13 == 0:
        if 600 < enemy13.xcor() < 650:
            moving13 = -1
        if -600 > enemy13.xcor() > -650:
            moving13 = 1
        if moving13 == 1:
            if 4 <= dc13 < 7:
                x = enemy13.xcor()
                enemy13.setx(x + 5)
                enemy13_health_bar.goto(x + 5, 290)
            if 7 <= dc13 < 10:
                x = enemy13.xcor()
                enemy13.setx(x + 10)
                enemy13_health_bar.goto(x + 10, 290)
            if 10 <= dc13 < 13:
                x = enemy13.xcor()
                enemy13.setx(x + 15)
                enemy13_health_bar.goto(x + 15, 290)
            if 13 <= dc13 < 16:
                x = enemy13.xcor()
                enemy13.setx(x + 20)
                enemy13_health_bar.goto(x + 20, 290)
            if 16 <= dc13:
                x = enemy13.xcor()
                enemy13.setx(x + 25)
                enemy13_health_bar.goto(x + 25, 290)
        if moving13 == -1:
            if 4 <= dc13 < 7:
                x = enemy13.xcor()
                enemy13.setx(x - 5)
                enemy13_health_bar.goto(x - 5, 290)
            if 7 <= dc13 < 10:
                x = enemy13.xcor()
                enemy13.setx(x - 10)
                enemy13_health_bar.goto(x - 10, 290)
            if 10 <= dc13 < 13:
                x = enemy13.xcor()
                enemy13.setx(x - 15)
                enemy13_health_bar.goto(x - 15, 290)
            if 13 <= dc13 < 16:
                x = enemy13.xcor()
                enemy13.setx(x - 20)
                enemy13_health_bar.goto(x - 20, 290)
            if 16 <= dc13:
                x = enemy13.xcor()
                enemy13.setx(x - 25)
                enemy13_health_bar.goto(x - 25, 290)

    if dc14 >= 4 and death_animation == 0 and update14 == 0:
        if 600 < enemy14.xcor() < 650:
            moving14 = -1
        if -600 > enemy14.xcor() > -650:
            moving14 = 1
        if moving14 == 1:
            if 4 <= dc14 < 7:
                x = enemy14.xcor()
                enemy14.setx(x + 5)
                enemy14_health_bar.goto(x + 5, 290)
            if 7 <= dc14 < 10:
                x = enemy14.xcor()
                enemy14.setx(x + 10)
                enemy14_health_bar.goto(x + 10, 290)
            if 10 <= dc14 < 13:
                x = enemy14.xcor()
                enemy14.setx(x + 15)
                enemy14_health_bar.goto(x + 15, 290)
            if 13 <= dc14 < 16:
                x = enemy14.xcor()
                enemy14.setx(x + 20)
                enemy14_health_bar.goto(x + 20, 290)
            if 16 <= dc14:
                x = enemy14.xcor()
                enemy14.setx(x + 25)
                enemy14_health_bar.goto(x + 25, 290)
        if moving14 == -1:
            if 4 <= dc14 < 7:
                x = enemy14.xcor()
                enemy14.setx(x - 5)
                enemy14_health_bar.goto(x - 5, 290)
            if 7 <= dc14 < 10:
                x = enemy14.xcor()
                enemy14.setx(x - 10)
                enemy14_health_bar.goto(x - 10, 290)
            if 10 <= dc14 < 13:
                x = enemy14.xcor()
                enemy14.setx(x - 15)
                enemy14_health_bar.goto(x - 15, 290)
            if 13 <= dc14 < 16:
                x = enemy14.xcor()
                enemy14.setx(x - 20)
                enemy14_health_bar.goto(x - 20, 290)
            if 16 <= dc14:
                x = enemy14.xcor()
                enemy14.setx(x - 25)
                enemy14_health_bar.goto(x - 25, 290)

    if dc15 >= 4 and death_animation == 0 and update15 == 0:
        if 600 < enemy15.xcor() < 650:
            moving15 = -1
        if -600 > enemy15.xcor() > -650:
            moving15 = 1
        if moving15 == 1:
            if 4 <= dc15 < 7:
                x = enemy15.xcor()
                enemy15.setx(x + 5)
                enemy15_health_bar.goto(x + 5, 290)
            if 7 <= dc15 < 10:
                x = enemy15.xcor()
                enemy15.setx(x + 10)
                enemy15_health_bar.goto(x + 10, 290)
            if 10 <= dc15 < 13:
                x = enemy15.xcor()
                enemy15.setx(x + 15)
                enemy15_health_bar.goto(x + 15, 290)
            if 13 <= dc15 < 16:
                x = enemy15.xcor()
                enemy15.setx(x + 20)
                enemy15_health_bar.goto(x + 20, 290)
            if 16 <= dc15:
                x = enemy15.xcor()
                enemy15.setx(x + 25)
                enemy15_health_bar.goto(x + 25, 290)
        if moving15 == -1:
            if 4 <= dc15 < 7:
                x = enemy15.xcor()
                enemy15.setx(x - 5)
                enemy15_health_bar.goto(x - 5, 290)
            if 7 <= dc15 < 10:
                x = enemy15.xcor()
                enemy15.setx(x - 10)
                enemy15_health_bar.goto(x - 10, 290)
            if 10 <= dc15 < 13:
                x = enemy15.xcor()
                enemy15.setx(x - 15)
                enemy15_health_bar.goto(x - 15, 290)
            if 13 <= dc15 < 16:
                x = enemy15.xcor()
                enemy15.setx(x - 20)
                enemy15_health_bar.goto(x - 20, 290)
            if 16 <= dc15:
                x = enemy15.xcor()
                enemy15.setx(x - 25)
                enemy15_health_bar.goto(x - 25, 290)

    if dc_boss >= 4 and death_animation == 0 and update_boss == 0:
        if 600 < boss.xcor() < 650:
            moving_boss = -1
        if -600 > boss.xcor() > -650:
            moving_boss = 1
        if moving_boss == 1:
            if 4 <= dc_boss < 7:
                x = boss.xcor()
                boss.setx(x + 5)
                boss_health_bar.goto(x + 5, 290)
            if 7 <= dc_boss < 10:
                x = boss.xcor()
                boss.setx(x + 10)
                boss_health_bar.goto(x + 10, 290)
            if 10 <= dc_boss < 13:
                x = boss.xcor()
                boss.setx(x + 15)
                boss_health_bar.goto(x + 15, 290)
            if 13 <= dc_boss < 16:
                x = boss.xcor()
                boss.setx(x + 20)
                boss_health_bar.goto(x + 20, 290)
            if 16 <= dc_boss:
                x = boss.xcor()
                boss.setx(x + 25)
                boss_health_bar.goto(x + 25, 290)
        if moving_boss == -1:
            if 4 <= dc_boss < 7:
                x = boss.xcor()
                boss.setx(x - 5)
                boss_health_bar.goto(x - 5, 290)
            if 7 <= dc_boss < 10:
                x = boss.xcor()
                boss.setx(x - 10)
                boss_health_bar.goto(x - 10, 290)
            if 10 <= dc_boss < 13:
                x = boss.xcor()
                boss.setx(x - 15)
                boss_health_bar.goto(x - 15, 290)
            if 13 <= dc_boss < 16:
                x = boss.xcor()
                boss.setx(x - 20)
                boss_health_bar.goto(x - 20, 290)
            if 16 <= dc_boss:
                x = boss.xcor()
                boss.setx(x - 25)
                boss_health_bar.goto(x - 25, 290)

    # Lines 2672 - 2690 are used to check if the sound is still on or still off
    soundfile = open("Sound.txt", "r")
    sound_number = soundfile.readlines()
    soundfile.close()
    soundfile2 = open("Machine War I #2.txt", "r")
    sound_number2 = soundfile2.readlines()
    soundfile2.close()
    if sound_number == sound_number2:
        sound = 1
    else:
        sound = 0

    if sound == 1:
        sound_indicator.clear()
        sound_indicator.color("green")
        sound_indicator.write("On", align="left", font=("Courier", 24, "normal"))
    else:
        sound_indicator.clear()
        sound_indicator.color("red")
        sound_indicator.write("Off", align="left", font=("Courier", 24, "normal"))

    # Used to check the score and high score every tick
    if god_mode == 0:
        if score > high_score:
            high_score = score
            score_file = open("High_score.txt", "w")
            score_file.writelines("{}".format(score))
            score_file.close()

    score_box.clear()
    score_box.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

