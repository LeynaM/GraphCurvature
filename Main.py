import numpy as np
from itertools import permutations
import time
import CurvatureCalculator as curvature
import copy
from operator import itemgetter


def menu():
    # gs = standardise(g)
    # adjmatrix = adjmat(gs)
    # curv = curvature.curv_calc(adjmatrix, 0)
    # outdegree = outdeg(gs)
    # s1out = s1outreg(outdegree)
    # curve_sharp = curv_sharp(curv, outdegree)
    # print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curv, s1out, curve_sharp)
    all_graphs = generate()
    write_to_file(all_graphs)
    return

def get_oneballs():
    return np.array([[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]])


def norm(g):
    gnorm = [g[0]]
    for i in range(1, len(g)):
        leaf = [0, 0, 0, 0]
        for j in range(len(g[i])):
            leaf[g[i][j] - 1] = 1
        gnorm.append(leaf)
    return gnorm


def standardise(g):
    gnew = g[:]
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
    m = np.zeros((4+length, 4+length))
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
    m1 = np.zeros((4, 4))
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
    g_std = standardise(g)
    outdeg = [0, 0, 0, 0]
    for i in range(1,len(g_std)):
        for j in range(len(g_std[i])):
            outdeg[g_std[i][j] - 1] += 1
    return outdeg


def curv_sharp(curve, outdeg):
    k = (7 - 0.25 * sum(outdeg)) * 0.5
    if abs(curve - k) <= 1e-6 :
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
        for i in p:
            m1_new = m1[i, :]
            m1_new = m1_new[:, i]
            if np.array_equal(m1_new, m2):
                for j in range(len_a):
                    for k in range(len(a[j])):
                        a[j][k] = i[a[j][k]-1] + 1
                for i in range(len_a):
                    a[i].sort()
                    b[i].sort()
                a.sort()
                b.sort()
                if a == b:
                    return True
        return False


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
        new_two_sphere = two_sphere[:]
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
        b_new = b[:]
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
            one_ball_graphs += unique_h
        all_two_balls.append(one_ball_graphs)
    return all_two_balls
    # length = 0
    # print "All of the graphs:"
    # for oneballsubset in all_two_balls:
    #     length += len(oneballsubset)
    #     for graph in oneballsubset:
    #         print graph
    # print all_two_balls
    # print "Number of graphs generated: ", length
    # print "Graphs with positive curvature:"
    # for graph in positivecurvature:
    #     print graph
    # print "Number of graphs with positive curvature: ", len(positivecurvature)
    # print "Graphs that are curvature sharp:"
    # for graph in curvaturesharp:
    #     print graph
    # print "Number of graphs that are curvature sharp: ", len(curvaturesharp)

def write_to_file(all_graphs):
    #Ordering data as required
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
            '\\usepackage{amssymb}\n\n'
            '\\title{Brief Article}\n'
            '\\author{The Author}\n'
            '\\date{}\n'
            '\\begin{document}\n'
            '\\maketitle\n'
            '\\newpage\n')
    # Tables
    index = 1
    for one_ball_table in all_tables:
        f.write('\\section{%s}\n\n'
                'S1 Out-regular: %s\n\n'
                'Curvature Bound: %.3f\n\n'
                '\\begin{center}\n'
                '\\includegraphics[height=5cm]{sample}\n\n'
                '\\begin{tabular}{| l | l | l | l |}\n'
                '\\hline\n'
                'Index & Two Ball & Curvature & Curvature Sharp \\\\ \\hline\n'
                % (str(one_ball_table[0]), one_ball_table[1], one_ball_table[2]))
        firstpage = True
        table_len = 1
        for table_line in one_ball_table[3]:
            f.write('%i & %s & %.3f & %s \\\\ \\hline\n' % (index, str(table_line[0]), table_line[1], table_line[2]))
            if table_len%50 == 0 and not firstpage:
                f.write('\\end{tabular}\n'
                        '\\end{center}\n'
                        '\\newpage\n'
                        '\\begin{center}\n'
                        '\\begin{tabular}{| l | l | l | l |}\n'
                        '\\hline\n'
                        'Index & Two Ball & Curvature & Curvature Sharp \\\\ \\hline\n')
            if table_len % 25 == 0 and firstpage:
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
    f.write('\\end{document}')
    f.close()


    # positivecurvature = []
    # curvaturesharp = []
    # curv = curvature.curv_calc(adjmat(i), 0)
    # if curv >= 0:
    #     positivecurvature.append(i)
    # # Does it have to be positive to be sharp?
    # if curv_sharp(curv, b):
    #     curvaturesharp.append(i)

# menu()
a = standardise([[1, 0, 0, 0, 0, 0],[2,3,4]])
b = adjmat(a)
c = adjmat2(a)
t1 = time.time()
for i in range(1,100000):
    adjmat(a)
t2 = time.time()
print t2 - t1
t1 = time.time()
for i in range(1,100000):
    adjmat2(a)
t2 = time.time()
print t2 - t1