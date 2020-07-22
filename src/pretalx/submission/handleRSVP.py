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
            if(email == entry[1]):
                print("positive email match")
                if(authKey == entry[2]):
                    print("valid attendee add to list")
                    registerAttendee(entry, submission)
                    return True
        return False
    except:
        return False

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
