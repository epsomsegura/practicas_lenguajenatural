# -*- coding: utf-8 -*-

# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 4
# Descripción: PageRank
# Por: Epsom Enrique Segura Jaramillo


from text_analysis import text_analysis
from node import node

from datetime import datetime
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import re

class pageRank:
    # Constructor
    def __init__(self):
        self.nodes = dict()
        self.txt_a = text_analysis('src/analizame.txt')
    

    # prepareSentences
    def prepareSentences(self):
        sentences = self.txt_a.sentences
        tokenizedSentences = []
        for s in sentences:
            tokenizedSentences.append(self.txt_a.getTokensBySentence(s))
        return tokenizedSentences



    # execPageRank
    def execPageRank(self,sentences,iterations):
        for s in sentences:
            x = 0
            end = len(s)
            while(x<end):
                y = x+1
                token_a = s[x]

                if not token_a in self.nodes.keys():
                    self.nodes[token_a] = node()
                    self.nodes[token_a].name = token_a
                    self.nodes[token_a].links = set()
                
                while(y<end):
                    token_b = s[y]

                    if not token_b in self.nodes.keys():
                        self.nodes[token_b] = node()
                        self.nodes[token_b].name = token_b
                        self.nodes[token_b].links = set()

                    if not token_b in self.nodes.get(token_a).links:
                        self.nodes.get(token_a).links.add(token_b)
                    
                    if not token_a in self.nodes.get(token_b).links:
                        self.nodes.get(token_b).links.add(token_a)
                    
                    y+=1
                x+=1
            
            startRanking = 1/len(self.nodes)

            for k,v in self.nodes.items():
                v.ranking = startRanking
            
            for i in range(iterations):
                for k,v in self.nodes.items():
                    z = 0
                    for l in v.links:
                        z = z + (self.nodes.get(l).ranking/len(self.nodes.get(l).links))
                    v.ranking = z





    # printPageRank
    def printPageRank(self):
        for k,n in self.nodes.items():
            print(n.name+"\t\t\t =>\t"+str(n.ranking))

                    
                

if __name__ == "__main__":
    print("*******************************\nHora y fecha de inicio de ejecución: ", datetime.now(),'\n\n')

    pr = pageRank()
    sentences = pr.prepareSentences()
    pr.execPageRank(sentences,5)
    pr.printPageRank()
    
    print("\n\n*******************************\nHora y fecha de final de ejecución: ", datetime.now())


    