import json
x=int(input("enter 1 to create, 2 to read, 3 to delete: "))
if x==1:
      ch=input("It is first time Y/N??")
      if ch=='Y':
            key=input("Enter the key: ")
            value=input("Enter the value: ")
            dic=dict()
            dic[key]=value
            with open('my_dict.json', 'w') as f:
                  json.dump(dic,f)
      else:
            key=input("Enter the key: ")
            value=input("Enter the value: ")
            dic=dict()
            dic[key]=value
            with open('my_dict.json', 'r') as f:
                  data= json.load(f)
            master=dict(data)
            master.update(dic)
            with open('my_dict.json', 'w') as f:
                json.dump(master,f)
elif x==2:
    data={}
    with open('my_dict.json', 'r') as f:
        data= json.load(f)
    key=input("Enter the key  to read: ")
    if key in data.keys():
        print(key,"=",data[key])
    else:
        print("Error")
elif x==3:
      data={}
      with open('my_dict.json', 'r') as f:
            data= json.load(f)
      key=input("Enter the key to delete: ")
      if key in data.keys():
            del data[key]
            with open('my_dict.json', 'w') as f:
                  json.dump(data,f)
      else:
            print("Error")

with open('my_dict.json', 'r') as f:
    data1= json.load(f)
print(data1)
