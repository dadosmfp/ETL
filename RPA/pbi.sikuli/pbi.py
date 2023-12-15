
doubleClick(Pattern("1702572469791.png").similar(0.95))

wait(Pattern("1702572545335.png").similar(0.96),200)

click("1702572567881.png")
sleep(60)
if exists(Pattern("1702572694721.png").similar(0.48)):
        click(Pattern("1702578140372.png").similar(0.53).targetOffset(181,71))
        click("1702572567881.png")
else: 
    click("1702572731571.png")
wait("1702572775202.png",100)
click(Pattern("1702572782984.png").targetOffset(60,48))
wait(Pattern("1702572821825.png").similar(0.50),60)
click(Pattern("1702572835937.png").targetOffset(127,150))
wait("1702572858297.png",60)
click(Pattern("1702572869620.png").targetOffset(-38,4))
sleep(60)
click(Pattern("1702577403380.png").similar(0.89))
wait("1702572898371.png",60)
click(Pattern("1702572909456.png").targetOffset(190,115))
click(Pattern("1702572941825.png").similar(0.98).targetOffset(170,-33))