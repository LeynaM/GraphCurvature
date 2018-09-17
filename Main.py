import numpy as np
import itertools
from itertools import permutations
from itertools import combinations
import time
import CurvatureCalculator as curvature
import copy
from operator import itemgetter
import ast
import new_iso_working as new_iso


def menu():
    run = True
    while run:
        print "Menu\n1. Evaluate a graph\n2. Generate latex document of all the graphs\n3. Give complete two-balls and their curvatures\n4. Exit"
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
            all_graphs = generate_incomplete_2balls()
            write_to_file(all_graphs)
        elif input == "3":
            g_in2 = raw_input("Input a graph: ")
            g2 = ast.literal_eval(g_in2)
            gs2 = standardise(g2)
            completed = complete_twoball(gs2)
            for graph in completed:
                curvature_list = curvatures(graph)
                print "\nTwo-ball: %s\nCurvatures: %s" % (graph, curvature_list)
        elif input == "4":
            run = False
        else:
            print "\nInvalid input\n\n"
    return

def get_oneballs():
    return [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]

def standardise(g):
    gnew = copy.deepcopy(g)
    adjmatrix = adjmat(gnew)
    col_sum = np.sum(adjmatrix[1:,1:5], axis=0)
    for i in range(4):
        col = 3 - int(col_sum[i])
        if col != 0:
            for j in range(col):
                gnew.append([i + 1])
    gnew.sort(key =itemgetter(0))
    gnew.sort(key=len, reverse=True)

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

def generate_incomplete_2balls():
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
    all_two_balls.append([[[1, 1, 1, 1, 1, 1]]])
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


def curvatures(completed_g):
    curvatures = []
    for v in range(4 +len(remove_spherical(completed_g))):
        curv = round(curvature.curv_calc(comp_adjmat(completed_g), v), 3)
        if curv < 0:
            return 'Negative Curvature'
            break
        else:
            curvatures.append(curv)
    curvatures.sort(reverse=True)
    return curvatures



def iso_complete(g1, g2):
    g1_new = copy.deepcopy(g1)
    g2_new = copy.deepcopy(g2)
    if curvatures(g1_new) != curvatures(g2_new):
        return False
    else:
        adj1 = comp_adjmat(g1_new)
        adj2 = comp_adjmat(g2_new)
        for v in range(len(adj2)):
            if curvature.curv_calc(adj1, 0) - curvature.curv_calc(adj2, v) < 10e-3:
                if np.array_equal(recentretest(adj1, 0),recentretest(adj2, v)):
                    return True
    return False


def iso_combined(g1, g2):
    g1_new = copy.deepcopy(g1)
    g2_new = copy.deepcopy(g2)
    completeg1 = False
    completeg2 = False
    for i in g1:
        if max(i) > 4:
            completeg1 = True
    if completeg1 == True:
        if curvatures(g1_new) != curvatures(g2_new):
            return False
        else:
            adj1 = comp_adjmat(g1_new)
            adj2 = comp_adjmat(g2_new)
            for v1 in range(len(adj1)):
                for v2 in range(len(adj2)):
                    if curvature.curv_calc(adj1, v1) == curvature.curv_calc(adj2, v2):
                        if np.array_equal(recentretest(adj1, v1), recentretest(adj2, v2)):
                            return True
    else:
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
                            anew[j][k] = perm[a[j][k] - 1] + 1
                    for i in range(len_a):
                        anew[i].sort()
                        b[i].sort()
                    anew.sort()
                    b.sort()
                    if anew == b:
                        return True
    return False






def complete_twoball(standardised_g):
    sorted_complete_graphs = []
    complete_graphs = []
    gst = copy.deepcopy(standardised_g)
    twoballvertices = len(gst[1:])
    d = []
    vertices = []
    for j in range(twoballvertices):
        d.append(4 - len(gst[1:][j]))
    for k in range(len(d)):
        if d[k] != 0:
            vertices.append(5+k)
    d.sort(reverse=True)
    vertices.sort(reverse=True)
    fillbrackets(d, vertices, complete_graphs, gst)
    for graph in complete_graphs:
        a = graph[:len(standardised_g)]
        b = graph[len(standardised_g):]
        b.sort(key=itemgetter(1))
        b.sort(key=itemgetter(0))
        for i in b:
            a.append(i)
        sorted_complete_graphs.append(a)
    # complete_graphs = [sorted_complete_graphs[0]]
    # for graph1 in sorted_complete_graphs[1:]:
    #     for graph2 in complete_graphs:
    #         if not iso_complete(graph1, graph2):
    #             complete_graphs.append(graph1)
    return sorted_complete_graphs




def fillbrackets(d, vertices, complete_graphs, g):
    if vertices == []:
        complete_graphs.append(g)
        return
    subsets = list(itertools.combinations(vertices[1:], d[0]))
    vertex_saturation = []
    for comb in subsets:
        vertex_saturation.append(list(comb))
    if vertex_saturation != [[]]:
        for choice in vertex_saturation:
            d_new = copy.deepcopy(d[1:])
            vertices_new = copy.deepcopy(vertices[1:])
            g_new = copy.deepcopy(g)
            for i in choice:
                g_new.append([i, vertices[0]])
                d_new[-(i-4)] -= 1
                if d_new[-(i-4)] == 0:
                    vertices_new.remove(i)
            fillbrackets(d_new, vertices_new, complete_graphs, g_new)
    return




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

def recentre(adjmatrix, x):
    if x == 0:
        return adjmatrix
    else:
        newmatrix = adjmatrix[:][:]
        copy = newmatrix[:, 0].copy()
        newmatrix[:, 0] = newmatrix[:, x]
        newmatrix[:, x] = copy
        copy = newmatrix[0, :].copy()
        newmatrix[0, :] = newmatrix[x, :]
        newmatrix[x, :] = copy
        j = 1
        for i in range(len(adjmatrix)):
            if adjmatrix[i][x] == 1:
                copy = newmatrix[:, i].copy()
                newmatrix[:, i] = newmatrix[:, x]
                newmatrix[:, x] = copy
                copy = newmatrix[i, :].copy()
                newmatrix[i, :] = newmatrix[x, :]
                newmatrix[x, :] = copy
                j += 1
        #oneball = [x]
        twoball = []
        contained = True
        # for a in range(len(newmatrix)):
        #     if adjmatrix[x][a]==1:
        #         oneball.append(a)
        for b in range(len(newmatrix)):
            for c in oneball[1:]:
                if newmatrix[b][c] == 1:
                    if b not in twoball and b not in oneball:
                        twoball.append(b)
        twoball.sort
        twoball_vertices = oneball + twoball
        for vertex in range(len(newmatrix)):
            if vertex not in twoball_vertices:
                contained = False
    print 'graph contained in 2-ball:', contained
    print newmatrix
    edges = [[oneball[1], oneball[2]], [oneball[1],
            oneball[3]], [oneball[1], oneball[4]],
            [oneball[2], oneball[3]], [oneball[2],
            oneball[4]], [oneball[3], oneball[4]]]
    oneball_list = [0, 0, 0, 0, 0, 0]
    for j in oneball[1:]:
        for k in oneball[2:]:
            if newmatrix[j][k]== 1:
                for l in range(len(edges)):
                    if edges[l] == [j, k]:
                        oneball_list[l] = 1
    graph = [oneball_list]
    for vertex2 in twoball:
        vertexlist = []
        for vertex1 in oneball:
            if newmatrix[vertex1][vertex2] == 1:
                for i in range(len(oneball[1:])+1):
                    if oneball[i] == vertex1:
                        vertexlist.append(i)
        graph.append(vertexlist)
    graph = sorted(graph)
    graph.sort(key=len, reverse=True)
    for vertex_a in twoball:
        for vertex_b in twoball[1:]:
            if newmatrix[vertex_a][vertex_b] == 1:
                for j in range(len(twoball)):
                    if twoball[j] == vertex_a:
                        a = j+5
                for k in range(len(twoball)):
                    if twoball[k] == vertex_b:
                        b = k+5
                new_edge = sorted([a, b])
                if new_edge not in graph:
                    graph.append(new_edge)
    return graph


def recentretest(adjmatrix, x):
    if x == 0:
        return adjmatrix
    else:
        oneball = [x] + curvature.one_sphere(adjmatrix, x)
        twosphere = curvature.two_sphere(adjmatrix, x)
        contained = True
        twosphere.sort
        twoball_vertices = oneball + twosphere
        for vertex in range(len(adjmatrix)):
            if vertex not in twoball_vertices:
                contained = False
    # print 'graph contained in 2-ball:', contained
    edges = [[oneball[1], oneball[2]], [oneball[1], oneball[3]],
             [oneball[1], oneball[4]], [oneball[2], oneball[3]],
             [oneball[2], oneball[4]], [oneball[3], oneball[4]]]
    oneball_list = [0, 0, 0, 0, 0, 0]
    for j in oneball[1:]:
        for k in oneball[2:]:
            if adjmatrix[j][k]== 1:
                for l in range(len(edges)):
                    if edges[l] == [j, k]:
                        oneball_list[l] = 1
    graph = [oneball_list]
    for vertex2 in twosphere:
        vertexlist = []
        for vertex1 in oneball:
            if adjmatrix[vertex1][vertex2] == 1:
                for i in range(len(oneball[1:])+1):
                    if oneball[i] == vertex1:
                        vertexlist.append(i)
        graph.append(vertexlist)
    graph = sorted(graph)
    graph.sort(key=len, reverse=True)
    for vertex_a in twosphere:
        for vertex_b in twosphere[1:]:
            if adjmatrix[vertex_a][vertex_b] == 1:
                for j in range(len(twosphere)):
                    if twosphere[j] == vertex_a:
                        a = j+5
                for k in range(len(twosphere)):
                    if twosphere[k] == vertex_b:
                        b = k+5
                new_edge = sorted([a, b])
                if new_edge not in graph:
                    graph.append(new_edge)
    return graph

# counter = 0
# incomplete_2balls = generate_incomplete_2balls()
# balllist = []
# for oneball in incomplete_2balls:
#     #print oneball[0]
#     for twoball in oneball:
#         if curvature.curv_calc(adjmat(twoball), 0) > 0:
#             #print twoball
#             twoball_list = complete_twoball(twoball)
#             print len(twoball_list)
#             for completed_twoball1 in twoball_list:
#                 # for completed_twoball2 in twoball_list:
#                 #     if iso_combined(completed_twoball1, completed_twoball2) == True:
#                 #         twoball_list.remove(completed_twoball2)
#                     if curvatures(completed_twoball1)[-1] >0:
#                         counter += 1
# print counter


# print complete_twoball([[0, 0, 0, 0, 0, 0], [1, 2, 3, 4], [1],[1],[2],[2],[3],[3],[4],[4]])
# print len(complete_twoball([[0, 0, 0, 0, 0, 0], [1, 2, 3, 4], [1],[1],[2],[2],[3],[3],[4],[4]]))


#print recentretest(comp_adjmat([[1, 0, 0, 1, 0, 0],[1,3,4],[1,3],[2],[4],[4], [5,8],[6,7],[6,9],[7,8],[7,9],[8,9]]), 3)



#print curvatures([[1, 0, 0, 0, 0, 0], [1, 2], [1, 4], [2, 3], [3, 4], [3], [4], [5, 8], [5, 9], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]])



a = [[1, 1, 0, 0, 1, 1], [1, 2], [3, 4]]
b = [[1, 1, 0, 0, 1, 1], [1, 4], [2, 3]]


#menu()
#print diam_less_than_2([[0, 0, 0, 0, 0, 0], [1, 2, 3, 4],[1, 2, 3, 4],[1], [2], [3,4]])
#generate()

#print remove_spherical(complete_twoball(standardise([[1, 0, 0, 0, 0, 0], [1, 2], [2, 3], [3, 4], [1, 4]]))[0])

#print complete_twoball([[1, 0, 0, 1, 0, 0],[1,3,4],[1,3],[2],[4],[4]])

#print iso_complete([[1, 0, 0, 1, 0, 0], [1, 3, 4],[1, 3],[2],[4],[4],[5,7],[6,8],[6,9],[7,8],[7,9],[8,9]], [[1, 0, 0, 1, 0, 0],[1, 3,4],[1,3],[2],[4],[4],[5, 8],[6,7],[6,9],[7,8],[7,9], [8,9]])

list1 = [[2,3,4,[[2,4],1]],[1,3,[2,3],[2,4]],[2,4,[2,3,4]],[2,3,[1,3]],[2,4,[1,3]],[1]]
list2 = [[5,7],[6,8],[6,9]]

list1.sort()
print list1