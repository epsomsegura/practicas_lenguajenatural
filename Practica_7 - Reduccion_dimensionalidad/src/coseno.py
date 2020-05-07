from src.text_analysis import text_analysis
import math

class coseno:
    def __init__(self):
        self.ta = text_analysis("src/author_corpus_all.txt")
        self.readText = self.ta.sentences

        self.clear_text = self.clearText()
        self.vectors,self.vocabulary = self.matrix(self.clear_text)
        self.coseno_matrix = self.coseno_matrix(self.vectors)

        self.console_matrix(self.coseno_matrix)
        self.save_csv(self.coseno_matrix)

        
    def clearText(self):
        no_stopwords=list()
        for i in self.readText:
            tbs = self.ta.getTokensBySentence(i)
            nsw = self.ta.stopwordsReduction(tbs)
            nl = self.ta.lemmaReduction(nsw)
            no_stopwords.append(nl)
        return no_stopwords
    

    def normalize_text(self,sentences):
        normalized_text_list = []
        vocabulary = []
        for i in sentences:
            for j in i:
                if j not in vocabulary:
                    vocabulary.append(j)
            normalized_text_list.append(i)
        return normalized_text_list, vocabulary

    def matrix(self,sentences):
        normalize_text, vocabulary = self.normalize_text(sentences)
        vocabulary.sort()
        vectors = []
        for i in normalize_text:
            vector = []
            for j in vocabulary:
                vector.append(self.calc_tfidf(j,i,normalize_text))
            vectors.append(vector)
        return vectors, vocabulary
    
    def calc_tfidf(self,word,doc,docs):
        c_exist_doc = doc.count(word)
        tf = c_exist_doc/len(doc)
        c_exist_docs = 0
        for i in docs:
            c_exist_docs += i.count(word)
        idf = math.log(len(docs)/c_exist_docs)
        return tf*idf

    def coseno_matrix(self,matrix):
        vectors = []
        for i in matrix:
            doc1_vector = []
            for j in matrix:
                doc1_vector.append(self.calc_coseno(i,j))
            vectors.append(doc1_vector)
        return vectors

    def calc_coseno(self,doc1,doc2):
        length = len(doc1)
        add_doc1_doc2 = 0
        pow_doc1 = 0
        pow_doc2 = 0
        for i in range(length):
            add_doc1_doc2 += doc1[i] * doc2[i]
            pow_doc1 += pow(doc1[i],2)
            pow_doc2 += pow(doc2[i],2)
        coseno = add_doc1_doc2/(math.sqrt(pow_doc1)*math.sqrt(pow_doc2))
        return coseno
    
    def console_matrix(self,matrix):
        doc_size = len(matrix)
        print('DX\t',end='')
        for i in range(doc_size):
            print("D"+str((i+1))+'\t',end='')
        print('\n')
        c=1
        for i in matrix:
            print("D"+str(c)+'\t',end='')
            for j in i:
                print(str(j)+'\t',end='')
            print('\n')
            c+=1

    def save_csv(self,matrix):
        new_file = open('exports/matriz.csv','w+')
        doc_size = len(matrix)
        new_file.write("DX,")
        for i in range(doc_size):
            new_file.write("D"+str((i+1))+",")
        new_file.write('\n')
        c=1
        for i in matrix:
            new_file.write("D"+str(c)+",")
            for j in i:
                new_file.write(str(j)+",")
            new_file.write("\n")
            c+=1
        new_file.close()

if __name__ == "__main__":
    cos=coseno()
    