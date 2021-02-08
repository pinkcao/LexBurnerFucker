import json,requests,time
def get():
    return int(json.loads(requests.get("https://api.bilibili.com/x/relation/stat?vmid=777536").text)["data"]["follower"])

def getTextAndWrite():
    fansCountLast = -1
    filename = 'fuckLex.txt'
    printFlag = False
    interval = int(input('请输入获取间隔'))
    while True:
        file_object = open(filename, 'a')
        fansCount = get()
        fansCountMinus = fansCountLast - fansCount
        localtime = time.asctime(time.localtime(time.time()))
        lexString = 'lexBurner fans:' + str(fansCount) + ' decreaseNum: ' + str(fansCountMinus) + ' Time: ' + str(localtime)
        if (printFlag):
            file_object.write(lexString + '\n')
            print(lexString)
        fansCountLast = fansCount
        printFlag = True
        file_object.close()
        time.sleep(interval)


if __name__ == '__main__':
    getTextAndWrite()