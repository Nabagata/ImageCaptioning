import pickle
from build_vocab import Vocabulary 

## open a file, where you stored the pickled data
#file = open('vocab1.pkl', 'rb')

## dump information to that file
#data = pickle.load(file)

## close the file
#file.close()

#print('Showing the pickled data:')

#cnt = 0
#for item in data:
#    print('The data ', cnt, ' is : ', item)
#    cnt += 1

objects = []
with (open("vocab1.pkl", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
            
for i in objects:
	print(i.word2idx)
