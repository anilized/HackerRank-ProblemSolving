# Convert AM/PM to Military
# s is a string
# only need to change the hours to convert the time from an AM/PM format to 24 hour format
# We need to add +12 to the hours if the time is in PM.
def timeConversion(s):
    zn = s[-2:]
    if zn == "PM" and s[:2] != "12":
        s = str(12 + int(s[:2])) + s[2:]
    if zn == "AM" and s[:2] == "12":
        s = "00" + s[2:]
    print (s[:-2])
    
timeConversion("07:05:45PM")