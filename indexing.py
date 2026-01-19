Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #indexing
>>> 
>>> a="vijayawada"
>>> a=[4]
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> a="vijayawada"
>>> a[4]
'y'
>>> a[7]
'a'
>>> a[0]+a[1]
'vi'
>>> a[7]+a[8]+a[9]+a[5]
'adaa'
>>> 
>>> #indexing with sentence
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> 
>>> #task
>>> a=" i love python"
>>> a="i love python"
>>> a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
>>> a[2]+a[3]+a[4]+a[5]
'love'
>>> 
>>> b="i am learning python coourse"
>>> a[2]+a[3]
'lo'
>>> b[2]+b[3]
'am'
>>> b[5]+b[6]+b[7]+b[8]+b[9]+b[10]
'learni'
>>> b[5]+b[6]+b[7]+b[8]+b[9]
'learn'
>>> b[21]+b[22]+b[24]+b[25]+b[26]+b[27]
'course'
>>> 
>>> c="vijayawada is a royal city"
c[16]+c[17]+c[18]+c[19]+c[20]
'royal'
c[22]+c[23]+c[24]+c[25]
'city'
c[11]+c[12]
'is'

\

#Negative Indexing
a="work until you succeed'
SyntaxError: unterminated string literal (detected at line 1)
a="work until you succeed"
a[-13]+a[-14]+a[-15]+a[-16]+a[-17]
'litnu'
a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'until'
a[-22]+a[-21]+a[-20]+a[-19]
'work'
a[-11]+a[-10]+a[-9]
'you'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'succeed'

b="simple is better than complex"
b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'better'
b[-7]+b[-6]+b[-5]+b[-[4]+b[-3]+b[-2]+b[-1]
                    b[-7]+b[-6]+b[-5]+b[-[4]+b[-3]+b[-2]+b[-1]
                                        
SyntaxError: '[' was never closed

b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
                                        
'complex'




]
                    
SyntaxError: unmatched ']'
b[-12]+b[-11]+b[-10]+b[-9]
                    
'than'

()
                    
()
#Slicing
                    
