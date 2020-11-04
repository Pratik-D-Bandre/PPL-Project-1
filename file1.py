import qrcode
qr=qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
    
    )

data = "Hello !!! Welcome to College of Engineering, Pune(COEP).\nIf you want more information about COEP, click on the Link below:\nhttps://www.coep.org.in/"
#data = "https://www.coep.org.in/"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", black_color = "white")
img.save("coep.png")