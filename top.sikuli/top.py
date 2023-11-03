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
click(Pattern("1695908149355.png").similar(0.92))
click(Pattern("1695908278821.png").similar(0.78))
wait("1695908335140.png",2)
click("1695908335140.png")
wait("1695908357596.png",2)
click("1695908357596.png")
click(Pattern("1695908394177.png").similar(0.95))
wait("1695908439626.png",10)
doubleClick(Pattern("1695908462215.png").targetOffset(34,-1))
type('01012022')
doubleClick(Pattern("1695908489387.png").targetOffset(30,-1))
type(data_do_dia_anterior)
doubleClick(Pattern("1695908507500.png").targetOffset(26,-6))
type('003')
doubleClick(Pattern("1695908524689.png").targetOffset(48,0))
type('371,375,379,678,623,698,699')
doubleClick(Pattern("1695908554959.png").similar(0.95).targetOffset(45,0))
type('24,21,22,23,50,45,9,7,18,19,30,1,40,20,51,54,56,58,59,60,61,62,66,114,115,116,117,118,119')
doubleClick(Pattern("1695908579323.png").similar(0.95).targetOffset(30,-2))
type('ADT,DEV')
click(Pattern("1695908844133.png").exact().targetOffset(97,-1))
doubleClick(Pattern("1695908655198.png").similar(0.95).targetOffset(27,-4))
type('ADT,DEV')
click(Pattern("1695908871017.png").exact().targetOffset(95,-2))
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
type('receitatop')
click(Pattern("1695910965711.png").exact())
wait(200)
click(Pattern("1695911057493.png").similar(0.47))
wait("1695908439626.png",10)
doubleClick(Pattern("1695908462215.png").targetOffset(34,-1))
type('01012022')
doubleClick(Pattern("1695908489387.png").targetOffset(30,-1))
type(data_do_dia_anterior)
doubleClick(Pattern("1695908507500.png").targetOffset(26,-6))
type('003')
doubleClick(Pattern("1695908524689.png").targetOffset(48,0))
type('371,375,379,678,623,698,699')
click(Pattern("1697822907454.png").exact().targetOffset(114,1))
doubleClick(Pattern("1695908554959.png").similar(0.95).targetOffset(45,0))
type('24,21,22,23,50,45,9,7,18,19,30,1,40,20,51,54,56,58,59,60,61,62,66,114,115,116,117,118,119')
doubleClick(Pattern("1695911201501.png").exact().targetOffset(44,-1))
type('16,44,45,34,43,14,6,47,39,11,10,1,19,32,15,17,20,46,37,48,49,52,54,56,57,58,59,60,61,62,63,64,65,66,310,311')
doubleClick(Pattern("1695908579323.png").similar(0.95).targetOffset(30,-2))
type('ADT,DEV')
doubleClick(Pattern("1695908655198.png").similar(0.95).targetOffset(27,-4))
type('ADT,DEV')
click("1695908987848.png")
wait(Pattern("1695909040774.png").similar(0.88),200)
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
type('despesatop')
click(Pattern("1695910965711.png").exact())
wait(600)
click("1695911057493.png")
wait("1695922786473.png",10)
click("1695922800239.png")
click("1695922818080.png")
click("1695923919188.png")
click(Pattern("1695923940675.png").similar(0.86))
wait("1695923985291.png",2)
click("1695923985291.png") 
click("1695924015834.png")
doubleClick(Pattern("1695924086606.png").similar(0.90).targetOffset(33,0))
type('01012022')
doubleClick(Pattern("1695924113314.png").similar(0.90).targetOffset(32,-3))
type(data_do_dia_anterior)
doubleClick(Pattern("1695924144378.png").similar(0.85).targetOffset(45,-1))
type('2,3,5,6,12,13')
doubleClick(Pattern("1695924174539.png").similar(0.76).targetOffset(27,-5))
type('003')
doubleClick(Pattern("1695924197074.png").targetOffset(50,1))
type('109')
click("1695924224356.png")
wait(Pattern("1695924271914.png").exact(),200)
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
type('borderotop')
click(Pattern("1695910965711.png").exact())
wait(200)
click("1695911057493.png")
click("1695924604946.png")
click("1695924619382.png")
click("1695924632148.png")
keyDown(Key.CTRL)
click(Pattern("1697807284964.png").exact())
click(Pattern("1697807313491.png").exact())
click(Pattern("1697807329981.png").exact())
keyUp(Key.CTRL)

# Copie o ícone para a área de transferência
type("c", Key.CTRL)
click(Pattern("1696276655498.png").similar(0.95).targetOffset(-28,-2))
sleep(5)
sleep(5)
doubleClick(Pattern("1696336171608-1.png").similar(0.92))
sleep(2)
click(Pattern("1696876253706.png").targetOffset(-11,115))
type("v", Key.CTRL)
sleep(1)
while exists("1696876316980.png"):
    click("1696876330645.png")
click(Pattern("1696337637998-1.png").similar(0.93).targetOffset(492,0))
click("1696276781684-1.png")
click(Pattern("1696276804309-1.png").targetOffset(244,-4))
click(Pattern("1696276827112-1.png").similar(0.88).targetOffset(-45,0))

