# Simple function to convert 2 bytes of data
    # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(self):
    data = bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
    return self.convertToNumber(data)

def main():
    sensor = LightSensor()
    try:
        while True:
            print("Light Level : " + str(sensor.readLight()) + " lx")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    