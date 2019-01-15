
import matplotlib.pyplot as plt

filtered = ["der", "die", "das", "ein", "eine", "einer", "es", "ist", "für", "im", "wird", 
"auch", "mit", "aus", "von", "als", "in", "werden", "wurde", "oder", "auf", "wie", "den" ,
"zu", "dieser", "nicht", "sind", "des", "einen", "um", "können" , "nur", "diese", "wird", 
"eines", "über", "hier", "dem", "so", "werde," ,"werde.", "werden." ,"dies", "muss", "alle", 
"an" , "das", "der", "nach", "zum", "gibt", "da", "mehr", "dass", "gibt", "zum" ]



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
    wordArray = []  
    for word in allWords:
        if len(allWords[word]) > 10 and word.lower() not in filtered:
            tmpArray = []
            for index in allWords[word]:
                tmpArray.append(len(tmpArray)) 
            wordArray.append(word)

            plt.scatter(allWords[word], tmpArray)
            print(word, len(tmpArray))
        
    plt.legend(wordArray)
    plt.show()
   

if __name__ == "__main__":
    main()
