
import time, pypresence, struct
from pypresence import *

clientID = "928300760989569084"
detay = "On drugs."
durum = "Overdose."
yenilenme = "10"
buyuk = "canabis"
buyukT = "Kill me pls."
buton1Yazi = "Join"
buton1Link = "https://www.youtube.com/watch?v=5QCaaAyz-yA"

RPC = Presence(clientID)
RPC.connect()
zaman = int(time.time())

while True:
    RPC.update(
        state = durum,
        details = detay,
        large_image = buyuk,
        large_text = buyukT,
        start = zaman,
        buttons = [{"label": buton1Yazi, "url": buton1Link}]
    )
    time.sleep(int(yenilenme))