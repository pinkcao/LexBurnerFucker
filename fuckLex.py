import json,requests,time,_thread
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

def outPutDecreseStringInterval(filename, interval):
    while True:
        print(outPutDecreseString(filename))
        time.sleep(interval)

if __name__ == '__main__':
    try:
        _thread.start_new_thread( getTextAndWrite, ('fuckLex.txt',) )
        _thread.start_new_thread( outPutDecreseStringInterval, ('fuckLex.txt', 60, ) )
    except:
        print("Error: 无法启动线程")

    while 1:
        pass