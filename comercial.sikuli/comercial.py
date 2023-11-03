# coding: UTF-8
# Importe as classes necessárias
from java.util import Calendar
from java.text import SimpleDateFormat

# Obtenha a data atual
cal = Calendar.getInstance()

# Subtrai um dia da data atual
cal.add(Calendar.DAY_OF_MONTH, -1)

# Obtenha a data do dia anterior
data_anterior = cal.getTime()

# Crie um formato de data para a formatação
formato_data = SimpleDateFormat("dd-MM-yyyy")

# Formate a data do dia anterior no formato desejado
data_do_dia_anterior = formato_data.format(data_anterior)

click("1695906922406.png")
if exists(Pattern("1695906944371.png").similar(0.91)):
    click("1695906944371.png")

wait(Pattern("1695906978944.png").similar(0.66),10)

doubleClick("1695906978944.png")
wait("1695907009092.png",10)

if exists(Pattern("1695907034423.png").similar(0.97)):
    doubleClick(Pattern("1695907048758.png").targetOffset(22,0))
    type('MATHEUS')
    doubleClick(Pattern("1695907067651.png").similar(0.87).targetOffset(21,-1))   
    type('75759496')
    click("1695907081326.png")
else: 
    if exists(Pattern("1695907103216.png").similar(0.94)):
        doubleClick(Pattern("1695907140998.png").similar(0.85).targetOffset(23,-3))
        type('002')
        doubleClick(Pattern("1695907048758.png").targetOffset(22,0))
        type('MATHEUS')
        doubleClick(Pattern("1695907067651.png").similar(0.86).targetOffset(20,-2))
        type('75759496')
        click("1695907081326.png")

wait("1695908134420.png",10)
click(Pattern("1696857634981.png").exact().targetOffset(-2,-5))
click(Pattern("1696857688376.png").exact())
wait("1696857933293.png",2)
click("1696857907004.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
wait(Pattern("1696857799445.png").similar(0.91),10)
doubleClick(Pattern("1696857819318.png").similar(0.94))
click("1696857959332.png")
click("1696858110249.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
doubleClick(Pattern("1696858136482.png").similar(0.91).targetOffset(32,4))
type('clientes')
click(Pattern("1695910965711.png").exact())
wait("1696858184981.png",2)
click("1696858203536.png")
click("1696858473765.png")
wait(20)
click("1696857907004.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
wait("1696859882840.png",10)
doubleClick("1696859882840.png")
click("1696857959332.png")
click("1696858110249.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
doubleClick(Pattern("1696858136482.png").similar(0.91).targetOffset(32,4))
type('pedidos')
click(Pattern("1695910965711.png").exact())
wait("1696858184981.png",2)
click("1696858203536.png")
click("1696858473765.png")
wait(20)
click("1696857907004.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
wait("1696860432488.png",10)
doubleClick("1696860441556.png")
click("1696857959332.png")
click("1696858110249.png")
wait("1696857756831.png",2)
click(Pattern("1696857767472.png").similar(0.89))
doubleClick(Pattern("1696858136482.png").similar(0.91).targetOffset(32,4))
type('ltv')
click(Pattern("1695910965711.png").exact())
wait("1696858184981.png",2)
click("1696858203536.png")
click("1696858473765.png")
wait(20)
click("1696860621808.png")
click("1695924619382.png")
click(Pattern("1695924632148.png").similar(0.50))

keyDown(Key.CTRL)
click(Pattern("1696875985245.png").exact())
click(Pattern("1696875994578.png").exact())
click(Pattern("1696876003397.png").exact())
keyUp(Key.CTRL)

# Copie o ícone para a área de transferência
type("c", Key.CTRL)
click(Pattern("1696276655498.png").similar(0.95).targetOffset(-28,-2))
sleep(5)
doubleClick(Pattern("1696336171608.png").similar(0.92))
sleep(2)
click(Pattern("1696876253706.png").targetOffset(-11,115))
type("v", Key.CTRL)
sleep(1)
while exists("1696876316980.png"):
    click("1696876330645.png")
click(Pattern("1696337637998.png").similar(0.93).targetOffset(492,0))
click("1696276781684.png")
click(Pattern("1696276804309.png").targetOffset(244,-4))
click(Pattern("1696276827112.png").similar(0.88).targetOffset(-45,0))

