//QR CODE VERIFICATION

import cv2 as cv
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
import wiotp.sdk.device

authenticator=BasicAuthenticator('apikey-v2-1w8tqt2prt3j7qz9d1rgrxhar3w9v43i2359u79ut5jb','86181a38eca19ae487f512b10aca0c80')
service=CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-1w8tqt2prt3j7qz9d1rgrxhar3w9v43i2359u79ut5jb:86181a38eca19ae487f512b10aca0c80@9163f25a-10b8-4374-a8de-cb92e4357567-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_PLAIN
if not cap.isOpened():
    print("Cannot open camera")
    exit()


myConfig = {
    "identity" :{
        "orgId":"78kd0j",
        "typeId":"ltx33",
        "deviceId":"12345678"
        },
    "auth":{
        "token":"LTx@33333"
        }
    }
def myCommandCallback(cmd):
    print("Message received fromIBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub(data):
    client.publishEvent(eventId = "status", msgFormat="json", data=response, qos=0, onPublish=None)
    print("Published data Successfully: %s",response)
    print("\n")

while True:
    ret, frame=cap.read()
    decodedObjects = pyzbar.decode(frame)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    for obj in decodedObjects:
        a=obj.data.decode('UTF-8')
        cv.putText(frame, "Ticket", (50,50),font,2,
                    (255 ,0, 0),3)

        try:
            response=service.get_document(
                db='bookingdetails',
                doc_id = a
                ) .get_result()
            print(response)
            print("\n\n")
            pub(response)
            time.sleep(5)
        except Exception as e:
            response={'Error':'Not a Valid Ticket'}
            pub(response)
            print("Not a Valid Ticket")
            print("\n\n")
            time.sleep(5)

    cv.imshow("Frame" ,frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    client.commandCallback = myCommandCallback
cap.release()
cv.destroyAllWindows()
client.disconnect()


//Train3GoaExpress

import wiotp.sdk.device
import time
import random
myConfig = {
    "identity" :{
        "orgId":"78kd0j",
        "typeId":"ltx33",
        "deviceId":"12345678"
        },
    "auth":{
        "token":"LTx@33333"
        }
    }
def myCommandCallback(cmd):
    print("Message received fromIBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub(data):
    client.publishEvent(eventId = "status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s",myData)

while True:
    myData = {'name':'Train3','lat':11.688572, 'lon':78.098877}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':11.711433, 'lon':78.076905}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':11.978226,  'lon':78.116730}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':12.085676, 'lon': 78.119477}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':12.402400, 'lon':78.023347}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':12.884795, 'lon':77.707490}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.018630,'lon'77.614106:}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.334194, 'lon':77.086762}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.299448, 'lon':76.858796}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.344884,'lon': 76.205109}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.619985, 'lon':75.966157}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':13.974739, 'lon':76.119965}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':14.423398, 'lon':75.949677}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':14.922914, 'lon':75.389374}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.119216, 'lon':75.389374}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.449980, 'lon':74.406230}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.352006,'lon':74.307353}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.314922, 'lon':74.218089}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.283131, 'lon':74.146678}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.276839, 'lon':74.129855}
    pub(myData)
    time.sleep(3)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.282800, 'lon':74.125392}
    pub(myData)
    time.sleep(3)
    time.sleep(3)
    myData = {'name':'Train3','lat':15.296378,'lon':74.135692}
    pub(myData)
    time.sleep(3)
    client.commandCallback = myCommandCallback
client.disconnect()

