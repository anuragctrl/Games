import qrcode

n = input("Enter Text or Link: ").strip()
file = input("Enter the File Name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(n)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file)

print(f"File is saved as {file}")