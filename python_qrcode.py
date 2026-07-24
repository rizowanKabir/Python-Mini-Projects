import qrcode as qr 
image = qr.make("https://blood-finder-web-app.onrender.com/")
image.save("blood_finder_qrcode.png") 