try:
    #with open ('sample.txt','r') as reader:
    with open('sample2.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)