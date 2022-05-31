from pickle import TRUE


f = open("demofile.txt", "r")
print(f.readline())
f.close()

f = open("demofile2.txt","a")
f.write("Now the file has more content!")
f.close()
