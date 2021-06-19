import qrcode
import sys
import time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END ,WARNING = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[93m'
def fancyDisplay(string, color = WARNING):
	sys.stdout.write(color)
	for i in string:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)
	sys.stdout.write(WHITE)
	return

def generate_qr_code():
	qr = qrcode.QRCode( version = 1, error_correction = qrcode.constants.ERROR_CORRECT_Q, box_size = 10, border = 4 )
	fancyDisplay("Enter URL : ", RED)
	qr.add_data(input())
	qr.make(fit=True)
	
	image= qr.make_image(fill_color='black', back_color='white')
	fancyDisplay("Enter filename : ", YELLOW)
	image.save(	input()+".png")

generate_qr_code()