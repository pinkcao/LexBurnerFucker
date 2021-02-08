# fuckLexBurner
由下水道居民制作，运行后自行设定以x秒间隔获取lexBurner粉丝数量并保存至同目录txt文件下。

## use with multiple threads:
```python
import fuckLex,_thread

try:
    _thread.start_new_thread(fuckLex.getTextAndWrite, ('fuckLex.txt',)) #获取数据写入fuckLex.txt
    _thread.start_new_thread(fuckLex.outPutDecreseStringInterval, ('fuckLex.txt', 60, 'fuckLexOutput.txt',) ) #朴素地分析数据并写入fuckLexOutput.txt
except:
    print("Error: 无法启动线程")

while 1:
    pass
```

## basic usage

### getTextAndWrite(filename):
descrption: get the fans sum and write it into 'fuckLex.txt'<br>
params: `String`<br>
return: `null`
```python
import fuckLex
fuckLex.getTextAndWrite('fuckLex.txt')
```

### get():
descrption: get current fans count<br>
Params: `null`<br>
return: `int`
```python
import fuckLex
print(fuckLex.get())
```

### calcDecreseSum(filename):
descrption: get the decreseSum <br>
Params: `String`<br>
return: `int`

```python
import fuckLex
print(fuckLex.calcDecreseSum('fuckLex.txt'))
```

### outPutDecreseString(filename):
descrption: get the decrese String <br>
Params: `String`<br>
return: `String`
```python
import fuckLex
print(fuckLex.outPutDecreseString('fuckLex.txt'))
```
-->from  Mon Feb  8 11:42:27 2021<br>
 to  Mon Feb  8 15:08:37 2021<br>
 lexBurner fans decresed: 50925

### outPutDecreseStringInterval(filename, interval):
descrption: get the decrese String at certain interval<br>
Params: `String, int`<br>
return: `null`
```python
import fuckLex
print(fuckLex.outPutDecreseStringInterval('fuckLex.txt', 60))
```

### outPutDecreseStringIntervalToFile(filename, interval, destfilename):
descrption: get the decrese String at certain interval and write record into certain file<br>
Params: `String, int, String`<br>
return: `null`
```python
import fuckLex
print(fuckLex.outPutDecreseStringInterval('fuckLex.txt', 60, 'fuckLexOutput.txt'))
```


