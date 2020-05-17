from datetime import datetime

'''
This is the key needed to access the 
user dictionary on the cotext.bot_data 
dictionary.
'''
userKey = "userDict"

'''
This is the key needed to access the 
random # of messages on the cotext.chat_data 
dictionary.
'''
randomKey = "randomMsg"

def printTime(textToPrint):
    now = datetime.now()
    current_time = now.strftime("[%Y/%m/%d - %r]")
    print(current_time, textToPrint)

def isMessageFromAGroup(typeOfMessage):
    return "group" in typeOfMessage or "channel" in typeOfMessage

def isNoEmptyDict(pDict):
    return bool(pDict)

def getMentions(entitiesDict, typeToSearch):
    for entity, text in entitiesDict.items():
        if(entity.type == typeToSearch):
            return text
    return None

def userIDFromUsername(username, userDict):
    test = userDict
    validUsername = username[1:]                    #The username on the dictionary does not contain 
                                                    #the "@" at the begining. It needs to be removed
                                                    #to be a valid key for the dictionary.
    if(validUsername in userDict):
        return userDict[validUsername]
    else:
        return None

def generateRandom():
    return 0

def processImage(mention, bot_data, chat_data):
    msgsToNextPicture = 0
    if(randomKey not in chat_data):
        msgsToNextPicture = generateRandom()
    else:
        msgsToNextPicture = chat_data[randomKey] - 1

    if(msgsToNextPicture < 1 and userKey in bot_data):
        userId = userIDFromUsername(mention, bot_data[userKey])
        if(userId):
            chat_data[randomKey] = generateRandom()
        return userId
    else:
        chat_data[randomKey] = msgsToNextPicture
        return None

def addUserIDToDict(messageUser, userDict):
    test = userDict
    userDict[messageUser.username] = messageUser.id
    return userDict

def processUser(messageUser, bot_data):
    if(not messageUser.is_bot):
        if(userKey not in bot_data):
            newUserDict = {}
            bot_data[userKey] = addUserIDToDict(messageUser, newUserDict)
        elif(messageUser.username not in bot_data[userKey]):
            bot_data[userKey] = addUserIDToDict(messageUser, bot_data[userKey])

if __name__ == "__main__":
    pass