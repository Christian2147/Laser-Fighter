# Copyright (C) [2023] [Christian Marinkovich]
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

# Created By: CMarink(aka Christian2147) This is the code for Laser Fighter.
# This code is currently very messy and needs a lot of cleanup.
# This is game version alpha 0.4.0 released on 8/1/2023

import random
import time
import turtle
import tkinter
import winsound
import ctypes

delay = 0.05

# The variables and what they mean:
# delay = used for the tick speed of the game
# mode = used for the screen that the game is on (important variable)
# title_moving/settings_moving/stats moving/controls moving = used to move the title on the title screen, settings screen, stats screen, and controls screen
# button_update = used for the buttons in the game
# score = used for the players score
# death_animation = this is used for when the player dies
# update_player = used for when the player gets killed by an enemy
# alien_random = used to teleport aliens to a random location
# laser_update = used for enemy piercing by player laser in alien mode
# power_up_update = used to set the rarity of power ups spawning in both classic mode and alien mode
# power_up_active = used to determine whether a certain power is active or not
# power_up_timer = used to set the duration of each power up
# tick_update = used to set a certain tick speed for things that slow the game down (ex: refresh rate of text on the screen)
# update(num) = these are used for when an enemy gets killed by the player in classic mode
# alien(num)_death = used for when an alien gets killed by the player
# dc(num)/ak(num) = used for the death count of each enemy/alien
# moving = used for when the enemies move across the screen
# health_bar/alien(num)_health = used for the health bars of stronger enemies/aliens
# hit_delay(num)/alien(num)_hit_delay = used to delay how often certain enemies/aliens can be hit
# jump_update/do_jump/vertex/direction = all used for player jumps in alien mode
# move_update/move_right/right_update/moving_right/move_left/left_update/moving_left = all used for player movement in alien mode
# Start_X/Start_Y = used as a starting position variable
# time = used for things that need a timer
# death_occuring/player_health/player_update/head_death_animation = used for player health and player death in alien mode
# shoot_update/shooting/laser_direction = used for shooting in alien mode
# updated_controls/(name)_key_backup/(name)_key_2/(name)_key_alert = used when the controls are changed
# message_output = used when the game is creating a message pop-up
# quit_loop = used when the program is terminated
# god_mode = used for the secret god mode feature

mode = "Title_Mode"
title_moving = 1
stats_moving = 1
settings_moving = 1
controls_moving = 1
button_update = 0
score = 0
death_animation = 0
update_player = 0
alien_random = 0
laser_update = 0
power_up_update = 0
yellow_power_up_active = 0
yellow_power_up_timer = 0
red_power_up_active = 0
red_power_up_timer = 0
green_power_up_active = 0
green_power_up_timer = 0
blue_power_up_active = 0
blue_power_up_timer = 0
tick_update = 0
update1 = 0
alien1_death = 0
update2 = 0
alien2_death = 0
update3 = 0
alien3_death = 0
update4 = 0
alien4_death = 0
update5 = 0
alien5_death = 0
update6 = 0
alien6_death = 0
alien6_health = 2
alien6_hit_delay = 0
update7 = 0
alien7_death = 0
alien7_health = 2
alien7_hit_delay = 0
update8 = 0
alien8_death = 0
alien8_health = 2
alien8_hit_delay = 0
update9 = 0
alien9_death = 0
alien9_health = 2
alien9_hit_delay = 0
update10 = 0
alien10_death = 0
alien10_health = 2
alien10_hit_delay = 0
update11 = 0
alien11_death = 0
alien11_health = 3
alien11_hit_delay = 0
update12 = 0
alien12_death = 0
alien12_health = 3
alien12_hit_delay = 0
update13 = 0
alien13_death = 0
alien13_health = 3
alien13_hit_delay = 0
update14 = 0
alien14_death = 0
alien14_health = 3
alien14_hit_delay = 0
update15 = 0
alien15_death = 0
alien15_health = 3
alien15_hit_delay = 0
update_boss = 0
alien_boss_death = 0
alien_boss_health = 10
alien_boss_hit_delay = 0
ak1 = 0
dc1 = 0
moving1 = 1
ak2 = 0
dc2 = 0
moving2 = 1
ak3 = 0
dc3 = 0
moving3 = 1
ak4 = 0
dc4 = 0
moving4 = 1
ak5 = 0
dc5 = 0
moving5 = 1
ak6 = 0
dc6 = 0
moving6 = 1
ak7 = 0
dc7 = 0
moving7 = 1
ak8 = 0
dc8 = 0
moving8 = 1
ak9 = 0
dc9 = 0
moving9 = 1
ak10 = 0
dc10 = 0
moving10 = 1
ak11 = 0
dc11 = 0
moving11 = 1
health_bar11 = 2
hit_delay11 = 0
ak12 = 0
dc12 = 0
moving12 = 1
health_bar12 = 2
hit_delay12 = 0
ak13 = 0
dc13 = 0
moving13 = 1
health_bar13 = 2
hit_delay13 = 0
ak14 = 0
dc14 = 0
moving14 = 1
health_bar14 = 2
hit_delay14 = 0
ak15 = 0
dc15 = 0
moving15 = 1
health_bar15 = 2
hit_delay15 = 0
ak_boss = 0
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
jump_update = 0
do_jump = 0
vertex = 0
direction = 0
move_update = 0
shoot_update = 0
shooting = 0
laser_direction = 0
move_right = 0
right_update = 0
moving_right = 0
move_left = 0
left_update = 0
moving_left = 0
Start_X = 0
Start_Y = 0
Time = 0
death_occurring = 0
player_health = 10
player_update = 0
head_death_animation = 0
updated_controls = 0
go_right_key_backup = 0
go_right_key_2 = 0
go_right_key_alert = 0
go_left_key_backup = 0
go_left_key_2 = 0
go_left_key_alert = 0
shoot_key_backup = 0
shoot_key_2 = 0
shoot_key_alert = 0
jump_key_backup = 0
jump_key_2 = 0
jump_key_alert = 0
message_output = 0
quit_loop = 0
god_mode = 0

# Used to set the stats screen to the correct values when the game is launched

stats = open("Config/Statistics.txt", "r")
stats_text = stats.readlines()
stats.close()
bosses_killed = int(stats_text[2])
red_bots_killed = int(stats_text[4])
yellow_bots_killed = int(stats_text[6])
blue_bots_killed = int(stats_text[8])
classic_deaths = int(stats_text[10])
classic_lasers_fired = int(stats_text[12])
classic_power_ups_picked_up = int(stats_text[14])
ufos_killed = int(stats_text[18])
big_aliens_killed = int(stats_text[20])
medium_aliens_killed = int(stats_text[22])
small_aliens_killed = int(stats_text[24])
alien_deaths = int(stats_text[26])
damage_taken = int(stats_text[28])
alien_lasers_fired = int(stats_text[30])
jumps = int(stats_text[32])
alien_power_ups_picked_up = int(stats_text[34])

# used to check what the controls are set to after the game starts/restarts

controls = open("Config/Controls.txt", "r")
control_text = controls.readlines()
controls.close()
right_control = control_text[0]
left_control = control_text[1]
shoot_control = control_text[2]
jump_control = control_text[3]
check_control_update = open("Config/Key_Update.txt", "r")
check_controls = check_control_update.readlines()
check_control_update.close()
if check_controls[0] == "space\n":
    go_right_key = "space"
else:
    go_right_key = right_control[12]
if check_controls[1] == "space\n":
    go_left_key = "space"
else:
    go_left_key = left_control[11]
if check_controls[2] == "space\n":
    shoot_key = "space"
else:
    shoot_key = shoot_control[9]
if check_controls[3] == "space\n":
    jump_key = "space"
else:
    jump_key = jump_control[8]

# Used to check if god mode has been set to true or false

file = open("Config/Cheat_Code.txt", "r")
f = file.readlines()
file.close()
file2 = open("Config/Laser_Fighter.txt", "r")
f2 = file2.readlines()
file2.close()
if f == f2:
    god_mode = 1
else:
    god_mode = 0

# Used to check whether certain sounds were previously set to on or off when the game launches

soundfile = open("Config/Sound.txt", "r")
sound_number = soundfile.readlines()
soundfile.close()
soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
sound_number2 = soundfile2.readlines()
soundfile2.close()
if sound_number[0] == sound_number2[0]:
    button_sound = 1
else:
    button_sound = 0
if sound_number[1] == sound_number2[1]:
    player_shooting_sound = 1
else:
    player_shooting_sound = 0
if sound_number[2] == sound_number2[2]:
    enemy_shooting_sound = 1
else:
    enemy_shooting_sound = 0
if sound_number[3] == sound_number2[3]:
    player_death_sound = 1
else:
    player_death_sound = 0
if sound_number[4] == sound_number2[4]:
    enemy_death_sound = 1
else:
    enemy_death_sound = 0
if sound_number[5] == sound_number2[5]:
    player_hit_sound = 1
else:
    player_hit_sound = 0
if sound_number[6] == sound_number2[6]:
    enemy_hit_sound = 1
else:
    enemy_hit_sound = 0
if sound_number[7] == sound_number2[7]:
    power_up_pickup_sound = 1
else:
    power_up_pickup_sound = 0
if sound_number[8] == sound_number2[8]:
    power_up_spawn_sound = 1
else:
    power_up_spawn_sound = 0

# Used to disable the high score when god mode is on and to set the high_score to what it previously was the last time the game was launched if god mode is off

if god_mode == 0:
    score_file = open("Config/High_Score.txt", "r")
    high_score_list = score_file.readlines()
    score_file.close()
    high_score_temp_1 = high_score_list[0]
    high_score_machine_war = int(high_score_temp_1[26:len(high_score_temp_1) - 2])
    high_score_temp_2 = high_score_list[1]
    high_score_alien_mode = int(high_score_temp_2[25:len(high_score_temp_2) - 2])
else:
    high_score_machine_war = "NA"
    high_score_alien_mode = "NA"

# Used to create the window canvas for the game and to add all the textures that are needed in it

wn = turtle.Screen()
wn.title("Laser Fighter")
wn.bgcolor("black")
wn.bgpic("Textures/Background/Shooting_Game_Background.gif")
wn.setup(width=1280, height=720)
wn.cv._rootwindow.resizable(False, False)
img = tkinter.Image("photo", file="Icon/Icon.png")
wn._root.iconphoto(True, img)
wn.tracer(0)
wn.addshape("Textures/Player/Player.gif")
wn.addshape("Textures/Lasers/Player_Laser.gif")
wn.addshape("Textures/Enemies/Enemy(1-5).gif")
wn.addshape("Textures/Lasers/Enemy(1-5)_Laser.gif")
wn.addshape("Textures/Enemies/Enemy(6-10).gif")
wn.addshape("Textures/Lasers/Enemy(6-10)_Laser.gif")
wn.addshape("Textures/Enemies/Enemy(11-15).gif")
wn.addshape("Textures/Lasers/Enemy(11-15)_Laser.gif")
wn.addshape("Textures/Enemies/Boss.gif")
wn.addshape("Textures/Lasers/Boss_Laser.gif")
wn.addshape("Textures/Health_Bars/HealthBar_2.2.gif")
wn.addshape("Textures/Health_Bars/HealthBar_2.1.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.10.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.9.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.8.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.7.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.6.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.5.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.4.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.3.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.2.gif")
wn.addshape("Textures/Health_Bars/HealthBar_10.1.gif")
wn.addshape("Textures/Health_Bars/HealthBar_3.3.gif")
wn.addshape("Textures/Health_Bars/HealthBar_3.2.gif")
wn.addshape("Textures/Health_Bars/HealthBar_3.1.gif")
wn.addshape("Textures/Explosions/Explosion1.gif")
wn.addshape("Textures/Explosions/Explosion2.gif")
wn.addshape("Textures/Ground/Ground.gif")
wn.addshape("Textures/Background/Earth.gif")
wn.addshape("Textures/Background/Space_Ship.gif")
wn.addshape("Textures/Player/Player_Head_Still_Right.gif")
wn.addshape("Textures/Player/Player_Head_Still_Left.gif")
wn.addshape("Textures/Player/Player_Head_Walking_Right.gif")
wn.addshape("Textures/Player/Player_Head_Walking_Left.gif")
wn.addshape("Textures/Lasers/Player_Head_Laser.gif")
wn.addshape("Textures/Gun/Player_Gun_Right.gif")
wn.addshape("Textures/Gun/Player_Gun_Left.gif")
wn.addshape("Textures/Other/Oxygen_Tank.gif")
wn.addshape("Textures/Aliens/Alien_Still_Left(1-5).gif")
wn.addshape("Textures/Aliens/Alien_Still_Right(1-5).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
wn.addshape("Textures/Aliens/Alien_Still_Left(6-10).gif")
wn.addshape("Textures/Aliens/Alien_Still_Right(6-10).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
wn.addshape("Textures/Aliens/Alien_Still_Left(11-15).gif")
wn.addshape("Textures/Aliens/Alien_Still_Right(11-15).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
wn.addshape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
wn.addshape("Textures/Aliens/Alien_Boss.gif")
wn.addshape("Textures/Explosions/Alien_Death_1.gif")
wn.addshape("Textures/Explosions/Alien_Death_2.gif")
wn.addshape("Textures/Explosions/Player_Death_1.gif")
wn.addshape("Textures/Explosions/Player_Death_2.gif")
wn.addshape("Textures/Buttons/Sound_Button.gif")
wn.addshape("Textures/Buttons/Control_Button.gif")
wn.addshape("Textures/Buttons/Settings_Main_Menu_Button.gif")
wn.addshape("Textures/Buttons/Main_Menu_Button_Main.gif")
wn.addshape("Textures/Buttons/Title_Screen_button.gif")
wn.addshape("Textures/Buttons/Settings_And_Controls_Button.gif")
wn.addshape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
wn.addshape("Textures/Power_Ups/Green_Lightning_Power_Up.gif")
wn.addshape("Textures/Power_Ups/Red_Lightning_Power_Up.gif")
wn.addshape("Textures/Power_Ups/Blue_Lightning_Power_Up.gif")
wn.addshape("Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif")
wn.addshape("Textures/Power_Ups/Green_Power_Up_Indicator_On.gif")
wn.addshape("Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif")
wn.addshape("Textures/Power_Ups/Red_Power_Up_Indicator_On.gif")
wn.addshape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
wn.addshape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
wn.addshape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
wn.addshape("Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif")

# Lines 437 - 1788 is where all the different sprites(turtles) that are needed are created
# These turtles are set to their initial title mode state when they are first created when the game launches

classic_mode_button_frame = turtle.Turtle()
classic_mode_button_frame.color("#3D3D3D")
classic_mode_button_frame.shape("Textures/Buttons/Title_Screen_button.gif")
classic_mode_button_frame.shapesize(3.5, 25)
classic_mode_button_frame.penup()
classic_mode_button_frame.goto(0, 70)
classic_mode_button_frame.showturtle()

classic_mode_button = turtle.Turtle()
classic_mode_button.color("white")
classic_mode_button.shape("square")
classic_mode_button.shapesize(1, 1)
classic_mode_button.penup()
classic_mode_button.goto(0, 48)
classic_mode_button.hideturtle()

alien_mode_button_frame = turtle.Turtle()
alien_mode_button_frame.color("#3D3D3D")
alien_mode_button_frame.shape("Textures/Buttons/Title_Screen_button.gif")
alien_mode_button_frame.shapesize(3.5, 25)
alien_mode_button_frame.penup()
alien_mode_button_frame.goto(0, -30)
alien_mode_button_frame.showturtle()

alien_mode_button = turtle.Turtle()
alien_mode_button.color("white")
alien_mode_button.shape("square")
alien_mode_button.shapesize(1, 1)
alien_mode_button.penup()
alien_mode_button.goto(0, -52)
alien_mode_button.hideturtle()

stats_mode_button_frame = turtle.Turtle()
stats_mode_button_frame.color("#3D3D3D")
stats_mode_button_frame.shape("Textures/Buttons/Title_Screen_button.gif")
stats_mode_button_frame.shapesize(3.5, 25)
stats_mode_button_frame.penup()
stats_mode_button_frame.goto(0, -130)
stats_mode_button_frame.showturtle()

stats_mode_button = turtle.Turtle()
stats_mode_button.color("white")
stats_mode_button.shape("square")
stats_mode_button.shapesize(1, 1)
stats_mode_button.penup()
stats_mode_button.goto(0, -152)
stats_mode_button.hideturtle()

settings_mode_button_frame = turtle.Turtle()
settings_mode_button_frame.color("#3D3D3D")
settings_mode_button_frame.shape("Textures/Buttons/Title_Screen_button.gif")
settings_mode_button_frame.shapesize(3.5, 25)
settings_mode_button_frame.penup()
settings_mode_button_frame.goto(0, -230)
settings_mode_button_frame.showturtle()

settings_mode_button = turtle.Turtle()
settings_mode_button.color("white")
settings_mode_button.shape("square")
settings_mode_button.shapesize(1, 1)
settings_mode_button.penup()
settings_mode_button.goto(0, -252)
settings_mode_button.hideturtle()

title_label = turtle.Turtle()
title_label.color("red")
title_label.shape("square")
title_label.penup()
title_label.goto(0, 140)
title_label.hideturtle()

version_number = turtle.Turtle()
version_number.color("white")
version_number.shape("square")
version_number.penup()
version_number.goto(510, -347)
version_number.hideturtle()

stats_label = turtle.Turtle()
stats_label.color("red")
stats_label.shape("square")
stats_label.penup()
stats_label.goto(0, 240)
stats_label.hideturtle()

classic_mode_label = turtle.Turtle()
classic_mode_label.color("#ff5349")
classic_mode_label.shape("square")
classic_mode_label.penup()
classic_mode_label.goto(-320, 140)
classic_mode_label.hideturtle()

alien_mode_label = turtle.Turtle()
alien_mode_label.color("#ff5349")
alien_mode_label.shape("square")
alien_mode_label.penup()
alien_mode_label.goto(320, 140)
alien_mode_label.hideturtle()

classic_high_score_text = turtle.Turtle()
classic_high_score_text.color("white")
classic_high_score_text.shape("square")
classic_high_score_text.penup()
classic_high_score_text.goto(-320, 90)
classic_high_score_text.hideturtle()

bosses_killed_text = turtle.Turtle()
bosses_killed_text.color("white")
bosses_killed_text.shape("square")
bosses_killed_text.penup()
bosses_killed_text.goto(-320, 50)
bosses_killed_text.hideturtle()

red_bots_killed_text = turtle.Turtle()
red_bots_killed_text.color("white")
red_bots_killed_text.shape("square")
red_bots_killed_text.penup()
red_bots_killed_text.goto(-320, 10)
red_bots_killed_text.hideturtle()

yellow_bots_killed_text = turtle.Turtle()
yellow_bots_killed_text.color("white")
yellow_bots_killed_text.shape("square")
yellow_bots_killed_text.penup()
yellow_bots_killed_text.goto(-320, -30)
yellow_bots_killed_text.hideturtle()

blue_bots_killed_text = turtle.Turtle()
blue_bots_killed_text.color("white")
blue_bots_killed_text.shape("square")
blue_bots_killed_text.penup()
blue_bots_killed_text.goto(-320, -70)
blue_bots_killed_text.hideturtle()

classic_deaths_text = turtle.Turtle()
classic_deaths_text.color("white")
classic_deaths_text.shape("square")
classic_deaths_text.penup()
classic_deaths_text.goto(-320, -110)
classic_deaths_text.hideturtle()

classic_lasers_fired_text = turtle.Turtle()
classic_lasers_fired_text.color("white")
classic_lasers_fired_text.shape("square")
classic_lasers_fired_text.penup()
classic_lasers_fired_text.goto(-320, -150)
classic_lasers_fired_text.hideturtle()

classic_power_ups_picked_up_text = turtle.Turtle()
classic_power_ups_picked_up_text.color("white")
classic_power_ups_picked_up_text.shape("square")
classic_power_ups_picked_up_text.penup()
classic_power_ups_picked_up_text.goto(-320, -190)
classic_power_ups_picked_up_text.hideturtle()

alien_high_score_text = turtle.Turtle()
alien_high_score_text.color("white")
alien_high_score_text.shape("square")
alien_high_score_text.penup()
alien_high_score_text.goto(320, 90)
alien_high_score_text.hideturtle()

ufos_killed_text = turtle.Turtle()
ufos_killed_text.color("white")
ufos_killed_text.shape("square")
ufos_killed_text.penup()
ufos_killed_text.goto(320, 50)
ufos_killed_text.hideturtle()

big_aliens_killed_text = turtle.Turtle()
big_aliens_killed_text.color("white")
big_aliens_killed_text.shape("square")
big_aliens_killed_text.penup()
big_aliens_killed_text.goto(320, 10)
big_aliens_killed_text.hideturtle()

medium_aliens_killed_text = turtle.Turtle()
medium_aliens_killed_text.color("white")
medium_aliens_killed_text.shape("square")
medium_aliens_killed_text.penup()
medium_aliens_killed_text.goto(320, -30)
medium_aliens_killed_text.hideturtle()

small_aliens_killed_text = turtle.Turtle()
small_aliens_killed_text.color("white")
small_aliens_killed_text.shape("square")
small_aliens_killed_text.penup()
small_aliens_killed_text.goto(320, -70)
small_aliens_killed_text.hideturtle()

alien_deaths_text = turtle.Turtle()
alien_deaths_text.color("white")
alien_deaths_text.shape("square")
alien_deaths_text.penup()
alien_deaths_text.goto(320, -110)
alien_deaths_text.hideturtle()

damage_taken_text = turtle.Turtle()
damage_taken_text.color("white")
damage_taken_text.shape("square")
damage_taken_text.penup()
damage_taken_text.goto(320, -150)
damage_taken_text.hideturtle()

alien_lasers_fired_text = turtle.Turtle()
alien_lasers_fired_text.color("white")
alien_lasers_fired_text.shape("square")
alien_lasers_fired_text.penup()
alien_lasers_fired_text.goto(320, -190)
alien_lasers_fired_text.hideturtle()

jumps_text = turtle.Turtle()
jumps_text.color("white")
jumps_text.shape("square")
jumps_text.penup()
jumps_text.goto(320, -230)
jumps_text.hideturtle()

alien_power_ups_picked_up_text = turtle.Turtle()
alien_power_ups_picked_up_text.color("white")
alien_power_ups_picked_up_text.shape("square")
alien_power_ups_picked_up_text.penup()
alien_power_ups_picked_up_text.goto(320, -270)
alien_power_ups_picked_up_text.hideturtle()

settings_label = turtle.Turtle()
settings_label.color("red")
settings_label.shape("square")
settings_label.penup()
settings_label.goto(0, 240)
settings_label.hideturtle()

controls_label = turtle.Turtle()
controls_label.color("red")
controls_label.shape("square")
controls_label.penup()
controls_label.goto(0, 240)
controls_label.hideturtle()

control_toggle_button = turtle.Turtle()
control_toggle_button.color("white")
control_toggle_button.shape("square")
control_toggle_button.shapesize(3, 25)
control_toggle_button.penup()
control_toggle_button.goto(315.5, -227)
control_toggle_button.hideturtle()

control_toggle_button_frame = turtle.Turtle()
control_toggle_button_frame.color("#3D3D3D")
control_toggle_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
control_toggle_button_frame.shapesize(3, 25)
control_toggle_button_frame.penup()
control_toggle_button_frame.goto(315.5, -205)
control_toggle_button_frame.hideturtle()

button_sound_button_indicator = turtle.Turtle()
button_sound_button_indicator.shape("square")
button_sound_button_indicator.shapesize(3, 20)
button_sound_button_indicator.penup()
button_sound_button_indicator.goto(-177, 173)
button_sound_button_indicator.hideturtle()

button_sound_button = turtle.Turtle()
button_sound_button.color("white")
button_sound_button.shape("square")
button_sound_button.shapesize(3, 32)
button_sound_button.penup()
button_sound_button.goto(-355, 173)
button_sound_button.hideturtle()

button_sound_button_frame = turtle.Turtle()
button_sound_button_frame.color("#3D3D3D")
button_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
button_sound_button_frame.shapesize(3, 32)
button_sound_button_frame.penup()
button_sound_button_frame.goto(-325, 195)
button_sound_button_frame.hideturtle()

player_shooting_sound_button_indicator = turtle.Turtle()
player_shooting_sound_button_indicator.shape("square")
player_shooting_sound_button_indicator.shapesize(3, 20)
player_shooting_sound_button_indicator.penup()
player_shooting_sound_button_indicator.goto(-79, 93)
player_shooting_sound_button_indicator.hideturtle()

player_shooting_sound_button = turtle.Turtle()
player_shooting_sound_button.color("white")
player_shooting_sound_button.shape("square")
player_shooting_sound_button.shapesize(3, 32)
player_shooting_sound_button.penup()
player_shooting_sound_button.goto(-355, 93)
player_shooting_sound_button.hideturtle()

player_shooting_sound_button_frame = turtle.Turtle()
player_shooting_sound_button_frame.color("#3D3D3D")
player_shooting_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
player_shooting_sound_button_frame.shapesize(3, 32)
player_shooting_sound_button_frame.penup()
player_shooting_sound_button_frame.goto(-325, 115)
player_shooting_sound_button_frame.hideturtle()

enemy_shooting_sound_button_indicator = turtle.Turtle()
enemy_shooting_sound_button_indicator.shape("square")
enemy_shooting_sound_button_indicator.shapesize(3, 20)
enemy_shooting_sound_button_indicator.penup()
enemy_shooting_sound_button_indicator.goto(-88, 13)
enemy_shooting_sound_button_indicator.hideturtle()

enemy_shooting_sound_button = turtle.Turtle()
enemy_shooting_sound_button.color("white")
enemy_shooting_sound_button.shape("square")
enemy_shooting_sound_button.shapesize(3, 32)
enemy_shooting_sound_button.penup()
enemy_shooting_sound_button.goto(-355, 13)
enemy_shooting_sound_button.hideturtle()

enemy_shooting_sound_button_frame = turtle.Turtle()
enemy_shooting_sound_button_frame.color("#3D3D3D")
enemy_shooting_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
enemy_shooting_sound_button_frame.shapesize(3, 32)
enemy_shooting_sound_button_frame.penup()
enemy_shooting_sound_button_frame.goto(-325, 35)
enemy_shooting_sound_button_frame.hideturtle()

player_death_sound_button_indicator = turtle.Turtle()
player_death_sound_button_indicator.shape("square")
player_death_sound_button_indicator.shapesize(3, 20)
player_death_sound_button_indicator.penup()
player_death_sound_button_indicator.goto(-111, -67)
player_death_sound_button_indicator.hideturtle()

player_death_sound_button = turtle.Turtle()
player_death_sound_button.color("white")
player_death_sound_button.shape("square")
player_death_sound_button.shapesize(3, 32)
player_death_sound_button.penup()
player_death_sound_button.goto(-355, -67)
player_death_sound_button.hideturtle()

player_death_sound_button_frame = turtle.Turtle()
player_death_sound_button_frame.color("#3D3D3D")
player_death_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
player_death_sound_button_frame.shapesize(3, 32)
player_death_sound_button_frame.penup()
player_death_sound_button_frame.goto(-325, -45)
player_death_sound_button_frame.hideturtle()

enemy_death_sound_button_indicator = turtle.Turtle()
enemy_death_sound_button_indicator.shape("square")
enemy_death_sound_button_indicator.shapesize(3, 20)
enemy_death_sound_button_indicator.penup()
enemy_death_sound_button_indicator.goto(-121, -147)
enemy_death_sound_button_indicator.hideturtle()

enemy_death_sound_button = turtle.Turtle()
enemy_death_sound_button.color("white")
enemy_death_sound_button.shape("square")
enemy_death_sound_button.shapesize(3, 32)
enemy_death_sound_button.penup()
enemy_death_sound_button.goto(-355, -147)
enemy_death_sound_button.hideturtle()

enemy_death_sound_button_frame = turtle.Turtle()
enemy_death_sound_button_frame.color("#3D3D3D")
enemy_death_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
enemy_death_sound_button_frame.shapesize(3, 32)
enemy_death_sound_button_frame.penup()
enemy_death_sound_button_frame.goto(-325, -125)
enemy_death_sound_button_frame.hideturtle()

player_hit_sound_button_indicator = turtle.Turtle()
player_hit_sound_button_indicator.shape("square")
player_hit_sound_button_indicator.shapesize(3, 20)
player_hit_sound_button_indicator.penup()
player_hit_sound_button_indicator.goto(-132, -227)
player_hit_sound_button_indicator.hideturtle()

player_hit_sound_button = turtle.Turtle()
player_hit_sound_button.color("white")
player_hit_sound_button.shape("square")
player_hit_sound_button.shapesize(3, 32)
player_hit_sound_button.penup()
player_hit_sound_button.goto(-355, -227)
player_hit_sound_button.hideturtle()

player_hit_sound_button_frame = turtle.Turtle()
player_hit_sound_button_frame.color("#3D3D3D")
player_hit_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
player_hit_sound_button_frame.shapesize(3, 32)
player_hit_sound_button_frame.penup()
player_hit_sound_button_frame.goto(-325, -205)
player_hit_sound_button_frame.hideturtle()

enemy_hit_sound_button_indicator = turtle.Turtle()
enemy_hit_sound_button_indicator.shape("square")
enemy_hit_sound_button_indicator.shapesize(3, 20)
enemy_hit_sound_button_indicator.penup()
enemy_hit_sound_button_indicator.goto(-143, -307)
enemy_hit_sound_button_indicator.hideturtle()

enemy_hit_sound_button = turtle.Turtle()
enemy_hit_sound_button.color("white")
enemy_hit_sound_button.shape("square")
enemy_hit_sound_button.shapesize(3, 32)
enemy_hit_sound_button.penup()
enemy_hit_sound_button.goto(-355, -307)
enemy_hit_sound_button.hideturtle()

enemy_hit_sound_button_frame = turtle.Turtle()
enemy_hit_sound_button_frame.color("#3D3D3D")
enemy_hit_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
enemy_hit_sound_button_frame.shapesize(3, 32)
enemy_hit_sound_button_frame.penup()
enemy_hit_sound_button_frame.goto(-325, -285)
enemy_hit_sound_button_frame.hideturtle()

power_up_pickup_sound_button_indicator = turtle.Turtle()
power_up_pickup_sound_button_indicator.shape("square")
power_up_pickup_sound_button_indicator.shapesize(3, 20)
power_up_pickup_sound_button_indicator.penup()
power_up_pickup_sound_button_indicator.goto(561.5, 173)
power_up_pickup_sound_button_indicator.hideturtle()

power_up_pickup_sound_button = turtle.Turtle()
power_up_pickup_sound_button.color("white")
power_up_pickup_sound_button.shape("square")
power_up_pickup_sound_button.shapesize(3, 32)
power_up_pickup_sound_button.penup()
power_up_pickup_sound_button.goto(285.5, 173)
power_up_pickup_sound_button.hideturtle()

power_up_pickup_sound_button_frame = turtle.Turtle()
power_up_pickup_sound_button_frame.color("#3D3D3D")
power_up_pickup_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
power_up_pickup_sound_button_frame.shapesize(3, 32)
power_up_pickup_sound_button_frame.penup()
power_up_pickup_sound_button_frame.goto(315.5, 195)
power_up_pickup_sound_button_frame.hideturtle()

power_up_spawn_sound_button_indicator = turtle.Turtle()
power_up_spawn_sound_button_indicator.shape("square")
power_up_spawn_sound_button_indicator.shapesize(3, 20)
power_up_spawn_sound_button_indicator.penup()
power_up_spawn_sound_button_indicator.goto(552.5, 93)
power_up_spawn_sound_button_indicator.hideturtle()

power_up_spawn_sound_button = turtle.Turtle()
power_up_spawn_sound_button.color("white")
power_up_spawn_sound_button.shape("square")
power_up_spawn_sound_button.shapesize(3, 32)
power_up_spawn_sound_button.penup()
power_up_spawn_sound_button.goto(285.5, 93)
power_up_spawn_sound_button.hideturtle()

power_up_spawn_sound_button_frame = turtle.Turtle()
power_up_spawn_sound_button_frame.color("#3D3D3D")
power_up_spawn_sound_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
power_up_spawn_sound_button_frame.shapesize(3, 32)
power_up_spawn_sound_button_frame.penup()
power_up_spawn_sound_button_frame.goto(315.5, 115)
power_up_spawn_sound_button_frame.hideturtle()

go_right_control_button = turtle.Turtle()
go_right_control_button.color("white")
go_right_control_button.shape("square")
go_right_control_button.shapesize(3, 25)
go_right_control_button.penup()
go_right_control_button.goto(-325, 173)
go_right_control_button.hideturtle()

go_right_control_button_frame = turtle.Turtle()
go_right_control_button_frame.color("#3D3D3D")
go_right_control_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
go_right_control_button_frame.shapesize(3, 25)
go_right_control_button_frame.penup()
go_right_control_button_frame.goto(-325, 195)
go_right_control_button_frame.hideturtle()

go_left_control_button = turtle.Turtle()
go_left_control_button.color("white")
go_left_control_button.shape("square")
go_left_control_button.shapesize(3, 25)
go_left_control_button.penup()
go_left_control_button.goto(-325, 93)
go_left_control_button.hideturtle()

go_left_control_button_frame = turtle.Turtle()
go_left_control_button_frame.color("#3D3D3D")
go_left_control_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
go_left_control_button_frame.shapesize(3, 25)
go_left_control_button_frame.penup()
go_left_control_button_frame.goto(-325, 115)
go_left_control_button_frame.hideturtle()

shoot_control_button = turtle.Turtle()
shoot_control_button.color("white")
shoot_control_button.shape("square")
shoot_control_button.shapesize(3, 25)
shoot_control_button.penup()
shoot_control_button.goto(-325, 13)
shoot_control_button.hideturtle()

shoot_control_button_frame = turtle.Turtle()
shoot_control_button_frame.color("#3D3D3D")
shoot_control_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
shoot_control_button_frame.shapesize(3, 25)
shoot_control_button_frame.penup()
shoot_control_button_frame.goto(-325, 35)
shoot_control_button_frame.hideturtle()

jump_control_button = turtle.Turtle()
jump_control_button.color("white")
jump_control_button.shape("square")
jump_control_button.shapesize(3, 25)
jump_control_button.penup()
jump_control_button.goto(-325, -67)
jump_control_button.hideturtle()

jump_control_button_frame = turtle.Turtle()
jump_control_button_frame.color("#3D3D3D")
jump_control_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
jump_control_button_frame.shapesize(3, 25)
jump_control_button_frame.penup()
jump_control_button_frame.goto(-325, -45)
jump_control_button_frame.hideturtle()

go_back_button = turtle.Turtle()
go_back_button.color("white")
go_back_button.shape("square")
go_back_button.shapesize(1, 1)
go_back_button.penup()
go_back_button.goto(0, 0)
go_back_button.hideturtle()

go_back_button_frame = turtle.Turtle()
go_back_button_frame.color("#3D3D3D")
go_back_button_frame.shape("square")
go_back_button_frame.shapesize(1.5, 9.5)
go_back_button_frame.penup()
go_back_button_frame.goto(0, 0)
go_back_button_frame.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.shape("Textures/Player/Player.gif")
player.color("gray")
player.shapesize(5, 2)
player.penup()
player.goto(0, -300)
player.direction = "stop"
player.hideturtle()

laser = turtle.Turtle()
laser.color("green")
laser.shape("Textures/Lasers/Player_Laser.gif")
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

enemy1 = turtle.Turtle()
enemy1.color("gray")
enemy1.shape("Textures/Enemies/Enemy(1-5).gif")
enemy1.penup()
enemy1.speed(0)
enemy1.shapesize(2, 2)
enemy1.goto(-200, 220)
enemy1.direction = "down"
enemy1.hideturtle()

enemy2 = turtle.Turtle()
enemy2.color("gray")
enemy2.shape("Textures/Enemies/Enemy(1-5).gif")
enemy2.penup()
enemy2.speed(0)
enemy2.shapesize(2, 2)
enemy2.goto(200, 220)
enemy2.direction = "down"
enemy2.hideturtle()

enemy3 = turtle.Turtle()
enemy3.color("gray")
enemy3.shape("Textures/Enemies/Enemy(1-5).gif")
enemy3.penup()
enemy3.speed(0)
enemy3.shapesize(2, 2)
enemy3.goto(500, 220)
enemy3.direction = "down"
enemy3.hideturtle()

enemy4 = turtle.Turtle()
enemy4.color("gray")
enemy4.shape("Textures/Enemies/Enemy(1-5).gif")
enemy4.penup()
enemy4.speed(0)
enemy4.shapesize(2, 2)
enemy4.goto(-500, 220)
enemy4.direction = "down"
enemy4.hideturtle()

enemy5 = turtle.Turtle()
enemy5.color("gray")
enemy5.shape("Textures/Enemies/Enemy(1-5).gif")
enemy5.penup()
enemy5.speed(0)
enemy5.shapesize(2, 2)
enemy5.goto(-400, 220)
enemy5.direction = "down"
enemy5.hideturtle()

enemy6 = turtle.Turtle()
enemy6.color("gray")
enemy6.shape("Textures/Enemies/Enemy(6-10).gif")
enemy6.penup()
enemy6.speed(0)
enemy6.shapesize(2, 2)
enemy6.goto(-300, 220)
enemy6.direction = "down"
enemy6.hideturtle()

enemy7 = turtle.Turtle()
enemy7.color("gray")
enemy7.shape("Textures/Enemies/Enemy(6-10).gif")
enemy7.penup()
enemy7.speed(0)
enemy7.shapesize(2, 2)
enemy7.goto(-250, 220)
enemy7.direction = "down"
enemy7.hideturtle()

enemy8 = turtle.Turtle()
enemy8.color("gray")
enemy8.shape("Textures/Enemies/Enemy(6-10).gif")
enemy8.penup()
enemy8.speed(0)
enemy8.shapesize(2, 2)
enemy8.goto(250, 220)
enemy8.direction = "down"
enemy8.hideturtle()

enemy9 = turtle.Turtle()
enemy9.color("gray")
enemy9.shape("Textures/Enemies/Enemy(6-10).gif")
enemy9.penup()
enemy9.speed(0)
enemy9.shapesize(2, 2)
enemy9.goto(-350, 220)
enemy9.direction = "down"
enemy9.hideturtle()

enemy10 = turtle.Turtle()
enemy10.color("gray")
enemy10.shape("Textures/Enemies/Enemy(6-10).gif")
enemy10.penup()
enemy10.speed(0)
enemy10.shapesize(2, 2)
enemy10.goto(350, 220)
enemy10.direction = "down"
enemy10.hideturtle()

enemy11 = turtle.Turtle()
enemy11.color("gray")
enemy11.shape("Textures/Enemies/Enemy(11-15).gif")
enemy11.penup()
enemy11.speed(0)
enemy11.shapesize(2, 2)
enemy11.goto(375, 220)
enemy11.direction = "down"
enemy11.hideturtle()

enemy12 = turtle.Turtle()
enemy12.color("gray")
enemy12.shape("Textures/Enemies/Enemy(11-15).gif")
enemy12.penup()
enemy12.speed(0)
enemy12.shapesize(2, 2)
enemy12.goto(-375, 220)
enemy12.direction = "down"
enemy12.hideturtle()

enemy13 = turtle.Turtle()
enemy13.color("gray")
enemy13.shape("Textures/Enemies/Enemy(11-15).gif")
enemy13.penup()
enemy13.speed(0)
enemy13.shapesize(2, 2)
enemy13.goto(325, 220)
enemy13.direction = "down"
enemy13.hideturtle()

enemy14 = turtle.Turtle()
enemy14.color("gray")
enemy14.shape("Textures/Enemies/Enemy(11-15).gif")
enemy14.penup()
enemy14.speed(0)
enemy14.shapesize(2, 2)
enemy14.goto(-325, 220)
enemy14.direction = "down"
enemy14.hideturtle()

enemy15 = turtle.Turtle()
enemy15.color("gray")
enemy15.shape("Textures/Enemies/Enemy(11-15).gif")
enemy15.penup()
enemy15.speed(0)
enemy15.shapesize(2, 2)
enemy15.goto(275, 220)
enemy15.direction = "down"
enemy15.hideturtle()

boss = turtle.Turtle()
boss.color("gray")
boss.shape("Textures/Enemies/Boss.gif")
boss.penup()
boss.speed(0)
boss.shapesize(2, 2)
boss.goto(175, 220)
boss.direction = "down"
boss.hideturtle()

enemy1_laser = turtle.Turtle()
enemy1_laser.color("blue")
enemy1_laser.shape("Textures/Lasers/Enemy(1-5)_Laser.gif")
enemy1_laser.penup()
enemy1_laser.speed(0)
enemy1_laser.shapesize(2.25, 0.5)
enemy1_laser.direction = "down"
enemy1_laser.goto(-200, 140)
enemy1_laser.hideturtle()

enemy2_laser = turtle.Turtle()
enemy2_laser.color("blue")
enemy2_laser.shape("Textures/Lasers/Enemy(1-5)_Laser.gif")
enemy2_laser.penup()
enemy2_laser.speed(0)
enemy2_laser.shapesize(2.25, 0.5)
enemy2_laser.direction = "down"
enemy2_laser.goto(200, 140)
enemy2_laser.hideturtle()

enemy3_laser = turtle.Turtle()
enemy3_laser.color("blue")
enemy3_laser.shape("Textures/Lasers/Enemy(1-5)_Laser.gif")
enemy3_laser.penup()
enemy3_laser.speed(0)
enemy3_laser.shapesize(2.25, 0.5)
enemy3_laser.direction = "down"
enemy3_laser.goto(500, 140)
enemy3_laser.hideturtle()

enemy4_laser = turtle.Turtle()
enemy4_laser.color("blue")
enemy4_laser.shape("Textures/Lasers/Enemy(1-5)_Laser.gif")
enemy4_laser.penup()
enemy4_laser.speed(0)
enemy4_laser.shapesize(2.25, 0.5)
enemy4_laser.direction = "down"
enemy4_laser.goto(-500, 140)
enemy4_laser.hideturtle()

enemy5_laser = turtle.Turtle()
enemy5_laser.color("blue")
enemy5_laser.shape("Textures/Lasers/Enemy(1-5)_Laser.gif")
enemy5_laser.penup()
enemy5_laser.speed(0)
enemy5_laser.shapesize(2.25, 0.5)
enemy5_laser.direction = "down"
enemy5_laser.goto(-400, 140)
enemy5_laser.hideturtle()

enemy6_laser = turtle.Turtle()
enemy6_laser.color("yellow")
enemy6_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
enemy6_laser.penup()
enemy6_laser.speed(0)
enemy6_laser.shapesize(2.25, 0.5)
enemy6_laser.direction = "down"
enemy6_laser.goto(-300, 140)
enemy6_laser.hideturtle()

enemy7_laser = turtle.Turtle()
enemy7_laser.color("yellow")
enemy7_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
enemy7_laser.penup()
enemy7_laser.speed(0)
enemy7_laser.shapesize(2.25, 0.5)
enemy7_laser.direction = "down"
enemy7_laser.goto(-250, 140)
enemy7_laser.hideturtle()

enemy8_laser = turtle.Turtle()
enemy8_laser.color("yellow")
enemy8_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
enemy8_laser.penup()
enemy8_laser.speed(0)
enemy8_laser.shapesize(2.25, 0.5)
enemy8_laser.direction = "down"
enemy8_laser.goto(250, 140)
enemy8_laser.hideturtle()

enemy9_laser = turtle.Turtle()
enemy9_laser.color("yellow")
enemy9_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
enemy9_laser.penup()
enemy9_laser.speed(0)
enemy9_laser.shapesize(2.25, 0.5)
enemy9_laser.direction = "down"
enemy9_laser.goto(-350, 140)
enemy9_laser.hideturtle()

enemy10_laser = turtle.Turtle()
enemy10_laser.color("yellow")
enemy10_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
enemy10_laser.penup()
enemy10_laser.speed(0)
enemy10_laser.shapesize(2.25, 0.5)
enemy10_laser.direction = "down"
enemy10_laser.goto(350, 140)
enemy10_laser.hideturtle()

enemy11_laser = turtle.Turtle()
enemy11_laser.color("red")
enemy11_laser.shape("Textures/Lasers/Enemy(11-15)_Laser.gif")
enemy11_laser.penup()
enemy11_laser.speed(0)
enemy11_laser.shapesize(2.25, 0.5)
enemy11_laser.direction = "down"
enemy11_laser.goto(375, 140)
enemy11_laser.hideturtle()

enemy12_laser = turtle.Turtle()
enemy12_laser.color("red")
enemy12_laser.shape("Textures/Lasers/Enemy(11-15)_Laser.gif")
enemy12_laser.penup()
enemy12_laser.speed(0)
enemy12_laser.shapesize(2.25, 0.5)
enemy12_laser.direction = "down"
enemy12_laser.goto(-375, 140)
enemy12_laser.hideturtle()

enemy13_laser = turtle.Turtle()
enemy13_laser.color("red")
enemy13_laser.shape("Textures/Lasers/Enemy(11-15)_Laser.gif")
enemy13_laser.penup()
enemy13_laser.speed(0)
enemy13_laser.shapesize(2.25, 0.5)
enemy13_laser.direction = "down"
enemy13_laser.goto(325, 140)
enemy13_laser.hideturtle()

enemy14_laser = turtle.Turtle()
enemy14_laser.color("red")
enemy14_laser.shape("Textures/Lasers/Enemy(11-15)_Laser.gif")
enemy14_laser.penup()
enemy14_laser.speed(0)
enemy14_laser.shapesize(2.25, 0.5)
enemy14_laser.direction = "down"
enemy14_laser.goto(-325, 140)
enemy14_laser.hideturtle()

enemy15_laser = turtle.Turtle()
enemy15_laser.color("red")
enemy15_laser.shape("Textures/Lasers/Enemy(11-15)_Laser.gif")
enemy15_laser.penup()
enemy15_laser.speed(0)
enemy15_laser.shapesize(2.25, 0.5)
enemy15_laser.direction = "down"
enemy15_laser.goto(275, 140)
enemy15_laser.hideturtle()

boss_laser = turtle.Turtle()
boss_laser.color("pink")
boss_laser.shape("Textures/Lasers/Boss_Laser.gif")
boss_laser.penup()
boss_laser.speed(0)
boss_laser.shapesize(2.25, 0.5)
boss_laser.direction = "down"
boss_laser.goto(175, 140)
boss_laser.hideturtle()

enemy11_health_bar = turtle.Turtle()
enemy11_health_bar.color("green")
enemy11_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
enemy11_health_bar.penup()
enemy11_health_bar.speed(0)
enemy11_health_bar.shapesize(1, 1)
enemy11_health_bar.direction = "down"
enemy11_health_bar.goto(375, 290)
enemy11_health_bar.hideturtle()

enemy12_health_bar = turtle.Turtle()
enemy12_health_bar.color("green")
enemy12_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
enemy12_health_bar.penup()
enemy12_health_bar.speed(0)
enemy12_health_bar.shapesize(1, 1)
enemy12_health_bar.direction = "down"
enemy12_health_bar.goto(-375, 290)
enemy12_health_bar.hideturtle()

enemy13_health_bar = turtle.Turtle()
enemy13_health_bar.color("green")
enemy13_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
enemy13_health_bar.penup()
enemy13_health_bar.speed(0)
enemy13_health_bar.shapesize(1, 1)
enemy13_health_bar.direction = "down"
enemy13_health_bar.goto(325, 290)
enemy13_health_bar.hideturtle()

enemy14_health_bar = turtle.Turtle()
enemy14_health_bar.color("green")
enemy14_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
enemy14_health_bar.penup()
enemy14_health_bar.speed(0)
enemy14_health_bar.shapesize(1, 1)
enemy14_health_bar.direction = "down"
enemy14_health_bar.goto(-325, 290)
enemy14_health_bar.hideturtle()

enemy15_health_bar = turtle.Turtle()
enemy15_health_bar.color("green")
enemy15_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
enemy15_health_bar.penup()
enemy15_health_bar.speed(0)
enemy15_health_bar.shapesize(1, 1)
enemy15_health_bar.direction = "down"
enemy15_health_bar.goto(275, 290)
enemy15_health_bar.hideturtle()

boss_health_bar = turtle.Turtle()
boss_health_bar.color("green")
boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
boss_health_bar.penup()
boss_health_bar.speed(0)
boss_health_bar.shapesize(1, 1)
boss_health_bar.direction = "down"
boss_health_bar.goto(175, 290)
boss_health_bar.hideturtle()

ground = turtle.Turtle()
ground.shape("Textures/Ground/Ground.gif")
ground.color("gray")
ground.shapesize(22.5, 80)
ground.penup()
ground.goto(0, -731)
ground.direction = "stop"
ground.hideturtle()

earth = turtle.Turtle()
earth.shape("Textures/Background/Earth.gif")
earth.color("blue")
earth.shapesize(3, 3)
earth.penup()
earth.goto(0, 200)
earth.direction = "stop"
earth.hideturtle()

space_ship = turtle.Turtle()
space_ship.shape("Textures/Background/Space_Ship.gif")
space_ship.color("gray")
space_ship.shapesize(3, 6)
space_ship.penup()
space_ship.goto(0, -116)
space_ship.direction = "stop"
space_ship.hideturtle()

player_head = turtle.Turtle()
player_head.shape("Textures/Player/Player_Head_Still_Right.gif")
player_head.color("brown")
player_head.shapesize(4, 2)
player_head.penup()
player_head.goto(0, -150)
player_head.direction = "stop"
player_head.hideturtle()

oxygen_tank = turtle.Turtle()
oxygen_tank.shape("Textures/Other/Oxygen_Tank.gif")
oxygen_tank.color("yellow")
oxygen_tank.shapesize(1.5, 0.75)
oxygen_tank.penup()
oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
oxygen_tank.direction = "stop"
oxygen_tank.hideturtle()

player_gun = turtle.Turtle()
player_gun.shape("Textures/Gun/Player_Gun_Right.gif")
player_gun.color("gray")
player_gun.shapesize(0.67, 2)
player_gun.penup()
player_gun.goto(player_head.xcor(), player_head.ycor() + 12)
player_gun.direction = "stop"
player_gun.hideturtle()

player_head_laser = turtle.Turtle()
player_head_laser.shape("Textures/Lasers/Player_Head_Laser.gif")
player_head_laser.color("red")
player_head_laser.shapesize(0.33, 2)
player_head_laser.penup()
player_head_laser.goto(player_gun.xcor(), player_gun.ycor())
player_head_laser.hideturtle()

player_head_health_bar = turtle.Turtle()
player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
player_head_health_bar.color("green")
player_head_health_bar.shapesize(1, 1)
player_head_health_bar.penup()
player_head_health_bar.goto(0, 0)
player_head_health_bar.hideturtle()

alien1 = turtle.Turtle()
alien1.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
alien1.color("green")
alien1.shapesize(4, 2)
alien1.penup()
alien1.goto(-800, -150)
alien1.direction = "stop"
alien1.hideturtle()

alien2 = turtle.Turtle()
alien2.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
alien2.color("green")
alien2.shapesize(4, 2)
alien2.penup()
alien2.goto(-700, -150)
alien2.direction = "stop"
alien2.hideturtle()

alien3 = turtle.Turtle()
alien3.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
alien3.color("green")
alien3.shapesize(4, 2)
alien3.penup()
alien3.goto(800, -150)
alien3.direction = "stop"
alien3.hideturtle()

alien4 = turtle.Turtle()
alien4.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
alien4.color("green")
alien4.shapesize(4, 2)
alien4.penup()
alien4.goto(700, -150)
alien4.direction = "stop"
alien4.hideturtle()

alien5 = turtle.Turtle()
alien5.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
alien5.color("green")
alien5.shapesize(4, 2)
alien5.penup()
alien5.goto(750, -150)
alien5.direction = "stop"
alien5.hideturtle()

alien6 = turtle.Turtle()
alien6.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
alien6.color("green")
alien6.shapesize(5.5, 3)
alien6.penup()
alien6.goto(850, -130)
alien6.direction = "stop"
alien6.hideturtle()

alien7 = turtle.Turtle()
alien7.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
alien7.color("green")
alien7.shapesize(5.5, 3)
alien7.penup()
alien7.goto(-850, -130)
alien7.direction = "stop"
alien7.hideturtle()

alien8 = turtle.Turtle()
alien8.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
alien8.color("green")
alien8.shapesize(5.5, 3)
alien8.penup()
alien8.goto(900, -130)
alien8.direction = "stop"
alien8.hideturtle()

alien9 = turtle.Turtle()
alien9.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
alien9.color("green")
alien9.shapesize(5.5, 3)
alien9.penup()
alien9.goto(-900, -130)
alien9.direction = "stop"
alien9.hideturtle()

alien10 = turtle.Turtle()
alien10.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
alien10.color("green")
alien10.shapesize(5.5, 3)
alien10.penup()
alien10.goto(725, -130)
alien10.direction = "stop"
alien10.hideturtle()

alien11 = turtle.Turtle()
alien11.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
alien11.color("green")
alien11.shapesize(8.5, 3.5)
alien11.penup()
alien11.goto(-725, -93)
alien11.direction = "stop"
alien11.hideturtle()

alien12 = turtle.Turtle()
alien12.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
alien12.color("green")
alien12.shapesize(8.5, 3.5)
alien12.penup()
alien12.goto(775, -93)
alien12.direction = "stop"
alien12.hideturtle()

alien13 = turtle.Turtle()
alien13.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
alien13.color("green")
alien13.shapesize(8.5, 3.5)
alien13.penup()
alien13.goto(-775, -93)
alien13.direction = "stop"
alien13.hideturtle()

alien14 = turtle.Turtle()
alien14.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
alien14.color("green")
alien14.shapesize(8.5, 3.5)
alien14.penup()
alien14.goto(825, -93)
alien14.direction = "stop"
alien14.hideturtle()

alien15 = turtle.Turtle()
alien15.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
alien15.color("green")
alien15.shapesize(8.5, 3.5)
alien15.penup()
alien15.goto(-825, -93)
alien15.direction = "stop"
alien15.hideturtle()

alien_boss = turtle.Turtle()
alien_boss.shape("Textures/Aliens/Alien_Boss.gif")
alien_boss.color("gray")
alien_boss.shapesize(1.75, 6)
alien_boss.penup()
alien_boss.goto(875, -20)
alien_boss.direction = "stop"
alien_boss.hideturtle()

alien_boss_laser = turtle.Turtle()
alien_boss_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
alien_boss_laser.color("yellow")
alien_boss_laser.shapesize(2.25, 0.5)
alien_boss_laser.penup()
alien_boss_laser.goto(877, -90)
alien_boss_laser.direction = "stop"
alien_boss_laser.hideturtle()

alien6_health_bar = turtle.Turtle()
alien6_health_bar.color("green")
alien6_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
alien6_health_bar.penup()
alien6_health_bar.shapesize(1, 1)
alien6_health_bar.goto(850, -45)
alien6_health_bar.hideturtle()

alien7_health_bar = turtle.Turtle()
alien7_health_bar.color("green")
alien7_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
alien7_health_bar.penup()
alien7_health_bar.shapesize(1, 1)
alien7_health_bar.goto(-850, -45)
alien7_health_bar.hideturtle()

alien8_health_bar = turtle.Turtle()
alien8_health_bar.color("green")
alien8_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
alien8_health_bar.penup()
alien8_health_bar.shapesize(1, 1)
alien8_health_bar.goto(900, -45)
alien8_health_bar.hideturtle()

alien9_health_bar = turtle.Turtle()
alien9_health_bar.color("green")
alien9_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
alien9_health_bar.penup()
alien9_health_bar.shapesize(1, 1)
alien9_health_bar.goto(-900, -45)
alien9_health_bar.hideturtle()

alien10_health_bar = turtle.Turtle()
alien10_health_bar.color("green")
alien10_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
alien10_health_bar.penup()
alien10_health_bar.shapesize(1, 1)
alien10_health_bar.goto(725, -45)
alien10_health_bar.hideturtle()

alien11_health_bar = turtle.Turtle()
alien11_health_bar.color("green")
alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
alien11_health_bar.penup()
alien11_health_bar.shapesize(1, 1)
alien11_health_bar.goto(-725, 30)
alien11_health_bar.hideturtle()

alien12_health_bar = turtle.Turtle()
alien12_health_bar.color("green")
alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
alien12_health_bar.penup()
alien12_health_bar.shapesize(1, 1)
alien12_health_bar.goto(775, 30)
alien12_health_bar.hideturtle()

alien13_health_bar = turtle.Turtle()
alien13_health_bar.color("green")
alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
alien13_health_bar.penup()
alien13_health_bar.shapesize(1, 1)
alien13_health_bar.goto(-775, 30)
alien13_health_bar.hideturtle()

alien14_health_bar = turtle.Turtle()
alien14_health_bar.color("green")
alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
alien14_health_bar.penup()
alien14_health_bar.shapesize(1, 1)
alien14_health_bar.goto(825, 30)
alien14_health_bar.hideturtle()

alien15_health_bar = turtle.Turtle()
alien15_health_bar.color("green")
alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
alien15_health_bar.penup()
alien15_health_bar.shapesize(1, 1)
alien15_health_bar.goto(-825, 30)
alien15_health_bar.hideturtle()

alien_boss_health_bar = turtle.Turtle()
alien_boss_health_bar.color("green")
alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
alien_boss_health_bar.penup()
alien_boss_health_bar.shapesize(1, 1)
alien_boss_health_bar.goto(875, 50)
alien_boss_health_bar.hideturtle()

yellow_lightning_power_up = turtle.Turtle()
yellow_lightning_power_up.color("yellow")
yellow_lightning_power_up.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
yellow_lightning_power_up.penup()
yellow_lightning_power_up.shapesize(2, 2)
yellow_lightning_power_up.direction = "stop"
yellow_lightning_power_up.hideturtle()

blue_lightning_power_up = turtle.Turtle()
blue_lightning_power_up.color("blue")
blue_lightning_power_up.shape("Textures/Power_Ups/Blue_Lightning_Power_Up.gif")
blue_lightning_power_up.penup()
blue_lightning_power_up.shapesize(2, 2)
blue_lightning_power_up.direction = "stop"
blue_lightning_power_up.hideturtle()

green_lightning_power_up = turtle.Turtle()
green_lightning_power_up.color("green")
green_lightning_power_up.shape("Textures/Power_Ups/Green_Lightning_Power_Up.gif")
green_lightning_power_up.penup()
green_lightning_power_up.shapesize(2, 2)
green_lightning_power_up.direction = "stop"
green_lightning_power_up.hideturtle()

red_lightning_power_up = turtle.Turtle()
red_lightning_power_up.color("red")
red_lightning_power_up.shape("Textures/Power_Ups/Red_Lightning_Power_Up.gif")
red_lightning_power_up.penup()
red_lightning_power_up.shapesize(2, 2)
red_lightning_power_up.direction = "stop"
red_lightning_power_up.hideturtle()

yellow_power_up_indicator = turtle.Turtle()
yellow_power_up_indicator.color("#737000")
yellow_power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
yellow_power_up_indicator.penup()
yellow_power_up_indicator.shapesize(1, 1)
yellow_power_up_indicator.direction = "stop"
yellow_power_up_indicator.goto(-95, 300)
yellow_power_up_indicator.hideturtle()

yellow_power_up_text = turtle.Turtle()
yellow_power_up_text.shape("square")
yellow_power_up_text.color("#737000")
yellow_power_up_text.penup()
yellow_power_up_text.hideturtle()
yellow_power_up_text.goto(-65, 278)

blue_power_up_indicator = turtle.Turtle()
blue_power_up_indicator.color("#00004A")
blue_power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
blue_power_up_indicator.penup()
blue_power_up_indicator.shapesize(1, 1)
blue_power_up_indicator.direction = "stop"
blue_power_up_indicator.goto(-20, 300)
blue_power_up_indicator.hideturtle()

blue_power_up_text = turtle.Turtle()
blue_power_up_text.shape("square")
blue_power_up_text.color("#00001A")
blue_power_up_text.penup()
blue_power_up_text.hideturtle()
blue_power_up_text.goto(10, 278)

extra_power_up_indicator = turtle.Turtle()
extra_power_up_indicator.color("#001C00")
extra_power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
extra_power_up_indicator.penup()
extra_power_up_indicator.shapesize(1, 1)
extra_power_up_indicator.direction = "stop"
extra_power_up_indicator.goto(50, 300)
extra_power_up_indicator.hideturtle()

extra_power_up_text = turtle.Turtle()
extra_power_up_text.shape("square")
extra_power_up_text.color("#001C00")
extra_power_up_text.penup()
extra_power_up_text.hideturtle()
extra_power_up_text.goto(80, 278)

# These are all the functions that are used for all the different controls in the game and buttons of the game
# The first 5 are for controlling the game. This includes code for how the player is to move, jump, and turn
# The functions work differently in different modes of the game


def go_right():
    if mode == "Classic_Mode":
        player.direction = "right"
        move()
    if mode == "Alien_Mode":
        global move_update
        global jump_update
        global move_right
        global Start_X
        global head_death_animation
        if move_update == 0 and jump_update == 0 and player_head.xcor() < 530 and head_death_animation == 0:
            player_head.direction = "right"
            player_gun.direction = "right"
            player_gun.goto(player_head.xcor() + 20, player_head.ycor())
            player_gun.showturtle()
            Start_X = player_head.xcor()
            move_right = 1


def go_left():
    if mode == "Classic_Mode":
        player.direction = "left"
        move()
    if mode == "Alien_Mode":
        global move_update
        global jump_update
        global move_left
        global Start_X
        global head_death_animation
        if move_update == 0 and jump_update == 0 and player_head.xcor() > -530 and head_death_animation == 0:
            player_head.direction = "left"
            player_gun.direction = "left"
            player_gun.goto(player_head.xcor() - 20, player_head.ycor())
            player_gun.showturtle()
            Start_X = player_head.xcor()
            move_left = 1


def move():
    if mode == "Classic_Mode":
        if player.direction == "left" and player.xcor() > -620 and death_animation == 0:
            x = player.xcor()
            player.setx(x - 30)

        if player.direction == "right" and player.xcor() < 620 and death_animation == 0:
            x = player.xcor()
            player.setx(x + 30)


def jump():
    if mode == "Alien_Mode":
        global jump_update
        global do_jump
        global jumps
        global Start_X
        global Start_Y
        if jump_update == 0 and player_head.direction != "stop":
            if (player_head.direction == "right" and player_head.xcor() < 390) or (player_head.direction == "left" and player_head.xcor() > -390):
                Start_Y = player_head.ycor()
                Start_X = player_head.xcor()
                do_jump = 1
                if god_mode == 0:
                    jumps = jumps + 1
                    stats = open("config/Statistics.txt", "r")
                    stats_text = stats.readlines()
                    stats.close()
                    stats_text[32] = str(jumps) + "\n"
                    stats_update = open("Config/Statistics.txt", "w")
                    stats_update.writelines(stats_text)
                    stats_update.close()


def shoot():
    global shoot_update
    global laser_direction
    global shooting
    global head_death_animation
    global classic_lasers_fired
    global alien_lasers_fired
    if mode == "Classic_Mode":
        if laser.ycor() > 359 and death_animation == 0:
            laser.showturtle()
            if player_shooting_sound == 1:
                winsound.PlaySound("Sound/Laser_Gun_Player.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                classic_lasers_fired = classic_lasers_fired + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[12] = str(classic_lasers_fired) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            x = player.xcor()
            y = player.ycor()
            laser.setx(x)
            laser.sety(y + 120)
    if mode == "Alien_Mode":
        if player_head.direction == "right" and shoot_update == 0 and head_death_animation == 0:
            laser_direction = 1
            player_head_laser.setx(player_gun.xcor() + 50)
            player_head_laser.sety(player_gun.ycor())
            if player_shooting_sound == 1:
                winsound.PlaySound("Sound/Laser_Gun_Player.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                alien_lasers_fired = alien_lasers_fired + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[30] = str(alien_lasers_fired) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        if player_head.direction == "left" and shoot_update == 0 and head_death_animation == 0:
            laser_direction = 2
            player_head_laser.setx(player_gun.xcor() - 50)
            player_head_laser.sety(player_gun.ycor())
            if player_shooting_sound == 1:
                winsound.PlaySound("Sound/Laser_Gun_Player.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                alien_lasers_fired = alien_lasers_fired + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[30] = str(alien_lasers_fired) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()


# The next 6 functions are for switching to different modes of the game. These are usually activated when the screen is clicked on a specific coordinate where there is a button located


def launch_title_mode(x, y):
    global mode
    global updated_controls
    global message_output
    if mode == "Classic_Mode" or mode == "Alien_Mode" or mode == "Stats":
        if (x > -637) and (x < -439) and (y > 316) and (y < 385):
            if button_sound == 1:
                winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
            mode = "Title_Mode"
            go_back_button.color("white")
            wn.onscreenclick(None)
    if mode == "Settings" or mode == "Controls":
        if (x > 26) and (x < 602) and (y > -316) and (y < -254):
            if button_sound == 1:
                winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
            if updated_controls == 1:
                message_output = ctypes.windll.user32.MessageBoxW(0, "A restart is required for these changes to take effect!\nDo you want to restart now?", "Restart Required!", 4+48)
                if message_output == 6:
                    on_quit()
                elif message_output == 7:
                    mode = "Title_Mode"
                    go_back_button.color("white")
                    wn.onscreenclick(None)
                    updated_controls = 0
                    message_output = 0
            else:
                mode = "Title_Mode"
                go_back_button.color("white")
                wn.onscreenclick(None)


def launch_classic_mode(x, y):
    global mode
    if (x > -252) and (x < 251) and (y > 34) and (y < 106):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        mode = "Classic_Mode"
        yellow_lightning_power_up.goto(random.randint(-620, 620), -300)
        blue_lightning_power_up.goto(random.randint(-620, 620), -300)
        green_lightning_power_up.goto(random.randint(-620, 620), -300)
        classic_mode_button.color("white")


def launch_alien_mode(x, y):
    global mode
    if (x > -400) and (x < 400) and (y > -180) and (y < 20):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        mode = "Alien_Mode"
        yellow_lightning_power_up.goto(random.randint(-620, 620), -150)
        blue_lightning_power_up.goto(random.randint(-620, 620), -150)
        red_lightning_power_up.goto(random.randint(-620, 620), -150)
        alien_mode_button.color("white")


def launch_stats_mode(x, y):
    global mode
    if (x > -400) and (x < 400) and (y > -320) and (y < -80):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        mode = "Stats"
        stats_mode_button.color("white")


def launch_settings_mode(x, y):
    global mode
    if mode == "Title_Mode":
        if (x > -400) and (x < 400) and (y > -320) and (y < -120):
            if button_sound == 1:
                winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
            mode = "Settings"
            settings_mode_button.color("white")
    if mode == "Controls":
        if (x > 26) and (x < 604) and (y > -240) and (y < -170):
            if button_sound == 1:
                winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
            mode = "Settings"


def launch_controls_mode(x, y):
    global mode
    if (x > 26) and (x < 604) and (y > -240) and (y < -170):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        mode = "Controls"


# The next 9 functions are for toggling certain sounds on or off in the game
# The functions do this by editing the actual text file where the on/off switch for the sounds is located
# After that, the text file is then checked to correctly change the value of the sound variables and turn the sound on or off


def toggle_button_sound(x, y):
    if (x > -612) and (x < -5) and (y > 164) and (y < 227):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[0] == sound2[0]:
            sound[0] = "Button_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[0] = "Button_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_player_shooting_sound(x, y):
    if (x > -612) and (x < -5) and (y > 84) and (y < 147):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[1] == sound2[1]:
            sound[1] = "Player_Shooting_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[1] = "Player_Shooting_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_enemy_shooting_sound(x, y):
    if (x > -612) and (x < -5) and (y > 4) and (y < 67):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[2] == sound2[2]:
            sound[2] = "Enemy_Shooting_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[2] = "Enemy_Shooting_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_player_death_sound(x, y):
    if (x > -612) and (x < -5) and (y > -80) and (y < -10):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[3] == sound2[3]:
            sound[3] = "Player_Death_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[3] = "Player_Death_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_enemy_death_sound(x, y):
    if (x > -612) and (x < -5) and (y > -160) and (y < -90):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[4] == sound2[4]:
            sound[4] = "Enemy_Death_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[4] = "Enemy_Death_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_player_hit_sound(x, y):
    if (x > -612) and (x < -5) and (y > -240) and (y < -170):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[5] == sound2[5]:
            sound[5] = "Player_Hit_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[5] = "Player_Hit_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_enemy_hit_sound(x, y):
    if (x > -612) and (x < -5) and (y > -320) and (y < -250):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[6] == sound2[6]:
            sound[6] = "Enemy_Hit_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[6] = "Enemy_Hit_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_power_up_pickup_sound(x, y):
    if (x > 26) and (x < 604) and (y > 164) and (y < 227):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[7] == sound2[7]:
            sound[7] = "Power_Up_Pickup_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[7] = "Power_Up_Pickup_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


def toggle_power_up_spawn_sound(x, y):
    if (x > 26) and (x < 604) and (y > 84) and (y < 147):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        soundfile = open("Config/Sound.txt", "r")
        sound = soundfile.readlines()
        soundfile.close()
        soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
        sound2 = soundfile2.readlines()
        soundfile2.close()
        if sound[8] == sound2[8]:
            sound[8] = "Power_Up_Spawn_Sound = 0\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()
        else:
            sound[8] = "Power_Up_Spawn_Sound = 1\n"
            soundupdate = open("Config/Sound.txt", "w")
            soundupdate.writelines(sound)
            soundupdate.close()


# The next 4 functions are for changing the controls of the game
# These functions are long because they need to capture every potentially invalid user input in order to prevent bugs and game crashes
# The function also need to be able to revert back to the old settings if the user does input something invalid
# This means the function needs to be able to save two instances of the same setting for a temporary period of time


def change_go_right_key(x, y):
    global go_right_key
    global go_right_key_2
    global go_right_key_backup
    global go_right_key_alert
    global message_output
    global updated_controls
    if (x > -612) and (x < -5) and (y > 155) and (y < 230):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        go_right_key_backup = go_right_key
        go_right_key_2 = wn.textinput("Go Right", "Insert new key here:")
        if go_right_key_2 == " ":
            go_right_key_2 = "space"
        wn.listen()
        if go_right_key_2 != None and go_right_key_2 != go_right_key_backup:
            if (len(go_right_key_2) > 1 and go_right_key_2 != "space") or go_right_key_2 == "":
                ctypes.windll.user32.MessageBoxW(0, "That is an invalid input!", "Invalid Input!", 16)
                go_right_key_2 = go_right_key_backup
            else:
                save_key = open("Config/Key_Update.txt", "r")
                save_key_read = save_key.readlines()
                save_key.close()
                save_key_read[0] = go_right_key_2 + "\n"
                save_key_update = open("Config/Key_Update.txt", "w")
                save_key_update.writelines(save_key_read)
                save_key_update.close()
                go_right_key = go_right_key_2
                if go_right_key != go_left_key and go_right_key != shoot_key and go_right_key != jump_key:
                    go_right_key_alert = 0
                else:
                    go_right_key_alert = 1
                if go_right_key_alert == 1:
                    message_output = ctypes.windll.user32.MessageBoxW(0, "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", "Conflict!", 4+48)
                    if message_output == 7:
                        go_right_key = go_right_key_backup
                        go_right_key_2 = go_right_key_backup
                        save_key = open("Config/Key_Update.txt", "r")
                        save_key_read = save_key.readlines()
                        save_key.close()
                        save_key_read[0] = go_right_key_2 + "\n"
                        save_key_update = open("Config/Key_Update.txt", "w")
                        save_key_update.writelines(save_key_read)
                        save_key_update.close()
                    else:
                        controls_read = open("Config/Controls.txt", "r")
                        controls_list = controls_read.readlines()
                        controls_read.close()
                        controls_list[0] = "Go_Right = " + '"' + go_right_key + '"\n'
                        controls_update = open("Config/Controls.txt", "w")
                        controls_update.writelines(controls_list)
                        controls_update.close()
                        go_right_key_backup = go_right_key
                        updated_controls = 1
                else:
                    controls_read = open("Config/Controls.txt", "r")
                    controls_list = controls_read.readlines()
                    controls_read.close()
                    controls_list[0] = "Go_Right = " + '"' + go_right_key + '"\n'
                    controls_update = open("Config/Controls.txt", "w")
                    controls_update.writelines(controls_list)
                    controls_update.close()
                    go_right_key_backup = go_right_key
                    updated_controls = 1
        else:
            go_right_key_2 = go_right_key_backup


def change_go_left_key(x, y):
    global go_left_key
    global go_left_key_2
    global go_left_key_backup
    global go_left_key_alert
    global message_output
    global updated_controls
    if (x > -612) and (x < -5) and (y > 70) and (y < 150):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        go_left_key_backup = go_left_key
        go_left_key_2 = wn.textinput("Go Left", "Insert new key here:")
        if go_left_key_2 == " ":
            go_left_key_2 = "space"
        wn.listen()
        if go_left_key_2 != None and go_left_key_2 != go_left_key_backup:
            if (len(go_left_key_2) > 1 and go_left_key_2 != "space") or go_left_key_2 == "":
                ctypes.windll.user32.MessageBoxW(0, "That is an invalid input!", "Invalid Input!", 16)
                go_left_key_2 = go_left_key_backup
            else:
                save_key = open("Config/Key_Update.txt", "r")
                save_key_read = save_key.readlines()
                save_key.close()
                save_key_read[1] = go_left_key_2 + "\n"
                save_key_update = open("Config/Key_Update.txt", "w")
                save_key_update.writelines(save_key_read)
                save_key_update.close()
                go_left_key = go_left_key_2
                if go_left_key != go_right_key and go_left_key != shoot_key and go_left_key != jump_key:
                    go_left_key_alert = 0
                else:
                    go_left_key_alert = 1
                if go_left_key_alert == 1:
                    message_output = ctypes.windll.user32.MessageBoxW(0, "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", "Conflict!", 4+48)
                    if message_output == 7:
                        go_left_key = go_left_key_backup
                        go_left_key_2 = go_left_key_backup
                        save_key = open("Config/Key_Update.txt", "r")
                        save_key_read = save_key.readlines()
                        save_key.close()
                        save_key_read[1] = go_left_key_2 + "\n"
                        save_key_update = open("Config/Key_Update.txt", "w")
                        save_key_update.writelines(save_key_read)
                        save_key_update.close()
                    else:
                        controls_read = open("Config/Controls.txt", "r")
                        controls_list = controls_read.readlines()
                        controls_read.close()
                        controls_list[1] = "Go_Left = " + '"' + go_left_key + '"\n'
                        controls_update = open("Config/Controls.txt", "w")
                        controls_update.writelines(controls_list)
                        controls_update.close()
                        go_left_key_backup = go_left_key
                        updated_controls = 1
                else:
                    controls_read = open("Config/Controls.txt", "r")
                    controls_list = controls_read.readlines()
                    controls_read.close()
                    controls_list[1] = "Go_Left = " + '"' + go_left_key + '"\n'
                    controls_update = open("Config/Controls.txt", "w")
                    controls_update.writelines(controls_list)
                    controls_update.close()
                    go_left_key_backup = go_left_key
                    updated_controls = 1
        else:
            go_left_key_2 = go_left_key_backup


def change_shoot_key(x, y):
    global shoot_key
    global shoot_key_2
    global shoot_key_backup
    global shoot_key_alert
    global message_output
    global updated_controls
    if (x > -612) and (x < -5) and (y > -5) and (y < 70):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        shoot_key_backup = shoot_key
        shoot_key_2 = wn.textinput("Shoot", "Insert new key here:")
        if shoot_key_2 == " ":
            shoot_key_2 = "space"
        wn.listen()
        if shoot_key_2 != None and shoot_key_2 != shoot_key_backup:
            if (len(shoot_key_2) > 1 and shoot_key_2 != "space") or shoot_key_2 == "":
                ctypes.windll.user32.MessageBoxW(0, "That is an invalid input!", "Invalid Input!", 16)
                shoot_key_2 = shoot_key_backup
            else:
                save_key = open("Config/Key_Update.txt", "r")
                save_key_read = save_key.readlines()
                save_key.close()
                save_key_read[2] = shoot_key_2 + "\n"
                save_key_update = open("Config/Key_Update.txt", "w")
                save_key_update.writelines(save_key_read)
                save_key_update.close()
                shoot_key = shoot_key_2
                if shoot_key != go_left_key and shoot_key != go_right_key and shoot_key != jump_key:
                    shoot_key_alert = 0
                else:
                    shoot_key_alert = 1
                if shoot_key_alert == 1:
                    message_output = ctypes.windll.user32.MessageBoxW(0, "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", "Conflict!", 4 + 48)
                    if message_output == 7:
                        shoot_key = shoot_key_backup
                        shoot_key_2 = shoot_key_backup
                        save_key = open("Config/Key_Update.txt", "r")
                        save_key_read = save_key.readlines()
                        save_key.close()
                        save_key_read[2] = shoot_key_2 + "\n"
                        save_key_update = open("Config/Key_Update.txt", "w")
                        save_key_update.writelines(save_key_read)
                        save_key_update.close()
                    else:
                        controls_read = open("Config/Controls.txt", "r")
                        controls_list = controls_read.readlines()
                        controls_read.close()
                        controls_list[2] = "Shoot = " + '"' + shoot_key + '"\n'
                        controls_update = open("Config/Controls.txt", "w")
                        controls_update.writelines(controls_list)
                        controls_update.close()
                        shoot_key_backup = shoot_key
                        updated_controls = 1
                else:
                    controls_read = open("Config/Controls.txt", "r")
                    controls_list = controls_read.readlines()
                    controls_read.close()
                    controls_list[2] = "Shoot = " + '"' + shoot_key + '"\n'
                    controls_update = open("Config/Controls.txt", "w")
                    controls_update.writelines(controls_list)
                    controls_update.close()
                    shoot_key_backup = shoot_key
                    updated_controls = 1
        else:
            shoot_key_2 = shoot_key_backup


def change_jump_key(x, y):
    global jump_key
    global jump_key_2
    global jump_key_backup
    global jump_key_alert
    global message_output
    global updated_controls
    if (x > -612) and (x < -5) and (y > -80) and (y < -10):
        if button_sound == 1:
            winsound.PlaySound("Sound/Button_Sound.wav", winsound.SND_ASYNC)
        jump_key_backup = jump_key
        jump_key_2 = wn.textinput("Jump", "Insert new key here:")
        if jump_key_2 == " ":
            jump_key_2 = "space"
        wn.listen()
        if jump_key_2 != None and jump_key_2 != jump_key_backup:
            if (len(jump_key_2) > 1 and jump_key_2 != "space") or jump_key_2 == "":
                ctypes.windll.user32.MessageBoxW(0, "That is an invalid input!", "Invalid Input!", 16)
                jump_key_2 = jump_key_backup
            else:
                save_key = open("Config/Key_Update.txt", "r")
                save_key_read = save_key.readlines()
                save_key.close()
                save_key_read[3] = jump_key_2 + "\n"
                save_key_update = open("Config/Key_Update.txt", "w")
                save_key_update.writelines(save_key_read)
                save_key_update.close()
                jump_key = jump_key_2
                if jump_key != go_left_key and jump_key != shoot_key and jump_key != go_right_key:
                    jump_key_alert = 0
                else:
                    jump_key_alert = 1
                if jump_key_alert == 1:
                    message_output = ctypes.windll.user32.MessageBoxW(0, "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", "Conflict!", 4 + 48)
                    if message_output == 7:
                        jump_key = jump_key_backup
                        jump_key_2 = jump_key_backup
                        save_key = open("Config/Key_Update.txt", "r")
                        save_key_read = save_key.readlines()
                        save_key.close()
                        save_key_read[3] = jump_key_2 + "\n"
                        save_key_update = open("Config/Key_Update.txt", "w")
                        save_key_update.writelines(save_key_read)
                        save_key_update.close()
                    else:
                        controls_read = open("Config/Controls.txt", "r")
                        controls_list = controls_read.readlines()
                        controls_read.close()
                        controls_list[3] = "Jump = " + '"' + jump_key + '"\n'
                        controls_update = open("Config/Controls.txt", "w")
                        controls_update.writelines(controls_list)
                        controls_update.close()
                        jump_key_backup = jump_key
                        updated_controls = 1
                else:
                    controls_read = open("Config/Controls.txt", "r")
                    controls_list = controls_read.readlines()
                    controls_read.close()
                    controls_list[3] = "Jump = " + '"' + jump_key + '"\n'
                    controls_update = open("Config/Controls.txt", "w")
                    controls_update.writelines(controls_list)
                    controls_update.close()
                    jump_key_backup = jump_key
                    updated_controls = 1
        else:
            jump_key_2 = jump_key_backup


# The function below is used to help detect when the users mouse is hovering over a button
# If the users mouse is hovering over a button, it will turn the buttons text yellow
# If the button text is yellow, the user is allowed to click the button and activate its function
# The function uses red and orange for the control buttons when there are interfering controls instead of white and yellow


def position(event):
    global button_update
    a, b = event.x, event.y
    if mode == "Title_Mode":
        if 390 < a < 893 and 256 < b < 328:
            classic_mode_button.color("yellow")
        else:
            classic_mode_button.color("white")
        if 390 < a < 893 and 356 < b < 428:
            alien_mode_button.color("yellow")
        else:
            alien_mode_button.color("white")
        if 390 < a < 893 and 456 < b < 528:
            stats_mode_button.color("yellow")
        else:
            stats_mode_button.color("white")
        if 390 < a < 893 and 556 < b < 628:
            settings_mode_button.color("yellow")
        else:
            settings_mode_button.color("white")
    if mode == "Classic_Mode" or mode == "Alien_Mode" or mode == "Stats":
        if 9 < a < 201 and 6 < b < 38:
            go_back_button.color("yellow")
            button_update = 1
        else:
            go_back_button.color("white")
            button_update = 0
    if mode == "Settings":
        if 671 < a < 1243 and 616 < b < 677:
            go_back_button.color("yellow")
            button_update = 1
        else:
            go_back_button.color("white")
            button_update = 0
        if 671 < a < 1243 and 536 < b < 597:
            control_toggle_button.color("yellow")
        else:
            control_toggle_button.color("white")
        if 30 < a < 601 and 135 < b < 198:
            button_sound_button.color("yellow")
        else:
            button_sound_button.color("white")
        if 30 < a < 601 and 215 < b < 278:
            player_shooting_sound_button.color("yellow")
        else:
            player_shooting_sound_button.color("white")
        if 30 < a < 601 and 295 < b < 358:
            enemy_shooting_sound_button.color("yellow")
        else:
            enemy_shooting_sound_button.color("white")
        if 30 < a < 601 and 375 < b < 438:
            player_death_sound_button.color("yellow")
        else:
            player_death_sound_button.color("white")
        if 30 < a < 601 and 455 < b < 518:
            enemy_death_sound_button.color("yellow")
        else:
            enemy_death_sound_button.color("white")
        if 30 < a < 601 and 535 < b < 598:
            player_hit_sound_button.color("yellow")
        else:
            player_hit_sound_button.color("white")
        if 30 < a < 601 and 615 < b < 678:
            enemy_hit_sound_button.color("yellow")
        else:
            enemy_hit_sound_button.color("white")
        if 671 < a < 1243 and 135 < b < 198:
            power_up_pickup_sound_button.color("yellow")
        else:
            power_up_pickup_sound_button.color("white")
        if 671 < a < 1243 and 215 < b < 278:
            power_up_spawn_sound_button.color("yellow")
        else:
            power_up_spawn_sound_button.color("white")
    if mode == "Controls":
        if 671 < a < 1243 and 616 < b < 677:
            go_back_button.color("yellow")
            button_update = 1
        else:
            go_back_button.color("white")
            button_update = 0
        if 671 < a < 1243 and 536 < b < 597:
            control_toggle_button.color("yellow")
        else:
            control_toggle_button.color("white")
        if go_right_key_alert == 1:
            if 30 < a < 601 and 135 < b < 198:
                go_right_control_button.color("orange")
            else:
                go_right_control_button.color("red")
        else:
            if 30 < a < 601 and 135 < b < 198:
                go_right_control_button.color("yellow")
            else:
                go_right_control_button.color("white")
        if go_left_key_alert == 1:
            if 30 < a < 601 and 215 < b < 278:
                go_left_control_button.color("orange")
            else:
                go_left_control_button.color("red")
        else:
            if 30 < a < 601 and 215 < b < 278:
                go_left_control_button.color("yellow")
            else:
                go_left_control_button.color("white")
        if shoot_key_alert == 1:
            if 30 < a < 601 and 295 < b < 358:
                shoot_control_button.color("orange")
            else:
                shoot_control_button.color("red")
        else:
            if 30 < a < 601 and 295 < b < 358:
                shoot_control_button.color("yellow")
            else:
                shoot_control_button.color("white")
        if jump_key_alert == 1:
            if 30 < a < 601 and 375 < b < 438:
                jump_control_button.color("orange")
            else:
                jump_control_button.color("red")
        else:
            if 30 < a < 601 and 375 < b < 438:
                jump_control_button.color("yellow")
            else:
                jump_control_button.color("white")


# The function below is activated when the user wants to exit the program by clicking the x in the top right corner


def on_quit():
    global quit_loop
    quit_loop = 1
    wn._root.after(100, wn._root.destroy)


# The five lines of code below are used to detect when the user presses a specific key on the keyboard for controlling the game

wn.listen()
wn.onkeypress(go_left, go_left_key)
wn.onkeypress(go_right, go_right_key)
wn.onkeypress(shoot, shoot_key)
wn.onkeypress(jump, jump_key)

wn._root.protocol("WM_DELETE_WINDOW", on_quit)

# The two lines of code below are used to collect the position of the users mouse on the canvas

mouse_position = wn.getcanvas()
mouse_position.bind('<Motion>', position)

# The code inside this loop is everything that needs to be checked after a certain amount of time:
# For settings mode, stats mode, and title mode, it is 1/5 of a delay tick
# For classic mode and alien mode, it is 1/25 of a delay tick

while True:

    # The line of code below is used to update the screen after every delay tick

    wn.update()

    # The two lines of code below are used to break the loop when the user terminates the program to avoid errors

    if quit_loop == 1:
        break

    # The two lines of code below are for setting the tick speed for specific items and setting the variable that determines how often power ups spawn in the game

    power_up_update = random.randint(-1800, 1800)
    tick_update = tick_update + 1

    # Lines 2676 - 2732 are for what happens when title mode is toggled on and off
    # Most of the code below is used to make the title screen buttons visible

    if mode == "Title_Mode":
        score = 0
        go_back_button.clear()
        go_back_button_frame.hideturtle()
        control_toggle_button.clear()
        control_toggle_button_frame.hideturtle()
        yellow_lightning_power_up.hideturtle()
        blue_lightning_power_up.hideturtle()
        green_lightning_power_up.hideturtle()
        red_lightning_power_up.hideturtle()
        yellow_power_up_indicator.hideturtle()
        blue_power_up_indicator.hideturtle()
        extra_power_up_indicator.hideturtle()
        yellow_power_up_active = 0
        yellow_power_up_timer = 0
        blue_power_up_active = 0
        blue_power_up_timer = 0
        green_power_up_active = 0
        green_power_up_timer = 0
        red_power_up_active = 0
        red_power_up_timer = 0
        classic_mode_button_frame.showturtle()
        classic_mode_button.clear()
        classic_mode_button.write("Machine Mode", align="center", font=("Courier", 30, "normal"))
        alien_mode_button_frame.showturtle()
        alien_mode_button.clear()
        alien_mode_button.write("Alien Mode", align="center", font=("Courier", 30, "normal"))
        stats_mode_button_frame.showturtle()
        stats_mode_button.clear()
        stats_mode_button.write("Statistics", align="center", font=("Courier", 30, "normal"))
        settings_mode_button_frame.showturtle()
        settings_mode_button.clear()
        settings_mode_button.write("Settings", align="center", font=("Courier", 30, "normal"))
        title_label.clear()
        title_label.write("Laser Fighter", align="center", font=("Courier", 72, "bold"))
        version_number.clear()
        version_number.write("Alpha 0.4.0a", align="center", font=("Courier", 24, "normal"))
        if title_label.xcor() < -120:
            title_moving = 1
        if title_label.xcor() > 120:
            title_moving = -1
        if title_moving == 1:
            title_label.setx(title_label.xcor() + 5)
        if title_moving == -1:
            title_label.setx(title_label.xcor() - 5)
    else:
        classic_mode_button_frame.hideturtle()
        classic_mode_button.clear()
        alien_mode_button_frame.hideturtle()
        alien_mode_button.clear()
        stats_mode_button_frame.hideturtle()
        stats_mode_button.clear()
        settings_mode_button_frame.hideturtle()
        settings_mode_button.clear()
        title_label.clear()
        title_label.setx(0)
        version_number.clear()

    # Lines 2737 - 2922 are for what happens when classic mode is toggled on and off
    # Most of the lines fo code below are used to reset the game to its default state when classic mode is exited

    if mode == "Classic_Mode":
        player.showturtle()
        enemy1.showturtle()
        enemy2.showturtle()
        enemy3.showturtle()
        enemy1_laser.showturtle()
        enemy2_laser.showturtle()
        enemy3_laser.showturtle()
        yellow_power_up_indicator.showturtle()
        blue_power_up_indicator.showturtle()
        extra_power_up_indicator.showturtle()
        go_back_button.goto(-537, 320)
        if tick_update % 20 == 0:
            go_back_button.clear()
            go_back_button.write("Main Menu", align="center", font=("Courier", 24, "normal"))
        go_back_button_frame.shapesize(1.5, 9.5)
        go_back_button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
        go_back_button_frame.showturtle()
        go_back_button_frame.goto(-537, 339)

        if yellow_power_up_active == 1:
            yellow_power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif")
            yellow_power_up_text.color("yellow")
        else:
            yellow_power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
            yellow_power_up_text.color("#737000")

        if blue_power_up_active == 1:
            blue_power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif")
            blue_power_up_text.color("#02CCFE")
        else:
            blue_power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
            blue_power_up_text.color("#00004A")

        if green_power_up_active == 1:
            extra_power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_On.gif")
            extra_power_up_text.color("#65FE08")
        else:
            extra_power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
            extra_power_up_text.color("#001C00")

        if power_up_update == 1 and yellow_power_up_active == 0:
            if yellow_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            yellow_lightning_power_up.showturtle()

        if power_up_update == 50 and blue_power_up_active == 0:
            if blue_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            blue_lightning_power_up.showturtle()

        if power_up_update == 100 and green_power_up_active == 0:
            if green_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            green_lightning_power_up.showturtle()

        if yellow_lightning_power_up.distance(player) < 27 and death_animation == 0 and yellow_lightning_power_up.isvisible() and yellow_power_up_active == 0:
            yellow_lightning_power_up.hideturtle()
            yellow_lightning_power_up.goto(random.randint(-620, 620), -300)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[14] = str(classic_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            yellow_power_up_active = 1

        if blue_lightning_power_up.distance(player) < 27 and death_animation == 0 and blue_lightning_power_up.isvisible() and blue_power_up_active == 0:
            blue_lightning_power_up.hideturtle()
            blue_lightning_power_up.goto(random.randint(-620, 620), -300)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[14] = str(classic_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            blue_power_up_active = 1

        if green_lightning_power_up.distance(player) < 27 and death_animation == 0 and green_lightning_power_up.isvisible() and green_power_up_active == 0:
            green_lightning_power_up.hideturtle()
            green_lightning_power_up.goto(random.randint(-620, 620), -300)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[14] = str(classic_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            green_power_up_active = 1

        if yellow_power_up_active == 1:
            yellow_power_up_timer = yellow_power_up_timer + 1
            if yellow_power_up_timer >= 1200:
                yellow_power_up_active = 0
                yellow_power_up_timer = 0

        if blue_power_up_active == 1:
            blue_power_up_timer = blue_power_up_timer + 1
            if blue_power_up_timer >= 2700:
                blue_power_up_active = 0
                blue_power_up_timer = 0

        if green_power_up_active == 1:
            green_power_up_timer = green_power_up_timer + 1
            if green_power_up_timer >= 900:
                green_power_up_active = 0
                green_power_up_timer = 0

    else:
        player.hideturtle()
        player.goto(0, -300)
        player.direction = "stop"
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy1_laser.hideturtle()
        enemy2_laser.hideturtle()
        enemy3_laser.hideturtle()
        enemy1.goto(-200, 220)
        enemy2.goto(200, 220)
        enemy3.goto(500, 220)
        enemy4.goto(-500, 220)
        enemy5.goto(-400, 220)
        enemy6.goto(-300, 220)
        enemy7.goto(-250, 220)
        enemy8.goto(250, 220)
        enemy9.goto(-350, 220)
        enemy10.goto(350, 220)
        enemy11.goto(375, 220)
        enemy11_health_bar.goto(375, 290)
        enemy12.goto(-375, 220)
        enemy12_health_bar.goto(-375, 290)
        enemy13.goto(325, 220)
        enemy13_health_bar.goto(325, 290)
        enemy14.goto(-325, 220)
        enemy14_health_bar.goto(-325, 290)
        enemy15.goto(275, 220)
        enemy15_health_bar.goto(275, 290)
        boss.goto(175, 220)
        boss_health_bar.goto(175, 290)
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
        moving1 = 1
        moving2 = 1
        moving3 = 1
        moving4 = 1
        moving5 = 1
        moving6 = 1
        moving7 = 1
        moving8 = 1
        moving9 = 1
        moving10 = 1
        moving11 = 1
        moving12 = 1
        moving13 = 1
        moving14 = 1
        moving15 = 1
        moving_boss = 1

    # Lines 2926 - 6323 is for what happens when alien mode is toggled on and off

    if mode == "Alien_Mode":
        go_back_button.goto(-537, 320)
        if tick_update % 20 == 0:
            go_back_button.clear()
            go_back_button.write("Main Menu", align="center", font=("Courier", 24, "normal"))
        go_back_button_frame.shapesize(1.5, 9.5)
        go_back_button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
        go_back_button_frame.showturtle()
        go_back_button_frame.goto(-537, 339)
        ground.showturtle()
        earth.showturtle()
        space_ship.showturtle()
        player_head.showturtle()
        if head_death_animation == 0:
            oxygen_tank.showturtle()
        alien1.showturtle()
        alien2.showturtle()
        alien3.showturtle()
        yellow_power_up_indicator.showturtle()
        blue_power_up_indicator.showturtle()
        extra_power_up_indicator.showturtle()

        # Lines 2950 - 3050 are used for the power ups in alien mode
        # This includes their timer, what happens when they are active, what happens when the pplayer picks them up, and what happens when they spawn

        if yellow_power_up_active == 1:
            yellow_power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif")
            yellow_power_up_text.color("yellow")
        else:
            yellow_power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
            yellow_power_up_text.color("#737000")

        if blue_power_up_active == 1:
            blue_power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif")
            blue_power_up_text.color("#02CCFE")
        else:
            blue_power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
            blue_power_up_text.color("#00004A")

        if red_power_up_active == 1:
            extra_power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_On.gif")
            extra_power_up_text.color("#FF0000")
        else:
            extra_power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif")
            extra_power_up_text.color("#300000")

        if power_up_update == 1 and yellow_power_up_active == 0:
            if yellow_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            yellow_lightning_power_up.showturtle()

        if power_up_update == 50 and blue_power_up_active == 0:
            if blue_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            blue_lightning_power_up.showturtle()

        if power_up_update == 100 and red_power_up_active == 0:
            if red_lightning_power_up.isvisible() == False and power_up_spawn_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Spawn_Sound.wav", winsound.SND_ASYNC)
            red_lightning_power_up.showturtle()

        if yellow_lightning_power_up.distance(player_head) < 27 and head_death_animation == 0 and yellow_lightning_power_up.isvisible() and yellow_power_up_active == 0:
            yellow_lightning_power_up.hideturtle()
            yellow_lightning_power_up.goto(random.randint(-620, 620), -150)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[34] = str(alien_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            yellow_power_up_active = 1

        if blue_lightning_power_up.distance(player_head) < 27 and head_death_animation == 0 and blue_lightning_power_up.isvisible() and blue_power_up_active == 0:
            blue_lightning_power_up.hideturtle()
            blue_lightning_power_up.goto(random.randint(-620, 620), -150)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[34] = str(alien_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            blue_power_up_active = 1

        if red_lightning_power_up.distance(player_head) < 27 and head_death_animation == 0 and red_lightning_power_up.isvisible() and red_power_up_active == 0:
            red_lightning_power_up.hideturtle()
            red_lightning_power_up.goto(random.randint(-620, 620), -150)
            if power_up_pickup_sound == 1:
                winsound.PlaySound("Sound/Power_Up_Pickup_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[34] = str(alien_power_ups_picked_up) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            red_power_up_active = 1

        if yellow_power_up_active == 1:
            yellow_power_up_timer = yellow_power_up_timer + 1
            if yellow_power_up_timer >= 1200:
                yellow_power_up_active = 0
                yellow_power_up_timer = 0

        if blue_power_up_active == 1:
            blue_power_up_timer = blue_power_up_timer + 1
            if blue_power_up_timer >= 2700:
                blue_power_up_active = 0
                blue_power_up_timer = 0

        if red_power_up_active == 1:
            red_power_up_timer = red_power_up_timer + 1
            if red_power_up_timer >= 900:
                red_power_up_active = 0
                red_power_up_timer = 0

        # Lines 3053 - 3142 make more aliens visible as the score increases.
        # The final boss appears when the score reaches 250

        if score > 20:
            alien4.showturtle()
        else:
            alien4.hideturtle()
        if score > 40:
            alien5.showturtle()
        else:
            alien5.hideturtle()
        if score > 60:
            alien6.showturtle()
            if alien6_health != 0:
                alien6_health_bar.showturtle()
        else:
            alien6.hideturtle()
            alien6_health_bar.hideturtle()
        if score > 80:
            alien7.showturtle()
            if alien7_health != 0:
                alien7_health_bar.showturtle()
        else:
            alien7.hideturtle()
            alien7_health_bar.hideturtle()
        if score > 100:
            alien8.showturtle()
            if alien8_health != 0:
                alien8_health_bar.showturtle()
        else:
            alien8.hideturtle()
            alien8_health_bar.hideturtle()
        if score > 120:
            alien9.showturtle()
            if alien9_health != 0:
                alien9_health_bar.showturtle()
        else:
            alien9.hideturtle()
            alien9_health_bar.hideturtle()
        if score > 140:
            alien10.showturtle()
            if alien10_health != 0:
                alien10_health_bar.showturtle()
        else:
            alien10.hideturtle()
            alien10_health_bar.hideturtle()
        if score > 160:
            alien11.showturtle()
            if alien11_health != 0:
                alien11_health_bar.showturtle()
        else:
            alien11.hideturtle()
            alien11_health_bar.hideturtle()
        if score > 180:
            alien12.showturtle()
            if alien12_health != 0:
                alien12_health_bar.showturtle()
        else:
            alien12.hideturtle()
            alien12_health_bar.hideturtle()
        if score > 200:
            alien13.showturtle()
            if alien13_health != 0:
                alien13_health_bar.showturtle()
        else:
            alien13.hideturtle()
            alien13_health_bar.hideturtle()
        if score > 220:
            alien14.showturtle()
            if alien14_health != 0:
                alien14_health_bar.showturtle()
        else:
            alien14.hideturtle()
            alien14_health_bar.hideturtle()
        if score > 240:
            alien15.showturtle()
            if alien15_health != 0:
                alien15_health_bar.showturtle()
        else:
            alien15.hideturtle()
            alien15_health_bar.hideturtle()
        if score > 250:
            alien_boss.showturtle()
            alien_boss_laser.showturtle()
            if alien_boss_health != 0:
                alien_boss_health_bar.showturtle()
        else:
            alien_boss.hideturtle()
            alien_boss_laser.hideturtle()
            alien_boss_health_bar.hideturtle()

        # These 3 lines below check if god mode is on or off for alien mode
        # If it is on, the health bar does not even appear. If it is off, it appears with 10 health

        if god_mode == 0:
            player_head_health_bar.goto(531, 339)
            player_head_health_bar.showturtle()

        # Lines 3154 - 3227 are for the players movement in alien mode
        # The code below basically determines how the player moves right and left and the players jump animation

        if move_right == 1 and player_head.direction == "right" and head_death_animation == 0:
            move_update = 1
            if player_head.xcor() < (Start_X + 100):
                player_head.setx(player_head.xcor() + 4)
                oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
                player_gun.goto(player_head.xcor() + 20, player_head.ycor() + 12)
                moving_right = 1
            else:
                moving_right = 0
            move_update = 0

        right_update = time.perf_counter()
        right_update = round(right_update, 1)

        if move_left == 1 and player_head.direction == "left" and head_death_animation == 0:
            move_update = 1
            if player_head.xcor() > (Start_X - 100):
                player_head.setx(player_head.xcor() - 4)
                oxygen_tank.goto(player_head.xcor() + 30.5, player_head.ycor() + 11)
                player_gun.goto(player_head.xcor() - 20, player_head.ycor() + 12)
                moving_left = 1
            else:
                moving_left = 0
            move_update = 0

        left_update = time.perf_counter()
        left_update = round(left_update, 1)

        if do_jump == 1 and head_death_animation == 0:
            jump_update = 1
            if (player_head.direction == "right" and direction == 0) or (direction == 1):
                direction = 1
                player_gun.direction = "right"
                oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
                player_gun.goto(player_head.xcor() + 20, player_head.ycor() + 12)
                player_gun.showturtle()
                if (player_head.ycor() < (Start_Y + 175)) and (player_head.xcor() < (Start_X + 400)) and vertex == 0:
                    player_head.sety(player_head.ycor() + 8)
                    player_head.setx(player_head.xcor() + 5)
                    oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
                    player_gun.goto(player_head.xcor() + 20, player_head.ycor() + 12)
                elif (player_head.ycor() > Start_Y) and (player_head.xcor() < (Start_X + 800)):
                    vertex = 1
                    player_head.sety(player_head.ycor() - 8)
                    player_head.setx(player_head.xcor() + 5)
                    oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
                    player_gun.goto(player_head.xcor() + 20, player_head.ycor() + 12)
                else:
                    jump_update = 0
                    vertex = 0
                    direction = 0
                    do_jump = 0
            elif (player_head.direction == "left" and direction == 0) or (direction == 2):
                direction = 2
                player_gun.direction = "left"
                oxygen_tank.goto(player_head.xcor() + 30.5, player_head.ycor() + 11)
                player_gun.goto(player_head.xcor() - 20, player_head.ycor() + 12)
                player_gun.showturtle()
                if (player_head.ycor() < (Start_Y + 175)) and (player_head.xcor() > (Start_X - 400)) and vertex == 0:
                    player_head.sety(player_head.ycor() + 8)
                    player_head.setx(player_head.xcor() - 5)
                    oxygen_tank.goto(player_head.xcor() + 30.5, player_head.ycor() + 11)
                    player_gun.goto(player_head.xcor() - 20, player_head.ycor() + 12)
                elif (player_head.ycor() > Start_Y) and (player_head.xcor() > (Start_X - 800)):
                    vertex = 1
                    player_head.sety(player_head.ycor() - 8)
                    player_head.setx(player_head.xcor() - 5)
                    oxygen_tank.goto(player_head.xcor() + 30.5, player_head.ycor() + 11)
                    player_gun.goto(player_head.xcor() - 20, player_head.ycor() + 12)
                else:
                    jump_update = 0
                    vertex = 0
                    direction = 0
                    do_jump = 0

        # Lines 3232 - 3253 are for the player laser movement
        # The lasers movement depends on the direction it is fired and it will only move when it is fired by the player

        if -1080 < player_head_laser.xcor() < 1080 and laser_direction == 1:
            shoot_update = 1
            if laser_update == 0 or laser_update == 1:
                player_head_laser.showturtle()
            player_head_laser.direction = "right"
            if yellow_power_up_active == 1:
                player_head_laser.forward(60)
            else:
                player_head_laser.forward(20)
        elif -1080 < player_head_laser.xcor() < 1080 and laser_direction == 2:
            shoot_update = 1
            if laser_update == 0 or laser_update == 1:
                player_head_laser.showturtle()
            player_head_laser.direction = "left"
            if yellow_power_up_active == 1:
                player_head_laser.backward(60)
            else:
                player_head_laser.backward(20)
        else:
            shoot_update = 0
            laser_update = 0
            player_head_laser.hideturtle()

        # Lines 3258 - 3365 are for the direction of both players and aliens
        # Aliens will always be facing the direction of the player and moving towards the player at a certain speed

        if player_head.direction == "right" and head_death_animation == 0:
            if (moving_right == 1 and right_update % 0.5 != 0) or jump_update == 1:
                player_head.shape("Textures/Player/Player_Head_Walking_Right.gif")
            else:
                player_head.shape("Textures/Player/Player_Head_Still_Right.gif")
        elif player_head.direction == "left" and head_death_animation == 0:
            if (moving_left == 1 and left_update % 0.5 != 0) or jump_update == 1:
                player_head.shape("Textures/Player/Player_Head_Walking_Left.gif")
            else:
                player_head.shape("Textures/Player/Player_Head_Still_Left.gif")

        if player_gun.direction == "right":
            player_gun.shape("Textures/Gun/Player_Gun_Right.gif")
        elif player_gun.direction == "left":
            player_gun.shape("Textures/Gun/Player_Gun_Left.gif")

        if alien1.xcor() > player_head.xcor():
            alien1.direction = "left"
        else:
            alien1.direction = "right"

        if alien2.xcor() > player_head.xcor():
            alien2.direction = "left"
        else:
            alien2.direction = "right"

        if alien3.xcor() > player_head.xcor():
            alien3.direction = "left"
        else:
            alien3.direction = "right"

        if alien4.isvisible():
            if alien4.xcor() > player_head.xcor():
                alien4.direction = "left"
            else:
                alien4.direction = "right"

        if alien5.isvisible():
            if alien5.xcor() > player_head.xcor():
                alien5.direction = "left"
            else:
                alien5.direction = "right"

        if alien6.isvisible():
            if alien6.xcor() > player_head.xcor():
                alien6.direction = "left"
            else:
                alien6.direction = "right"

        if alien7.isvisible():
            if alien7.xcor() > player_head.xcor():
                alien7.direction = "left"
            else:
                alien7.direction = "right"

        if alien8.isvisible():
            if alien8.xcor() > player_head.xcor():
                alien8.direction = "left"
            else:
                alien8.direction = "right"

        if alien9.isvisible():
            if alien9.xcor() > player_head.xcor():
                alien9.direction = "left"
            else:
                alien9.direction = "right"

        if alien10.isvisible():
            if alien10.xcor() > player_head.xcor():
                alien10.direction = "left"
            else:
                alien10.direction = "right"

        if alien11.isvisible():
            if alien11.xcor() > player_head.xcor():
                alien11.direction = "left"
            else:
                alien11.direction = "right"

        if alien12.isvisible():
            if alien12.xcor() > player_head.xcor():
                alien12.direction = "left"
            else:
                alien12.direction = "right"

        if alien13.isvisible():
            if alien13.xcor() > player_head.xcor():
                alien13.direction = "left"
            else:
                alien13.direction = "right"

        if alien14.isvisible():
            if alien14.xcor() > player_head.xcor():
                alien14.direction = "left"
            else:
                alien14.direction = "right"

        if alien15.isvisible():
            if alien15.xcor() > player_head.xcor():
                alien15.direction = "left"
            else:
                alien15.direction = "right"

        if alien_boss.isvisible():
            if alien_boss.xcor() > player_head.xcor():
                alien_boss.direction = "left"
            else:
                alien_boss.direction = "right"

        # Lines 3371 - 3949 are for the alien speeds
        # If a specific alien is killed enough times, its movement speed towards the player will increase
        # The speed of all aliens is the exact same with the exception of the final boss

        if alien1_death == 0:
            if alien1.direction == "right":
                if 0 <= ak1 < 6:
                    alien1.setx(alien1.xcor() + 0.3)
                if 6 <= ak1 < 12:
                    alien1.setx(alien1.xcor() + 0.6)
                if 12 <= ak1 < 18:
                    alien1.setx(alien1.xcor() + 0.9)
                if 18 <= ak1 < 24:
                    alien1.setx(alien1.xcor() + 1.2)
                if 24 <= ak1 < 30:
                    alien1.setx(alien1.xcor() + 1.5)
                if 30 <= ak1:
                    alien1.setx(alien1.xcor() + 1.8)
            else:
                if 0 <= ak1 < 6:
                    alien1.setx(alien1.xcor() - 0.3)
                if 6 <= ak1 < 12:
                    alien1.setx(alien1.xcor() - 0.6)
                if 12 <= ak1 < 18:
                    alien1.setx(alien1.xcor() - 0.9)
                if 18 <= ak1 < 24:
                    alien1.setx(alien1.xcor() - 1.2)
                if 24 <= ak1 < 30:
                    alien1.setx(alien1.xcor() - 1.5)
                if 30 <= ak1:
                    alien1.setx(alien1.xcor() - 1.8)

        if alien2_death == 0:
            if alien2.direction == "right":
                if 0 <= ak2 < 6:
                    alien2.setx(alien2.xcor() + 0.3)
                if 6 <= ak2 < 12:
                    alien2.setx(alien2.xcor() + 0.6)
                if 12 <= ak2 < 18:
                    alien2.setx(alien2.xcor() + 0.9)
                if 18 <= ak2 < 24:
                    alien2.setx(alien2.xcor() + 1.2)
                if 24 <= ak2 < 30:
                    alien2.setx(alien2.xcor() + 1.5)
                if 30 <= ak2:
                    alien2.setx(alien2.xcor() + 1.8)
            else:
                if 0 <= ak2 < 6:
                    alien2.setx(alien2.xcor() - 0.3)
                if 6 <= ak2 < 12:
                    alien2.setx(alien2.xcor() - 0.6)
                if 12 <= ak2 < 18:
                    alien2.setx(alien2.xcor() - 0.9)
                if 18 <= ak2 < 24:
                    alien2.setx(alien2.xcor() - 1.2)
                if 24 <= ak2 < 30:
                    alien2.setx(alien2.xcor() - 1.5)
                if 30 <= ak2:
                    alien2.setx(alien2.xcor() - 1.8)

        if alien3_death == 0:
            if alien3.direction == "right":
                if 0 <= ak3 < 6:
                    alien3.setx(alien3.xcor() + 0.3)
                if 6 <= ak3 < 12:
                    alien3.setx(alien3.xcor() + 0.6)
                if 12 <= ak3 < 18:
                    alien3.setx(alien3.xcor() + 0.9)
                if 18 <= ak3 < 24:
                    alien3.setx(alien3.xcor() + 1.2)
                if 24 <= ak3 < 30:
                    alien3.setx(alien3.xcor() + 1.5)
                if 30 <= ak3:
                    alien3.setx(alien3.xcor() + 1.8)
            else:
                if 0 <= ak3 < 6:
                    alien3.setx(alien3.xcor() - 0.3)
                if 6 <= ak3 < 12:
                    alien3.setx(alien3.xcor() - 0.6)
                if 12 <= ak3 < 18:
                    alien3.setx(alien3.xcor() - 0.9)
                if 18 <= ak3 < 24:
                    alien3.setx(alien3.xcor() - 1.2)
                if 24 <= ak3 < 30:
                    alien3.setx(alien3.xcor() - 1.5)
                if 30 <= ak3:
                    alien3.setx(alien3.xcor() - 1.8)

        if alien4.isvisible() and alien4_death == 0:
            if alien4.direction == "right":
                if 0 <= ak4 < 6:
                    alien4.setx(alien4.xcor() + 0.3)
                if 6 <= ak4 < 12:
                    alien4.setx(alien4.xcor() + 0.6)
                if 12 <= ak4 < 18:
                    alien4.setx(alien4.xcor() + 0.9)
                if 18 <= ak4 < 24:
                    alien4.setx(alien4.xcor() + 1.2)
                if 24 <= ak4 < 30:
                    alien4.setx(alien4.xcor() + 1.5)
                if 30 <= ak4:
                    alien4.setx(alien4.xcor() + 1.8)
            else:
                if 0 <= ak4 < 6:
                    alien4.setx(alien4.xcor() - 0.3)
                if 6 <= ak4 < 12:
                    alien4.setx(alien4.xcor() - 0.6)
                if 12 <= ak4 < 18:
                    alien4.setx(alien4.xcor() - 0.9)
                if 18 <= ak4 < 24:
                    alien4.setx(alien4.xcor() - 1.2)
                if 24 <= ak4 < 30:
                    alien4.setx(alien4.xcor() - 1.5)
                if 30 <= ak4:
                    alien4.setx(alien4.xcor() - 1.8)

        if alien5.isvisible() and alien5_death == 0:
            if alien5.direction == "right":
                if 0 <= ak5 < 6:
                    alien5.setx(alien5.xcor() + 0.3)
                if 6 <= ak5 < 12:
                    alien5.setx(alien5.xcor() + 0.6)
                if 12 <= ak5 < 18:
                    alien5.setx(alien5.xcor() + 0.9)
                if 18 <= ak5 < 24:
                    alien5.setx(alien5.xcor() + 1.2)
                if 24 <= ak5 < 30:
                    alien5.setx(alien5.xcor() + 1.5)
                if 30 <= ak5:
                    alien5.setx(alien5.xcor() + 1.8)
            else:
                if 0 <= ak5 < 6:
                    alien5.setx(alien5.xcor() - 0.3)
                if 6 <= ak5 < 12:
                    alien5.setx(alien5.xcor() - 0.6)
                if 12 <= ak5 < 18:
                    alien5.setx(alien5.xcor() - 0.9)
                if 18 <= ak5 < 24:
                    alien5.setx(alien5.xcor() - 1.2)
                if 24 <= ak5 < 30:
                    alien5.setx(alien5.xcor() - 1.5)
                if 30 <= ak5:
                    alien5.setx(alien5.xcor() - 1.8)

        if alien6.isvisible() and alien6_death == 0:
            if alien6.direction == "right":
                if 0 <= ak6 < 6:
                    alien6.setx(alien6.xcor() + 0.3)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 0.3)
                if 6 <= ak6 < 12:
                    alien6.setx(alien6.xcor() + 0.6)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 0.6)
                if 12 <= ak6 < 18:
                    alien6.setx(alien6.xcor() + 0.9)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 0.9)
                if 18 <= ak6 < 24:
                    alien6.setx(alien6.xcor() + 1.2)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 1.2)
                if 24 <= ak6 < 30:
                    alien6.setx(alien6.xcor() + 1.5)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 1.5)
                if 30 <= ak6:
                    alien6.setx(alien6.xcor() + 1.8)
                    alien6_health_bar.setx(alien6_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak6 < 6:
                    alien6.setx(alien6.xcor() - 0.3)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 0.3)
                if 6 <= ak6 < 12:
                    alien6.setx(alien6.xcor() - 0.6)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 0.6)
                if 12 <= ak6 < 18:
                    alien6.setx(alien6.xcor() - 0.9)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 0.9)
                if 18 <= ak6 < 24:
                    alien6.setx(alien6.xcor() - 1.2)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 1.2)
                if 24 <= ak6 < 30:
                    alien6.setx(alien6.xcor() - 1.5)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 1.5)
                if 30 <= ak6:
                    alien6.setx(alien6.xcor() - 1.8)
                    alien6_health_bar.setx(alien6_health_bar.xcor() - 1.8)

        if alien7.isvisible() and alien7_death == 0:
            if alien7.direction == "right":
                if 0 <= ak7 < 6:
                    alien7.setx(alien7.xcor() + 0.3)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 0.3)
                if 6 <= ak7 < 12:
                    alien7.setx(alien7.xcor() + 0.6)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 0.6)
                if 12 <= ak7 < 18:
                    alien7.setx(alien7.xcor() + 0.9)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 0.9)
                if 18 <= ak7 < 24:
                    alien7.setx(alien7.xcor() + 1.2)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 1.2)
                if 24 <= ak7 < 30:
                    alien7.setx(alien7.xcor() + 1.5)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 1.5)
                if 30 <= ak7:
                    alien7.setx(alien7.xcor() + 1.8)
                    alien7_health_bar.setx(alien7_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak7 < 6:
                    alien7.setx(alien7.xcor() - 0.3)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 0.3)
                if 6 <= ak7 < 12:
                    alien7.setx(alien7.xcor() - 0.6)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 0.6)
                if 12 <= ak7 < 18:
                    alien7.setx(alien7.xcor() - 0.9)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 0.9)
                if 18 <= ak7 < 24:
                    alien7.setx(alien7.xcor() - 1.2)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 1.2)
                if 24 <= ak7 < 30:
                    alien7.setx(alien7.xcor() - 1.5)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 1.5)
                if 30 <= ak7:
                    alien7.setx(alien7.xcor() - 1.8)
                    alien7_health_bar.setx(alien7_health_bar.xcor() - 1.8)

        if alien8.isvisible() and alien8_death == 0:
            if alien8.direction == "right":
                if 0 <= ak8 < 6:
                    alien8.setx(alien8.xcor() + 0.3)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 0.3)
                if 6 <= ak8 < 12:
                    alien8.setx(alien8.xcor() + 0.6)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 0.6)
                if 12 <= ak8 < 18:
                    alien8.setx(alien8.xcor() + 0.9)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 0.9)
                if 18 <= ak8 < 24:
                    alien8.setx(alien8.xcor() + 1.2)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 1.2)
                if 24 <= ak8 < 30:
                    alien8.setx(alien8.xcor() + 1.5)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 1.5)
                if 30 <= ak8:
                    alien8.setx(alien8.xcor() + 1.8)
                    alien8_health_bar.setx(alien8_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak8 < 6:
                    alien8.setx(alien8.xcor() - 0.3)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 0.3)
                if 6 <= ak8 < 12:
                    alien8.setx(alien8.xcor() - 0.6)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 0.6)
                if 12 <= ak8 < 18:
                    alien8.setx(alien8.xcor() - 0.9)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 0.9)
                if 18 <= ak8 < 24:
                    alien8.setx(alien8.xcor() - 1.2)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 1.2)
                if 24 <= ak8 < 30:
                    alien8.setx(alien8.xcor() - 1.5)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 1.5)
                if 30 <= ak8:
                    alien8.setx(alien8.xcor() - 1.8)
                    alien8_health_bar.setx(alien8_health_bar.xcor() - 1.8)

        if alien9.isvisible() and alien9_death == 0:
            if alien9.direction == "right":
                if 0 <= ak9 < 6:
                    alien9.setx(alien9.xcor() + 0.3)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 0.3)
                if 6 <= ak9 < 12:
                    alien9.setx(alien9.xcor() + 0.6)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 0.6)
                if 12 <= ak9 < 18:
                    alien9.setx(alien9.xcor() + 0.9)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 0.9)
                if 18 <= ak9 < 24:
                    alien9.setx(alien9.xcor() + 1.2)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 1.2)
                if 24 <= ak9 < 30:
                    alien9.setx(alien9.xcor() + 1.5)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 1.5)
                if 30 <= ak9:
                    alien9.setx(alien9.xcor() + 1.8)
                    alien9_health_bar.setx(alien9_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak9 < 6:
                    alien9.setx(alien9.xcor() - 0.3)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 0.3)
                if 6 <= ak9 < 12:
                    alien9.setx(alien9.xcor() - 0.6)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 0.6)
                if 12 <= ak9 < 18:
                    alien9.setx(alien9.xcor() - 0.9)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 0.9)
                if 18 <= ak9 < 24:
                    alien9.setx(alien9.xcor() - 1.2)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 1.2)
                if 24 <= ak9 < 30:
                    alien9.setx(alien9.xcor() - 1.5)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 1.5)
                if 30 <= ak9:
                    alien9.setx(alien9.xcor() - 1.8)
                    alien9_health_bar.setx(alien9_health_bar.xcor() - 1.8)

        if alien10.isvisible() and alien10_death == 0:
            if alien10.direction == "right":
                if 0 <= ak10 < 6:
                    alien10.setx(alien10.xcor() + 0.3)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 0.3)
                if 6 <= ak10 < 12:
                    alien10.setx(alien10.xcor() + 0.6)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 0.6)
                if 12 <= ak10 < 18:
                    alien10.setx(alien10.xcor() + 0.9)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 0.9)
                if 18 <= ak10 < 24:
                    alien10.setx(alien10.xcor() + 1.2)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 1.2)
                if 24 <= ak10 < 30:
                    alien10.setx(alien10.xcor() + 1.5)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 1.5)
                if 30 <= ak10:
                    alien10.setx(alien10.xcor() + 1.8)
                    alien10_health_bar.setx(alien10_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak10 < 6:
                    alien10.setx(alien10.xcor() - 0.3)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 0.3)
                if 6 <= ak10 < 12:
                    alien10.setx(alien10.xcor() - 0.6)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 0.6)
                if 12 <= ak10 < 18:
                    alien10.setx(alien10.xcor() - 0.9)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 0.9)
                if 18 <= ak10 < 24:
                    alien10.setx(alien10.xcor() - 1.2)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 1.2)
                if 24 <= ak10 < 30:
                    alien10.setx(alien10.xcor() - 1.5)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 1.5)
                if 30 <= ak10:
                    alien10.setx(alien10.xcor() - 1.8)
                    alien10_health_bar.setx(alien10_health_bar.xcor() - 1.8)

        if alien11.isvisible() and alien11_death == 0:
            if alien11.direction == "right":
                if 0 <= ak11 < 6:
                    alien11.setx(alien11.xcor() + 0.3)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 0.3)
                if 6 <= ak11 < 12:
                    alien11.setx(alien11.xcor() + 0.6)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 0.6)
                if 12 <= ak11 < 18:
                    alien11.setx(alien11.xcor() + 0.9)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 0.9)
                if 18 <= ak11 < 24:
                    alien11.setx(alien11.xcor() + 1.2)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 1.2)
                if 24 <= ak11 < 30:
                    alien11.setx(alien11.xcor() + 1.5)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 1.5)
                if 30 <= ak11:
                    alien11.setx(alien11.xcor() + 1.8)
                    alien11_health_bar.setx(alien11_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak11 < 6:
                    alien11.setx(alien11.xcor() - 0.3)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 0.3)
                if 6 <= ak11 < 12:
                    alien11.setx(alien11.xcor() - 0.6)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 0.6)
                if 12 <= ak11 < 18:
                    alien11.setx(alien11.xcor() - 0.9)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 0.9)
                if 18 <= ak11 < 24:
                    alien11.setx(alien11.xcor() - 1.2)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 1.2)
                if 24 <= ak11 < 30:
                    alien11.setx(alien11.xcor() - 1.5)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 1.5)
                if 30 <= ak11:
                    alien11.setx(alien11.xcor() - 1.8)
                    alien11_health_bar.setx(alien11_health_bar.xcor() - 1.8)

        if alien12.isvisible() and alien12_death == 0:
            if alien12.direction == "right":
                if 0 <= ak12 < 6:
                    alien12.setx(alien12.xcor() + 0.3)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 0.3)
                if 6 <= ak12 < 12:
                    alien12.setx(alien12.xcor() + 0.6)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 0.6)
                if 12 <= ak12 < 18:
                    alien12.setx(alien12.xcor() + 0.9)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 0.9)
                if 18 <= ak12 < 24:
                    alien12.setx(alien12.xcor() + 1.2)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 1.2)
                if 24 <= ak12 < 30:
                    alien12.setx(alien12.xcor() + 1.5)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 1.5)
                if 30 <= ak12:
                    alien12.setx(alien12.xcor() + 1.8)
                    alien12_health_bar.setx(alien12_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak12 < 6:
                    alien12.setx(alien12.xcor() - 0.3)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 0.3)
                if 6 <= ak12 < 12:
                    alien12.setx(alien12.xcor() - 0.6)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 0.6)
                if 12 <= ak12 < 18:
                    alien12.setx(alien12.xcor() - 0.9)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 0.9)
                if 18 <= ak12 < 24:
                    alien12.setx(alien12.xcor() - 1.2)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 1.2)
                if 24 <= ak12 < 30:
                    alien12.setx(alien12.xcor() - 1.5)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 1.5)
                if 30 <= ak12:
                    alien12.setx(alien12.xcor() - 1.8)
                    alien12_health_bar.setx(alien12_health_bar.xcor() - 1.8)

        if alien13.isvisible() and alien13_death == 0:
            if alien13.direction == "right":
                if 0 <= ak13 < 6:
                    alien13.setx(alien13.xcor() + 0.3)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 0.3)
                if 6 <= ak13 < 12:
                    alien13.setx(alien13.xcor() + 0.6)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 0.6)
                if 12 <= ak13 < 18:
                    alien13.setx(alien13.xcor() + 0.9)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 0.9)
                if 18 <= ak13 < 24:
                    alien13.setx(alien13.xcor() + 1.2)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 1.2)
                if 24 <= ak13 < 30:
                    alien13.setx(alien13.xcor() + 1.5)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 1.5)
                if 30 <= ak13:
                    alien13.setx(alien13.xcor() + 1.8)
                    alien13_health_bar.setx(alien13_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak13 < 6:
                    alien13.setx(alien13.xcor() - 0.3)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 0.3)
                if 6 <= ak13 < 12:
                    alien13.setx(alien13.xcor() - 0.6)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 0.6)
                if 12 <= ak13 < 18:
                    alien13.setx(alien13.xcor() - 0.9)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 0.9)
                if 18 <= ak13 < 24:
                    alien13.setx(alien13.xcor() - 1.2)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 1.2)
                if 24 <= ak13 < 30:
                    alien13.setx(alien13.xcor() - 1.5)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 1.5)
                if 30 <= ak13:
                    alien13.setx(alien13.xcor() - 1.8)
                    alien13_health_bar.setx(alien13_health_bar.xcor() - 1.8)

        if alien14.isvisible() and alien14_death == 0:
            if alien14.direction == "right":
                if 0 <= ak14 < 6:
                    alien14.setx(alien14.xcor() + 0.3)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 0.3)
                if 6 <= ak14 < 12:
                    alien14.setx(alien14.xcor() + 0.6)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 0.6)
                if 12 <= ak14 < 18:
                    alien14.setx(alien14.xcor() + 0.9)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 0.9)
                if 18 <= ak14 < 24:
                    alien14.setx(alien14.xcor() + 1.2)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 1.2)
                if 24 <= ak14 < 30:
                    alien14.setx(alien14.xcor() + 1.5)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 1.5)
                if 30 <= ak14:
                    alien14.setx(alien14.xcor() + 1.8)
                    alien14_health_bar.setx(alien14_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak14 < 6:
                    alien14.setx(alien14.xcor() - 0.3)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 0.3)
                if 6 <= ak14 < 12:
                    alien14.setx(alien14.xcor() - 0.6)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 0.6)
                if 12 <= ak14 < 18:
                    alien14.setx(alien14.xcor() - 0.9)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 0.9)
                if 18 <= ak14 < 24:
                    alien14.setx(alien14.xcor() - 1.2)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 1.2)
                if 24 <= ak14 < 30:
                    alien14.setx(alien14.xcor() - 1.5)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 1.5)
                if 30 <= ak14:
                    alien14.setx(alien14.xcor() - 1.8)
                    alien14_health_bar.setx(alien14_health_bar.xcor() - 1.8)

        if alien15.isvisible() and alien15_death == 0:
            if alien15.direction == "right":
                if 0 <= ak15 < 6:
                    alien15.setx(alien15.xcor() + 0.3)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 0.3)
                if 6 <= ak15 < 12:
                    alien15.setx(alien15.xcor() + 0.6)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 0.6)
                if 12 <= ak15 < 18:
                    alien15.setx(alien15.xcor() + 0.9)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 0.9)
                if 18 <= ak15 < 24:
                    alien15.setx(alien15.xcor() + 1.2)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 1.2)
                if 24 <= ak15 < 30:
                    alien15.setx(alien15.xcor() + 1.5)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 1.5)
                if 30 <= ak15:
                    alien15.setx(alien15.xcor() + 1.8)
                    alien15_health_bar.setx(alien15_health_bar.xcor() + 1.8)
            else:
                if 0 <= ak15 < 6:
                    alien15.setx(alien15.xcor() - 0.3)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 0.3)
                if 6 <= ak15 < 12:
                    alien15.setx(alien15.xcor() - 0.6)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 0.6)
                if 12 <= ak15 < 18:
                    alien15.setx(alien15.xcor() - 0.9)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 0.9)
                if 18 <= ak15 < 24:
                    alien15.setx(alien15.xcor() - 1.2)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 1.2)
                if 24 <= ak15 < 30:
                    alien15.setx(alien15.xcor() - 1.5)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 1.5)
                if 30 <= ak15:
                    alien15.setx(alien15.xcor() - 1.8)
                    alien15_health_bar.setx(alien15_health_bar.xcor() - 1.8)

        if alien_boss.isvisible() and alien_boss_death == 0:
            if alien_boss.direction == "right":
                if 0 <= ak_boss < 3:
                    alien_boss.setx(alien_boss.xcor() + 0.25)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 0.25)
                if 3 <= ak_boss < 6:
                    alien_boss.setx(alien_boss.xcor() + 0.5)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 0.5)
                if 6 <= ak_boss < 9:
                    alien_boss.setx(alien_boss.xcor() + 1)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 1)
                if 9 <= ak_boss < 12:
                    alien_boss.setx(alien_boss.xcor() + 2)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 2)
                if 12 <= ak_boss < 15:
                    alien_boss.setx(alien_boss.xcor() + 4)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 4)
                if 15 <= ak_boss:
                    alien_boss.setx(alien_boss.xcor() + 8)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() + 8)
            else:
                if 0 <= ak_boss < 3:
                    alien_boss.setx(alien_boss.xcor() - 0.25)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 0.25)
                if 3 <= ak_boss < 6:
                    alien_boss.setx(alien_boss.xcor() - 0.5)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 0.5)
                if 6 <= ak_boss < 9:
                    alien_boss.setx(alien_boss.xcor() - 1)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 1)
                if 9 <= ak_boss < 12:
                    alien_boss.setx(alien_boss.xcor() - 2)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 2)
                if 12 <= ak_boss < 15:
                    alien_boss.setx(alien_boss.xcor() - 4)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 4)
                if 15 <= ak_boss:
                    alien_boss.setx(alien_boss.xcor() - 8)
                    alien_boss_health_bar.setx(alien_boss_health_bar.xcor() - 8)

        # Lines 3953 - 3970 are for configuring the boss aliens laser

        if alien_boss.isvisible() or alien_boss_death != 0:
            if alien_boss_laser.ycor() > -600:
                alien_boss_laser.direction = "down"
                YL = alien_boss_laser.ycor()
                alien_boss_laser.sety(YL - 3.2)
            elif alien_boss_death == 0:
                x = alien_boss.xcor()
                alien_boss_laser.setx(x + 2)
                alien_boss_laser.sety(-90)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            x = alien_boss.xcor()
            alien_boss_laser.setx(x + 2)
            alien_boss_laser.sety(-90)

        if alien_boss_laser.ycor() < -170:
            alien_boss_laser.hideturtle()

        # Lines 3976 - 4151 are for setting the aliens texture as it is moving and changing directions
        # Each alien has 4 textures: The still and walking animations of both the left and right directions
        # The textures are changed depending on what the alien is doing

        if alien1.direction == "right" and alien1_death == 0:
            if right_update % 0.5 != 0:
                alien1.shape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
            else:
                alien1.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        elif alien1.direction == "left" and alien1_death == 0:
            if left_update % 0.5 != 0:
                alien1.shape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
            else:
                alien1.shape("Textures/Aliens/Alien_Still_Left(1-5).gif")

        if alien2.direction == "right" and alien2_death == 0:
            if right_update % 0.5 != 0:
                alien2.shape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
            else:
                alien2.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        elif alien2.direction == "left" and alien2_death == 0:
            if left_update % 0.5 != 0:
                alien2.shape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
            else:
                alien2.shape("Textures/Aliens/Alien_Still_Left(1-5).gif")

        if alien3.direction == "right" and alien3_death == 0:
            if right_update % 0.5 != 0:
                alien3.shape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
            else:
                alien3.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        elif alien3.direction == "left" and alien3_death == 0:
            if left_update % 0.5 != 0:
                alien3.shape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
            else:
                alien3.shape("Textures/Aliens/Alien_Still_Left(1-5).gif")

        if alien4.isvisible():
            if alien4.direction == "right" and alien4_death == 0:
                if right_update % 0.5 != 0:
                    alien4.shape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
                else:
                    alien4.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
            elif alien4.direction == "left" and alien4_death == 0:
                if left_update % 0.5 != 0:
                    alien4.shape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
                else:
                    alien4.shape("Textures/Aliens/Alien_Still_Left(1-5).gif")

        if alien5.isvisible():
            if alien5.direction == "right" and alien5_death == 0:
                if right_update % 0.5 != 0:
                    alien5.shape("Textures/Aliens/Alien_Walking_Right(1-5).gif")
                else:
                    alien5.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
            elif alien5.direction == "left" and alien5_death == 0:
                if left_update % 0.5 != 0:
                    alien5.shape("Textures/Aliens/Alien_Walking_Left(1-5).gif")
                else:
                    alien5.shape("Textures/Aliens/Alien_Still_Left(1-5).gif")

        if alien6.isvisible():
            if alien6.direction == "right" and alien6_death == 0:
                if right_update % 0.5 != 0:
                    alien6.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    alien6.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            elif alien6.direction == "left" and alien6_death == 0:
                if left_update % 0.5 != 0:
                    alien6.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    alien6.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")

        if alien7.isvisible():
            if alien7.direction == "right" and alien7_death == 0:
                if right_update % 0.5 != 0:
                    alien7.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    alien7.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            elif alien7.direction == "left" and alien7_death == 0:
                if left_update % 0.5 != 0:
                    alien7.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    alien7.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")

        if alien8.isvisible():
            if alien8.direction == "right" and alien8_death == 0:
                if right_update % 0.5 != 0:
                    alien8.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    alien8.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            elif alien8.direction == "left" and alien8_death == 0:
                if left_update % 0.5 != 0:
                    alien8.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    alien8.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")

        if alien9.isvisible():
            if alien9.direction == "right" and alien9_death == 0:
                if right_update % 0.5 != 0:
                    alien9.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    alien9.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            elif alien9.direction == "left" and alien9_death == 0:
                if left_update % 0.5 != 0:
                    alien9.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    alien9.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")

        if alien10.isvisible():
            if alien10.direction == "right" and alien10_death == 0:
                if right_update % 0.5 != 0:
                    alien10.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    alien10.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            elif alien10.direction == "left" and alien10_death == 0:
                if left_update % 0.5 != 0:
                    alien10.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    alien10.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")

        if alien11.isvisible():
            if alien11.direction == "right" and alien11_death == 0:
                if right_update % 0.5 != 0:
                    alien11.shape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
                else:
                    alien11.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
            elif alien11.direction == "left" and alien11_death == 0:
                if left_update % 0.5 != 0:
                    alien11.shape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
                else:
                    alien11.shape("Textures/Aliens/Alien_Still_Left(11-15).gif")

        if alien12.isvisible():
            if alien12.direction == "right" and alien12_death == 0:
                if right_update % 0.5 != 0:
                    alien12.shape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
                else:
                    alien12.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
            elif alien12.direction == "left" and alien12_death == 0:
                if left_update % 0.5 != 0:
                    alien12.shape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
                else:
                    alien12.shape("Textures/Aliens/Alien_Still_Left(11-15).gif")

        if alien13.isvisible():
            if alien13.direction == "right" and alien13_death == 0:
                if right_update % 0.5 != 0:
                    alien13.shape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
                else:
                    alien13.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
            elif alien13.direction == "left" and alien13_death == 0:
                if left_update % 0.5 != 0:
                    alien13.shape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
                else:
                    alien13.shape("Textures/Aliens/Alien_Still_Left(11-15).gif")

        if alien14.isvisible():
            if alien14.direction == "right" and alien14_death == 0:
                if right_update % 0.5 != 0:
                    alien14.shape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
                else:
                    alien14.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
            elif alien14.direction == "left" and alien14_death == 0:
                if left_update % 0.5 != 0:
                    alien14.shape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
                else:
                    alien14.shape("Textures/Aliens/Alien_Still_Left(11-15).gif")

        if alien15.isvisible():
            if alien15.direction == "right" and alien15_death == 0:
                if right_update % 0.5 != 0:
                    alien15.shape("Textures/Aliens/Alien_Walking_Right(11-15).gif")
                else:
                    alien15.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
            elif alien15.direction == "left" and alien15_death == 0:
                if left_update % 0.5 != 0:
                    alien15.shape("Textures/Aliens/Alien_Walking_Left(11-15).gif")
                else:
                    alien15.shape("Textures/Aliens/Alien_Still_Left(11-15).gif")

        # Lines 4156 - 5400 are for what happens when each of the aliens gets hit/dies
        # The smaller aliens instantly die when they are hit. The larger ones have a certain amount of health

        if 4.5 <= alien1_death < 5:
            alien1.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien1.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien1.goto(random.randint(690, 900), -150)
            alien1.showturtle()
            alien1_death = 0

        if 3 <= alien1_death < 4.5:
            alien1_death = alien1_death + 0.1

        if 2 <= alien1_death < 3:
            alien1.shape("Textures/Explosions/Alien_Death_2.gif")
            alien1_death = 3

        if 1 <= alien1_death < 2:
            alien1_death = alien1_death + 0.1

        if (player_head_laser.distance(alien1) < 53 and ((alien1.xcor() - 15 < player_head_laser.xcor() < alien1.xcor() + 15) or yellow_power_up_active == 1)) and alien1_death == 0 and alien1.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            ak1 = ak1 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                small_aliens_killed = small_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[24] = str(small_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien1.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien1_death = 1

        if 4.5 <= alien2_death < 5:
            alien2.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien2.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien2.goto(random.randint(690, 900), -150)
            alien2.showturtle()
            alien2_death = 0

        if 3 <= alien2_death < 4.5:
            alien2_death = alien2_death + 0.1

        if 2 <= alien2_death < 3:
            alien2.shape("Textures/Explosions/Alien_Death_2.gif")
            alien2_death = 3

        if 1 <= alien2_death < 2:
            alien2_death = alien2_death + 0.1

        if (player_head_laser.distance(alien2) < 53 and ((alien2.xcor() - 15 < player_head_laser.xcor() < alien2.xcor() + 15) or yellow_power_up_active == 1)) and alien2_death == 0 and alien2.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            ak2 = ak2 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                small_aliens_killed = small_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[24] = str(small_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien2.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien2_death = 1

        if 4.5 <= alien3_death < 5:
            alien3.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien3.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien3.goto(random.randint(690, 900), -150)
            alien3.showturtle()
            alien3_death = 0

        if 3 <= alien3_death < 4.5:
            alien3_death = alien3_death + 0.1

        if 2 <= alien3_death < 3:
            alien3.shape("Textures/Explosions/Alien_Death_2.gif")
            alien3_death = 3

        if 1 <= alien3_death < 2:
            alien3_death = alien3_death + 0.1

        if (player_head_laser.distance(alien3) < 53 and ((alien3.xcor() - 15 < player_head_laser.xcor() < alien3.xcor() + 15) or yellow_power_up_active == 1)) and alien3_death == 0 and alien3.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            ak3 = ak3 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                small_aliens_killed = small_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[24] = str(small_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien3.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien3_death = 1

        if 4.5 <= alien4_death < 5:
            alien4.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien4.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien4.goto(random.randint(690, 900), -150)
            alien4.showturtle()
            alien4_death = 0

        if 3 <= alien4_death < 4.5:
            alien4_death = alien4_death + 0.1

        if 2 <= alien4_death < 3:
            alien4.shape("Textures/Explosions/Alien_Death_2.gif")
            alien4_death = 3

        if 1 <= alien4_death < 2:
            alien4_death = alien4_death + 0.1

        if (player_head_laser.distance(alien4) < 53 and ((alien4.xcor() - 15 < player_head_laser.xcor() < alien4.xcor() + 15) or yellow_power_up_active == 1)) and alien4_death == 0 and alien4.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            ak4 = ak4 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                small_aliens_killed = small_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[24] = str(small_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien4.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien4_death = 1

        if 4.5 <= alien5_death < 5:
            alien5.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien5.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien5.goto(random.randint(690, 900), -150)
            alien5.showturtle()
            alien5_death = 0

        if 3 <= alien5_death < 4.5:
            alien5_death = alien5_death + 0.1

        if 2 <= alien5_death < 3:
            alien5.shape("Textures/Explosions/Alien_Death_2.gif")
            alien5_death = 3

        if 1 <= alien5_death < 2:
            alien5_death = alien5_death + 0.1

        if (player_head_laser.distance(alien5) < 53 and ((alien5.xcor() - 15 < player_head_laser.xcor() < alien5.xcor() + 15) or yellow_power_up_active == 1)) and alien5_death == 0 and alien5.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            ak5 = ak5 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                small_aliens_killed = small_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[24] = str(small_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien5.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien5_death = 1

        if 4.5 <= alien6_death < 5:
            alien6.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien6.goto(random.randint(-900, -690), -130)
                alien6_health_bar.goto(alien6.xcor(), -45)
            if alien_random == 2:
                alien6.goto(random.randint(690, 900), -130)
                alien6_health_bar.goto(alien6.xcor(), -45)
            alien6_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien6_health = 2
            alien6.showturtle()
            alien6_health_bar.showturtle()
            alien6_death = 0

        if 3 <= alien6_death < 4.5:
            alien6_death = alien6_death + 0.1

        if 2 <= alien6_death < 3:
            alien6.shape("Textures/Explosions/Alien_Death_2.gif")
            alien6_death = 3

        if 1 <= alien6_death < 2:
            alien6_death = alien6_death + 0.1

        if (player_head_laser.distance(alien6) < 72 and ((alien6.xcor() - 15 < player_head_laser.xcor() < alien6.xcor() + 15) or yellow_power_up_active == 1)) and alien6_health == 1 and alien6_death == 0 and alien6.isvisible() and player_head_laser.isvisible() and alien6_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            ak6 = ak6 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                medium_aliens_killed = medium_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[22] = str(medium_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien6_health = 0
            alien6_health_bar.hideturtle()
            alien6.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien6_death = 1

        if alien6_hit_delay == 9:
            alien6_hit_delay = 0

        if 1 <= alien6_hit_delay < 9:
            alien6_hit_delay = alien6_hit_delay + 1

        if (player_head_laser.distance(alien6) < 72 and ((alien6.xcor() - 15 < player_head_laser.xcor() < alien6.xcor() + 15) or yellow_power_up_active == 1)) and alien6_health == 2 and alien6_death == 0 and alien6.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien6_health = 1
            alien6_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien6_hit_delay = 1

        if 4.5 <= alien7_death < 5:
            alien7.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien7.goto(random.randint(-900, -690), -130)
                alien7_health_bar.goto(alien7.xcor(), -45)
            if alien_random == 2:
                alien7.goto(random.randint(690, 900), -130)
                alien7_health_bar.goto(alien7.xcor(), -45)
            alien7_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien7_health = 2
            alien7.showturtle()
            alien7_health_bar.showturtle()
            alien7_death = 0

        if 3 <= alien7_death < 4.5:
            alien7_death = alien7_death + 0.1

        if 2 <= alien7_death < 3:
            alien7.shape("Textures/Explosions/Alien_Death_2.gif")
            alien7_death = 3

        if 1 <= alien7_death < 2:
            alien7_death = alien7_death + 0.1

        if (player_head_laser.distance(alien7) < 72 and ((alien7.xcor() - 15 < player_head_laser.xcor() < alien7.xcor() + 15) or yellow_power_up_active == 1)) and alien7_health == 1 and alien7_death == 0 and alien7.isvisible() and player_head_laser.isvisible() and alien7_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            ak7 = ak7 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                medium_aliens_killed = medium_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[22] = str(medium_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien7_health = 0
            alien7_health_bar.hideturtle()
            alien7.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien7_death = 1

        if alien7_hit_delay == 9:
            alien7_hit_delay = 0

        if 1 <= alien7_hit_delay < 9:
            alien7_hit_delay = alien7_hit_delay + 1

        if (player_head_laser.distance(alien7) < 72 and ((alien7.xcor() - 15 < player_head_laser.xcor() < alien7.xcor() + 15) or yellow_power_up_active == 1)) and alien7_health == 2 and alien7_death == 0 and alien7.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien7_health = 1
            alien7_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien7_hit_delay = 1

        if 4.5 <= alien8_death < 5:
            alien8.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien8.goto(random.randint(-900, -690), -130)
                alien8_health_bar.goto(alien8.xcor(), -45)
            if alien_random == 2:
                alien8.goto(random.randint(690, 900), -130)
                alien8_health_bar.goto(alien8.xcor(), -45)
            alien8_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien8_health = 2
            alien8.showturtle()
            alien8_health_bar.showturtle()
            alien8_death = 0

        if 3 <= alien8_death < 4.5:
            alien8_death = alien8_death + 0.1

        if 2 <= alien8_death < 3:
            alien8.shape("Textures/Explosions/Alien_Death_2.gif")
            alien8_death = 3

        if 1 <= alien8_death < 2:
            alien8_death = alien8_death + 0.1

        if (player_head_laser.distance(alien8) < 72 and ((alien8.xcor() - 15 < player_head_laser.xcor() < alien8.xcor() + 15) or yellow_power_up_active == 1)) and alien8_health == 1 and alien8_death == 0 and alien8.isvisible() and player_head_laser.isvisible() and alien8_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            ak8 = ak8 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                medium_aliens_killed = medium_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[22] = str(medium_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien8_health = 0
            alien8_health_bar.hideturtle()
            alien8.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien8_death = 1

        if alien8_hit_delay == 9:
            alien8_hit_delay = 0

        if 1 <= alien8_hit_delay < 9:
            alien8_hit_delay = alien8_hit_delay + 1

        if (player_head_laser.distance(alien8) < 72 and ((alien8.xcor() - 15 < player_head_laser.xcor() < alien8.xcor() + 15) or yellow_power_up_active == 1)) and alien8_health == 2 and alien8_death == 0 and alien8.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien8_health = 1
            alien8_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien8_hit_delay = 1

        if 4.5 <= alien9_death < 5:
            alien9.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien9.goto(random.randint(-900, -690), -130)
                alien9_health_bar.goto(alien9.xcor(), -45)
            if alien_random == 2:
                alien9.goto(random.randint(690, 900), -130)
                alien9_health_bar.goto(alien9.xcor(), -45)
            alien9_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien9_health = 2
            alien9.showturtle()
            alien9_health_bar.showturtle()
            alien9_death = 0

        if 3 <= alien9_death < 4.5:
            alien9_death = alien9_death + 0.1

        if 2 <= alien9_death < 3:
            alien9.shape("Textures/Explosions/Alien_Death_2.gif")
            alien9_death = 3

        if 1 <= alien9_death < 2:
            alien9_death = alien9_death + 0.1

        if (player_head_laser.distance(alien9) < 72 and ((alien9.xcor() - 15 < player_head_laser.xcor() < alien9.xcor() + 15) or yellow_power_up_active == 1)) and alien9_health == 1 and alien9_death == 0 and alien9.isvisible() and player_head_laser.isvisible() and alien9_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            ak9 = ak9 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                medium_aliens_killed = medium_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[22] = str(medium_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien9_health = 0
            alien9_health_bar.hideturtle()
            alien9.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien9_death = 1

        if alien9_hit_delay == 9:
            alien9_hit_delay = 0

        if 1 <= alien9_hit_delay < 9:
            alien9_hit_delay = alien9_hit_delay + 1

        if (player_head_laser.distance(alien9) < 72 and ((alien9.xcor() - 15 < player_head_laser.xcor() < alien9.xcor() + 15) or yellow_power_up_active == 1)) and alien9_health == 2 and alien9_death == 0 and alien9.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien9_health = 1
            alien9_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien9_hit_delay = 1

        if 4.5 <= alien10_death < 5:
            alien10.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien10.goto(random.randint(-900, -690), -130)
                alien10_health_bar.goto(alien10.xcor(), -45)
            if alien_random == 2:
                alien10.goto(random.randint(690, 900), -130)
                alien10_health_bar.goto(alien10.xcor(), -45)
            alien10_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien10_health = 2
            alien10.showturtle()
            alien10_health_bar.showturtle()
            alien10_death = 0

        if 3 <= alien10_death < 4.5:
            alien10_death = alien10_death + 0.1

        if 2 <= alien10_death < 3:
            alien10.shape("Textures/Explosions/Alien_Death_2.gif")
            alien10_death = 3

        if 1 <= alien10_death < 2:
            alien10_death = alien10_death + 0.1

        if (player_head_laser.distance(alien10) < 72 and ((alien10.xcor() - 15 < player_head_laser.xcor() < alien10.xcor() + 15) or yellow_power_up_active == 1)) and alien10_health == 1 and alien10_death == 0 and alien10.isvisible() and player_head_laser.isvisible() and alien10_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            ak10 = ak10 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                medium_aliens_killed = medium_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[22] = str(medium_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien10_health = 0
            alien10_health_bar.hideturtle()
            alien10.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien10_death = 1

        if alien10_hit_delay == 9:
            alien10_hit_delay = 0

        if 1 <= alien10_hit_delay < 9:
            alien10_hit_delay = alien10_hit_delay + 1

        if (player_head_laser.distance(alien10) < 72 and ((alien10.xcor() - 15 < player_head_laser.xcor() < alien10.xcor() + 15) or yellow_power_up_active == 1)) and alien10_health == 2 and alien10_death == 0 and alien10.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien10_health = 1
            alien10_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien10_hit_delay = 1

        if 4.5 <= alien11_death < 5:
            alien11.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien11.goto(random.randint(-900, -690), -93)
                alien11_health_bar.goto(alien11.xcor(), 30)
            if alien_random == 2:
                alien11.goto(random.randint(690, 900), -93)
                alien11_health_bar.goto(alien11.xcor(), 30)
            alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien11_health = 3
            alien11.showturtle()
            alien11_health_bar.showturtle()
            alien11_death = 0

        if 3 <= alien11_death < 4.5:
            alien11_death = alien11_death + 0.1

        if 2 <= alien11_death < 3:
            alien11.shape("Textures/Explosions/Alien_Death_2.gif")
            alien11_death = 3

        if 1 <= alien11_death < 2:
            alien11_death = alien11_death + 0.1

        if (player_head_laser.distance(alien11) < 112 and ((alien11.xcor() - 15 < player_head_laser.xcor() < alien11.xcor() + 15) or yellow_power_up_active == 1)) and alien11_health == 1 and alien11_death == 0 and alien11.isvisible() and player_head_laser.isvisible() and alien11_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 8
            else:
                score = score + 4
            ak11 = ak11 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                big_aliens_killed = big_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[20] = str(big_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien11_health = 0
            alien11_health_bar.hideturtle()
            alien11.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien11_death = 1

        if alien11_hit_delay == 9:
            alien11_hit_delay = 0

        if 1 <= alien11_hit_delay < 9:
            alien11_hit_delay = alien11_hit_delay + 1

        if (player_head_laser.distance(alien11) < 112 and ((alien11.xcor() - 15 < player_head_laser.xcor() < alien11.xcor() + 15) or yellow_power_up_active == 1)) and alien11_health == 2 and alien11_death == 0 and alien11.isvisible() and player_head_laser.isvisible() and alien11_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien11_health = 1
            alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien11_hit_delay = 1

        if alien11_hit_delay == 9:
            alien11_hit_delay = 0

        if 1 <= alien11_hit_delay < 9:
            alien11_hit_delay = alien11_hit_delay + 1

        if (player_head_laser.distance(alien11) < 112 and ((alien11.xcor() - 15 < player_head_laser.xcor() < alien11.xcor() + 15) or yellow_power_up_active == 1)) and alien11_health == 3 and alien11_death == 0 and alien11.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien11_health = 2
            alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien11_hit_delay = 1

        if 4.5 <= alien12_death < 5:
            alien12.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien12.goto(random.randint(-900, -690), -93)
                alien12_health_bar.goto(alien12.xcor(), 30)
            if alien_random == 2:
                alien12.goto(random.randint(690, 900), -93)
                alien12_health_bar.goto(alien12.xcor(), 30)
            alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien12_health = 3
            alien12.showturtle()
            alien12_health_bar.showturtle()
            alien12_death = 0

        if 3 <= alien12_death < 4.5:
            alien12_death = alien12_death + 0.1

        if 2 <= alien12_death < 3:
            alien12.shape("Textures/Explosions/Alien_Death_2.gif")
            alien12_death = 3

        if 1 <= alien12_death < 2:
            alien12_death = alien12_death + 0.1

        if (player_head_laser.distance(alien12) < 112 and ((alien12.xcor() - 15 < player_head_laser.xcor() < alien12.xcor() + 15) or yellow_power_up_active == 1)) and alien12_health == 1 and alien12_death == 0 and alien12.isvisible() and player_head_laser.isvisible() and alien12_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 8
            else:
                score = score + 4
            ak12 = ak12 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                big_aliens_killed = big_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[20] = str(big_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien12_health = 0
            alien12_health_bar.hideturtle()
            alien12.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien12_death = 1

        if alien12_hit_delay == 9:
            alien12_hit_delay = 0

        if 1 <= alien12_hit_delay < 9:
            alien12_hit_delay = alien12_hit_delay + 1

        if (player_head_laser.distance(alien12) < 112 and ((alien12.xcor() - 15 < player_head_laser.xcor() < alien12.xcor() + 15) or yellow_power_up_active == 1)) and alien12_health == 2 and alien12_death == 0 and alien12.isvisible() and player_head_laser.isvisible() and alien12_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien12_health = 1
            alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien12_hit_delay = 1

        if alien12_hit_delay == 9:
            alien12_hit_delay = 0

        if 1 <= alien12_hit_delay < 9:
            alien12_hit_delay = alien12_hit_delay + 1

        if (player_head_laser.distance(alien12) < 112 and ((alien12.xcor() - 15 < player_head_laser.xcor() < alien12.xcor() + 15) or yellow_power_up_active == 1)) and alien12_health == 3 and alien12_death == 0 and alien12.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien12_health = 2
            alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien12_hit_delay = 1

        if 4.5 <= alien13_death < 5:
            alien13.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien13.goto(random.randint(-900, -690), -93)
                alien13_health_bar.goto(alien13.xcor(), 30)
            if alien_random == 2:
                alien13.goto(random.randint(690, 900), -93)
                alien13_health_bar.goto(alien13.xcor(), 30)
            alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien13_health = 3
            alien13.showturtle()
            alien13_health_bar.showturtle()
            alien13_death = 0

        if 3 <= alien13_death < 4.5:
            alien13_death = alien13_death + 0.1

        if 2 <= alien13_death < 3:
            alien13.shape("Textures/Explosions/Alien_Death_2.gif")
            alien13_death = 3

        if 1 <= alien13_death < 2:
            alien13_death = alien13_death + 0.1

        if (player_head_laser.distance(alien13) < 112 and ((alien13.xcor() - 15 < player_head_laser.xcor() < alien13.xcor() + 15) or yellow_power_up_active == 1)) and alien13_health == 1 and alien13_death == 0 and alien13.isvisible() and player_head_laser.isvisible() and alien13_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 8
            else:
                score = score + 4
            ak13 = ak13 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                big_aliens_killed = big_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[20] = str(big_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien13_health = 0
            alien13_health_bar.hideturtle()
            alien13.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien13_death = 1

        if alien13_hit_delay == 9:
            alien13_hit_delay = 0

        if 1 <= alien13_hit_delay < 9:
            alien13_hit_delay = alien13_hit_delay + 1

        if (player_head_laser.distance(alien13) < 112 and ((alien13.xcor() - 15 < player_head_laser.xcor() < alien13.xcor() + 15) or yellow_power_up_active == 1)) and alien13_health == 2 and alien13_death == 0 and alien13.isvisible() and player_head_laser.isvisible() and alien13_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien13_health = 1
            alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien13_hit_delay = 1

        if alien13_hit_delay == 9:
            alien13_hit_delay = 0

        if 1 <= alien13_hit_delay < 9:
            alien13_hit_delay = alien13_hit_delay + 1

        if (player_head_laser.distance(alien13) < 112 and ((alien13.xcor() - 15 < player_head_laser.xcor() < alien13.xcor() + 15) or yellow_power_up_active == 1)) and alien13_health == 3 and alien13_death == 0 and alien13.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien13_health = 2
            alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien13_hit_delay = 1

        if 4.5 <= alien14_death < 5:
            alien14.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien14.goto(random.randint(-900, -690), -93)
                alien14_health_bar.goto(alien14.xcor(), 30)
            if alien_random == 2:
                alien14.goto(random.randint(690, 900), -93)
                alien14_health_bar.goto(alien14.xcor(), 30)
            alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien14_health = 3
            alien14.showturtle()
            alien14_health_bar.showturtle()
            alien14_death = 0

        if 3 <= alien14_death < 4.5:
            alien14_death = alien14_death + 0.1

        if 2 <= alien14_death < 3:
            alien14.shape("Textures/Explosions/Alien_Death_2.gif")
            alien14_death = 3

        if 1 <= alien14_death < 2:
            alien14_death = alien14_death + 0.1

        if (player_head_laser.distance(alien14) < 112 and ((alien14.xcor() - 15 < player_head_laser.xcor() < alien14.xcor() + 15) or yellow_power_up_active == 1)) and alien14_health == 1 and alien14_death == 0 and alien14.isvisible() and player_head_laser.isvisible() and alien14_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 8
            else:
                score = score + 4
            ak14 = ak14 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                big_aliens_killed = big_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[20] = str(big_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien14_health = 0
            alien14_health_bar.hideturtle()
            alien14.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien14_death = 1

        if alien14_hit_delay == 9:
            alien14_hit_delay = 0

        if 1 <= alien14_hit_delay < 9:
            alien14_hit_delay = alien14_hit_delay + 1

        if (player_head_laser.distance(alien14) < 112 and ((alien14.xcor() - 15 < player_head_laser.xcor() < alien14.xcor() + 15) or yellow_power_up_active == 1)) and alien14_health == 2 and alien14_death == 0 and alien14.isvisible() and player_head_laser.isvisible() and alien14_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien14_health = 1
            alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien14_hit_delay = 1

        if alien14_hit_delay == 9:
            alien14_hit_delay = 0

        if 1 <= alien14_hit_delay < 9:
            alien14_hit_delay = alien14_hit_delay + 1

        if (player_head_laser.distance(alien14) < 112 and ((alien14.xcor() - 15 < player_head_laser.xcor() < alien14.xcor() + 15) or yellow_power_up_active == 1)) and alien14_health == 3 and alien14_death == 0 and alien14.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien14_health = 2
            alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien14_hit_delay = 1

        if 4.5 <= alien15_death < 5:
            alien15.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien15.goto(random.randint(-900, -690), -93)
                alien15_health_bar.goto(alien15.xcor(), 30)
            if alien_random == 2:
                alien15.goto(random.randint(690, 900), -93)
                alien15_health_bar.goto(alien15.xcor(), 30)
            alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien15_health = 3
            alien15.showturtle()
            alien15_health_bar.showturtle()
            alien15_death = 0

        if 3 <= alien15_death < 4.5:
            alien15_death = alien15_death + 0.1

        if 2 <= alien15_death < 3:
            alien15.shape("Textures/Explosions/Alien_Death_2.gif")
            alien15_death = 3

        if 1 <= alien15_death < 2:
            alien15_death = alien15_death + 0.1

        if (player_head_laser.distance(alien15) < 112 and ((alien15.xcor() - 15 < player_head_laser.xcor() < alien15.xcor() + 15) or yellow_power_up_active == 1)) and alien15_health == 1 and alien15_death == 0 and alien15.isvisible() and player_head_laser.isvisible() and alien15_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 8
            else:
                score = score + 4
            ak15 = ak15 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Alien_Death_Sound.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                big_aliens_killed = big_aliens_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[20] = str(big_aliens_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien15_health = 0
            alien15_health_bar.hideturtle()
            alien15.shape("Textures/Explosions/Alien_Death_1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien15_death = 1

        if alien15_hit_delay == 9:
            alien15_hit_delay = 0

        if 1 <= alien15_hit_delay < 9:
            alien15_hit_delay = alien15_hit_delay + 1

        if (player_head_laser.distance(alien15) < 112 and ((alien15.xcor() - 15 < player_head_laser.xcor() < alien15.xcor() + 15) or yellow_power_up_active == 1)) and alien15_health == 2 and alien15_death == 0 and alien15.isvisible() and player_head_laser.isvisible() and alien15_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien15_health = 1
            alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien15_hit_delay = 1

        if alien15_hit_delay == 9:
            alien15_hit_delay = 0

        if 1 <= alien15_hit_delay < 9:
            alien15_hit_delay = alien15_hit_delay + 1

        if (player_head_laser.distance(alien15) < 112 and ((alien15.xcor() - 15 < player_head_laser.xcor() < alien15.xcor() + 15) or yellow_power_up_active == 1)) and alien15_health == 3 and alien15_death == 0 and alien15.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Alien_Hit_Sound.wav", winsound.SND_ASYNC)
            alien15_health = 2
            alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien15_hit_delay = 1

        if 4.5 <= alien_boss_death < 5:
            alien_boss.hideturtle()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien_boss.goto(random.randint(-900, -690), -20)
                alien_boss_health_bar.goto(alien_boss.xcor(), 50)
            if alien_random == 2:
                alien_boss.goto(random.randint(690, 900), -20)
                alien_boss_health_bar.goto(alien_boss.xcor(), 50)
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            alien_boss.shape("Textures/Aliens/Alien_Boss.gif")
            alien_boss_health = 10
            alien_boss.showturtle()
            alien_boss_health_bar.showturtle()
            alien_boss_death = 0

        if 3 <= alien_boss_death < 4.5:
            alien_boss_death = alien_boss_death + 0.1

        if 2 <= alien_boss_death < 3:
            alien_boss.shape("Textures/Explosions/Explosion2.gif")
            alien_boss_death = 3

        if 1 <= alien_boss_death < 2:
            alien_boss_death = alien_boss_death + 0.1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 1 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 100
            else:
                score = score + 50
            ak_boss = ak_boss + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                ufos_killed = ufos_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[18] = str(ufos_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien_boss_health = 0
            alien_boss_health_bar.hideturtle()
            alien_boss.shape("Textures/Explosions/Explosion1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_death = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 2 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 6
            else:
                score = score + 3
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 1
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 3 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 6
            else:
                score = score + 3
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 2
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 4 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 3
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 5 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 4
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 6 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 5
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 7 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 6
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 8 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 7
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 9 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible() and alien_boss_hit_delay == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 8
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        if 99.9 < alien_boss_hit_delay < 100.1:
            alien_boss_hit_delay = 0

        if 1 <= alien_boss_hit_delay < 100:
            alien_boss_hit_delay = alien_boss_hit_delay + 1

        if (player_head_laser.distance(alien_boss) < 72 and (alien_boss.ycor() - 53 < player_head_laser.ycor() < alien_boss.ycor() + 53)) and alien_boss_health == 10 and alien_boss_death == 0 and alien_boss.isvisible() and player_head_laser.isvisible():
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            alien_boss_health = 9
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            player_head_laser.hideturtle()
            if red_power_up_active == 0:
                laser_update = laser_update + 1
            alien_boss_hit_delay = 1

        # Lines 5405 - 5588 are for what happens when the player dies
        # When the player dies, the game basically resets

        if head_death_animation == 1:
            if 0 < player_update < 2:
                player_update = player_update + 0.125
            elif 2 <= player_update < 3:
                player_update = 3
            elif player_update == 3:
                player_head.shape("Textures/Explosions/Player_Death_2.gif")
                player_update = player_update + 0.125
            elif 3 < player_update < 5:
                player_update = player_update + 0.125
            elif 5 <= player_update < 6:
                player_update = 6
            elif player_update == 6:
                player_health = 10
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
                player_head.goto(0, -150)
                oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
                player_gun.goto(player_head.xcor(), player_head.ycor() + 12)
                player_head.shape("Textures/Player/Player_Head_Still_Right.gif")
                player_head.direction = "stop"
                player_update = 0
                head_death_animation = 0
                death_occurring = 0.015

        if player_health == 0 and death_occurring == 0 and god_mode == 0 and head_death_animation != 1:
            player_head.shape("Textures/Explosions/Player_Death_1.gif")
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Player_Death_Sound.wav", winsound.SND_ASYNC)
            score = 0
            ak1 = 0
            ak2 = 0
            ak3 = 0
            ak4 = 0
            ak5 = 0
            ak6 = 0
            ak7 = 0
            ak8 = 0
            ak9 = 0
            ak10 = 0
            ak11 = 0
            ak12 = 0
            ak13 = 0
            ak14 = 0
            ak15 = 0
            ak_boss = 0
            if god_mode == 0:
                alien_deaths = alien_deaths + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[26] = str(alien_deaths) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien1.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien1.goto(random.randint(690, 900), -150)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien2.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien2.goto(random.randint(690, 900), -150)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien3.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien3.goto(random.randint(690, 900), -150)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien4.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien4.goto(random.randint(690, 900), -150)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien5.goto(random.randint(-900, -690), -150)
            if alien_random == 2:
                alien5.goto(random.randint(690, 900), -150)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien6.goto(random.randint(-900, -690), -130)
                alien6_health_bar.goto(alien6.xcor(), -45)
            if alien_random == 2:
                alien6.goto(random.randint(690, 900), -130)
                alien6_health_bar.goto(alien6.xcor(), -45)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien7.goto(random.randint(-900, -690), -130)
                alien7_health_bar.goto(alien7.xcor(), -45)
            if alien_random == 2:
                alien7.goto(random.randint(690, 900), -130)
                alien7_health_bar.goto(alien7.xcor(), -45)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien8.goto(random.randint(-900, -690), -130)
                alien8_health_bar.goto(alien8.xcor(), -45)
            if alien_random == 2:
                alien8.goto(random.randint(690, 900), -130)
                alien8_health_bar.goto(alien8.xcor(), -45)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien9.goto(random.randint(-900, -690), -130)
                alien9_health_bar.goto(alien9.xcor(), -45)
            if alien_random == 2:
                alien9.goto(random.randint(690, 900), -130)
                alien9_health_bar.goto(alien9.xcor(), -45)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien10.goto(random.randint(-900, -690), -130)
                alien10_health_bar.goto(alien10.xcor(), -45)
            if alien_random == 2:
                alien10.goto(random.randint(690, 900), -130)
                alien10_health_bar.goto(alien10.xcor(), -45)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien11.goto(random.randint(-900, -690), -93)
                alien11_health_bar.goto(alien11.xcor(), 30)
            if alien_random == 2:
                alien11.goto(random.randint(690, 900), -93)
                alien11_health_bar.goto(alien11.xcor(), 30)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien12.goto(random.randint(-900, -690), -93)
                alien12_health_bar.goto(alien12.xcor(), 30)
            if alien_random == 2:
                alien12.goto(random.randint(690, 900), -93)
                alien12_health_bar.goto(alien12.xcor(), 30)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien13.goto(random.randint(-900, -690), -93)
                alien13_health_bar.goto(alien13.xcor(), 30)
            if alien_random == 2:
                alien13.goto(random.randint(690, 900), -93)
                alien13_health_bar.goto(alien13.xcor(), 30)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien14.goto(random.randint(-900, -690), -93)
                alien14_health_bar.goto(alien14.xcor(), 30)
            if alien_random == 2:
                alien14.goto(random.randint(690, 900), -93)
                alien14_health_bar.goto(alien14.xcor(), 30)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien15.goto(random.randint(-900, -690), -93)
                alien15_health_bar.goto(alien15.xcor(), 30)
            if alien_random == 2:
                alien15.goto(random.randint(690, 900), -93)
                alien15_health_bar.goto(alien15.xcor(), 30)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                alien_boss.goto(random.randint(-900, -690), -20)
                alien_boss_health_bar.goto(alien_boss.xcor(), 50)
                alien_boss_laser.goto(alien_boss.xcor(), -90)
            if alien_random == 2:
                alien_boss.goto(random.randint(690, 900), -20)
                alien_boss_health_bar.goto(alien_boss.xcor(), 50)
                alien_boss_laser.goto(alien_boss.xcor(), -90)
            alien6_health = 2
            alien6_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien7_health = 2
            alien7_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien8_health = 2
            alien8_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien9_health = 2
            alien9_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien10_health = 2
            alien10_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            alien11_health = 3
            alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien12_health = 3
            alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien13_health = 3
            alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien14_health = 3
            alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien15_health = 3
            alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
            alien_boss_health = 10
            alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            oxygen_tank.hideturtle()
            player_gun.hideturtle()
            player_update = 0.125
            head_death_animation = 1

        # Lines 5594 - 6175 are for what happens when the player gets hit
        # The player must get hit 10 times in order to die
        # This code decreases the players health by 1 and updates the health bars texture when the player gets hit

        if 0 < death_occurring < 1:
            death_occurring = death_occurring + 0.015
        else:
            death_occurring = 0

        if death_occurring == 0 and player_health != 0 and (alien1.distance(player_head) < 70 and alien1.xcor() - 12.5 < player_head.xcor() < alien1.xcor() + 12.5) and god_mode == 0 and player_update == 0 and alien1_death == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien2.distance(player_head) < 70 and alien2.xcor() - 12.5 < player_head.xcor() < alien2.xcor() + 12.5) and god_mode == 0 and player_update == 0 and alien2_death == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien3.distance(player_head) < 70 and alien3.xcor() - 12.5 < player_head.xcor() < alien3.xcor() + 12.5) and god_mode == 0 and player_update == 0 and alien3_death == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien4.distance(player_head) < 70 and alien4.xcor() - 12.5 < player_head.xcor() < alien4.xcor() + 12.5) and alien4.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien5.distance(player_head) < 70 and alien5.xcor() - 12.5 < player_head.xcor() < alien5.xcor() + 12.5) and alien5.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien6.distance(player_head) < 100 and alien6.xcor() - 15 < player_head.xcor() < alien6.xcor() + 15) and alien6.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien7.distance(player_head) < 100 and alien7.xcor() - 15 < player_head.xcor() < alien7.xcor() + 15) and alien7.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien8.distance(player_head) < 100 and alien8.xcor() - 15 < player_head.xcor() < alien8.xcor() + 15) and alien8.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien9.distance(player_head) < 100 and alien9.xcor() - 15 < player_head.xcor() < alien9.xcor() + 15) and alien9.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien10.distance(player_head) < 100 and alien10.xcor() - 15 < player_head.xcor() < alien10.xcor() + 15) and alien10.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien11.distance(player_head) < 160 and alien11.xcor() - 18 < player_head.xcor() < alien11.xcor() + 18) and alien11.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien12.distance(player_head) < 160 and alien12.xcor() - 18 < player_head.xcor() < alien12.xcor() + 18) and alien12.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien13.distance(player_head) < 160 and alien13.xcor() - 18 < player_head.xcor() < alien13.xcor() + 18) and alien13.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien14.distance(player_head) < 160 and alien14.xcor() - 18 < player_head.xcor() < alien14.xcor() + 18) and alien14.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien15.distance(player_head) < 160 and alien15.xcor() - 18 < player_head.xcor() < alien15.xcor() + 18) and alien15.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and (alien_boss.distance(player_head) < 53 and alien_boss.ycor() - 18 < player_head.ycor() < alien_boss.ycor() + 18) and alien_boss.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015

        if death_occurring == 0 and player_health != 0 and alien_boss_laser.distance(player_head) < 25 and alien_boss_laser.isvisible() and god_mode == 0 and player_update == 0:
            player_health = player_health - 1
            if god_mode == 0:
                damage_taken = damage_taken + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[28] = str(damage_taken) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            if player_hit_sound == 1:
                winsound.PlaySound("Sound/Player_Hit_Sound.wav", winsound.SND_ASYNC)
            if player_health == 9:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if player_health == 8:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if player_health == 7:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if player_health == 6:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if player_health == 5:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if player_health == 4:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if player_health == 3:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if player_health == 2:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if player_health == 1:
                player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if player_health != 0:
                death_occurring = 0.015
    else:

        # Lines 6181 - 6323 are for what happens when alien mode is off
        # The game is basically reset to its default state

        ground.hideturtle()
        earth.hideturtle()
        space_ship.hideturtle()
        player_head.hideturtle()
        player_head.goto(0, -150)
        player_head.direction = "stop"
        player_head.shape("Textures/Player/Player_Head_Still_Right.gif")
        oxygen_tank.hideturtle()
        oxygen_tank.goto(player_head.xcor() - 30.5, player_head.ycor() + 11)
        player_gun.hideturtle()
        player_gun.goto(player_head.xcor(), player_head.ycor() + 12)
        player_gun.direction = "stop"
        player_gun.shape("Textures/Gun/Player_Gun_Right.gif")
        player_head_laser.hideturtle()
        player_head_laser.goto(player_gun.xcor(), player_gun.ycor())
        laser_direction = 0
        direction = 0
        player_health = 10
        player_update = 0
        head_death_animation = 0
        death_occurring = 0
        alien_random = 0
        laser_update = 0
        alien1_death = 0
        alien2_death = 0
        alien3_death = 0
        alien4_death = 0
        alien5_death = 0
        alien6_death = 0
        alien7_death = 0
        alien8_death = 0
        alien9_death = 0
        alien10_death = 0
        alien11_death = 0
        alien12_death = 0
        alien13_death = 0
        alien14_death = 0
        alien15_death = 0
        alien_boss_death = 0
        ak1 = 0
        ak2 = 0
        ak3 = 0
        ak4 = 0
        ak5 = 0
        ak6 = 0
        ak7 = 0
        ak8 = 0
        ak9 = 0
        ak10 = 0
        ak11 = 0
        ak12 = 0
        ak13 = 0
        ak14 = 0
        ak15 = 0
        ak_boss = 0
        alien1.hideturtle()
        alien2.hideturtle()
        alien3.hideturtle()
        player_head_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        player_head_health_bar.hideturtle()
        player_head_health_bar.goto(0, 0)
        alien1.direction = "stop"
        alien2.direction = "stop"
        alien3.direction = "stop"
        alien4.direction = "stop"
        alien5.direction = "stop"
        alien6.direction = "stop"
        alien7.direction = "stop"
        alien8.direction = "stop"
        alien9.direction = "stop"
        alien10.direction = "stop"
        alien11.direction = "stop"
        alien12.direction = "stop"
        alien13.direction = "stop"
        alien14.direction = "stop"
        alien15.direction = "stop"
        alien_boss.direction = "stop"
        alien1.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        alien2.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        alien3.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        alien4.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        alien5.shape("Textures/Aliens/Alien_Still_Right(1-5).gif")
        alien6.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        alien6_health = 2
        alien6_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        alien7.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        alien7_health = 2
        alien7_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        alien8.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        alien8_health = 2
        alien8_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        alien9.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        alien9_health = 2
        alien9_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        alien10.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        alien10_health = 2
        alien10_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        alien11.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
        alien11_health = 3
        alien11_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
        alien12.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
        alien12_health = 3
        alien12_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
        alien13.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
        alien13_health = 3
        alien13_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
        alien14.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
        alien14_health = 3
        alien14_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
        alien15.shape("Textures/Aliens/Alien_Still_Right(11-15).gif")
        alien15_health = 3
        alien15_health_bar.shape("Textures/Health_Bars/HealthBar_3.3.gif")
        alien_boss.shape("Textures/Aliens/Alien_Boss.gif")
        alien_boss_health = 10
        alien_boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        alien1.goto(-800, -150)
        alien2.goto(-700, -150)
        alien3.goto(800, -150)
        alien4.goto(700, -150)
        alien5.goto(750, -150)
        alien6.goto(850, -130)
        alien6_health_bar.goto(850, -45)
        alien7.goto(-850, -130)
        alien7_health_bar.goto(-850, -45)
        alien8.goto(900, -130)
        alien8_health_bar.goto(900, -45)
        alien9.goto(-900, -130)
        alien9_health_bar.goto(-900, -45)
        alien10.goto(725, -130)
        alien10_health_bar.goto(725, -45)
        alien11.goto(-725, -93)
        alien11_health_bar.goto(-725, 30)
        alien12.goto(775, -93)
        alien12_health_bar.goto(775, 30)
        alien13.goto(-775, -93)
        alien13_health_bar.goto(-775, 30)
        alien14.goto(825, -93)
        alien14_health_bar.goto(825, 30)
        alien15.goto(-825, -93)
        alien15_health_bar.goto(-825, 30)
        alien_boss.goto(875, -20)
        alien_boss_laser.goto(877, -90)
        alien_boss_health_bar.goto(875, 50)

    # Lines 6328 - 6409 is for what happens when the stats mode is toggled on or off
    # This basically includes making the stats visible when the mode is on and taking them off the screen when the mode is turned off

    if mode == "Stats":
        go_back_button.goto(-537, 320)
        if tick_update % 3 == 0:
            go_back_button.clear()
            go_back_button.write("Main Menu", align="center", font=("Courier", 24, "normal"))
        go_back_button_frame.shapesize(1.5, 9.5)
        go_back_button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
        go_back_button_frame.showturtle()
        go_back_button_frame.goto(-537, 339)
        stats_label.clear()
        stats_label.write("Statistics", align="center", font=("Courier", 72, "bold"))
        if tick_update % 4 == 0:
            classic_mode_label.clear()
            classic_mode_label.write("Machine Mode", align="center", font=("Courier", 48, "bold"))
            alien_mode_label.clear()
            alien_mode_label.write("Alien Mode", align="center", font=("Courier", 48, "bold"))
            classic_high_score_text.clear()
            classic_high_score_text.write("High Score: {}".format(high_score_machine_war), align="center", font=("Courier", 24, "normal"))
            bosses_killed_text.clear()
            bosses_killed_text.write("Bosses Killed: {}".format(bosses_killed), align="center", font=("Courier", 24, "normal"))
            red_bots_killed_text.clear()
            red_bots_killed_text.write("Red Bots Killed: {}".format(red_bots_killed), align="center", font=("Courier", 24, "normal"))
            yellow_bots_killed_text.clear()
            yellow_bots_killed_text.write("Yellow Bots Killed: {}".format(yellow_bots_killed), align="center", font=("Courier", 24, "normal"))
            blue_bots_killed_text.clear()
            blue_bots_killed_text.write("Blue Bots Killed: {}".format(blue_bots_killed), align="center", font=("Courier", 24, "normal"))
            classic_deaths_text.clear()
            classic_deaths_text.write("Deaths: {}".format(classic_deaths), align="center", font=("Courier", 24, "normal"))
            classic_lasers_fired_text.clear()
            classic_lasers_fired_text.write("Lasers Fired: {}".format(classic_lasers_fired), align="center", font=("Courier", 24, "normal"))
            classic_power_ups_picked_up_text.clear()
            classic_power_ups_picked_up_text.write("Power Ups Picked Up: {}".format(classic_power_ups_picked_up), align="center", font=("Courier", 24, "normal"))
            alien_high_score_text.clear()
            alien_high_score_text.write("High Score: {}".format(high_score_alien_mode), align="center", font=("Courier", 24, "normal"))
            ufos_killed_text.clear()
            ufos_killed_text.write("UFOs Killed: {}".format(ufos_killed), align="center", font=("Courier", 24, "normal"))
            big_aliens_killed_text.clear()
            big_aliens_killed_text.write("Big Aliens Killed: {}".format(big_aliens_killed), align="center", font=("Courier", 24, "normal"))
            medium_aliens_killed_text.clear()
            medium_aliens_killed_text.write("Medium Aliens Killed: {}".format(medium_aliens_killed), align="center", font=("Courier", 24, "normal"))
            small_aliens_killed_text.clear()
            small_aliens_killed_text.write("Small Aliens Killed: {}".format(small_aliens_killed), align="center", font=("Courier", 24, "normal"))
            alien_deaths_text.clear()
            alien_deaths_text.write("Deaths: {}".format(alien_deaths), align="center", font=("Courier", 24, "normal"))
            damage_taken_text.clear()
            damage_taken_text.write("Damage Taken: {}".format(damage_taken), align="center", font=("Courier", 24, "normal"))
            alien_lasers_fired_text.clear()
            alien_lasers_fired_text.write("Lasers Fired: {}".format(alien_lasers_fired), align="center", font=("Courier", 24, "normal"))
            jumps_text.clear()
            jumps_text.write("Jumps: {}".format(jumps), align="center", font=("Courier", 24, "normal"))
            alien_power_ups_picked_up_text.clear()
            alien_power_ups_picked_up_text.write("Power Ups Picked Up: {}".format(alien_power_ups_picked_up), align="center", font=("Courier", 24, "normal"))
        if stats_label.xcor() < -120:
            stats_moving = 1
        if stats_label.xcor() > 120:
            stats_moving = -1
        if stats_moving == 1:
            stats_label.setx(stats_label.xcor() + 5)
        if stats_moving == -1:
            stats_label.setx(stats_label.xcor() - 5)
    else:
        stats_label.clear()
        classic_mode_label.clear()
        alien_mode_label.clear()
        classic_high_score_text.clear()
        bosses_killed_text.clear()
        red_bots_killed_text.clear()
        yellow_bots_killed_text.clear()
        blue_bots_killed_text.clear()
        classic_deaths_text.clear()
        classic_lasers_fired_text.clear()
        classic_power_ups_picked_up_text.clear()
        alien_high_score_text.clear()
        ufos_killed_text.clear()
        big_aliens_killed_text.clear()
        medium_aliens_killed_text.clear()
        small_aliens_killed_text.clear()
        alien_deaths_text.clear()
        damage_taken_text.clear()
        alien_lasers_fired_text.clear()
        jumps_text.clear()
        alien_power_ups_picked_up_text.clear()

    # Lines 6413 - 6590 are for when the settings mode is toggled on or off

    if mode == "Settings":
        go_back_button.goto(315.5, -307)
        if tick_update % 5 == 0:
            go_back_button.clear()
            go_back_button.write("Main Menu", align="center", font=("Courier", 28, "bold"))
        go_back_button_frame.shapesize(3, 25)
        go_back_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        go_back_button_frame.showturtle()
        go_back_button_frame.goto(315.5, -285)
        if tick_update % 5 == 0:
            control_toggle_button.clear()
            control_toggle_button.write("Controls", align="center", font=("Courier", 28, "bold"))
        control_toggle_button_frame.showturtle()
        button_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            button_sound_button.clear()
            button_sound_button.write("Button Sound:", align="center", font=("Courier", 28, "normal"))
        player_shooting_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            player_shooting_sound_button.clear()
            player_shooting_sound_button.write("Player Shooting Sound:", align="center", font=("Courier", 28, "normal"))
        enemy_shooting_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            enemy_shooting_sound_button.clear()
            enemy_shooting_sound_button.write("Enemy Shooting Sound:", align="center", font=("Courier", 28, "normal"))
        player_death_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            player_death_sound_button.clear()
            player_death_sound_button.write("Player Death Sound:", align="center", font=("Courier", 28, "normal"))
        enemy_death_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            enemy_death_sound_button.clear()
            enemy_death_sound_button.write("Enemy Death Sound:", align="center", font=("Courier", 28, "normal"))
        player_hit_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            player_hit_sound_button.clear()
            player_hit_sound_button.write("Player Hit Sound:", align="center", font=("Courier", 28, "normal"))
        enemy_hit_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            enemy_hit_sound_button.clear()
            enemy_hit_sound_button.write("Enemy Hit Sound:", align="center", font=("Courier", 28, "normal"))
        power_up_pickup_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            power_up_pickup_sound_button.clear()
            power_up_pickup_sound_button.write("Power Up Pickup Sound:", align="center", font=("Courier", 28, "normal"))
        power_up_spawn_sound_button_frame.showturtle()
        if tick_update % 5 == 0:
            power_up_spawn_sound_button.clear()
            power_up_spawn_sound_button.write("Power Up Spawn Sound:", align="center", font=("Courier", 28, "normal"))
        settings_label.clear()
        settings_label.write("Settings", align="center", font=("Courier", 72, "bold"))
        if button_sound == 1:
            button_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                button_sound_button_indicator.clear()
                button_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            button_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                button_sound_button_indicator.clear()
                button_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if player_shooting_sound == 1:
            player_shooting_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                player_shooting_sound_button_indicator.clear()
                player_shooting_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            player_shooting_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                player_shooting_sound_button_indicator.clear()
                player_shooting_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if enemy_shooting_sound == 1:
            enemy_shooting_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                enemy_shooting_sound_button_indicator.clear()
                enemy_shooting_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            enemy_shooting_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                enemy_shooting_sound_button_indicator.clear()
                enemy_shooting_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if player_death_sound == 1:
            player_death_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                player_death_sound_button_indicator.clear()
                player_death_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            player_death_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                player_death_sound_button_indicator.clear()
                player_death_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if enemy_death_sound == 1:
            enemy_death_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                enemy_death_sound_button_indicator.clear()
                enemy_death_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            enemy_death_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                enemy_death_sound_button_indicator.clear()
                enemy_death_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if player_hit_sound == 1:
            player_hit_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                player_hit_sound_button_indicator.clear()
                player_hit_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            player_hit_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                player_hit_sound_button_indicator.clear()
                player_hit_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if enemy_hit_sound == 1:
            enemy_hit_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                enemy_hit_sound_button_indicator.clear()
                enemy_hit_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            enemy_hit_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                enemy_hit_sound_button_indicator.clear()
                enemy_hit_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if power_up_pickup_sound == 1:
            power_up_pickup_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                power_up_pickup_sound_button_indicator.clear()
                power_up_pickup_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            power_up_pickup_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                power_up_pickup_sound_button_indicator.clear()
                power_up_pickup_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if power_up_spawn_sound == 1:
            power_up_spawn_sound_button_indicator.color("green")
            if tick_update % 3 == 0:
                power_up_spawn_sound_button_indicator.clear()
                power_up_spawn_sound_button_indicator.write("On", align="center", font=("Courier", 28, "bold"))
        else:
            power_up_spawn_sound_button_indicator.color("red")
            if tick_update % 3 == 0:
                power_up_spawn_sound_button_indicator.clear()
                power_up_spawn_sound_button_indicator.write("Off", align="center", font=("Courier", 28, "bold"))
        if settings_label.xcor() < -120:
            settings_moving = 1
        if settings_label.xcor() > 120:
            settings_moving = -1
        if settings_moving == 1:
            settings_label.setx(settings_label.xcor() + 5)
        if settings_moving == -1:
            settings_label.setx(settings_label.xcor() - 5)
    else:
        settings_label.clear()
        button_sound_button_frame.hideturtle()
        button_sound_button.clear()
        button_sound_button_indicator.clear()
        player_shooting_sound_button_frame.hideturtle()
        player_shooting_sound_button.clear()
        player_shooting_sound_button_indicator.clear()
        enemy_shooting_sound_button_frame.hideturtle()
        enemy_shooting_sound_button.clear()
        enemy_shooting_sound_button_indicator.clear()
        player_death_sound_button_frame.hideturtle()
        player_death_sound_button.clear()
        player_death_sound_button_indicator.clear()
        enemy_death_sound_button_frame.hideturtle()
        enemy_death_sound_button.clear()
        enemy_death_sound_button_indicator.clear()
        player_hit_sound_button_frame.hideturtle()
        player_hit_sound_button.clear()
        player_hit_sound_button_indicator.clear()
        enemy_hit_sound_button_frame.hideturtle()
        enemy_hit_sound_button.clear()
        enemy_hit_sound_button_indicator.clear()
        power_up_pickup_sound_button_frame.hideturtle()
        power_up_pickup_sound_button.clear()
        power_up_pickup_sound_button_indicator.clear()
        power_up_spawn_sound_button_frame.hideturtle()
        power_up_spawn_sound_button.clear()
        power_up_spawn_sound_button_indicator.clear()

# Lines 6594 - 6646 are for what happens when controls mode is toggled on or off

    if mode == "Controls":
        go_back_button.goto(315.5, -307)
        if tick_update % 5 == 0:
            go_back_button.clear()
            go_back_button.write("Main Menu", align="center", font=("Courier", 28, "bold"))
        go_back_button_frame.shapesize(3, 25)
        go_back_button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        go_back_button_frame.showturtle()
        go_back_button_frame.goto(315.5, -285)

        if tick_update % 5 == 0:
            control_toggle_button.clear()
            control_toggle_button.write("Settings", align="center", font=("Courier", 28, "bold"))
        control_toggle_button_frame.showturtle()

        controls_label.clear()
        controls_label.write("Controls", align="center", font=("Courier", 72, "bold"))

        if controls_label.xcor() < -120:
            controls_moving = 1
        if controls_label.xcor() > 120:
            controls_moving = -1
        if controls_moving == 1:
            controls_label.setx(controls_label.xcor() + 5)
        if controls_moving == -1:
            controls_label.setx(controls_label.xcor() - 5)

        go_right_control_button_frame.showturtle()
        if tick_update % 5 == 0:
            go_right_control_button.clear()
            go_right_control_button.write("Go Right: " + go_right_key, align="center", font=("Courier", 28, "normal"))
        go_left_control_button_frame.showturtle()
        if tick_update % 5 == 0:
            go_left_control_button.clear()
            go_left_control_button.write("Go Left: " + go_left_key, align="center", font=("Courier", 28, "normal"))
        shoot_control_button_frame.showturtle()
        if tick_update % 5 == 0:
            shoot_control_button.clear()
            shoot_control_button.write("Shoot: " + shoot_key, align="center", font=("Courier", 28, "normal"))
        jump_control_button_frame.showturtle()
        if tick_update % 5 == 0:
            jump_control_button.clear()
            jump_control_button.write("Jump: " + jump_key, align="center", font=("Courier", 28, "normal"))
    else:
        controls_label.clear()
        go_right_control_button_frame.hideturtle()
        go_right_control_button.clear()
        go_left_control_button_frame.hideturtle()
        go_left_control_button.clear()
        shoot_control_button_frame.hideturtle()
        shoot_control_button.clear()
        jump_control_button_frame.hideturtle()
        jump_control_button.clear()

    # Lines 6653 - 6715 activate certain functions when certain buttons are clicked
    # The way this works is that the code checks if any of the buttons have yellow text
    # If a button has yellow text, that means that the user is hovering over it and is allowed to click it
    # If the user clicks it, then the button function is activated

    classic_mode_button_color = classic_mode_button.fillcolor()
    alien_mode_button_color = alien_mode_button.fillcolor()
    stats_mode_button_color = stats_mode_button.fillcolor()
    settings_mode_button_color = settings_mode_button.fillcolor()
    go_back_button_color = go_back_button.fillcolor()
    control_toggle_button_color = control_toggle_button.fillcolor()
    button_sound_button_color = button_sound_button.fillcolor()
    player_shooting_sound_button_color = player_shooting_sound_button.fillcolor()
    enemy_shooting_sound_button_color = enemy_shooting_sound_button.fillcolor()
    player_death_sound_button_color = player_death_sound_button.fillcolor()
    enemy_death_sound_button_color = enemy_death_sound_button.fillcolor()
    player_hit_sound_button_color = player_hit_sound_button.fillcolor()
    enemy_hit_sound_button_color = enemy_hit_sound_button.fillcolor()
    power_up_pickup_sound_button_color = power_up_pickup_sound_button.fillcolor()
    power_up_spawn_sound_button_color = power_up_spawn_sound_button.fillcolor()
    go_right_control_button_color = go_right_control_button.fillcolor()
    go_left_control_button_color = go_left_control_button.fillcolor()
    shoot_control_button_color = shoot_control_button.fillcolor()
    jump_control_button_color = jump_control_button.fillcolor()

    if classic_mode_button_color == "yellow" and classic_mode_button_frame.isvisible():
        wn.onscreenclick(launch_classic_mode)
    elif alien_mode_button_color == "yellow" and alien_mode_button_frame.isvisible():
        wn.onscreenclick(launch_alien_mode)
    elif stats_mode_button_color == "yellow" and stats_mode_button_frame.isvisible():
        wn.onscreenclick(launch_stats_mode)
    elif settings_mode_button_color == "yellow" and settings_mode_button_frame.isvisible():
        wn.onscreenclick(launch_settings_mode)
    elif go_back_button_color == "yellow" and go_back_button_frame.isvisible():
        wn.onscreenclick(launch_title_mode)
    elif control_toggle_button_color == "yellow" and control_toggle_button_frame.isvisible():
        if mode == "Settings":
            wn.onscreenclick(launch_controls_mode)
        else:
            wn.onscreenclick(launch_settings_mode)
    elif button_sound_button_color == "yellow" and button_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_button_sound)
    elif player_shooting_sound_button_color == "yellow" and player_shooting_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_player_shooting_sound)
    elif enemy_shooting_sound_button_color == "yellow" and enemy_shooting_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_enemy_shooting_sound)
    elif player_death_sound_button_color == "yellow" and player_death_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_player_death_sound)
    elif enemy_death_sound_button_color == "yellow" and enemy_death_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_enemy_death_sound)
    elif player_hit_sound_button_color == "yellow" and player_hit_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_player_hit_sound)
    elif enemy_hit_sound_button_color == "yellow" and enemy_hit_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_enemy_hit_sound)
    elif power_up_pickup_sound_button_color == "yellow" and power_up_pickup_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_power_up_pickup_sound)
    elif power_up_spawn_sound_button_color == "yellow" and power_up_spawn_sound_button_frame.isvisible():
        wn.onscreenclick(toggle_power_up_spawn_sound)
    elif (go_right_control_button_color == "yellow" or go_right_control_button_color == "orange") and go_right_control_button_frame.isvisible():
        wn.onscreenclick(change_go_right_key)
    elif (go_left_control_button_color == "yellow" or go_left_control_button_color == "orange") and go_left_control_button_frame.isvisible():
        wn.onscreenclick(change_go_left_key)
    elif (shoot_control_button_color == "yellow" or shoot_control_button_color == "orange") and shoot_control_button_frame.isvisible():
        wn.onscreenclick(change_shoot_key)
    elif (jump_control_button_color == "yellow" or jump_control_button_color == "orange") and jump_control_button_frame.isvisible():
        wn.onscreenclick(change_jump_key)
    else:
        wn.onscreenclick(None)

    # The code below checks if there is conflict in the controls configuration and sets the button text color accordingly

    if go_right_key != go_left_key and go_right_key != shoot_key and go_right_key != jump_key:
        go_right_key_alert = 0
    else:
        go_right_key_alert = 1

    if go_left_key != go_right_key and go_left_key != shoot_key and go_left_key != jump_key:
        go_left_key_alert = 0
    else:
        go_left_key_alert = 1

    if shoot_key != go_left_key and shoot_key != go_right_key and shoot_key != jump_key:
        shoot_key_alert = 0
    else:
        shoot_key_alert = 1

    if jump_key != go_left_key and jump_key != shoot_key and jump_key != go_right_key:
        jump_key_alert = 0
    else:
        jump_key_alert = 1

    # This is used for when the player fires his laser in classic mode.
    # If it reaches the edge of the screen, it goes back to him, ready to be fired again

    if mode == "Classic_Mode":
        if laser.ycor() < 360:
            laser.direction = "up"
            if yellow_power_up_active == 0:
                laser.forward(14.5)
            elif yellow_power_up_active == 1:
                laser.forward(43.5)
        else:
            laser.hideturtle()
    else:
        laser.hideturtle()
        laser.goto(0, 360)

    # Lines 6758 - 7273 is used for updating and firing the lasers of all the enemies in classic mode
    # The more powerful enemies have faster moving lasers

    if enemy1.isvisible():
        if green_power_up_active == 0:
            enemy1_laser.showturtle()
            if enemy1_laser.ycor() > -360:
                enemy1_laser.direction = "down"
                YL = enemy1_laser.ycor()
                enemy1_laser.sety(YL - 4.8)
            else:
                x = enemy1.xcor()
                y = enemy1.ycor()
                enemy1_laser.setx(x)
                enemy1_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy1_laser.hideturtle()
            x = enemy1.xcor()
            y = enemy1.ycor()
            enemy1_laser.setx(x)
            enemy1_laser.sety(y - 80)
    else:
        x = enemy1.xcor()
        y = enemy1.ycor()
        enemy1_laser.setx(x)
        enemy1_laser.sety(y - 80)

    if enemy2.isvisible():
        if green_power_up_active == 0:
            enemy2_laser.showturtle()
            if enemy2_laser.ycor() > -360:
                enemy2_laser.direction = "down"
                YL = enemy2_laser.ycor()
                enemy2_laser.sety(YL - 4.8)
            else:
                x = enemy2.xcor()
                y = enemy2.ycor()
                enemy2_laser.setx(x)
                enemy2_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy2_laser.hideturtle()
            x = enemy2.xcor()
            y = enemy2.ycor()
            enemy2_laser.setx(x)
            enemy2_laser.sety(y - 80)
    else:
        x = enemy2.xcor()
        y = enemy2.ycor()
        enemy2_laser.setx(x)
        enemy2_laser.sety(y - 80)

    if enemy3.isvisible():
        if green_power_up_active == 0:
            enemy3_laser.showturtle()
            if enemy3_laser.ycor() > -360:
                enemy3_laser.direction = "down"
                YL = enemy3_laser.ycor()
                enemy3_laser.sety(YL - 4.8)
            else:
                x = enemy3.xcor()
                y = enemy3.ycor()
                enemy3_laser.setx(x)
                enemy3_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy3_laser.hideturtle()
            x = enemy3.xcor()
            y = enemy3.ycor()
            enemy3_laser.setx(x)
            enemy3_laser.sety(y - 80)
    else:
        x = enemy3.xcor()
        y = enemy3.ycor()
        enemy3_laser.setx(x)
        enemy3_laser.sety(y - 80)

    if score >= 5 and mode == "Classic_Mode":
        enemy4.showturtle()
        enemy4_laser.showturtle()
        if green_power_up_active == 0:
            enemy4_laser.showturtle()
            if enemy4_laser.ycor() > -360:
                enemy4_laser.direction = "down"
                YL = enemy4_laser.ycor()
                enemy4_laser.sety(YL - 4.8)
            else:
                x = enemy4.xcor()
                y = enemy4.ycor()
                enemy4_laser.setx(x)
                enemy4_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy4_laser.hideturtle()
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

    if score >= 10 and mode == "Classic_Mode":
        enemy5.showturtle()
        enemy5_laser.showturtle()
        if green_power_up_active == 0:
            enemy5_laser.showturtle()
            if enemy5_laser.ycor() > -360:
                enemy5_laser.direction = "down"
                YL = enemy5_laser.ycor()
                enemy5_laser.sety(YL - 4.8)
            else:
                x = enemy5.xcor()
                y = enemy5.ycor()
                enemy5_laser.setx(x)
                enemy5_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy5_laser.hideturtle()
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

    if score >= 15 and mode == "Classic_Mode":
        enemy6.showturtle()
        enemy6_laser.showturtle()
        if green_power_up_active == 0:
            enemy6_laser.showturtle()
            if enemy6_laser.ycor() > -360:
                enemy6_laser.direction = "down"
                YL = enemy6_laser.ycor()
                enemy6_laser.sety(YL - 8.7)
            else:
                x = enemy6.xcor()
                y = enemy6.ycor()
                enemy6_laser.setx(x)
                enemy6_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy6_laser.hideturtle()
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

    if score >= 20 and mode == "Classic_Mode":
        enemy7.showturtle()
        enemy7_laser.showturtle()
        if green_power_up_active == 0:
            enemy7_laser.showturtle()
            if enemy7_laser.ycor() > -360:
                enemy7_laser.direction = "down"
                YL = enemy7_laser.ycor()
                enemy7_laser.sety(YL - 8.7)
            else:
                x = enemy7.xcor()
                y = enemy7.ycor()
                enemy7_laser.setx(x)
                enemy7_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy7_laser.hideturtle()
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

    if score >= 25 and mode == "Classic_Mode":
        enemy8.showturtle()
        enemy8_laser.showturtle()
        if green_power_up_active == 0:
            enemy8_laser.showturtle()
            if enemy8_laser.ycor() > -360:
                enemy8_laser.direction = "down"
                YL = enemy8_laser.ycor()
                enemy8_laser.sety(YL - 8.7)
            else:
                x = enemy8.xcor()
                y = enemy8.ycor()
                enemy8_laser.setx(x)
                enemy8_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy8_laser.hideturtle()
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

    if score >= 30 and mode == "Classic_Mode":
        enemy9.showturtle()
        enemy9_laser.showturtle()
        if green_power_up_active == 0:
            enemy9_laser.showturtle()
            if enemy9_laser.ycor() > -360:
                enemy9_laser.direction = "down"
                YL = enemy9_laser.ycor()
                enemy9_laser.sety(YL - 8.7)
            else:
                x = enemy9.xcor()
                y = enemy9.ycor()
                enemy9_laser.setx(x)
                enemy9_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy9_laser.hideturtle()
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

    if score >= 35 and mode == "Classic_Mode":
        enemy10.showturtle()
        enemy10_laser.showturtle()
        if green_power_up_active == 0:
            enemy10_laser.showturtle()
            if enemy10_laser.ycor() > -360:
                enemy10_laser.direction = "down"
                YL = enemy10_laser.ycor()
                enemy10_laser.sety(YL - 8.7)
            else:
                x = enemy10.xcor()
                y = enemy10.ycor()
                enemy10_laser.setx(x)
                enemy10_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy10_laser.hideturtle()
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

    if score >= 40 and mode == "Classic_Mode":
        if update11 == 0:
            enemy11.showturtle()
            enemy11_laser.showturtle()
            enemy11_health_bar.showturtle()
        if green_power_up_active == 0:
            enemy11_laser.showturtle()
            if enemy11_laser.ycor() > -360:
                enemy11_laser.direction = "down"
                YL = enemy11_laser.ycor()
                enemy11_laser.sety(YL - 11)
            else:
                x = enemy11.xcor()
                y = enemy11.ycor()
                enemy11_laser.setx(x)
                enemy11_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy11_laser.hideturtle()
            x = enemy11.xcor()
            y = enemy11.ycor()
            enemy11_laser.setx(x)
            enemy11_laser.sety(y - 80)
    else:
        if update11 == 0:
            enemy11.hideturtle()
            enemy11_laser.hideturtle()
            enemy11_health_bar.hideturtle()
            enemy11_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            health_bar11 = 2
            x = enemy11.xcor()
            y = enemy11.ycor()
            enemy11_laser.setx(x)
            enemy11_laser.sety(y - 80)

    if score >= 50 and mode == "Classic_Mode":
        if update12 == 0:
            enemy12.showturtle()
            enemy12_laser.showturtle()
            enemy12_health_bar.showturtle()
        if green_power_up_active == 0:
            enemy12_laser.showturtle()
            if enemy12_laser.ycor() > -360:
                enemy12_laser.direction = "down"
                YL = enemy12_laser.ycor()
                enemy12_laser.sety(YL - 11)
            else:
                x = enemy12.xcor()
                y = enemy12.ycor()
                enemy12_laser.setx(x)
                enemy12_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy12_laser.hideturtle()
            x = enemy12.xcor()
            y = enemy12.ycor()
            enemy12_laser.setx(x)
            enemy12_laser.sety(y - 80)
    else:
        if update12 == 0:
            enemy12.hideturtle()
            enemy12_laser.hideturtle()
            enemy12_health_bar.hideturtle()
            enemy12_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            health_bar12 = 2
            x = enemy12.xcor()
            y = enemy12.ycor()
            enemy12_laser.setx(x)
            enemy12_laser.sety(y - 80)

    if score >= 60 and mode == "Classic_Mode":
        if update13 == 0:
            enemy13.showturtle()
            enemy13_laser.showturtle()
            enemy13_health_bar.showturtle()
        if green_power_up_active == 0:
            enemy13_laser.showturtle()
            if enemy13_laser.ycor() > -360:
                enemy13_laser.direction = "down"
                YL = enemy13_laser.ycor()
                enemy13_laser.sety(YL - 11)
            else:
                x = enemy13.xcor()
                y = enemy13.ycor()
                enemy13_laser.setx(x)
                enemy13_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy13_laser.hideturtle()
            x = enemy13.xcor()
            y = enemy13.ycor()
            enemy13_laser.setx(x)
            enemy13_laser.sety(y - 80)
    else:
        if update13 == 0:
            enemy13.hideturtle()
            enemy13_laser.hideturtle()
            enemy13_health_bar.hideturtle()
            enemy13_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            health_bar13 = 2
            x = enemy13.xcor()
            y = enemy13.ycor()
            enemy13_laser.setx(x)
            enemy13_laser.sety(y - 80)

    if score >= 70 and mode == "Classic_Mode":
        if update14 == 0:
            enemy14.showturtle()
            enemy14_laser.showturtle()
            enemy14_health_bar.showturtle()
        if green_power_up_active == 0:
            enemy14_laser.showturtle()
            if enemy14_laser.ycor() > -360:
                enemy14_laser.direction = "down"
                YL = enemy14_laser.ycor()
                enemy14_laser.sety(YL - 11)
            else:
                x = enemy14.xcor()
                y = enemy14.ycor()
                enemy14_laser.setx(x)
                enemy14_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy14_laser.hideturtle()
            x = enemy14.xcor()
            y = enemy14.ycor()
            enemy14_laser.setx(x)
            enemy14_laser.sety(y - 80)
    else:
        if update14 == 0:
            enemy14.hideturtle()
            enemy14_laser.hideturtle()
            enemy14_health_bar.hideturtle()
            enemy14_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            health_bar14 = 2
            x = enemy14.xcor()
            y = enemy14.ycor()
            enemy14_laser.setx(x)
            enemy14_laser.sety(y - 80)

    if score >= 80 and mode == "Classic_Mode":
        if update15 == 0:
            enemy15.showturtle()
            enemy15_laser.showturtle()
            enemy15_health_bar.showturtle()
        if green_power_up_active == 0:
            enemy15_laser.showturtle()
            if enemy15_laser.ycor() > -360:
                enemy15_laser.direction = "down"
                YL = enemy15_laser.ycor()
                enemy15_laser.sety(YL - 11)
            else:
                x = enemy15.xcor()
                y = enemy15.ycor()
                enemy15_laser.setx(x)
                enemy15_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            enemy15_laser.hideturtle()
            x = enemy15.xcor()
            y = enemy15.ycor()
            enemy15_laser.setx(x)
            enemy15_laser.sety(y - 80)
    else:
        if update15 == 0:
            enemy15.hideturtle()
            enemy15_laser.hideturtle()
            enemy15_health_bar.hideturtle()
            enemy15_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            health_bar15 = 2
            x = enemy15.xcor()
            y = enemy15.ycor()
            enemy15_laser.setx(x)
            enemy15_laser.sety(y - 80)

    if score >= 100 and mode == "Classic_Mode":
        if update_boss == 0:
            boss.showturtle()
            boss_laser.showturtle()
            boss_health_bar.showturtle()
        if green_power_up_active == 0:
            boss_laser.showturtle()
            if boss_laser.ycor() > -360:
                boss_laser.direction = "down"
                if 10 >= health_bar_boss > 8:
                    YL = boss_laser.ycor()
                    boss_laser.sety(YL - 9.5)
                if 8 >= health_bar_boss > 6:
                    YL = boss_laser.ycor()
                    boss_laser.sety(YL - 11)
                if 6 >= health_bar_boss > 4:
                    YL = boss_laser.ycor()
                    boss_laser.sety(YL - 12.5)
                if 4 >= health_bar_boss > 2:
                    YL = boss_laser.ycor()
                    boss_laser.sety(YL - 14)
                if 2 >= health_bar_boss > -1:
                    YL = boss_laser.ycor()
                    boss_laser.sety(YL - 15.5)
            else:
                x = boss.xcor()
                y = boss.ycor()
                boss_laser.setx(x)
                boss_laser.sety(y - 80)
                if enemy_shooting_sound == 1:
                    winsound.PlaySound("Sound/Laser_Gun_Enemy.wav", winsound.SND_ASYNC)
        else:
            boss_laser.hideturtle()
            x = boss.xcor()
            y = boss.ycor()
            boss_laser.setx(x)
            boss_laser.sety(y - 80)
    else:
        if update_boss == 0:
            boss.hideturtle()
            boss_laser.hideturtle()
            boss_health_bar.hideturtle()
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            health_bar_boss = 10
            x = boss.xcor()
            y = boss.ycor()
            boss_laser.setx(x)
            boss_laser.sety(y - 80)

    # Lines 7279 - 8309 is for what happens when each of the enemies die in classic mode
    # This includes resetting them to their default state and updating the players score when they die
    # Some of the more powerful enemies must be hit multiple times before they die

    if update1 == 6:
        enemy1.showturtle()
        update1 = 0

    if 3.5 <= update1 < 6:
        update1 = update1 + 0.5

    if update1 == 3:
        enemy1.hideturtle()
        enemy1.shape("Textures/Enemies/Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy1.goto(x, 220)
        update1 = 3.5

    if 1.5 <= update1 < 3:
        update1 = update1 + 0.5

    if update1 == 1:
        enemy1.shape("Textures/Explosions/Explosion2.gif")
        update1 = 1.5

    if 0.5 <= update1 < 1:
        update1 = update1 + 0.25

    if laser.distance(enemy1) < 55:
        if update1 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            dc1 = dc1 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                blue_bots_killed = blue_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[8] = str(blue_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy1.shape("Textures/Explosions/Explosion1.gif")
        update1 = 0.5

    if update2 == 6:
        enemy2.showturtle()
        update2 = 0

    if 3.5 <= update2 < 6:
        update2 = update2 + 0.5

    if update2 == 3:
        enemy2.hideturtle()
        enemy2.shape("Textures/Enemies/Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy2.goto(x, 220)
        update2 = 3.5

    if 1.5 <= update2 < 3:
        update2 = update2 + 0.5

    if update2 == 1:
        enemy2.shape("Textures/Explosions/Explosion2.gif")
        update2 = 1.5

    if 0.5 <= update2 < 1:
        update2 = update2 + 0.25

    if laser.distance(enemy2) < 55:
        if update2 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            dc2 = dc2 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                blue_bots_killed = blue_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[8] = str(blue_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy2.shape("Textures/Explosions/Explosion1.gif")
        update2 = 0.5

    if update3 == 6:
        enemy3.showturtle()
        update3 = 0

    if 3.5 <= update3 < 6:
        update3 = update3 + 0.5

    if update3 == 3:
        enemy3.hideturtle()
        enemy3.shape("Textures/Enemies/Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy3.goto(x, 220)
        update3 = 3.5

    if 1.5 <= update3 < 3:
        update3 = update3 + 0.5

    if update3 == 1:
        enemy3.shape("Textures/Explosions/Explosion2.gif")
        update3 = 1.5

    if 0.5 <= update3 < 1:
        update3 = update3 + 0.25

    if laser.distance(enemy3) < 55:
        if update3 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            dc3 = dc3 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                blue_bots_killed = blue_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[8] = str(blue_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy3.shape("Textures/Explosions/Explosion1.gif")
        update3 = 0.5

    if update4 == 6:
        enemy4.showturtle()
        update4 = 0

    if 3.5 <= update4 < 6:
        update4 = update4 + 0.5

    if update4 == 3:
        enemy4.hideturtle()
        enemy4.shape("Textures/Enemies/Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy4.goto(x, 220)
        update4 = 3.5

    if 1.5 <= update4 < 3:
        update4 = update4 + 0.5

    if update4 == 1:
        enemy4.shape("Textures/Explosions/Explosion2.gif")
        update4 = 1.5

    if 0.5 <= update4 < 1:
        update4 = update4 + 0.25

    if enemy4.isvisible() and laser.distance(enemy4) < 55:
        if update4 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            dc4 = dc4 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                blue_bots_killed = blue_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[8] = str(blue_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy4.shape("Textures/Explosions/Explosion1.gif")
        update4 = 0.5

    if update5 == 6:
        enemy5.showturtle()
        update5 = 0

    if 3.5 <= update5 < 6:
        update5 = update5 + 0.5

    if update5 == 3:
        enemy5.hideturtle()
        enemy5.shape("Textures/Enemies/Enemy(1-5).gif")
        x = random.randint(-640, 640)
        enemy5.goto(x, 220)
        update5 = 3.5

    if 1.5 <= update5 < 3:
        update5 = update5 + 0.5

    if update5 == 1:
        enemy5.shape("Textures/Explosions/Explosion2.gif")
        update5 = 1.5

    if 0.5 <= update5 < 1:
        update5 = update5 + 0.25

    if enemy5.isvisible() and laser.distance(enemy5) < 55:
        if update5 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            dc5 = dc5 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                blue_bots_killed = blue_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[8] = str(blue_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy5.shape("Textures/Explosions/Explosion1.gif")
        update5 = 0.5

    if update6 == 6:
        enemy6.showturtle()
        update6 = 0

    if 3.5 <= update6 < 6:
        update6 = update6 + 0.5

    if update6 == 3:
        enemy6.hideturtle()
        enemy6.shape("Textures/Enemies/Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy6.goto(x, 220)
        update6 = 3.5

    if 1.5 <= update6 < 3:
        update6 = update6 + 0.5

    if update6 == 1:
        enemy6.shape("Textures/Explosions/Explosion2.gif")
        update6 = 1.5

    if 0.5 <= update6 < 1:
        update6 = update6 + 0.25

    if enemy6.isvisible() and laser.distance(enemy6) < 55:
        if update6 == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            dc6 = dc6 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                yellow_bots_killed = yellow_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[6] = str(yellow_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy6.shape("Textures/Explosions/Explosion1.gif")
        update6 = 0.5

    if update7 == 6:
        enemy7.showturtle()
        update7 = 0

    if 3.5 <= update7 < 6:
        update7 = update7 + 0.5

    if update7 == 3:
        enemy7.hideturtle()
        enemy7.shape("Textures/Enemies/Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy7.goto(x, 220)
        update7 = 3.5

    if 1.5 <= update7 < 3:
        update7 = update7 + 0.5

    if update7 == 1:
        enemy7.shape("Textures/Explosions/Explosion2.gif")
        update7 = 1.5

    if 0.5 <= update7 < 1:
        update7 = update7 + 0.25

    if enemy7.isvisible() and laser.distance(enemy7) < 55:
        if update7 == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            dc7 = dc7 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                yellow_bots_killed = yellow_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[6] = str(yellow_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy7.shape("Textures/Explosions/Explosion1.gif")
        update7 = 0.5

    if update8 == 6:
        enemy8.showturtle()
        update8 = 0

    if 3.5 <= update8 < 6:
        update8 = update8 + 0.5

    if update8 == 3:
        enemy8.hideturtle()
        enemy8.shape("Textures/Enemies/Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy8.goto(x, 220)
        update8 = 3.5

    if 1.5 <= update8 < 3:
        update8 = update8 + 0.5

    if update8 == 1:
        enemy8.shape("Textures/Explosions/Explosion2.gif")
        update8 = 1.5

    if 0.5 <= update8 < 1:
        update8 = update8 + 0.25

    if enemy8.isvisible() and laser.distance(enemy8) < 55:
        if update8 == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            dc8 = dc8 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                yellow_bots_killed = yellow_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[6] = str(yellow_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy8.shape("Textures/Explosions/Explosion1.gif")
        update8 = 0.5

    if update9 == 6:
        enemy9.showturtle()
        update9 = 0

    if 3.5 <= update9 < 6:
        update9 = update9 + 0.5

    if update9 == 3:
        enemy9.hideturtle()
        enemy9.shape("Textures/Enemies/Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy9.goto(x, 220)
        update9 = 3.5

    if 1.5 <= update9 < 3:
        update9 = update9 + 0.5

    if update9 == 1:
        enemy9.shape("Textures/Explosions/Explosion2.gif")
        update9 = 1.5

    if 0.5 <= update9 < 1:
        update9 = update9 + 0.25

    if enemy9.isvisible() and laser.distance(enemy9) < 55:
        if update9 == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            dc9 = dc9 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                yellow_bots_killed = yellow_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[6] = str(yellow_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy9.shape("Textures/Explosions/Explosion1.gif")
        update9 = 0.5

    if update10 == 6:
        enemy10.showturtle()
        update10 = 0

    if 3.5 <= update10 < 6:
        update10 = update10 + 0.5

    if update10 == 3:
        enemy10.hideturtle()
        enemy10.shape("Textures/Enemies/Enemy(6-10).gif")
        x = random.randint(-640, 640)
        enemy10.goto(x, 220)
        update10 = 3.5

    if 1.5 <= update10 < 3:
        update10 = update10 + 0.5

    if update10 == 1:
        enemy10.shape("Textures/Explosions/Explosion2.gif")
        update10 = 1.5

    if 0.5 <= update10 < 1:
        update10 = update10 + 0.25

    if enemy10.isvisible() and laser.distance(enemy10) < 55:
        if update10 == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            dc10 = dc10 + 1
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                yellow_bots_killed = yellow_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[6] = str(yellow_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
        enemy10.shape("Textures/Explosions/Explosion1.gif")
        update10 = 0.5

    if update11 == 6:
        enemy11.showturtle()
        enemy11_health_bar.showturtle()
        update11 = 0

    if 4 <= update11 < 6:
        update11 = update11 + 0.5

    if update11 == 3.5:
        x = enemy11.xcor()
        enemy11_health_bar.goto(x, 290)
        enemy11_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        health_bar11 = 2
        update11 = 4

    if update11 == 3:
        enemy11.hideturtle()
        enemy11.shape("Textures/Enemies/Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy11.goto(x, 220)
        update11 = 3.5

    if 1.5 <= update11 < 3:
        update11 = update11 + 0.5

    if update11 == 1:
        enemy11.shape("Textures/Explosions/Explosion2.gif")
        update11 = 1.5

    if 0.5 <= update11 < 1:
        update11 = update11 + 0.25

    if enemy11.isvisible() and laser.distance(enemy11) < 55 and health_bar11 == 1 and hit_delay11 == 0:
        if update11 == 0:
            if blue_power_up_active == 1:
                score = score + 10
            else:
                score = score + 5
            dc11 = dc11 + 1
            health_bar11 = 0
            enemy11_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                red_bots_killed = red_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[4] = str(red_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            enemy11.shape("Textures/Explosions/Explosion1.gif")
            update11 = 0.5

    if hit_delay11 == 9:
        hit_delay11 = 0

    if 1 <= hit_delay11 < 9:
        hit_delay11 = hit_delay11 + 1

    if enemy11.isvisible() and laser.distance(enemy11) < 55 and health_bar11 == 2:
        if update11 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            enemy11_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar11 = 1
            hit_delay11 = 1

    if update12 == 6:
        enemy12.showturtle()
        enemy12_health_bar.showturtle()
        update12 = 0

    if 4 <= update12 < 6:
        update12 = update12 + 0.5

    if update12 == 3.5:
        x = enemy12.xcor()
        enemy12_health_bar.goto(x, 290)
        enemy12_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        health_bar12 = 2
        update12 = 4

    if update12 == 3:
        enemy12.hideturtle()
        enemy12.shape("Textures/Enemies/Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy12.goto(x, 220)
        update12 = 3.5

    if 1.5 <= update12 < 3:
        update12 = update12 + 0.5

    if update12 == 1:
        enemy12.shape("Textures/Explosions/Explosion2.gif")
        update12 = 1.5

    if 0.5 <= update12 < 1:
        update12 = update12 + 0.25

    if enemy12.isvisible() and laser.distance(enemy12) < 55 and health_bar12 == 1 and hit_delay12 == 0:
        if update12 == 0:
            if blue_power_up_active == 1:
                score = score + 10
            else:
                score = score + 5
            dc12 = dc12 + 1
            health_bar12 = 0
            enemy12_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                red_bots_killed = red_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[4] = str(red_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            enemy12.shape("Textures/Explosions/Explosion1.gif")
            update12 = 0.5

    if hit_delay12 == 9:
        hit_delay12 = 0

    if 1 <= hit_delay12 < 9:
        hit_delay12 = hit_delay12 + 1

    if enemy12.isvisible() and laser.distance(enemy12) < 55 and health_bar12 == 2:
        if update12 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            enemy12_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar12 = 1
            hit_delay12 = 1

    if update13 == 6:
        enemy13.showturtle()
        enemy13_health_bar.showturtle()
        update13 = 0

    if 4 <= update13 < 6:
        update13 = update13 + 0.5

    if update13 == 3.5:
        x = enemy13.xcor()
        enemy13_health_bar.goto(x, 290)
        enemy13_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        health_bar13 = 2
        update13 = 4

    if update13 == 3:
        enemy13.hideturtle()
        enemy13.shape("Textures/Enemies/Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy13.goto(x, 220)
        update13 = 3.5

    if 1.5 <= update13 < 3:
        update13 = update13 + 0.5

    if update13 == 1:
        enemy13.shape("Textures/Explosions/Explosion2.gif")
        update13 = 1.5

    if 0.5 <= update13 < 1:
        update13 = update13 + 0.25

    if enemy13.isvisible() and laser.distance(enemy13) < 55 and health_bar13 == 1 and hit_delay13 == 0:
        if update13 == 0:
            if blue_power_up_active == 1:
                score = score + 10
            else:
                score = score + 5
            dc13 = dc13 + 1
            health_bar13 = 0
            enemy13_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                red_bots_killed = red_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[4] = str(red_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            enemy13.shape("Textures/Explosions/Explosion1.gif")
            update13 = 0.5

    if hit_delay13 == 9:
        hit_delay13 = 0

    if 1 <= hit_delay13 < 9:
        hit_delay13 = hit_delay13 + 1

    if enemy13.isvisible() and laser.distance(enemy13) < 55 and health_bar13 == 2:
        if update13 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            enemy13_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar13 = 1
            hit_delay13 = 1

    if update14 == 6:
        enemy14.showturtle()
        enemy14_health_bar.showturtle()
        update14 = 0

    if 4 <= update14 < 6:
        update14 = update14 + 0.5

    if update14 == 3.5:
        x = enemy14.xcor()
        enemy14_health_bar.goto(x, 290)
        enemy14_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        health_bar14 = 2
        update14 = 4

    if update14 == 3:
        enemy14.hideturtle()
        enemy14.shape("Textures/Enemies/Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy14.goto(x, 220)
        update14 = 3.5

    if 1.5 <= update14 < 3:
        update14 = update14 + 0.5

    if update14 == 1:
        enemy14.shape("Textures/Explosions/Explosion2.gif")
        update14 = 1.5

    if 0.5 <= update14 < 1:
        update14 = update14 + 0.25

    if enemy14.isvisible() and laser.distance(enemy14) < 55 and health_bar14 == 1 and hit_delay14 == 0:
        if update14 == 0:
            if blue_power_up_active == 1:
                score = score + 10
            else:
                score = score + 5
            dc14 = dc14 + 1
            health_bar14 = 0
            enemy14_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                red_bots_killed = red_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[4] = str(red_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            enemy14.shape("Textures/Explosions/Explosion1.gif")
            update14 = 0.5

    if hit_delay14 == 9:
        hit_delay14 = 0

    if 1 <= hit_delay14 < 9:
        hit_delay14 = hit_delay14 + 1

    if enemy14.isvisible() and laser.distance(enemy14) < 55 and health_bar14 == 2:
        if update14 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            enemy14_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar14 = 1
            hit_delay14 = 1

    if update15 == 6:
        enemy15.showturtle()
        enemy15_health_bar.showturtle()
        update15 = 0

    if 4 <= update15 < 6:
        update15 = update15 + 0.5

    if update15 == 3.5:
        x = enemy15.xcor()
        enemy15_health_bar.goto(x, 290)
        enemy15_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        health_bar15 = 2
        update15 = 4

    if update15 == 3:
        enemy15.hideturtle()
        enemy15.shape("Textures/Enemies/Enemy(11-15).gif")
        x = random.randint(-640, 640)
        enemy15.goto(x, 220)
        update15 = 3.5

    if 1.5 <= update15 < 3:
        update15 = update15 + 0.5

    if update15 == 1:
        enemy15.shape("Textures/Explosions/Explosion2.gif")
        update15 = 1.5

    if 0.5 <= update15 < 1:
        update15 = update15 + 0.25

    if enemy15.isvisible() and laser.distance(enemy15) < 55 and health_bar15 == 1 and hit_delay15 == 0:
        if update15 == 0:
            if blue_power_up_active == 1:
                score = score + 10
            else:
                score = score + 5
            dc15 = dc15 + 1
            health_bar15 = 0
            enemy15_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                red_bots_killed = red_bots_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[4] = str(red_bots_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            enemy15.shape("Textures/Explosions/Explosion1.gif")
            update15 = 0.5

    if hit_delay15 == 9:
        hit_delay15 = 0

    if 1 <= hit_delay15 < 9:
        hit_delay15 = hit_delay15 + 1

    if enemy15.isvisible() and laser.distance(enemy15) < 55 and health_bar15 == 2:
        if update15 == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            enemy15_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar15 = 1
            hit_delay15 = 1

    if update_boss == 6:
        boss.showturtle()
        boss_health_bar.showturtle()
        update_boss = 0

    if 4 <= update_boss < 6:
        update_boss = update_boss + 0.5

    if update_boss == 3.5:
        x = boss.xcor()
        boss_health_bar.goto(x, 290)
        boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        health_bar_boss = 10
        update_boss = 4

    if update_boss == 3:
        boss.hideturtle()
        boss.shape("Textures/Enemies/Boss.gif")
        x = random.randint(-640, 640)
        boss.goto(x, 220)
        update_boss = 3.5

    if 1.5 <= update_boss < 3:
        update_boss = update_boss + 0.5

    if update_boss == 1:
        boss.shape("Textures/Explosions/Explosion2.gif")
        update_boss = 1.5

    if 0.5 <= update_boss < 1:
        update_boss = update_boss + 0.25

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 1 and hit_delay_boss9 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 100
            else:
                score = score + 50
            dc_boss = dc_boss + 1
            health_bar_boss = 0
            boss_health_bar.hideturtle()
            if enemy_death_sound == 1:
                winsound.PlaySound("Sound/Explosion.wav", winsound.SND_ASYNC)
            if god_mode == 0:
                bosses_killed = bosses_killed + 1
                stats = open("config/Statistics.txt", "r")
                stats_text = stats.readlines()
                stats.close()
                stats_text[2] = str(bosses_killed) + "\n"
                stats_update = open("Config/Statistics.txt", "w")
                stats_update.writelines(stats_text)
                stats_update.close()
            boss.shape("Textures/Explosions/Explosion1.gif")
            update_boss = 0.5

    if hit_delay_boss9 == 9:
        hit_delay_boss9 = 0

    if 1 <= hit_delay_boss9 < 9:
        hit_delay_boss9 = hit_delay_boss9 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 2 and hit_delay_boss8 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 1
            hit_delay_boss9 = 1

    if hit_delay_boss8 == 9:
        hit_delay_boss8 = 0

    if 1 <= hit_delay_boss8 < 9:
        hit_delay_boss8 = hit_delay_boss8 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 3 and hit_delay_boss7 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 2
            hit_delay_boss8 = 1

    if hit_delay_boss7 == 9:
        hit_delay_boss7 = 0

    if 1 <= hit_delay_boss7 < 9:
        hit_delay_boss7 = hit_delay_boss7 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 4 and hit_delay_boss6 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 3
            hit_delay_boss7 = 1

    if hit_delay_boss6 == 9:
        hit_delay_boss6 = 0

    if 1 <= hit_delay_boss6 < 9:
        hit_delay_boss6 = hit_delay_boss6 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 5 and hit_delay_boss5 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 4
            hit_delay_boss6 = 1

    if hit_delay_boss5 == 9:
        hit_delay_boss5 = 0

    if 1 <= hit_delay_boss5 < 9:
        hit_delay_boss5 = hit_delay_boss5 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 6 and hit_delay_boss4 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 5
            hit_delay_boss5 = 1

    if hit_delay_boss4 == 9:
        hit_delay_boss4 = 0

    if 1 <= hit_delay_boss4 < 9:
        hit_delay_boss4 = hit_delay_boss4 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 7 and hit_delay_boss3 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 6
            hit_delay_boss4 = 1

    if hit_delay_boss3 == 9:
        hit_delay_boss3 = 0

    if 1 <= hit_delay_boss3 < 9:
        hit_delay_boss3 = hit_delay_boss3 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 8 and hit_delay_boss2 == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 7
            hit_delay_boss3 = 1

    if hit_delay_boss2 == 9:
        hit_delay_boss2 = 0

    if 1 <= hit_delay_boss2 < 9:
        hit_delay_boss2 = hit_delay_boss2 + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 9 and hit_delay_boss == 0:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 2
            else:
                score = score + 1
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 8
            hit_delay_boss2 = 1

    if hit_delay_boss == 9:
        hit_delay_boss = 0

    if 1 <= hit_delay_boss < 9:
        hit_delay_boss = hit_delay_boss + 1

    if boss.isvisible() and laser.distance(boss) < 55 and health_bar_boss == 10:
        if update_boss == 0:
            if blue_power_up_active == 1:
                score = score + 4
            else:
                score = score + 2
            boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            if enemy_hit_sound == 1:
                winsound.PlaySound("Sound/Explosion2.wav", winsound.SND_ASYNC)
            health_bar_boss = 9
            hit_delay_boss = 1

    # Lines 8314 - 8505 are for what happens when the player gets hit and dies in classic mode
    # This basically resets the game back to its default state

    if update_player == 6:
        player.showturtle()
        update_player = 0
        death_animation = 0

    if 3.5 <= update_player < 6:
        update_player = update_player + 0.5

    if update_player == 3:
        player.hideturtle()
        player.shape("Textures/Player/Player.gif")
        player.goto(0, -300)
        update_player = 3.5

    if 1.5 <= update_player < 3:
        update_player = update_player + 0.5

    if update_player == 1:
        player.shape("Textures/Explosions/Explosion2.gif")
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
        if god_mode == 0:
            classic_deaths = classic_deaths + 1
            stats = open("config/Statistics.txt", "r")
            stats_text = stats.readlines()
            stats.close()
            stats_text[10] = str(classic_deaths) + "\n"
            stats_update = open("Config/Statistics.txt", "w")
            stats_update.writelines(stats_text)
            stats_update.close()
        update_player = 1.5

    if 0.5 <= update_player < 1:
        update_player = update_player + 0.25

    if enemy1_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy1_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy2_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy2_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy3_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy3_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy4_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy4_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy5_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy5_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy6_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy6_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy7_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy7_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy8_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy8_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy9_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy9_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy10_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy10_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy11_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy11_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy12_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy12_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy13_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy13_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy14_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy14_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if enemy15_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (enemy15_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    if boss_laser.distance(player) < 125 and death_animation == 0 and mode == "Classic_Mode" and god_mode == 0:
        if -30 < (boss_laser.xcor() - player.xcor()) < 30:
            death_animation = 1
            if player_death_sound == 1:
                winsound.PlaySound("Sound/Explosion3.wav", winsound.SND_ASYNC)
            player.shape("Textures/Explosions/Explosion1.gif")
            score = 0
            update_player = 0.5

    # Lines 8511 - 9177 are for the movement of all the enemies in classic mode.
    # The more times the player kills a specific enemy, the faster that specific enemy moves
    # The rate of movement is the exact same for all enemies in classic mode

    if dc1 >= 4 and death_animation == 0 and update1 == 0:
        if 600 < enemy1.xcor() < 650:
            moving1 = -1
        if -600 > enemy1.xcor() > -650:
            moving1 = 1
        if moving1 == 1:
            if 4 <= dc1 < 7:
                x = enemy1.xcor()
                enemy1.setx(x + 2)
            if 7 <= dc1 < 10:
                x = enemy1.xcor()
                enemy1.setx(x + 4)
            if 10 <= dc1 < 13:
                x = enemy1.xcor()
                enemy1.setx(x + 6)
            if 13 <= dc1 < 16:
                x = enemy1.xcor()
                enemy1.setx(x + 8)
            if 16 <= dc1:
                x = enemy1.xcor()
                enemy1.setx(x + 10)
        if moving1 == -1:
            if 4 <= dc1 < 7:
                x = enemy1.xcor()
                enemy1.setx(x - 2)
            if 7 <= dc1 < 10:
                x = enemy1.xcor()
                enemy1.setx(x - 4)
            if 10 <= dc1 < 13:
                x = enemy1.xcor()
                enemy1.setx(x - 6)
            if 13 <= dc1 < 16:
                x = enemy1.xcor()
                enemy1.setx(x - 8)
            if 16 <= dc1:
                x = enemy1.xcor()
                enemy1.setx(x - 10)

    if dc2 >= 4 and death_animation == 0 and update2 == 0:
        if 600 < enemy2.xcor() < 650:
            moving2 = -1
        if -600 > enemy2.xcor() > -650:
            moving2 = 1
        if moving2 == 1:
            if 4 <= dc2 < 7:
                x = enemy2.xcor()
                enemy2.setx(x + 2)
            if 7 <= dc2 < 10:
                x = enemy2.xcor()
                enemy2.setx(x + 4)
            if 10 <= dc2 < 13:
                x = enemy2.xcor()
                enemy2.setx(x + 6)
            if 13 <= dc2 < 16:
                x = enemy2.xcor()
                enemy2.setx(x + 8)
            if 16 <= dc2:
                x = enemy2.xcor()
                enemy2.setx(x + 10)
        if moving2 == -1:
            if 4 <= dc2 < 7:
                x = enemy2.xcor()
                enemy2.setx(x - 2)
            if 7 <= dc2 < 10:
                x = enemy2.xcor()
                enemy2.setx(x - 4)
            if 10 <= dc2 < 13:
                x = enemy2.xcor()
                enemy2.setx(x - 6)
            if 13 <= dc2 < 16:
                x = enemy2.xcor()
                enemy2.setx(x - 8)
            if 16 <= dc2:
                x = enemy2.xcor()
                enemy2.setx(x - 10)

    if dc3 >= 4 and death_animation == 0 and update3 == 0:
        if 600 < enemy3.xcor() < 650:
            moving3 = -1
        if -600 > enemy3.xcor() > -650:
            moving3 = 1
        if moving3 == 1:
            if 4 <= dc3 < 7:
                x = enemy3.xcor()
                enemy3.setx(x + 2)
            if 7 <= dc3 < 10:
                x = enemy3.xcor()
                enemy3.setx(x + 4)
            if 10 <= dc3 < 13:
                x = enemy3.xcor()
                enemy3.setx(x + 6)
            if 13 <= dc3 < 16:
                x = enemy3.xcor()
                enemy3.setx(x + 8)
            if 16 <= dc3:
                x = enemy3.xcor()
                enemy3.setx(x + 10)
        if moving3 == -1:
            if 4 <= dc3 < 7:
                x = enemy3.xcor()
                enemy3.setx(x - 2)
            if 7 <= dc3 < 10:
                x = enemy3.xcor()
                enemy3.setx(x - 4)
            if 10 <= dc3 < 13:
                x = enemy3.xcor()
                enemy3.setx(x - 6)
            if 13 <= dc3 < 16:
                x = enemy3.xcor()
                enemy3.setx(x - 8)
            if 16 <= dc3:
                x = enemy3.xcor()
                enemy3.setx(x - 10)

    if dc4 >= 4 and death_animation == 0 and update4 == 0:
        if 600 < enemy4.xcor() < 650:
            moving4 = -1
        if -600 > enemy4.xcor() > -650:
            moving4 = 1
        if moving4 == 1:
            if 4 <= dc4 < 7:
                x = enemy4.xcor()
                enemy4.setx(x + 2)
            if 7 <= dc4 < 10:
                x = enemy4.xcor()
                enemy4.setx(x + 4)
            if 10 <= dc4 < 13:
                x = enemy4.xcor()
                enemy4.setx(x + 6)
            if 13 <= dc4 < 16:
                x = enemy4.xcor()
                enemy4.setx(x + 8)
            if 16 <= dc4:
                x = enemy4.xcor()
                enemy4.setx(x + 10)
        if moving4 == -1:
            if 4 <= dc4 < 7:
                x = enemy4.xcor()
                enemy4.setx(x - 2)
            if 7 <= dc4 < 10:
                x = enemy4.xcor()
                enemy4.setx(x - 4)
            if 10 <= dc4 < 13:
                x = enemy4.xcor()
                enemy4.setx(x - 6)
            if 13 <= dc4 < 16:
                x = enemy4.xcor()
                enemy4.setx(x - 8)
            if 16 <= dc4:
                x = enemy4.xcor()
                enemy4.setx(x - 10)

    if dc5 >= 4 and death_animation == 0 and update5 == 0:
        if 600 < enemy5.xcor() < 650:
            moving5 = -1
        if -600 > enemy5.xcor() > -650:
            moving5 = 1
        if moving5 == 1:
            if 4 <= dc5 < 7:
                x = enemy5.xcor()
                enemy5.setx(x + 2)
            if 7 <= dc5 < 10:
                x = enemy5.xcor()
                enemy5.setx(x + 4)
            if 10 <= dc5 < 13:
                x = enemy5.xcor()
                enemy5.setx(x + 6)
            if 13 <= dc5 < 16:
                x = enemy5.xcor()
                enemy5.setx(x + 8)
            if 16 <= dc5:
                x = enemy5.xcor()
                enemy5.setx(x + 10)
        if moving5 == -1:
            if 4 <= dc5 < 7:
                x = enemy5.xcor()
                enemy5.setx(x - 2)
            if 7 <= dc5 < 10:
                x = enemy5.xcor()
                enemy5.setx(x - 4)
            if 10 <= dc5 < 13:
                x = enemy5.xcor()
                enemy5.setx(x - 6)
            if 13 <= dc5 < 16:
                x = enemy5.xcor()
                enemy5.setx(x - 8)
            if 16 <= dc5:
                x = enemy5.xcor()
                enemy5.setx(x - 10)

    if dc6 >= 4 and death_animation == 0 and update6 == 0:
        if 600 < enemy6.xcor() < 650:
            moving6 = -1
        if -600 > enemy6.xcor() > -650:
            moving6 = 1
        if moving6 == 1:
            if 4 <= dc6 < 7:
                x = enemy6.xcor()
                enemy6.setx(x + 2)
            if 7 <= dc6 < 10:
                x = enemy6.xcor()
                enemy6.setx(x + 4)
            if 10 <= dc6 < 13:
                x = enemy6.xcor()
                enemy6.setx(x + 6)
            if 13 <= dc6 < 16:
                x = enemy6.xcor()
                enemy6.setx(x + 8)
            if 16 <= dc6:
                x = enemy6.xcor()
                enemy6.setx(x + 10)
        if moving6 == -1:
            if 4 <= dc6 < 7:
                x = enemy6.xcor()
                enemy6.setx(x - 2)
            if 7 <= dc6 < 10:
                x = enemy6.xcor()
                enemy6.setx(x - 4)
            if 10 <= dc6 < 13:
                x = enemy6.xcor()
                enemy6.setx(x - 6)
            if 13 <= dc6 < 16:
                x = enemy6.xcor()
                enemy6.setx(x - 8)
            if 16 <= dc6:
                x = enemy6.xcor()
                enemy6.setx(x - 10)

    if dc7 >= 4 and death_animation == 0 and update7 == 0:
        if 600 < enemy7.xcor() < 650:
            moving7 = -1
        if -600 > enemy7.xcor() > -650:
            moving7 = 1
        if moving7 == 1:
            if 4 <= dc7 < 7:
                x = enemy7.xcor()
                enemy7.setx(x + 2)
            if 7 <= dc7 < 10:
                x = enemy7.xcor()
                enemy7.setx(x + 4)
            if 10 <= dc7 < 13:
                x = enemy7.xcor()
                enemy7.setx(x + 6)
            if 13 <= dc7 < 16:
                x = enemy7.xcor()
                enemy7.setx(x + 8)
            if 16 <= dc7:
                x = enemy7.xcor()
                enemy7.setx(x + 10)
        if moving7 == -1:
            if 4 <= dc7 < 7:
                x = enemy7.xcor()
                enemy7.setx(x - 2)
            if 7 <= dc7 < 10:
                x = enemy7.xcor()
                enemy7.setx(x - 4)
            if 10 <= dc7 < 13:
                x = enemy7.xcor()
                enemy7.setx(x - 6)
            if 13 <= dc7 < 16:
                x = enemy7.xcor()
                enemy7.setx(x - 8)
            if 16 <= dc7:
                x = enemy7.xcor()
                enemy7.setx(x - 10)

    if dc8 >= 4 and death_animation == 0 and update8 == 0:
        if 600 < enemy8.xcor() < 650:
            moving8 = -1
        if -600 > enemy8.xcor() > -650:
            moving8 = 1
        if moving8 == 1:
            if 4 <= dc8 < 7:
                x = enemy8.xcor()
                enemy8.setx(x + 2)
            if 7 <= dc8 < 10:
                x = enemy8.xcor()
                enemy8.setx(x + 4)
            if 10 <= dc8 < 13:
                x = enemy8.xcor()
                enemy8.setx(x + 6)
            if 13 <= dc8 < 16:
                x = enemy8.xcor()
                enemy8.setx(x + 8)
            if 16 <= dc8:
                x = enemy8.xcor()
                enemy8.setx(x + 10)
        if moving8 == -1:
            if 4 <= dc8 < 7:
                x = enemy8.xcor()
                enemy8.setx(x - 2)
            if 7 <= dc8 < 10:
                x = enemy8.xcor()
                enemy8.setx(x - 4)
            if 10 <= dc8 < 13:
                x = enemy8.xcor()
                enemy8.setx(x - 6)
            if 13 <= dc8 < 16:
                x = enemy8.xcor()
                enemy8.setx(x - 8)
            if 16 <= dc8:
                x = enemy8.xcor()
                enemy8.setx(x - 10)

    if dc9 >= 4 and death_animation == 0 and update9 == 0:
        if 600 < enemy9.xcor() < 650:
            moving9 = -1
        if -600 > enemy9.xcor() > -650:
            moving9 = 1
        if moving9 == 1:
            if 4 <= dc9 < 7:
                x = enemy9.xcor()
                enemy9.setx(x + 2)
            if 7 <= dc9 < 10:
                x = enemy9.xcor()
                enemy9.setx(x + 4)
            if 10 <= dc9 < 13:
                x = enemy9.xcor()
                enemy9.setx(x + 6)
            if 13 <= dc9 < 16:
                x = enemy9.xcor()
                enemy9.setx(x + 8)
            if 16 <= dc9:
                x = enemy9.xcor()
                enemy9.setx(x + 10)
        if moving9 == -1:
            if 4 <= dc9 < 7:
                x = enemy9.xcor()
                enemy9.setx(x - 2)
            if 7 <= dc9 < 10:
                x = enemy9.xcor()
                enemy9.setx(x - 4)
            if 10 <= dc9 < 13:
                x = enemy9.xcor()
                enemy9.setx(x - 6)
            if 13 <= dc9 < 16:
                x = enemy9.xcor()
                enemy9.setx(x - 8)
            if 16 <= dc9:
                x = enemy9.xcor()
                enemy9.setx(x - 10)

    if dc10 >= 4 and death_animation == 0 and update10 == 0:
        if 600 < enemy10.xcor() < 650:
            moving10 = -1
        if -600 > enemy10.xcor() > -650:
            moving10 = 1
        if moving10 == 1:
            if 4 <= dc10 < 7:
                x = enemy10.xcor()
                enemy10.setx(x + 2)
            if 7 <= dc10 < 10:
                x = enemy10.xcor()
                enemy10.setx(x + 4)
            if 10 <= dc10 < 13:
                x = enemy10.xcor()
                enemy10.setx(x + 6)
            if 13 <= dc10 < 16:
                x = enemy10.xcor()
                enemy10.setx(x + 8)
            if 16 <= dc10:
                x = enemy10.xcor()
                enemy10.setx(x + 10)
        if moving10 == -1:
            if 4 <= dc10 < 7:
                x = enemy10.xcor()
                enemy10.setx(x - 2)
            if 7 <= dc10 < 10:
                x = enemy10.xcor()
                enemy10.setx(x - 4)
            if 10 <= dc10 < 13:
                x = enemy10.xcor()
                enemy10.setx(x - 6)
            if 13 <= dc10 < 16:
                x = enemy10.xcor()
                enemy10.setx(x - 8)
            if 16 <= dc10:
                x = enemy10.xcor()
                enemy10.setx(x - 10)

    if dc11 >= 4 and death_animation == 0 and update11 == 0:
        if 600 < enemy11.xcor() < 650:
            moving11 = -1
        if -600 > enemy11.xcor() > -650:
            moving11 = 1
        if moving11 == 1:
            if 4 <= dc11 < 7:
                x = enemy11.xcor()
                enemy11.setx(x + 2)
                enemy11_health_bar.goto(x + 2, 290)
            if 7 <= dc11 < 10:
                x = enemy11.xcor()
                enemy11.setx(x + 4)
                enemy11_health_bar.goto(x + 4, 290)
            if 10 <= dc11 < 13:
                x = enemy11.xcor()
                enemy11.setx(x + 6)
                enemy11_health_bar.goto(x + 6, 290)
            if 13 <= dc11 < 16:
                x = enemy11.xcor()
                enemy11.setx(x + 8)
                enemy11_health_bar.goto(x + 8, 290)
            if 16 <= dc11:
                x = enemy11.xcor()
                enemy11.setx(x + 10)
                enemy11_health_bar.goto(x + 10, 290)
        if moving11 == -1:
            if 4 <= dc11 < 7:
                x = enemy11.xcor()
                enemy11.setx(x - 2)
                enemy11_health_bar.goto(x - 2, 290)
            if 7 <= dc11 < 10:
                x = enemy11.xcor()
                enemy11.setx(x - 4)
                enemy11_health_bar.goto(x - 4, 290)
            if 10 <= dc11 < 13:
                x = enemy11.xcor()
                enemy11.setx(x - 6)
                enemy11_health_bar.goto(x - 6, 290)
            if 13 <= dc11 < 16:
                x = enemy11.xcor()
                enemy11.setx(x - 8)
                enemy11_health_bar.goto(x - 8, 290)
            if 16 <= dc11:
                x = enemy11.xcor()
                enemy11.setx(x - 10)
                enemy11_health_bar.goto(x - 10, 290)

    if dc12 >= 4 and death_animation == 0 and update12 == 0:
        if 600 < enemy12.xcor() < 650:
            moving12 = -1
        if -600 > enemy12.xcor() > -650:
            moving12 = 1
        if moving12 == 1:
            if 4 <= dc12 < 7:
                x = enemy12.xcor()
                enemy12.setx(x + 2)
                enemy12_health_bar.goto(x + 2, 290)
            if 7 <= dc12 < 10:
                x = enemy12.xcor()
                enemy12.setx(x + 4)
                enemy12_health_bar.goto(x + 4, 290)
            if 10 <= dc12 < 13:
                x = enemy12.xcor()
                enemy12.setx(x + 6)
                enemy12_health_bar.goto(x + 6, 290)
            if 13 <= dc12 < 16:
                x = enemy12.xcor()
                enemy12.setx(x + 8)
                enemy12_health_bar.goto(x + 8, 290)
            if 16 <= dc12:
                x = enemy12.xcor()
                enemy12.setx(x + 10)
                enemy12_health_bar.goto(x + 10, 290)
        if moving12 == -1:
            if 4 <= dc12 < 7:
                x = enemy12.xcor()
                enemy12.setx(x - 2)
                enemy12_health_bar.goto(x - 2, 290)
            if 7 <= dc12 < 10:
                x = enemy12.xcor()
                enemy12.setx(x - 4)
                enemy12_health_bar.goto(x - 4, 290)
            if 10 <= dc12 < 13:
                x = enemy12.xcor()
                enemy12.setx(x - 6)
                enemy12_health_bar.goto(x - 6, 290)
            if 13 <= dc12 < 16:
                x = enemy12.xcor()
                enemy12.setx(x - 8)
                enemy12_health_bar.goto(x - 8, 290)
            if 16 <= dc12:
                x = enemy12.xcor()
                enemy12.setx(x - 10)
                enemy12_health_bar.goto(x - 10, 290)

    if dc13 >= 4 and death_animation == 0 and update13 == 0:
        if 600 < enemy13.xcor() < 650:
            moving13 = -1
        if -600 > enemy13.xcor() > -650:
            moving13 = 1
        if moving13 == 1:
            if 4 <= dc13 < 7:
                x = enemy13.xcor()
                enemy13.setx(x + 2)
                enemy13_health_bar.goto(x + 2, 290)
            if 7 <= dc13 < 10:
                x = enemy13.xcor()
                enemy13.setx(x + 4)
                enemy13_health_bar.goto(x + 4, 290)
            if 10 <= dc13 < 13:
                x = enemy13.xcor()
                enemy13.setx(x + 6)
                enemy13_health_bar.goto(x + 6, 290)
            if 13 <= dc13 < 16:
                x = enemy13.xcor()
                enemy13.setx(x + 8)
                enemy13_health_bar.goto(x + 8, 290)
            if 16 <= dc13:
                x = enemy13.xcor()
                enemy13.setx(x + 10)
                enemy13_health_bar.goto(x + 10, 290)
        if moving13 == -1:
            if 4 <= dc13 < 7:
                x = enemy13.xcor()
                enemy13.setx(x - 2)
                enemy13_health_bar.goto(x - 2, 290)
            if 7 <= dc13 < 10:
                x = enemy13.xcor()
                enemy13.setx(x - 4)
                enemy13_health_bar.goto(x - 4, 290)
            if 10 <= dc13 < 13:
                x = enemy13.xcor()
                enemy13.setx(x - 6)
                enemy13_health_bar.goto(x - 6, 290)
            if 13 <= dc13 < 16:
                x = enemy13.xcor()
                enemy13.setx(x - 8)
                enemy13_health_bar.goto(x - 8, 290)
            if 16 <= dc13:
                x = enemy13.xcor()
                enemy13.setx(x - 10)
                enemy13_health_bar.goto(x - 10, 290)

    if dc14 >= 4 and death_animation == 0 and update14 == 0:
        if 600 < enemy14.xcor() < 650:
            moving14 = -1
        if -600 > enemy14.xcor() > -650:
            moving14 = 1
        if moving14 == 1:
            if 4 <= dc14 < 7:
                x = enemy14.xcor()
                enemy14.setx(x + 2)
                enemy14_health_bar.goto(x + 2, 290)
            if 7 <= dc14 < 10:
                x = enemy14.xcor()
                enemy14.setx(x + 4)
                enemy14_health_bar.goto(x + 4, 290)
            if 10 <= dc14 < 13:
                x = enemy14.xcor()
                enemy14.setx(x + 6)
                enemy14_health_bar.goto(x + 6, 290)
            if 13 <= dc14 < 16:
                x = enemy14.xcor()
                enemy14.setx(x + 8)
                enemy14_health_bar.goto(x + 8, 290)
            if 16 <= dc14:
                x = enemy14.xcor()
                enemy14.setx(x + 10)
                enemy14_health_bar.goto(x + 10, 290)
        if moving14 == -1:
            if 4 <= dc14 < 7:
                x = enemy14.xcor()
                enemy14.setx(x - 2)
                enemy14_health_bar.goto(x - 2, 290)
            if 7 <= dc14 < 10:
                x = enemy14.xcor()
                enemy14.setx(x - 4)
                enemy14_health_bar.goto(x - 4, 290)
            if 10 <= dc14 < 13:
                x = enemy14.xcor()
                enemy14.setx(x - 6)
                enemy14_health_bar.goto(x - 6, 290)
            if 13 <= dc14 < 16:
                x = enemy14.xcor()
                enemy14.setx(x - 8)
                enemy14_health_bar.goto(x - 8, 290)
            if 16 <= dc14:
                x = enemy14.xcor()
                enemy14.setx(x - 10)
                enemy14_health_bar.goto(x - 10, 290)

    if dc15 >= 4 and death_animation == 0 and update15 == 0:
        if 600 < enemy15.xcor() < 650:
            moving15 = -1
        if -600 > enemy15.xcor() > -650:
            moving15 = 1
        if moving15 == 1:
            if 4 <= dc15 < 7:
                x = enemy15.xcor()
                enemy15.setx(x + 2)
                enemy15_health_bar.goto(x + 2, 290)
            if 7 <= dc15 < 10:
                x = enemy15.xcor()
                enemy15.setx(x + 4)
                enemy15_health_bar.goto(x + 4, 290)
            if 10 <= dc15 < 13:
                x = enemy15.xcor()
                enemy15.setx(x + 6)
                enemy15_health_bar.goto(x + 6, 290)
            if 13 <= dc15 < 16:
                x = enemy15.xcor()
                enemy15.setx(x + 8)
                enemy15_health_bar.goto(x + 8, 290)
            if 16 <= dc15:
                x = enemy15.xcor()
                enemy15.setx(x + 10)
                enemy15_health_bar.goto(x + 10, 290)
        if moving15 == -1:
            if 4 <= dc15 < 7:
                x = enemy15.xcor()
                enemy15.setx(x - 2)
                enemy15_health_bar.goto(x - 2, 290)
            if 7 <= dc15 < 10:
                x = enemy15.xcor()
                enemy15.setx(x - 4)
                enemy15_health_bar.goto(x - 4, 290)
            if 10 <= dc15 < 13:
                x = enemy15.xcor()
                enemy15.setx(x - 6)
                enemy15_health_bar.goto(x - 6, 290)
            if 13 <= dc15 < 16:
                x = enemy15.xcor()
                enemy15.setx(x - 8)
                enemy15_health_bar.goto(x - 8, 290)
            if 16 <= dc15:
                x = enemy15.xcor()
                enemy15.setx(x - 10)
                enemy15_health_bar.goto(x - 10, 290)

    if dc_boss >= 4 and death_animation == 0 and update_boss == 0:
        if 600 < boss.xcor() < 650:
            moving_boss = -1
        if -600 > boss.xcor() > -650:
            moving_boss = 1
        if moving_boss == 1:
            if 4 <= dc_boss < 7:
                x = boss.xcor()
                boss.setx(x + 2)
                boss_health_bar.goto(x + 2, 290)
            if 7 <= dc_boss < 10:
                x = boss.xcor()
                boss.setx(x + 4)
                boss_health_bar.goto(x + 4, 290)
            if 10 <= dc_boss < 13:
                x = boss.xcor()
                boss.setx(x + 6)
                boss_health_bar.goto(x + 6, 290)
            if 13 <= dc_boss < 16:
                x = boss.xcor()
                boss.setx(x + 8)
                boss_health_bar.goto(x + 8, 290)
            if 16 <= dc_boss:
                x = boss.xcor()
                boss.setx(x + 10)
                boss_health_bar.goto(x + 10, 290)
        if moving_boss == -1:
            if 4 <= dc_boss < 7:
                x = boss.xcor()
                boss.setx(x - 2)
                boss_health_bar.goto(x - 2, 290)
            if 7 <= dc_boss < 10:
                x = boss.xcor()
                boss.setx(x - 4)
                boss_health_bar.goto(x - 4, 290)
            if 10 <= dc_boss < 13:
                x = boss.xcor()
                boss.setx(x - 6)
                boss_health_bar.goto(x - 6, 290)
            if 13 <= dc_boss < 16:
                x = boss.xcor()
                boss.setx(x - 8)
                boss_health_bar.goto(x - 8, 290)
            if 16 <= dc_boss:
                x = boss.xcor()
                boss.setx(x - 10)
                boss_health_bar.goto(x - 10, 290)

    # Lines 9182 - 9223 are used to check if the sounds are still on or still off
    # This is so that any in-game changes to the sound text file is immediately checked and updated

    soundfile = open("Config/Sound.txt", "r")
    sound_number = soundfile.readlines()
    soundfile.close()
    soundfile2 = open("Config/Laser_Fighter_2.txt", "r")
    sound_number2 = soundfile2.readlines()
    soundfile2.close()
    if sound_number[0] == sound_number2[0]:
        button_sound = 1
    else:
        button_sound = 0
    if sound_number[1] == sound_number2[1]:
        player_shooting_sound = 1
    else:
        player_shooting_sound = 0
    if sound_number[2] == sound_number2[2]:
        enemy_shooting_sound = 1
    else:
        enemy_shooting_sound = 0
    if sound_number[3] == sound_number2[3]:
        player_death_sound = 1
    else:
        player_death_sound = 0
    if sound_number[4] == sound_number2[4]:
        enemy_death_sound = 1
    else:
        enemy_death_sound = 0
    if sound_number[5] == sound_number2[5]:
        player_hit_sound = 1
    else:
        player_hit_sound = 0
    if sound_number[6] == sound_number2[6]:
        enemy_hit_sound = 1
    else:
        enemy_hit_sound = 0
    if sound_number[7] == sound_number2[7]:
        power_up_pickup_sound = 1
    else:
        power_up_pickup_sound = 0
    if sound_number[8] == sound_number2[8]:
        power_up_spawn_sound = 1
    else:
        power_up_spawn_sound = 0

    # Lines 9227 - 9244 are used to check the score and high score in both modes every tick and update them if needed

    if god_mode == 0 and mode == "Classic_Mode":
        if score > high_score_machine_war:
            high_score_machine_war = score
            high_score_machine_war_write = str(high_score_machine_war)
            high_score_alien_mode_write = str(high_score_alien_mode)
            high_score_update = "High_Score_Machine_War = " + '"' + high_score_machine_war_write + '"\n' + "High_Score_Alien_Mode = " + '"' + high_score_alien_mode_write + '"\n'
            score_file = open("Config/High_score.txt", "w")
            score_file.writelines(high_score_update)
            score_file.close()
    elif god_mode == 0 and mode == "Alien_Mode":
        if score > high_score_alien_mode:
            high_score_alien_mode = score
            high_score_machine_war_write = str(high_score_machine_war)
            high_score_alien_mode_write = str(high_score_alien_mode)
            high_score_update = "High_Score_Machine_War = " + '"' + high_score_machine_war_write + '"\n' + "High_Score_Alien_Mode = " + '"' + high_score_alien_mode_write + '"\n'
            score_file = open("Config/High_score.txt", "w")
            score_file.writelines(high_score_update)
            score_file.close()

    # Lines 9248 - 9305 are used to write the score and high score on the screen when playing one of the game modes and also used to update and write the power up timers on the screen when needed

    if mode == "Classic_Mode":
        if tick_update % 12 == 0:

            score_box.clear()
            score_box.write("Score: {}  High Score: {}".format(score, high_score_machine_war), align="center", font=("Courier", 24, "normal"))

            if yellow_power_up_active == 1:
                yellow_power_up_text.clear()
                yellow_power_up_text.write("{}".format(round((1200 - yellow_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                yellow_power_up_text.clear()
                yellow_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))

            if blue_power_up_active == 1:
                blue_power_up_text.clear()
                blue_power_up_text.write("{}".format(round((2700 - blue_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                blue_power_up_text.clear()
                blue_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))

            if green_power_up_active == 1:
                extra_power_up_text.clear()
                extra_power_up_text.write("{}".format(round((900 - green_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                extra_power_up_text.clear()
                extra_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))
    elif mode == "Alien_Mode":
        if tick_update % 12 == 0:

            score_box.clear()
            score_box.write("Score: {}  High Score: {}".format(score, high_score_alien_mode), align="center", font=("Courier", 24, "normal"))

            if yellow_power_up_active == 1:
                yellow_power_up_text.clear()
                yellow_power_up_text.write("{}".format(round((1200 - yellow_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                yellow_power_up_text.clear()
                yellow_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))

            if blue_power_up_active == 1:
                blue_power_up_text.clear()
                blue_power_up_text.write("{}".format(round((2700 - blue_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                blue_power_up_text.clear()
                blue_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))

            if red_power_up_active == 1:
                extra_power_up_text.clear()
                extra_power_up_text.write("{}".format(round((900 - red_power_up_timer) / 60)), align="center", font=("Courier", 24, "normal"))
            else:
                extra_power_up_text.clear()
                extra_power_up_text.write("{}".format("0"), align="center", font=("Courier", 24, "normal"))
    else:
        yellow_power_up_text.clear()
        blue_power_up_text.clear()
        extra_power_up_text.clear()
        score_box.clear()
        score = 0

    # Lines 9309 - 9320 are used to correctly set the tick delays for each of the modes of the game

    if mode == "Title_Mode":
        time.sleep(delay/5)
    elif mode == "Classic_Mode":
        time.sleep(delay/25)
    elif mode == "Alien_Mode":
        time.sleep(delay/25)
    elif mode == "Stats":
        time.sleep(delay/5)
    elif mode == "Settings":
        time.sleep(delay/5)
    elif mode == "Controls":
        time.sleep(delay/5)