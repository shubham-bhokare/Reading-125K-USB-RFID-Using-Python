while True:

    #This Will Read Card Details From Terminal
    rfid_data = raw_input().strip()
    #Length Of Data Might Change Depending Upon Card And Reader
    #Mine Printed 10 Digit ID of Card
    if len(rfid_data) == 10:
        rfid_data = rfid_data[0:12]
        print(rfid_data)
