
from os import listdir
from os.path import isfile, join
import glob
import json

def loadfilejson():

    js = []
    defaultpath = 'dataset/files/'

    for nb in listdir(defaultpath):

        a = {
                'text' : nb,
                'path' : defaultpath + nb,
                'nodes' : [],
                'isleaf' : True
            }
        js.append(a)
        recur(defaultpath + nb + '/', a['nodes'], 1)

    fp = open('./data/menu.json', 'w')
    json.dump(js, fp)

def recur(path, ls, level):

    for elem in listdir(path):
        if not(level == 0 and 'md' in elem):
            a = {'text': elem.replace('.md', ''), 'path' : path + elem , 'nodes': [], 'isLeaf' : False}

            ls.append(a)
            if level > 0:
                recur( path + elem + '/' , a['nodes'], level-1)
            else:
                a['isLeaf'] = True
                   # a['path'] = a['path'].replace('.md', '.html')
                    #print(elem)

if __name__ == '__main__':
    loadfilejson()