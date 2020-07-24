import csv
from pretalx.submission.models import Submission
import hashlib
import logging
LOGGER = logging.getLogger(__name__)


def checkAttendee (request, submission):
    print("in register RSVP")

    try:
        attendeeInfo={}
        print("check if valid attentt")
        try:
            attendeeInfo['name'] = request.POST['name']
        except:
            attendeeInfo['name'] = ""
        attendeeInfo['email'] = request.POST['email']
        authKey = hashlib.sha256(request.POST['authKey'].encode('utf-8')).hexdigest()
        attendeeInfo['hashed']=authKey

        print(request.POST['authKey'])
        print(authKey)
        logging.info(authKey)
        logging.info(attendeeInfo['name'])
        logging.info(attendeeInfo['email'])
        logging.info(submission)
        print("key done")

        with open('/var/pretalx/data/attendee-secret-codes-hashed') as file:
            for line in file:
                print(line.replace("-","").strip())
                if(authKey == line.replace("-","").strip()):
                    print("valid attendee add to list")
                    if registeredForWorkshop(attendeeInfo, submission):
                        logging.info("already")
                        return "3"
                    else:
                        print("registering attendee")
                        if registerAttendee(attendeeInfo, submission):
                            logging.info("sucess")
                            return "2" #success
                        else:
                            logging.info("fail A")
                            return "1" #fail
            logging.info("fail D")   
            return "1"
    except:
        # print(e)
        logging.info("fail C")   
        return "1" #fail


    return "1"

def registerAttendee(attendeeInfo, submission):
    # attendeeInfo = str(attendeeInfo).replace("[","").replace("]","").replace("\'","")
    logging.info("!!!!!!!!!!!!!!! IN Z")   

    if submission.attendees is None:
        submission.attendees= attendeeInfo["name"] + " "+attendeeInfo["email"]+","+attendeeInfo["hashed"]
        logging.info("fail Z1")   
    else:
        attendees = submission.attendees + "\n" + attendeeInfo["name"] + " "+attendeeInfo["email"]+","+attendeeInfo["hashed"]
        submission.attendees = attendees
        logging.info("fail Z2")   


    if submission.attendeeRSVP == None:
        submission.attendeeRSVP = 1
        logging.info("fail Z3")   

    else:
        submission.attendeeRSVP=submission.attendeeRSVP+1
        logging.info("fail Z5")   

    logging.info("fail Z7")   
    submission.save()
    logging.info("fail Z6")   


    return True

def registeredForWorkshop(attendeeInfo, submission):
    logging.info("in Y")   

    if not submission.attendees:
        return False
        
    if submission.attendees == "":
        ##field is currently empty
        return False
    registeredAttendees = submission.attendees.splitlines()
    registeredAttendees = csv.reader(registeredAttendees, delimiter=',')

    for registeredAttendee in registeredAttendees:
        print(registeredAttendee)
        if registeredAttendee:
            if registeredAttendee[1].strip() == attendeeInfo["hashed"].strip():
                print("already registered")
                return True

    return False
