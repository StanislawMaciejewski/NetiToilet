import RPi.GPIO as GPIO
import time
import datetime
import csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(27, GPIO.IN)

with open('WC_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['timestamp', 'PIR', 'FOTORES', 'OCCUPIED?']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    pirout = 0
    isOccupied = 0
    while True:
        timestamp=datetime.datetime.now()
        foto=GPIO.input(25)
        pir=GPIO.input(27)

        if pir:
            pirout=1
            timestamp_past = time.time()

        if pirout:
            if (time.time() - timestamp_past) > 30:
                pirout=0

        if pirout and foto :
            isOccupied = 1
        else:
            isOccupied = 0
        writer.writerow({'timestamp': timestamp, 'PIR': pirout, 'FOTORES': foto, 'OCCUPIED?': isOccupied})
        #print(isOccupied)
        time.sleep(1)
