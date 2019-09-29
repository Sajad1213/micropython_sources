from machine import Pin,I2C
import ssd1306

i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)

lcd = ssd1306.SSD1306_I2C(128,64,i2c)
lcd.text("Micropython",0,0)
lcd.text("are",24,16)
lcd.text("Awesome",64,24)
lcd.show()

"""
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(15), machine.Pin(0), machine.Pin(16))
oled.text("hello")
"""
