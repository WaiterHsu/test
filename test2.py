try:
  with open('未命名.txt','r') as rf:
    print(rf.readlines())
  print('已讀取，修改後的未命名')
except:
  print('this is false')

  
