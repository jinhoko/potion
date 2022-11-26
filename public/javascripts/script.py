import json
import sys

class Node():

    def __init__(self, name):
        self.parent = None
        self.name = name
        self.childs = {}

    def setroot(self):
        self.parent = None

color = ["#F42B03","#D84A05", "#EC7505",  "#E89005"]
gop = 1.5
depths = [100, 50, 25, 15]


def getTree(path):

    default_path = './files/'
    # format ==> 'notebook1.section1.file1.tag1'
    fp = open('./connections/'+path+'.txt', 'r')

    tot = fp.read()
    lines = tot.split('\n')

    root = Node('[ROOT]')
    root.setroot()

    lines.append(path)
    for line in lines:
        members = line.split('.')

        p = root
        for mem in members:
            if mem in p.childs.keys(): # already exist
                p = p.childs[mem]
            else:                      # make new.
                tmp = Node(mem)
                tmp.parent = p
                p.childs[mem] = tmp
                p = tmp

    # print(root.childs)
    # print(root.childs['notebook1'].childs)
    # print(root.childs['notebook1'].childs['section1'].childs)
    # print(root.childs['notebook1'].childs['section1'].childs['file2'].childs)

    start = root
    for mem in path.split('.'):
        start = start.childs[mem]

    data = []

    st = dict()
    st['name'] = start.name
    st['depth'] = 0
    st['color'] = color[st['depth']]
    st['value'] = 200
    st['fixed'] = True

    recur(start, st, 0, True, None)

    fp = open('../data/data.json', 'w')
    json.dump(st, fp)

    return None

def recurdown(me, st, depth, init, before):

    godown = [] # tuple (me, st)

    # parent's child(except me) + parent's siblings.
    hubo = list(me.childs.keys())
    for h in hubo:
        if h == before.name:
            hubo.remove(h)


    for child in hubo:
        godown.append( (me.childs[child], {'name':child, 'depth':depth-1, 'color': color[depth-1], 'value':depths[depth-1]}) )

    # consider color.
    if len(godown) > 0:
        st['children'] = []
        for po in godown:
            st['children'].append(po[1])
            recurdown( po[0], po[1], depth-1, False, me)
def recur(me, st, depth, init, before):

    godown = [] # tuple (me, st)
    goup = []  # tuple (me, st)

    # append my children -> godown except before

    sibs = list(me.childs.keys())
    if before is not None:
        for sib in sibs:
            if sib == before.name:
                sibs.remove(sib)

    for sib in sibs:
        sib = me.childs[sib]
        godown.append(
            ( sib, {'name':sib.name, 'depth':depth-1 , 'color':color[depth-1], 'value':depths[depth-1]})
        )

    # append my parent -> goup , but pass before(me)

    if me.parent is not None:        # go up

        if len(me.parent.childs.keys()) > 1:
            goup.append( (me.parent, {'name' : me.parent.name, 'depth':depth+1 , 'color':color[depth+1], 'value':depths[depth+1] }) )


    # append my parent.

    # consider color.

    if len(godown) + len(goup) > 0:
        st['children'] = []

        for po in godown:
            st['children'].append(po[1])
            recurdown( po[0], po[1], depth-1, False, me)

        for po in goup:
            st['children'].append(po[1])
            recur( po[0], po[1], depth+1, False, me)


if __name__ == '__main__':

    st = sys.argv[1]

  #  print(getTree('Physics.Part1 Mechanics.Ch13 Universal Gravitation.13-2 Free-Fall Acceleration and the Gravitational Force'))