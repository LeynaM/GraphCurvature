import numpy as np
from itertools import permutations
import time
import CurvatureCalculator as curvature
import copy
from operator import itemgetter
import ast


def menu():
    run = True
    while run:
        print "Menu\n1. Evaluate a graph\n2. Generate latex document of all the graphs\n3. Exit"
        input = raw_input("Select: ")
        if input == "1":
            g_in = raw_input("Input a graph: ")
            g = ast.literal_eval(g_in)
            gs = standardise(g)
            adjmatrix = adjmat(gs)
            curv = curvature.curv_calc(adjmatrix, 0)
            outdegree = outdeg(gs)
            s1out = s1outreg(outdegree)
            curve_sharp = curv_sharp(curv, outdegree)
            print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curv, s1out, curve_sharp)
        elif input == "2":
            all_graphs = generate()
            write_to_file(all_graphs)
        elif input == "3":
            run = False
        else:
            print "\nInvalid input\n\n"
    return

def get_oneballs():
    return [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]


def norm(g):
    gnorm = [g[0]]
    for i in range(1, len(g)):
        leaf = [0, 0, 0, 0]
        for j in range(len(g[i])):
            leaf[g[i][j] - 1] = 1
        gnorm.append(leaf)
    return gnorm


def standardise(g):
    gnew = copy.deepcopy(g)
    adjmatrix = adjmat(gnew)
    col_sum = np.sum(adjmatrix[1:,1:5], axis=0)
    for i in range(4):
        col = 3 - int(col_sum[i])
        if col != 0:
            for j in range(col):
                gnew.append([i + 1])
    return gnew


def adjmat(g):
    length = len(g)
    m = np.zeros((4+length, 4+length), dtype=int)
    m[0, 1:5] = 1
    m[1:5, 0] = 1
    m[1:5, 1:5] = one_ball(g[0])
    for i in range(1, length):
        if type(g[i]) is int:
            m[i + 4, g[i]] = 1
            m[g[i], i + 4] = 1
        else:
            for j in range(len(g[i])):
                m[i + 4, g[i][j]] = 1
                m[g[i][j], i + 4] = 1
    return m


def one_ball(g1):
    m1 = np.zeros((4, 4), dtype = int)
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        if g1[n] == 1:
            m1[i[n]-1, j[n]-1] = 1
            m1[j[n]-1, i[n]-1] = 1
    return m1


def two_ball(g2, m):
    for i in range(len(g2)):
        if type(g2[i]) is int:
            m[i + 5, g2[i]] = 1
            m[g2[i], i + 5] = 1
        else:
            for j in range(len(g2[i])):
                m[i + 5, g2[i][j]] = 1
                m[g2[i][j], i + 5] = 1


def s1outreg(outdeg):
    for i in range(1,4):
        if outdeg[i] != outdeg[0]:
            return False
    return True


def outdeg(g):
    j = (1, 1, 1, 2, 2, 3)
    k = (2, 3, 4, 3, 4, 4)
    outdegree = [0,0,0,0]
    for i in range(6):
        if g[0][i] == 0:
            outdegree[j[i]-1] += 1
            outdegree[k[i]-1] += 1
    return outdegree


def curv_sharp(curve, outdeg):
    k = (7 - 0.25 * sum(outdeg)) * 0.5
    if abs(curve - k) <= 1e-6:
        return True
    else:
        return False


def iso(g1, g2):
    g1_std = standardise(g1)
    g2_std = standardise(g2)
    a = g1_std[1:]
    b = g2_std[1:]
    len_a = len(a)
    if len_a != len(b):
        return False
    else:
        p = list(permutations([0, 1, 2, 3]))
        m1 = one_ball(g1_std[0])
        m2 = one_ball(g2_std[0])
        for perm in p:
            anew = copy.deepcopy(a)
            m1_new = m1[perm, :]
            m1_new = m1_new[:, perm]
            if np.array_equal(m1_new, m2):
                for j in range(len_a):
                    for k in range(len(a[j])):
                        anew[j][k] = perm[a[j][k]-1] + 1
                for i in range(len_a):
                    anew[i].sort()
                    b[i].sort()
                anew.sort()
                b.sort()
                if anew == b:
                    return True
        return False


class Node:
    def __init__(self):
        self.neighbours = []
        self.visited = False

    def __iadd__(self, neighbour):
        self.neighbours.append(neighbour)
        return self

    def __len__(self):
        return len(self.neighbours)


class Network:
    def __init__(self, g):
        num_2ball = len(g[1:])
        network = []
        #
        networkdict = {}
        #
        for i in range(4+num_2ball):
            network.append(Node())
            #
            networkdict[i] = []
            #
        # for i in range(len(network)):
        #     print "%i + %s" % (i, network[i])
        #Establish one ball connections
        j = (1, 1, 1, 2, 2, 3)
        k = (2, 3, 4, 3, 4, 4)
        for i in range(6):
            if g[0][i] == 1:
                node1 = network[j[i]-1]
                node2 = network[k[i]-1]
                node1 += node2
                node2 += node1
                #
                networkdict[j[i]-1].append(k[i]-1)
                networkdict[k[i]-1].append(j[i]-1)
                #
        #Establish two ball connections
        for i in range(num_2ball):
            node1 = network[i+4]
            for j in range(len(g[i+1])):
                node2 = network[g[i+1][j]-1]
                node1 += node2
                node2 += node1
                #
                networkdict[i+4].append(g[i+1][j]-1)
                networkdict[g[i+1][j]-1].append(i+4)
                #
        #
        print networkdict
        #
        network.sort(key=len, reverse=True)
        self.network = network
        degrees = []
        for node in network:
            degrees.append(len(node))
        self.degrees = degrees

    def __eq__(self, other):
        if self.degrees != other.degrees:
            return False

    #def path(self, node1, node2):

def partition(n):
    m = [[n]]
    for x in range(1, n):
        for y in partition(n - x):
            s = sorted([x] + y, reverse=True)
            if s not in m:
                m.append(s)
    return m


def fill_twoballs(b, part, two_sphere, h, vertices):
    if len(part) == 0:
        if two_sphere not in h:
            h.append(two_sphere)
        return
    if part[0] == 1:
        new_two_sphere = copy.deepcopy(two_sphere)
        for i in range(4):
            for j in range(b[i]):
                new_two_sphere = new_two_sphere + [[i+1]]
        if new_two_sphere not in h:
            h.append(new_two_sphere)
        return
    p = part[0]
    part_new = part[1:]
    for a in vertices[p - 2]:
        valid = True
        b_new = copy.deepcopy(b)
        for i in a:
            if b[i-1] == 0:
                valid = False
            b_new[i-1] -= 1
        if valid:
            new_two_sphere = two_sphere + [a]
            fill_twoballs(b_new, part_new, new_two_sphere, h, vertices)
    return

def generate():
    oneballs = get_oneballs()
    vertices = [[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                          [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
                          [[1, 2, 3, 4]]]
    all_two_balls = []
    for oneball in oneballs[:-1]:
        b = outdeg([oneball])
        n = sum(b)
        l = 0
        for i in range(4):
            if b[i] != 0:
                l += 1
        parts = partition(n)
        partsnew = []
        for a in parts:
            length_a = len(a)
            max_a = max(a)
            if max_a <= l and max(b) <= length_a:
                partsnew.append(a)
        one_ball_graphs = []
        for part in partsnew:
            twoball = [oneball]
            h = []
            fill_twoballs(b, part, twoball, h, vertices)
            unique_h = [h[0]]
            for i in h[1:]:
                for j in unique_h:
                    k = copy.deepcopy(i)
                    l = copy.deepcopy(j)
                    isomorphic = iso(k, l)
                    if isomorphic:
                        break
                else:
                    unique_h.append(i)
            # unique_h.sort(key=itemgetter(0))
            # unique_h.sort(key=lambda x: len(x[0]))

            one_ball_graphs += unique_h
        all_two_balls.append(one_ball_graphs)
    # length = 0
    # print "All of the graphs:"
    # for oneballsubset in all_two_balls:
    #     length += len(oneballsubset)
    #     for graph in oneballsubset:
    #         print graph
    # print all_two_balls
    # print "Number of graphs generated: ", length
    all_two_balls.append([[[1, 1, 1, 1, 1, 1]]])
    n = 0
    for list in all_two_balls:
        for list2 in list:
            n += len(list2)
    print n
    return all_two_balls


def write_to_file(all_graphs):
    oneballimages = ['\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v3) edge[red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v3) edge[red] (v4)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v3) edge[red] (v4)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}']
    #Ordering data as required
    curvature_sharp_graphs = []
    all_tables = []
    index = 0
    for one_ball_graphs in all_graphs:
        table = []
        oneball = [copy.deepcopy(one_ball_graphs[0][0])]
        outdegree = outdeg(oneball)
        s1out = s1outreg(outdegree)
        k = (7 - 0.25 * sum(outdegree)) * 0.5
        for h in one_ball_graphs:
            two_ball = h[1:]
            curv = curvature.curv_calc(adjmat(h), 0)
            curv_sharpness = curv_sharp(curv, outdegree)
            if curv_sharpness:
                curvature_sharp_graphs.append(h)
            table.append([two_ball, curv, curv_sharpness])
            table.sort(key=itemgetter(1), reverse=True)
        all_tables.append([one_ball_graphs[0][0], s1out, k, table])
    #Writing data to file
    f = open('latex/classification.tex', 'w')
    # Front page and template
    f.write('\\documentclass[11pt, oneside]{article}\n'
            '\\usepackage{geometry}\n'
            '\\geometry{a4paper, margin = 1in}\n'
            '\\usepackage[parfill]{parskip}\n'
            '\\usepackage{graphicx}\n'
            '\\graphicspath{ {/latex/} }\n'
            '\\usepackage{wrapfig}\n'
            '\\usepackage{tikz}\n'
            '\\usepackage{amssymb}\n\n'
            '\\title{Brief Article}\n'
            '\\author{The Author}\n'
            '\\date{}\n'
            '\\begin{document}\n'
            '\\maketitle\n'
            '\\newpage\n')
    # Tables
    index = 1
    n = 0
    for one_ball_table in all_tables:
        f.write('\\section{%s}\n\n'
                'S1 Out-regular: %s\n\n'
                'Curvature Bound: %.3f\n\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=2]\n'
                '\\tikzstyle{every node}=[draw, shape=circle, scale = 0.9, thick]\n'
                '\\path(1:0cm)\tnode(v0) [fill, text = white]{$v_0$};\n'
                '\\path(180:1cm)\tnode(v1) [fill = red, red, text =white]{$v_1$};\n'
                '\\path(90:1cm)\tnode(v2) [fill = red, red, text =white]{$v_2$};\n'
                '\\path(0:1cm)\tnode(v3) [fill = red, red, text =white]{$v_3$};\n'
                '\\path(270:1cm)\tnode(v4) [fill = red, red, text =white]{$v_4$};\n\n'
                '%s\n\n'
                '\\vspace{1cm}\n'
                '\\begin{tabular}{| l | l | l | l |}\n'
                '\\hline\n'
                'Index & Two Ball & Curvature & Curvature Sharp \\\\ \\hline\n'
                % (str(one_ball_table[0]), one_ball_table[1], one_ball_table[2], oneballimages[n]))
        n += 1
        firstpage = True
        table_len = 1
        for table_line in one_ball_table[3]:
            f.write('%i & %s & %.3f & %s \\\\ \\hline\n' % (index, str(table_line[0]), table_line[1], table_line[2]))
            if table_len%47 == 0 and not firstpage:
                f.write('\\end{tabular}\n'
                        '\\end{center}\n'
                        '\\newpage\n'
                        '\\begin{center}\n'
                        '\\begin{tabular}{| l | l | l | l |}\n'
                        '\\hline\n'
                        'Index & Two Ball & Curvature & Curvature Sharp \\\\ \\hline\n')
            if table_len % 30 == 0 and firstpage:
                f.write('\\end{tabular}\n'
                        '\\end{center}\n'
                        '\\newpage\n'
                        '\\begin{center}\n'
                        '\\begin{tabular}{| l | l | l | l |}\n'
                        '\\hline\n'
                        'Index & Two Ball & Curvature & Curvature Sharp \\\\ \\hline\n')
                table_len = 0
                firstpage = False
            table_len += 1
            index += 1
        f.write('\\end{tabular}\n'
                '\\end{center}\n'
                '\\newpage\n')
    f.write('\\begin{center}\n'
            '\\title{Curvature Sharp Graphs}\n'
            '\\begin{tabular}{|l|}\n'
            '\\hline\n')
    for graph in curvature_sharp_graphs:
        f.write('%s\\\\ \\hline\n' %(graph))
    f.write('\\end{tabular}\n'
            '\\end{center}\n'
            '\\end{document}')
    f.close()

#from now on functions working with completed graphs

def complete_twoball(standardised_g):
    complete_graphs = []
    gst= copy.deepcopy(standardised_g)
    twoballvertices = len(gst[1:])
    d = []
    for j in range(twoballvertices):
        d.append([j+5, 4-len(gst[1:][j])])
    part = [2 for i in range(int(0.5 * (sum(edge[1] for edge in d))))]
    fill_brackets(gst, d, part, complete_graphs)
    return complete_graphs



def fill_brackets(g, d, part, complete_graphs):
    if len(part)==0:
        complete_graphs.append(g)
    p = part[0]
    part_new = part[1:]
    d_new = copy.deepcopy(d)
    valid = True
    for vertex1 in d_new:
        for vertex2 in d_new:
            if vertex1 != vertex2:
                if len(part) == 0:
                    valid = False
                    return
                if vertex1[1] > len(part) and vertex2[1] > len(part):
                    valid = False
                if valid:
                    if vertex1[1] and vertex2[1] >0:
                        vertex1[1] -= 1
                        vertex2[1] -= 1
                        g_new = copy.deepcopy(g) + [[vertex1[0], vertex2[0]]]
                        fill_brackets(g_new, d_new, part_new, complete_graphs)




"""
part_new = part[1:]
    for a in vertices[p - 2]:
        valid = True
        b_new = copy.deepcopy(b)
        for i in a:
            if b[i-1] == 0:
                valid = False
            b_new[i-1] -= 1
        if valid:
            new_two_sphere = two_sphere + [a]
            fill_twoballs(b_new, part_new, new_two_sphere, h, vertices)
    return
"""




print complete_twoball([[1, 0, 0, 0, 0, 1], [2, 3, 4], [1, 2], [1, 4], [3]])
def remove_spherical(completed_g):
    gnew = copy.deepcopy(completed_g)
    toremove = []
    for i in range(len(gnew)):
        for element in gnew[i]:
            if element > 4:
                toremove.append(gnew[i])
                break
    for edge in toremove:
        gnew.remove(edge)
    return gnew

def comp_adjmat(completed_g):
    gnew = remove_spherical(completed_g)
    adj = adjmat(standardise(gnew))
    vertexnumber = 4 + len(gnew)
    for sphericaledge in completed_g[vertexnumber - 4:]:
        adj[sphericaledge[0]][sphericaledge[1]] = 1
        adj[sphericaledge[1]][sphericaledge[0]] = 1
    return adj
#print comp_adjmat([[1, 0, 0, 0, 0, 1], [2, 3],[1, 2], [1, 4], [3, 4], [5, 6],[6,7],[7,8],[5,8]])
#check this example!!

def diam_less_than_2(completed_g):
    adj = comp_adjmat(completed_g)
    matrix = adj + np.matmul(adj, adj)
    dim = adj.shape[0]
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j] <= 0:
                return False
    return True

def curvatures(completed_g):
    curvatures = []
    for v in range(4 +len(remove_spherical(completed_g))):
        curv = round(curvature.curv_calc(comp_adjmat(completed_g), v), 3)
        if curv < 0:
            return 'Negative Curvature:', True
            break
        else:
            curvatures.append(curv)
    curvatures.sort(reverse=True)
    return curvatures




#print curvatures([[1, 0, 0, 0, 0, 1], [2, 3],[1, 2], [1, 4], [3, 4], [5, 6],[6,7],[7,8],[5,8]])



a = [[1, 1, 0, 0, 1, 1], [1, 2], [3, 4]]
b = [[1, 1, 0, 0, 1, 1], [1, 4], [2, 3]]


#menu()
#print diam_less_than_2([[0, 0, 0, 0, 0, 0], [1, 2, 3, 4],[1, 2, 3, 4],[1], [2], [3,4]])
#generate()