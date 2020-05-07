import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class text_analysis:  
    """
    Class Info
    ----------------
    Developer: 
        Epsom Enrique Segura Jaramillo
    Institution:
        Universidad Veracruzana
        Maestría en Sistemas Interactivos Centrados en el Usuario
    Description
        A class to represent a text analysis
    
    Attributes
    ----------------
    file_path: String  
        The relative path to txt file

    Methods
    ----------------
    readText(file_path)
        Read a TXT file and return a String with the content
    getStopwords()
        Return a list that contains the spanish stopwords
    getLemmas()
        Read a relative path to TXT file that contains a list of lemma words
        That lemma words parsed to a dictionary for a future use
    getSentences()
        Read a string that contains a text, the text is analized and split in sentences and return a list of sentences
    getTokens()
        Read a list of sentences and each of this sentences is analized and splited in tokens, return a list that contains all the tokens from all the sentences
    getTokensBySentence(sentence)
        Read a sentence and is analized and splited in tokens, return a list with all the tokens from one sentence
    stopwordsReduction(tokens)
        Read a list of tokens, clear non alhpanumeric characters and reduce info clearing all the stopWords contained in text
    snowballStemmerReduction(tokens)
        Read a list of tokens and apply the Porter´s 2 algorithm to reduce the content
    lemmaReduction(tokens)
        Read a list of tokens and replace by lemmas if exists in corpus
    frequencyDistribution(tokens)
        Create a dictionary with the result of evaluate the frequency of items from a list of tokens ordered by descendent frequency
    printFrequencyDistribution(freqDist)
        Print each item from the freqDist dictionary
    """
    # Constructor
    def __init__(self,file_path):
        """
        Parameters
        ----------------
        file_path: String 
            The relative path to TXT file
        Variables
        ----------------
        lemmas_path: String
            The relative path to lemmatization words
        text: String
            The string of a TXT file
        stopwords: list()
            The list of NLTK spanish stopwords
        lemmas: dict()
            The dictionary analized from lemmas_path TXT file
        sentences: list()
            The list of sentences analized from readed text file
        tokens: list()
            The tokens analized from sentences
        """
        self.lemmas_path = "./src/lemmatization-es.txt"

        self.text = self.readText(file_path)
        self.stopwords = self.getStopwords()
        self.lemmas = self.getLemmas()
        self.sentences = self.getSentences()
        self.tokens = self.getTokens()
        self.removeSW = self.stopwordsReduction(self.tokens)
        


    # Read Text Function
    def readText(self,file_path):
        """
        Parameters
        ----------------
        file_path: String (The relative path to TXT file)
        Description
        ----------------
        Read a TXT file and return a String with the content
        Return
        ----------------
        read_text: String (The content of a TXT file)
        """
        fp = open(file_path,'r',encoding="UTF-8")
        read_text = fp.read()
        fp.close()
        return read_text





    # Get Stopwords Function
    def getStopwords(self):
        """
        Description
        ----------------
        Return a list that contains the spanish stopwords
        Return
        ----------------
        sw: list() (The list of spanish stopwords)
        """
        sw = stopwords.words("spanish")
        return sw


    
    # Get Lemmas Function
    def getLemmas(self):
        """
        Description
        ----------------
        Read a relative path to TXT file that contains a list of lemma words
        That lemma words parsed to a dictionary for a future use
        Return
        lemmas: dict() (The dict of lemma words)
        """
        lemmas = dict()
        fp = open(self.lemmas_path,'r',encoding="utf-8-sig")
        lines = fp.readlines()
        fp.close()
        for i in lines:
            temp = i.rstrip("\n")
            lp = temp.replace("\t","-").split('-')
            lemmas.update({lp[1] : lp[0]})
        
        return lemmas




    # Get sentences from text Function
    def getSentences(self):
        """
        Description
        ----------------
        Read a string that contains a text, the text is analized and split in sentences and return a list of sentences
        Return
        ----------------
        sentences: list() (A list of sentences from text)
        """
        sentences_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
        sentences = sentences_tokenizer.tokenize(self.text)
        return sentences





    # Get tokens from sentences
    def getTokens(self):
        """
        Description
        ----------------
        Read a list of sentences and each of this sentences is analized an splited in tokens, return a list that contains all the tokens from all the sentences
        Return
        ----------------
        tokens: list()
            A list with all tokens from all sentences
        """
        tokens = list()
        toktok = ToktokTokenizer()
        for s in self.sentences:
            for t in toktok.tokenize(s):
                tokens.append(t)
        return tokens

    



    # Get tokens from a sentence
    def getTokensBySentence(self,sentence):
        """
        Description
        ----------------
        Read a sentence and is analized an splited in tokens, return a list that contains the tokens from this sentence
        Return
        ----------------
        tokens: list()
            A list with all tokens from one sentence[]
        """
        tokens = list()
        toktok = ToktokTokenizer()
        for t in toktok.tokenize(sentence):
            tokens.append(t.lower())
        return tokens





    # StopwordsReduction
    def stopwordsReduction(self,tokens):
        """
        Parameters
        ----------------
        tokens: list()
            A list of tokens to apply stopWordsReduction
        Description
        ----------------
        Read a list of tokens, clear non alhpanumeric characters and reduce info clearing all the stopWords contained in text
        Return
        ----------------
        tokens: list()
            Return a list of tokens without stopWords and not alphanumeric symbols
        """
        regexp = r"^[üá-úÁ-Úa-zA-Z0-9]*$"
        i=0
        stopW = self.getStopwords()
        mx = len(tokens)
        while i < mx:
            if re.match(regexp,tokens[i]):
                if tokens[i].lower() in stopW:
                    del tokens[i]
                    mx-=1
                elif tokens[i][0]=="“":
                    tokens[i]=tokens[i].lstrip("“")
            else:
                del tokens[i]
                mx-=1
            i+=1
        return tokens





    # SnowballStemmerReduction
    def snowballStemmerReduction(self,tokens):
        """
        Parameters
        ----------------
        tokens: list()
            A list of stopwords reduced tokens
        Description
        ----------------
        Read a list of tokens and apply the Porter´s 2 algorithm to reduce the content
        Return
        ----------------
        r_tokens: list()
            A list of tokens reduced by Porter´s 2 algorithm
        """
        stemmer = SnowballStemmer("spanish")
        r_tokens=[]
        for i in tokens:
            r_tokens.append(stemmer.stem(i))
        
        return r_tokens





    # LemmaReduction
    def lemmaReduction(self,tokens):
        """
        Parameters
        ----------------
        tokens: list()
            A list of stopwords reduced tokens
        Description
        ----------------
        Read a list of tokens and replace by lemmas if exists in corpus
        Return
        ----------------
        tokens: list()
            A list of tokens replaced by lemmas if exists in corpus
        """
        lemmas = self.lemmas
        for i in tokens:
            n=tokens.index(i)
            if i in lemmas.keys():
                tokens[n] = lemmas.get(i)
        return tokens





    # frequencyDistribution
    def frequencyDistribution(self,tokens):
        """
        Parameters
        ----------------
        tokens: list()
            A list of tokens
        Description
        ----------------
        Create a dictionary with the result of evaluate the frequency of items from a list of tokens ordered by descendent frequency
        Return
        ----------------
        freqDist: dict()
            A dictionary sorted by frequency of items ordered by descendent frequency
        """
        freqDist = dict()
        for i in tokens:
            if i in freqDist:
                freqDist[i]+=1
            else:
                freqDist[i]=1
        return sorted(freqDist.items(),key=lambda x:x[1],reverse=True)

    



    # printFrequencyDistribution
    def printFrequencyDistribution(self, freqDist):
        """
        Parameters
        ----------------
        freqDist: dict()
            A dictionary that contains the frequency of items
        Description
        ----------------
        Print each item from the freqDist dictionary
        """
        for i in freqDist:
            print(i[0]+'\t'+('' if len(i[0])>15 else '\t')+('\t' if len(i[0])<8 else '')+'=>\t'+str(i[1]))



if __name__ == "__main__":
    txt_a = text_analysis("./src/practica3.txt")

    # Tokens originales
    print('*****************************************************************************')
    print('*\tTokens originales')
    print('*\tDistribución de frecuencias de los tokens('+str(len(txt_a.getTokens()))+')\n')
    print('*****************************************************************************')
    txt_a.printFrequencyDistribution(txt_a.frequencyDistribution(txt_a.getTokens()))



    # Tokens Stemmer
    print('*****************************************************************************')
    print('*\tTokens sin stopwords y reducción Stemmer')
    print('*\tDistribución de frecuencias de los tokens('+str(len(txt_a.snowballStemmerReduction(txt_a.stopwordsReduction(txt_a.getTokens()))))+')\n')
    print('*****************************************************************************')
    txt_a.printFrequencyDistribution(txt_a.frequencyDistribution(txt_a.snowballStemmerReduction(txt_a.stopwordsReduction(txt_a.getTokens()))))



    # Tokens Lemma
    print('*****************************************************************************')
    print('*\tTokens sin stopwords y reducción por lemas')
    print('*\tDistribución de frecuencias de los tokens('+str(len(txt_a.lemmaReduction(txt_a.stopwordsReduction(txt_a.getTokens()))))+')\n')
    print('*****************************************************************************')
    txt_a.printFrequencyDistribution(txt_a.frequencyDistribution(txt_a.lemmaReduction(txt_a.stopwordsReduction(txt_a.getTokens()))))
   