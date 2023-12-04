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
if exists(Pattern("1695906944371.png").similar(0.75)):
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
click(Pattern("1695908149355.png").similar(0.92))
click(Pattern("1695908278821.png").similar(0.78))
wait("1695908335140.png",2)
click("1695908335140.png")
wait("1695908357596.png",2)
click("1695908357596.png")
click(Pattern("1700757618013.png").similar(0.97))
wait("1700757649095.png",10)
click(Pattern("1700758279855.png").targetOffset(103,-2))
sleep(1)
click(Pattern("1700758211163.png").targetOffset(-14,-28))
click(Pattern("1700758725237.png").similar(0.96).targetOffset(117,1))
sleep(1)
click(Pattern("1700758752537.png").targetOffset(-35,-3))
doubleClick(Pattern("1695908462215.png").targetOffset(34,-1))
type('01012022')
doubleClick(Pattern("1695908489387.png").targetOffset(30,-1))
type(data_do_dia_anterior)
doubleClick(Pattern("1695908507500.png").targetOffset(26,-6))
type('003')
if exists(Pattern("1700757930392.png").exact()):
    click(Pattern("1700757930392.png").exact().targetOffset(32,0))
click("1695908987848.png")
wait(Pattern("1695909040774.png").exact(),60)
click("1695909062042.png")
wait("1695909081242.png",2)
click("1695909081242.png")
if exists(Pattern("1695909429956.png").exact().targetOffset(-25,-1)):
    click(Pattern("1695909429956.png").exact().targetOffset(-25,-1))
else:
    if exists(Pattern("1695909371545.png").exact()):
        pass
if exists(Pattern("1695909471581.png").exact().targetOffset(98,126)):
    click(Pattern("1695909510180.png").exact().targetOffset(-19,0))
else:
    # Faça algo quando a terceira imagem existe
    pass
if exists(Pattern("1695909643070.png").exact()):
    pass
if exists(Pattern("1695909703533.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695909727560.png").exact()):
        click(Pattern("1695909755325.png").exact().targetOffset(-46,-3))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass
if exists(Pattern("1695909787580.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695909804932.png").exact()):
        click(Pattern("1695909829419.png").exact().targetOffset(-41,2))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass
if exists(Pattern("1695909861791.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695909888601.png").exact()):
        click(Pattern("1695909907972.png").exact().targetOffset(-39,0))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass
if exists(Pattern("1695909935259.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695909955981.png").exact()):
        click(Pattern("1695909977093.png").exact().targetOffset(-24,1))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass
if exists(Pattern("1695910032634.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695910050603.png").exact()):
        click(Pattern("1695910069126.png").exact().targetOffset(-37,-1))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass
if exists(Pattern("1695910391486.png").exact()):
    # Faça algo quando a quarta imagem existe
    pass
else:
    if exists(Pattern("1695910414819.png").exact()):
        click(Pattern("1695910442909.png").exact().targetOffset(-43,-1))
    else:
        # Faça algo quando nenhuma das imagens existe
        pass

click("1695910538321.png")
wait("1695910890210.png",10)
click(Pattern("1695910916949.png").similar(0.85))
doubleClick(Pattern("1695910944256.png").similar(0.91).targetOffset(23,4))
type('emissatop')
click(Pattern("1695910965711.png").exact())
wait(600)
click(Pattern("1695911057493.png").similar(0.47))
wait("1700757742698.png",10)
click("1695922800239.png")
click("1695922818080.png")
click("1695924619382.png")
click("1695924632148.png")
keyDown(Key.CTRL)
click(Pattern("1701698562498.png").exact())
keyUp(Key.CTRL)

# Copie o ícone para a área de transferência
type("c", Key.CTRL)
click(Pattern("1696276655498.png").similar(0.95).targetOffset(-28,-2))
sleep(5)
sleep(5)
doubleClick(Pattern("1700222578202.png").similar(0.95))
sleep(2)
click(Pattern("1696876253706.png").targetOffset(-11,115))
type("v", Key.CTRL)
sleep(1)
while exists("1696876316980.png"):
    click("1696876330645.png")
click(Pattern("1701280865967.png").targetOffset(547,-3))
click("1696276781684-1.png")
click(Pattern("1696276804309-1.png").targetOffset(244,-4))
click(Pattern("1696276827112-1.png").similar(0.88).targetOffset(-45,0))

