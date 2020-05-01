import qrcode
#setting the qr code size and width
qr=qrcode.QRCode(version=1, box_size=10, border=5)
# setting the data to the qr code
data = 'hii i am Niranjan'

qr.add_data(data)
qr.make(fit=True)
# saving the qr code as image
myqrcode = qr.make_image(fill='black', back_color='white')

myqrcode.save('Myqrcode.png')


