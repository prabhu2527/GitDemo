try:
    #with open ('sample.txt','r') as reader:
    with open('sample2.txt', 'r') as reader:
        reader.read()
except:
    print("Some how I reached here because of failure in try block")