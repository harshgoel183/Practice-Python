fw = open('sample.txt', 'w')

fw.write('Writing new stuff!!\n')
fw.write('I like coke\n')
fw.close()

fr = open('sample.txt', 'r')
#text = fr.read()
for i in fr.read().split('\n'):
    print(i)
#print()
#print(text)
fr.close()
