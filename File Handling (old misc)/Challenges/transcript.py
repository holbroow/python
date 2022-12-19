file1 = open("transcript1.txt","r")
file2 = open("transcript2.txt","r")

transcript1 = []
transcript2 = []


for line in file1:
    transcript1.append(line.strip())


for line in file2:
    transcript2.append(line.strip())


lengthT1 = len(transcript1)
lengthT2 = len(transcript2)



for i in range(lengthT1):
    print(transcript1[i])
    print(transcript2[i])


file1.close()
file2.close()

