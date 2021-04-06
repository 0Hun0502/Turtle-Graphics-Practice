from turtle import *


reset()
hideturtle()
speed(0)

fillcolor('red')
begin_fill()

penup()  # A 그리기 (전체 레이아웃 조정을 위해 x좌표 값에 300씩 감소시켜 주었습니다.)
goto(91-300, 0)

pendown()
goto(5-300, -179)
goto(34-300, -179)
goto(60-300, -129)
goto(93-300, -129)
goto(93-300, -139)
goto(120-300, -119)
goto(93-300, -96)
goto(93-300, -106)
goto(68-300, -106)
goto(93-300, -44)
goto(93-300, -88)
goto(116-300, -109)
goto(116-300, 0)
goto(91-300, 0)
end_fill()

penup()  # 작은 직각삼각형

fillcolor('black')
begin_fill()
goto(116-300, -128)

pendown()
goto(116-300, -146)
goto(93-300, -146)
goto(116-300, -128)
end_fill()

penup()  # 호 그리기1

fillcolor('black')
begin_fill()
goto(124-300, -150)

pendown()
setheading(-135)
circle(-69, 70)
goto(43-300, -172)
setheading(-25)
circle(78, 76)
goto(124-300, -150)
end_fill()

penup()  # 호 그리기2

fillcolor('black')
begin_fill()
goto(22-300, -133)

pendown()
setheading(115)
circle(-69, 100)
goto(74-300, -25)
setheading(187)
circle(78, 115)
goto(22-300, -133)
end_fill()

penup()  # V 그리기

fillcolor('black')
begin_fill()
goto(124-300, -145)

pendown()
goto(137-300, -44)
goto(156-300, -44)
goto(150-300, -91)
goto(170-300, -44)
goto(190-300, -44)
goto(147-300, -145)
goto(124-300, -145)
end_fill()

penup()  # E 그리기

fillcolor('black')
begin_fill()
goto(198-300, -44)

pendown()
goto(236-300, -44)
goto(232-300, -62)
goto(214-300, -62)
goto(206-300, -85)
goto(225-300, -85)
goto(221-300, -103)
goto(201-300, -103)
goto(195-300, -126)
goto(214-300, -126)
goto(210-300, -145)
goto(167-300, -145)
goto(198-300, -44)
end_fill()

penup()  # N 그리기

fillcolor('black')
begin_fill()
goto(244-300, -44)

pendown()
goto(261-300, -44)
goto(263-300, -82)
goto(276-300, -44)
goto(295-300, -44)
goto(266-300, -146)
goto(249-300, -146)
goto(246-300, -107)
goto(234-300, -146)
goto(214-300, -146)
goto(244-300, -44)
end_fill()

penup()  # G 그리기

fillcolor('black')
begin_fill()
goto(347-300, -44)

pendown()
goto(318-300, -44)
setheading(180)
circle(22, 60)
goto(278-300, -130)
setheading(-90)
circle(22, 60)
goto(304-300, -149)
goto(304-300, -154)
goto(327-300, -142)
goto(342-300, -86)
goto(320-300, -86)
goto(313-300, -102)
goto(320-300, -102)
goto(311-300, -128)
goto(305-300, -128)
setheading(150)
circle(-7, 60)
goto(316-300, -65)
setheading(60)
circle(-7, 60)
goto(343-300, -61.5)
goto(347-300, -44)
end_fill()

penup()  # E 그리기

fillcolor('black')
begin_fill()
goto(364-300, -44)

pendown()
goto(402-300, -44)
goto(398-300, -62)
goto(380-300, -62)
goto(372-300, -85)
goto(391-300, -85)
goto(387-300, -103)
goto(367-300, -103)
goto(361-300, -126)
goto(380-300, -126)
goto(376-300, -145)
goto(333-300, -145)
goto(364-300, -44)
end_fill()

penup()  # R 그리기

fillcolor('black')
begin_fill()
goto(410-300, -44)

pendown()
goto(381-300, -146)
goto(402-300, -146)
goto(415-300, -103)
goto(419-300, -103)
setheading(0)
circle(-7, 60)
goto(413-300, -146)
goto(434-300, -146)
goto(443-300, -109)
setheading(90)
circle(7, 60)
setheading(-20)
circle(7, 60)
goto(459-300, -56)
setheading(60)
circle(7, 100)
goto(410-300, -44)
end_fill()

penup()
fillcolor('white')
begin_fill()
goto(427-300, -61)

pendown()
goto(419-300, -88)
goto(422-300, -88)
setheading(-20)
circle(7, 100)
goto(437-300, -65)
setheading(110)
circle(7, 60)
goto(427-300, -61)
end_fill()

penup()  # S 그리기

fillcolor('black')
begin_fill()
goto(512-300, -44)

pendown()
goto(479-300, -44)
setheading(160)
circle(7, 100)
goto(456-300, -93)
setheading(-130)
circle(7, 100)
goto(477-300, -103.56)
goto(470-300, -127)
goto(450-300, -127)
goto(443-300, -146)
goto(476-300, -146)
setheading(-20)
circle(7, 100)
goto(499-300, -97)
setheading(80)
circle(7, 100)
goto(478-300, -88.78)
goto(484-300, -67)
setheading(90)
circle(-7, 100)
goto(507-300, -60)
goto(512-300, -44)
end_fill()

screen = Screen()
screen.bgpic('avengers.gif')

mainloop()
