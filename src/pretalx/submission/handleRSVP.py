import csv
from pretalx.submission.models import Submission



def checkAttendee (request, submission):
    print("in register RSVP")

    try:
        print("check if valid attentt")
        email = request.POST['email']
        print("email")
        authKey = request.POST['authKey']
        print("key")

        with open('data/sampleAttendeeList.txt') as csvfile:
            data = list(csv.reader(csvfile))
        print(data)

        for entry in data:
            if(authKey == entry[2]):
                print("valid attendee add to list")
                if not registeredForWorkshop(entry, submission):
                    if registerAttendee(entry, submission):
                        return 2 #success
                    else:
                        return 1 #fail
                else:
                    return 3 #already registered
        return 1 #fail
    except:
        return 1 #fail

def registerAttendee(attendeeInfo, submission):
    attendeeInfo = str(attendeeInfo).replace("[","").replace("]","").replace("\'","")
    if submission.attendees is None:
        submission.attendees= attendeeInfo
    else:
        attendees = submission.attendees + "\n" + attendeeInfo
        submission.attendees = attendees
    if submission.attendeeRSVP == None:
        submission.attendeeRSVP = 0
    else:
        submission.attendeeRSVP=submission.attendeeRSVP+1
    submission.save()

    return True

def registeredForWorkshop(attendeeInfo, submission):
    registerAttendees = submission.attendees.splitlines()
    registerAttendees = csv.reader(registerAttendees, delimiter=',')

    for registeredAttendee in registerAttendees:
        print(registeredAttendee)
        if registeredAttendee[2].strip() == attendeeInfo[2].strip():
            print("already registered")
            return True
    return False
