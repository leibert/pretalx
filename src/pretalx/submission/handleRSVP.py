import csv
from pretalx.submission.models import Submission
import hashlib



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
        print("key done")

        with open('/var/pretalx/data/attendee-secret-codes-hashed') as file:
            for line in file:
                print(line.replace("-","").strip())
                if(authKey == line.replace("-","").strip()):
                    print("valid attendee add to list")
                    if registeredForWorkshop(attendeeInfo, submission):
                        return "3"
                    else:
                        print("registering attendee")
                        if registerAttendee(attendeeInfo, submission):
                            return "2" #success
                        else:
                            return "1" #fail
            return "1"
    except:
        print(e)
        return 1 #fail

    return "1"

def registerAttendee(attendeeInfo, submission):
    # attendeeInfo = str(attendeeInfo).replace("[","").replace("]","").replace("\'","")
    if submission.attendees is None:
        submission.attendees= attendeeInfo["name"] + " "+attendeeInfo["email"]+","+attendeeInfo["hashed"]
    else:
        attendees = submission.attendees + "\n" + attendeeInfo["name"] + " "+attendeeInfo["email"]+","+attendeeInfo["hashed"]
        submission.attendees = attendees

    if submission.attendeeRSVP == None:
        submission.attendeeRSVP = 1
    else:
        submission.attendeeRSVP=submission.attendeeRSVP+1
        
    submission.save()

    return True

def registeredForWorkshop(attendeeInfo, submission):

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
