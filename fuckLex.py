import json,requests,time
def get():
    return int(json.loads(requests.get("https://api.bilibili.com/x/relation/stat?vmid=777536").text)["data"]["follower"])

def getTextAndWrite(filename):
    fansCountLast = -1
    filename = filename
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

def calcDecreseSum(filename):
    fname = filename
    with open(fname, 'r', encoding='utf-8') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        first_line = lines[0]  # 取第一行
        last_line = lines[-1]  # 取最后一行
        print(first_line)

        firstStamp = first_line.split('Time:')[1]
        lastStamp = last_line.split('Time:')[1]
        firstFansCount = first_line.split(' ')[1].split(':')[1]
        lastFansCount = last_line.split(' ')[1].split(':')[1]
        return int(firstFansCount) - int(lastFansCount)

def outPutDecreseString(filename):
    fname = filename
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        first_line = lines[0]
        last_line = lines[-1]
        print(first_line)

        firstStamp = first_line.split('Time:')[1]
        lastStamp = last_line.split('Time:')[1]
        firstFansCount = first_line.split(' ')[1].split(':')[1]
        lastFansCount = last_line.split(' ')[1].split(':')[1]
        return 'from ' + firstStamp + ' to ' + lastStamp + ' lexBurner fans decresed: ' + str(int(firstFansCount) - int(lastFansCount))

if __name__ == '__main__':
    # getTextAndWrite('fuckLex.txt')
    # print(calcDecreseSum('fuckLex.txt'))
    print(outPutDecreseString('fuckLex.txt'))