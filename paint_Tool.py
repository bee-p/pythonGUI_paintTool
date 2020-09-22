from tkinter import *
from tkinter.messagebox import *


def clear() : #그림판 초기화
    canvas.delete(ALL)

def exitWindow() : #그림판 종료
    window.destroy()

def drawing(event) : #캔버스에 그림 그리기
    if var.get() != 0 :
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        canvas.create_oval(x1, y1, x2, y2, fill = set_color(), outline = set_color())
    else :
        showinfo("ERROR", "색상을 선택하세요!")

def set_color() : #색상 선택
    if page == 0 :
        return color_warm[var.get() - 1]
    elif page == 1 :
        return color_modern[var.get() - 1]
    elif page == 2:
        return color_cool[var.get() - 1]

def nextPage() : #페이지 이동(다음)
    global page
    
    if page == 2 :
        page = 0
    else :
        page += 1
        
    page_pallete(page)

def prePage() : #페이지 이동(이전)
    global page
    
    if page == 0 :
        page = 2
    else :
        page -= 1
        
    page_pallete(page)

def page_pallete(page) : #팔레트 색상 보여주기,,,테마 이름 바꾸기
    p = 0
    
    for p in range(3) :
        if page == p :
            colorLabel.configure(image = photo[p])
            textLabel.configure(text = textList[p])
            break
    

#----------------------메인 코드 부분--------------------------
window = Tk()
window.title("그림판")
window.geometry("500x700")
window.resizable(width = FALSE, height = FALSE)
window.configure(bg = "white")

page = 0

#메뉴 추가
mainMenu = Menu(window)
window.config(menu = mainMenu)

toolMenu = Menu(mainMenu, font = ("맑은 고딕", 12))
tempMenu= Menu(mainMenu)
mainMenu.add_cascade(label = "도구", menu = toolMenu)
toolMenu.add_command(label = "초기화", command = clear)
toolMenu.add_separator()
toolMenu.add_command(label = "종료", command = exitWindow)
for m in range(13) :
    mainMenu.add_cascade(label = "  *  ", menu = tempMenu)

#이미지 주소 목록/저장
pallete = ["color/color1.gif", "color/color2.gif", "color/color3.gif"]
photo = [None] * 3

for i in range(3) :
    photo[i] = PhotoImage(file = pallete[i])

#그 외 목록들,,,
textList = ["포근", "모던", "시원"]
color_warm = ["#F4B2B8", "#F6E8F2", "#D2B2EC", "#46BEC6"]
color_modern = ["#5E5E5E", "#D0F2F2", "#F8F8F0", "#C4C2C2"]
color_cool = ["#D4ECFA", "#14ACE4", "#1C6AAC", "#FED870"]

#canvas 설정
canvas = Canvas(window, width = 500, height = 420, relief = "solid", bd = 2, bg = "white")
canvas.bind("<B1-Motion>", drawing)
canvas.bind("<Button-1>", drawing)

#그 외 레이블/버튼 생성
colorLabel = Label(window, image = photo[0])
textLabel = Label(window, text = textList[0], font = ("HY헤드라인M", 25), bg = "white")

var = IntVar()

rbList = [None] * 4

for z in range(4) :
    rbList[z] = Radiobutton(window, variable = var, value = (z + 1), bg = "white", command = set_color)

bt1 = Button(window, text = "◀", font = ("맑은 고딕", 25), bg = "white", command = prePage)
bt2 = Button(window, text = "▶", font = ("맑은 고딕", 25), bg = "white", command = nextPage)

#pack, place... . ..
xPos, num = 50, 0

canvas.pack()
colorLabel.pack(pady = 10)
for k in range(4) :
    rbList[num].place(x = xPos, y = 500)
    num += 1
    xPos += 125

bt1.place(x = 100, y = 590)
textLabel.place(x = 215, y = 610)
bt2.place(x = 335, y = 590)

window.mainloop()
