#Homework-1 of 'Pyhon is Easy' Course  Submitted by Abdullah Khan

#Title of the Album
Title = "Nasheed"

#Name of the Song
Name = "Mera Dil Badal Dey"

#Name of the Singer
Singer = "Junaid Jamshed"

LatestRelease = False

"""
Release Date as the below format:
Year
Month
Day
"""
Year,Month,Day = "2015", "September", "2"

# #Song Duration in Mintues & Seconds
# Duration = 5.43
# Minutes = 5
# Seconds = 43
#
# #Print Summary
# print("-------Summary-------")
# print("The Title of the Album is " + Title + ", " + "the Name of the Song is " + Name + " & " + "the singer is " + Singer + ".")
#
# #Print Details
# print('')
# print("-------Details-------")
# print("Title: " + Title)
# print("Name: " + Name)
# print("Singer: " + Singer)
# print("Release Date: " + Day +"/" + Month + "/" + Year)
# print("Duration: ", Minutes, "Minutes & ", Seconds, "Seconds")
# print('MashaAllah')

#Returns the Song Title
def STitle():
    SongTitle = Title
    return SongTitle

print(STitle())
numTwo = 2

def addOne():
    numThree = numTwo + 1
    print(numThree)
    return numThree

addOne()
#Returns Name of the Song
def Song():
    Song = Name
    print(Song)
    return Song

Song()

#Release Year
def SYear():
    Saal = Year
    print(Saal)
    return Saal

SYear()

def Release():
    NewSongYear=LatestRelease
    return NewSongYear

print("Is latest Song Available:",Release())

