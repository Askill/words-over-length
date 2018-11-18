
import matplotlib.pyplot as plt

def main():
    filename = "test.txt"
    allWords = {}
    counter = 0
    for line in open(filename, 'r'):  
        words = line.split(' ')
        if '\n' in words:
            words.remove("\n")
        for word in words:
            if word not in allWords:
                allWords[word] = [counter]
            else:
                allWords[word].append(counter) 
            counter+=1
            
    # x,y,z for ribbon Plot
    wordArray = [] #x
    indexes = []   #y
    counts = []    #z
    for word in allWords:
        if len(allWords[word]) > 10:
            tmpArray = []
            for index in allWords[word]:
                tmpArray.append(len(tmpArray)) 

            counts.append(tmpArray)
            indexes.append(allWords[word])
            wordArray.append(word)

            plt.plot(allWords[word], tmpArray)
           
    plt.legend(wordArray)
    plt.show()
   

if __name__ == "__main__":
    main()