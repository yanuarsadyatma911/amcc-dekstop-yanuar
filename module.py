#module

import sys
print('commandilen argumrnts')
for i in sys.argv:
    """
    kita dapat memberikan argumen saat menjalankan
    progrsm python
    """
    print(i)

if __name__ == 'main':
    print('run itselt')
else:
    print('run from another module')
    


print (sys.argv)
print (sys.path)

#module


