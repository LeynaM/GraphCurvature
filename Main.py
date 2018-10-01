import copy
import ast
import numpy as np
from operator import itemgetter
from itertools import permutations
import CurvatureCalculator as curvature
import math
from itertools import izip
from itertools import repeat
from itertools import chain
from itertools import combinations


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
            s1out = s1_outreg(outdegree)
            curve_sharp = curv_sharp(curv, outdegree)
            print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curv, s1out, curve_sharp)
        elif input == "2":
            all_graphs = generate_incomp_twoballs()
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


# GET FUNCTIONS #
def get_oneballs(oneball=None):
    """ Get a one ball in standard form or, if no arguments are specified, a list of standard one balls.

    :param oneball: a single one ball (default [])
    :return: A one ball in standard form or a list of all standard one balls
    """
    # Dictionary of all the standard one balls and their equivalent representations
    oneball_dict = {(0, 0, 0, 0, 0, 0): [],
                    (1, 0, 0, 0, 0, 0): [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]],
                    (1, 0, 0, 0, 0, 1): [[0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0]],
                    (1, 1, 0, 0, 0, 0): [[1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0],
                                         [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1],
                                         [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1]],
                    (1, 1, 1, 0, 0, 0): [[1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1]],
                    (1, 1, 0, 1, 0, 0): [[1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1]],
                    (1, 1, 0, 0, 1, 0): [[1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1],
                                         [0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 1],
                                         [0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]],
                    (1, 1, 0, 0, 1, 1): [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]],
                    (1, 1, 1, 1, 0, 0): [[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0],
                                         [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1],
                                         [1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1]],
                    (1, 1, 1, 1, 1, 0): [[1, 1, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                                         [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]],
                    (1, 1, 1, 1, 1, 1): []}
    # If function was called without specifying any arguments, return list of all standard one balls
    if oneball is None:
        return map(list, oneball_dict.keys())
    # If one ball parameter is in standard form, return it
    if tuple(oneball) in oneball_dict.keys():
        return oneball
    # Otherwise, return the equivalent one ball in standard form
    for key in oneball_dict:
        if oneball in oneball_dict[key]:
            return list(key)


# SINGLE GRAPH FUNCTIONS #
def standardise(g):
    """ Standardises a graph by standardising the one ball, adding the leaves and sorting the two ball.

    :param g: graph
    :return: standardised graph
    """
    # STANDARDISE ONE BALL #
    g_new = standardise_oneball(g)

    # SORT TWO BALL #
    for vertex in g_new[1]:
        vertex.sort()
    # Create a data structure of a list of lists containing the two ball vertex and its connections
    two_ball_struct = []
    for i in range(len(g_new[1])):
        two_ball_struct.append([i + 5, g_new[1][i]])
    two_ball_struct.sort(key=lambda x: x[1][:])
    two_ball_struct.sort(key=lambda x: len(x[1]))
    # Create list of sorted two ball vertices
    two_ball_struct = list(izip(*two_ball_struct))
    g_new[1] = list(two_ball_struct[1])
    # Relabel and sort the two sphere spherical edges
    for edge in g_new[2]:
        for i in range(2):
            edge[i] = two_ball_struct[0].index(edge[i]) + 5
        edge.sort()
    g_new[2].sort(key=lambda x: x[1])
    g_new[2].sort(key=lambda x: x[0])

    # ADD LEAVES #
    # Calculate number of existing connections
    out_degree = outdeg(g_new)
    radial_edges = chain.from_iterable(g_new[1])
    freq = [0, 0, 0, 0]  # Frequency of radial edges from each one ball vertex
    for edge in radial_edges:
        freq[edge - 1] += 1
    leaf_freq = np.subtract(out_degree, freq)
    for i in range(4):
        for j in range(leaf_freq[i]):
            g_new[1].append([i + 1])

    # SORT TWO SPHERE SPHERICAL EDGES #
    g_new[2].sort(key=lambda x: x[:])
    return g_new


def standardise_oneball(g):
    """ Standardises the one ball.

    :param g: graph
    :return: graph with standardised one ball
    """
    oneball_orig = g[0]
    oneball_std = get_oneballs(oneball_orig)

    # RELABEL VERTICES #
    # Create data structure, oneball_struct, containing original one ball and its connections
    oneball_sph_edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    oneball_struct = list(izip(oneball_sph_edges, oneball_orig))
    for i in range(6):
        oneball_struct[i] = list(oneball_struct[i])
    # Find permutation that maps the original one ball to the standard one ball
    perms = permutations([1, 2, 3, 4])
    for perm in perms:
        oneball_perm_struct = copy.deepcopy(oneball_struct)
        for i in range(6):
            for j in range(2):
                oneball_perm_struct[i][0][j] = perm[oneball_struct[i][0][j] - 1]
            oneball_perm_struct[i][0].sort()
        oneball_perm_struct.sort(key=lambda x: x[0][:])
        oneball_perm = []
        for i in range(6):
            oneball_perm.append(oneball_perm_struct[i][1])
        # If the permuted one ball is the same as the standardised one ball, relabel two ball vertices and return graph
        if oneball_perm == oneball_std:
            g[0] = oneball_std
            for vertex in g[1]:
                for i in range(len(vertex)):
                    vertex[i] = perm[vertex[i] - 1]
            for two_ball_vertex in g[1]:
                two_ball_vertex.sort()
            return g


def adjmat_oneball(oneball):
    """ Create adjacency submatrix for the one ball.

    :param oneball: the one ball
    :return: submatrix for the one ball
    """
    oneball_matrix = np.zeros((4, 4), dtype=int)
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        if oneball[n] == 1:
            oneball_matrix[i[n] - 1, j[n] - 1] = 1
            oneball_matrix[j[n] - 1, i[n] - 1] = 1
    return oneball_matrix


def adjmat(g):
    """ Creates the adjacency matrix for a graph.

    :param g: graph
    :return: adjacency matrix
    """
    g_new = g[0:2]
    num_vertices = 5 + len(g_new[1])
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    # Edges from the center
    adj_matrix[0, 1:5] = 1
    adj_matrix[1:5, 0] = 1
    # Fill in one ball
    adj_matrix[1:5, 1:5] = adjmat_oneball(g_new[0])
    # Two ball radial edges
    for i in range(num_vertices - 5):
        vertex = g_new[1][i]
        for j in range(len(vertex)):
            adj_matrix[i + 5, vertex[j]] = 1
            adj_matrix[vertex[j], i + 5] = 1
    # If there are spherical edges add them to the matrix
    if g[2]:
        for sph_edge in g[2]:
            adj_matrix[sph_edge[0], sph_edge[1]] = 1
            adj_matrix[sph_edge[1], sph_edge[0]] = 1
    return adj_matrix


def curvatures(g):
    """ Creates a list of lists of vertex and corresponding curvature.

    :param g: graph
    :return: list of lists of vertex and corresponding curvature
    """
    adj_matrix = adjmat(g)
    curvatures = []
    for i in range(5 + len(g[1])):
        curv = round(curvature.curv_calc(adj_matrix, i), 3)
        curvatures.append([i, curv])
    return curvatures


def outdeg(g):
    """ Creates a list of the out degrees for the one sphere.

    :param g: graph
    :return: list of the out degrees for the one sphere
    """
    j = (1, 1, 1, 2, 2, 3)
    k = (2, 3, 4, 3, 4, 4)
    out_degrees = [0, 0, 0, 0]
    for i in range(6):
        if g[0][i] == 0:
            out_degrees[j[i] - 1] += 1
            out_degrees[k[i] - 1] += 1
    return out_degrees


def curv_sharp(curv, out_degrees):
    """ Determines whether a graph is infinity curvature sharp using its curvature and out degrees.

    :param curv: curvature of the central vertex
    :param out_degrees: list of the out degrees for the one sphere
    :return: True if the graph is infinity curvature sharp
    """
    k = (7 - 0.25 * sum(out_degrees)) * 0.5  # Curvature bound
    if abs(curv - k) <= 1e-6:
        return True
    else:
        return False


def s1_outreg(out_degrees):
    """ Determines whether a graph is s1 out regular by checking if the one sphere out degrees are constant.

    :param out_degrees: list of the out degrees for the one sphere
    :return: True if the graph is s1 out regular
    """
    for i in range(1, 4):
        if out_degrees[i] != out_degrees[0]:
            return False
    return True


def diam_less_than_two(g):
    """ Determines whether a graph has a diameter of less than two.

    :param g: graph
    :return: True if the graph has a diameter of less than two
    """
    adj_matrix = adjmat(g)
    matrix = adj_matrix + np.matmul(adj_matrix, adj_matrix)
    length = len(adj_matrix)
    for i in range(length):
        for j in range(length):
            if matrix[i][j] <= 0:
                return False
    return True


# ISOMORPHIC FUNCTIONS #
def get_oneball_perms(oneball):
    """ Returns a list of the permutations for a one ball that preserve its structure.

    :param oneball: one ball
    :return: permutations
    """
    all_oneball_perms = {(0, 0, 0, 0, 0, 0): [(1, 2, 3, 4)],
                         (1, 0, 0, 0, 0, 0): [(1, 2, 3, 4), (2, 1, 3, 4), (1, 2, 4, 3), (2, 1, 4, 3)],
                         (1, 0, 0, 0, 0, 1): [(1, 2, 3, 4), (2, 1, 3, 4), (1, 2, 4, 3), (2, 1, 4, 3),
                                              (3, 4, 1, 2), (4, 3, 1, 2), (3, 4, 2, 1), (4, 3, 2, 1)],
                         (1, 1, 0, 0, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4)],
                         (1, 1, 1, 0, 0, 0): [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4),
                                              (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2)],
                         (1, 1, 0, 1, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4), (2, 1, 3, 4),
                                              (2, 3, 1, 4), (3, 1, 2, 4), (3, 2, 1, 4)],
                         (1, 1, 0, 0, 1, 0): [(1, 2, 3, 4), (3, 4, 1, 2)],
                         (1, 1, 0, 0, 1, 1): [(1, 2, 3, 4), (2, 4, 1, 3), (4, 3, 2, 1), (3, 1, 4, 2)],
                         (1, 1, 1, 1, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4)],
                         (1, 1, 1, 1, 1, 0): [(1, 2, 3, 4), (1, 2, 4, 3), (2, 1, 3, 4), (2, 1, 4, 3)]}
    return all_oneball_perms[tuple(oneball)]


def recenter(g, x):
    """ Recenter the graph about a vertex.

    :param g: graph
    :param x: new central vertex
    :return: recentered graph
    """
    adj_matrix = adjmat(g)
    # If original center is given, return graph
    if x == 0:
        return g
    # Otherwise get the new one ball, two sphere and two ball vertices
    oneball_vertices = [x] + curvature.one_sphere(adj_matrix, x)  # List of new one ball vertices
    twosphere_vertices = curvature.two_sphere(adj_matrix, x)  # List of new two sphere vertices
    twoball_vertices = oneball_vertices + twosphere_vertices  # List of vertices contained in the new two ball
    # If the new two ball does not contain all of the original vertices, i.e has a diameter > 2, raise an exception
    if len(twoball_vertices) != len(adj_matrix):
        return None

    # ONE BALL NOTATION #
    g_new = [[0, 0, 0, 0, 0, 0], [], []]
    vertices_a = (1, 1, 1, 2, 2, 3)
    vertices_b = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        vertex_a = oneball_vertices[vertices_a[n]]
        vertex_b = oneball_vertices[vertices_b[n]]
        if adj_matrix[vertex_a, vertex_b] == 1:
            g_new[0][n] = 1

    # TWO BALL NOTATION #
    for i in range(len(twosphere_vertices)):
        radial_edges = []
        for j in range(1, len(oneball_vertices)):
            if adj_matrix[twosphere_vertices[i], oneball_vertices[j]] == 1:
                radial_edges.append(j)
        g_new[1].append(radial_edges)

    # SPHERICAL EDGE NOTATION #
    for i in range(5, len(twoball_vertices)):
        for j in range(i + 1, len(twoball_vertices)):
            if adj_matrix[twoball_vertices[i], twoball_vertices[j]] == 1:
                g_new[2].append([i, j])

    # STANDARDISE #
    g_new = standardise_oneball(g_new)
    return g_new


def iso(g1, g2, fix_center=False):
    """ Determines whether two graphs are isomorphic.

    :param g1: graph one
    :param g2: graph two
    :param fix_center: True if the centers are fixed (default False)
    :return: True if the graphs are isomorphic
    """
    # Standardise the one balls
    g1 = standardise_oneball(g1)
    g2 = standardise_oneball(g2)
    # If number of vertices differ, return False
    num_vertices = 5 + len(g1[1])
    if num_vertices != 5 + len(g2[1]):
        return False
    # If there is no two ball, return True
    if g1[0] == [1, 1, 1, 1, 1, 1]:
        return True
    # Calculate curvatures
    curv1 = curvatures(g1)
    curv2 = curvatures(g2)

    g2_center = num_vertices
    original_g2 = g2
    exit_flag = True
    while exit_flag:

        # PRELIMINARY CHECKS #
        # If one balls are the same, continue checks
        if g1[0] == g2[0]:
            # If number of spherical edges are the same, continue
            if len(g1[2]) == len(g2[2]):
                # # If curvatures of centers are the same, continue
                # if curv1[0][1] == curv2[0][1]:
                #     # If one ball curvatures are the same, continue
                #     only_curvatures1 = list(izip(*curv1))[1]
                #     only_curvatures2 = list(izip(*curv2))[1]
                #     if sorted(only_curvatures1[1:5]) == sorted(only_curvatures2[1:5]):
                #         # If two ball curvatures are the same, continue
                #         if sorted(only_curvatures1[5:]) == sorted(only_curvatures2[5:]):

                # CREATE NETWORK #
                num_radial = len(g1[1])  # Number of two ball vertices
                # Create dictionary for each network graph
                network1 = {}
                network2 = {}
                for i in range(num_vertices):
                    network1[i] = []
                    network2[i] = []
                # Connect one sphere to centre
                for i in range(1, 5):
                    network1[0].append(i)
                    network1[i].append(0)
                    network2[0].append(i)
                    network2[i].append(0)
                # Establish one ball connections
                j = (1, 1, 1, 2, 2, 3)
                k = (2, 3, 4, 3, 4, 4)
                for i in range(6):
                    if g1[0][i] == 1:
                        network1[j[i]].append(k[i])
                        network1[k[i]].append(j[i])
                    if g2[0][i] == 1:
                        network2[j[i]].append(k[i])
                        network2[k[i]].append(j[i])
                # Establish radial connections
                radial1 = g1[1]
                radial2 = g2[1]
                for i in range(num_radial):
                    for j in range(len(radial1[i])):
                        network1[i + 5].append(radial1[i][j])
                        network1[radial1[i][j]].append(i + 5)
                    for j in range(len(radial2[i])):
                        network2[i + 5].append(radial2[i][j])
                        network2[radial2[i][j]].append(i + 5)
                # Establish spherical connections
                if g1[2] != []:
                    for i in range(len(g1[2])):
                        network1[g1[2][i][0]].append(g1[2][i][1])
                        network1[g1[2][i][1]].append(g1[2][i][0])
                        network2[g2[2][i][0]].append(g2[2][i][1])
                        network2[g2[2][i][1]].append(g2[2][i][0])

                # GENERATE PERMUTATIONS #
                # Add one ball permutations
                vertex_perms = [get_oneball_perms(g2[0])]
                # Group two ball vertices by curvature
                curv2_sort = sorted(curv2[5:], key=lambda x: x[1])
                two_ball_grouped = [[curv2_sort[0][0]]]  # Two ball vertices grouped by curvature
                previous_curv = curv2_sort[0][1]
                for i in range(1, len(curv2_sort)):
                    if curv2_sort[i][1] != previous_curv:
                        two_ball_grouped.append([curv2_sort[i][0]])
                        previous_curv = curv2_sort[i][1]
                    else:
                        two_ball_grouped[-1].append(curv2_sort[i][0])
                # Permute vertices to match networks
                all_vertices_grouped = [[1, 2, 3, 4]] + two_ball_grouped
                all_vertices_grouped.sort(key=len)
                num_perms = []
                for i in range(len(two_ball_grouped)):
                    num = len(two_ball_grouped[i])
                    if num == 1:
                        perms = [tuple(two_ball_grouped[i])]
                        vertex_perms.append(perms)
                    if num > 1:
                        perms = list(list(permutations(two_ball_grouped[i])))
                        vertex_perms.append(perms)
                    # Remove empty sets from degrees
                    num_perms.append(len(two_ball_grouped[i]))
                # Duplicate and merge permutations for each partition to get all permutations
                num_perms = map(lambda x: math.factorial(x), num_perms)
                num_perms.append(len(vertex_perms[0]))
                vertex_perms.sort(key=len)
                num_perms.sort()
                total_perms = reduce(lambda x, y: x * y, num_perms, 1)
                all_perms = [list(chain.from_iterable(list(repeat(vertex_perms[0], total_perms / num_perms[0]))))]
                individual_repeats = num_perms[0]
                for i in range(1, len(num_perms)):
                    perms = []
                    for j in range(len(vertex_perms[i])):
                        perms.extend(list(repeat(vertex_perms[i][j], individual_repeats)))
                    all_perms.append(list(chain.from_iterable(list(repeat(perms, total_perms / len(perms))))))
                    individual_repeats = individual_repeats * num_perms[i]

                # COMPARISON #
                # Compare permutations of the second network with the first network
                for n in range(1, total_perms):
                    network_cmp = copy.deepcopy(network2)
                    cmp_keys = network2.keys()
                    for i in range(len(all_vertices_grouped)):
                        for j in range(len(all_vertices_grouped[i])):
                            vertex1 = all_vertices_grouped[i][j]
                            vertex2 = all_perms[i][n][j]
                            if vertex1 != vertex2:
                                # Switch keys
                                cmp_keys[vertex1] = vertex2
                                for k in range(len(network1)):
                                    network_cmp[k] = map(lambda x: -vertex2 if x == vertex1 else x, network_cmp[k])
                    # Combine switched keys and values
                    network_cmp_cmplt = copy.deepcopy(network_cmp)
                    for k in range(len(cmp_keys)):
                        network_cmp_cmplt[cmp_keys[k]] = sorted(map(abs, network_cmp[k]))
                    if network1 == network_cmp_cmplt:
                        return True

        # RECENTERING #
        # Recenter unless only comparing graphs with fixed centers
        exit_flag = False
        if not fix_center:
            for i in range(g2_center - 1, 0, -1):
                # If the curvatures are the same recenter around the new vertex
                if curv1[0][1] == curv2[i][1]:
                    g2 = recenter(original_g2, i)
                    if g2 is not None:
                        curv2 = curvatures(g2)
                        g2_center = i
                        exit_flag = True
                        break
    return False


# GRAPH GENERATING FUNCTIONS #
def partition(n, num_unsat_vert, avail_outdeg_max):
    """ Returns a list of partitions of an integer that satisfies the conditions.

    :param n: integer to be partitioned
    :param num_unsat_vert: number of unsaturated vertices in the one sphere
    :param avail_outdeg_max: maximum available out degree
    :return: list of partitions of integer n
    """
    m = [[n]]
    for x in range(1, n):
        for y in partition(n - x, num_unsat_vert, avail_outdeg_max):
            s = sorted([x] + y, reverse=True)
            if s not in m:
                m.append(s)
    return m


def generate_twoball(avail_outdeg, part, twoball, all_twoballs, vertices):
    """ Recursively generates all two balls for a specific one ball.

    :param avail_outdeg: available outdegrees
    :param part: current partition
    :param twoball: current two ball
    :param all_twoballs: list of all the two balls for the specific one ball
    :param vertices: list of available vertices with multiplicity
    :return: None
    """
    # Tail of recursion is reached when part is empty, therefore current two sphere is complete
    if not part:
        if twoball not in all_twoballs:
            twoball.append([])
            all_twoballs.append(twoball)
        return
    # Tail of recursion is also reached when there are only leaves left
    if part[0] == 1:
        twoball_new = copy.deepcopy(twoball)
        for i in range(4):
            for j in range(avail_outdeg[i]):
                if len(twoball_new) == 1:
                    twoball_new.append([[i + 1]])
                else:
                    twoball_new[1].append([i + 1])
        if twoball_new not in all_twoballs:
            twoball_new.append([])
            all_twoballs.append(twoball_new)
        return
    # Generating a radial edge
    p = part[0]
    part_new = part[1:]
    for a in vertices[p - 2]:
        valid = True
        avail_outdeg_new = copy.deepcopy(avail_outdeg)
        for i in a:
            if avail_outdeg[i - 1] == 0:
                valid = False
            avail_outdeg_new[i - 1] -= 1
        # If radial edge is valid, add it to the current two ball and repeat to generate the next edge
        if valid:
            twoball_new = copy.deepcopy(twoball)
            if len(twoball_new) == 1:
                twoball_new.append([a])
            else:
                twoball_new[1] = twoball_new[1] + [a]
            generate_twoball(avail_outdeg_new, part_new, twoball_new, all_twoballs, vertices)
    return


def generate_incomp_twoballs():
    """ Generates all incomplete two balls grouped by one ball

    :return: list of lists of two balls
    """
    oneballs = get_oneballs()
    vertices = [[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
                [[1, 2, 3, 4]]]
    twoballs_incomp = []
    for oneball in oneballs[:-1]:
        avail_outdeg = outdeg([oneball, [], []])
        # Calculate number of unsaturated vertices
        num_unsat_vert = 0
        for i in range(4):
            if avail_outdeg[i] != 0:
                num_unsat_vert += 1
        # Get list of valid partitions
        n = sum(avail_outdeg)
        parts = partition(n, num_unsat_vert, max(avail_outdeg))
        # Create list of valid partitions
        parts_new = []
        avail_outdeg_max = max(avail_outdeg)
        for part in parts:
            part_len = len(part)
            part_max = max(part)
            if part_max <= num_unsat_vert and avail_outdeg_max <= part_len:
                parts_new.append(part)
        twoballs_incomp_oneball = []  # All incomplete two balls for a specific one ball
        # Generate two ball for each partition
        for part in parts_new:
            twoball = [oneball]
            all_twoballs = []
            generate_twoball(avail_outdeg, part, twoball, all_twoballs, vertices)
            unique_twoballs = [all_twoballs[0]]
            # Remove isomorphisms
            for graph1 in all_twoballs[1:]:
                for graph2 in unique_twoballs:
                    if not iso(graph1, graph2):
                        unique_twoballs.append(graph1)
            twoballs_incomp_oneball += unique_twoballs
        twoballs_incomp.append(twoballs_incomp_oneball)
    twoballs_incomp.append([[[1, 1, 1, 1, 1, 1], [], []]])
    return twoballs_incomp


def complete_twoball(g):
    """ Generates completions of a two ball by adding spherical edges.

    :param g: incomplete two ball
    :return: list of completed graphs
    """
    # If there is no two sphere, return g
    if not g[1]:
        return g
    else:
        g_new = copy.deepcopy(g)
        twoball_vertices = len(g_new[1])
        degrees = []
        unsat_vertices = []  # Unsaturated vertices in the two sphere
        # Create list of degrees and unsaturated vertices
        for j in range(twoball_vertices):
            deg = 4 - len(g_new[1][j])
            degrees.append(deg)
            if deg != 0:
                unsat_vertices.append(5 + j)
        degrees.sort(reverse=True)
        unsat_vertices.sort(reverse=True)
        # Generate spherical edges
        complete_graphs = []
        generate_sph_edges(degrees, unsat_vertices, complete_graphs, g_new)
        # Sort graphs
        sorted_graphs = []
        for graph in complete_graphs:
            graph[2].sort(key=lambda x: x[:])
            sorted_graphs.append(graph)
        # Remove isomorphisms
        unique_twoballs = [sorted_graphs[0]]
        for graph1 in sorted_graphs[1:]:
            for graph2 in unique_twoballs:
                if not iso(graph1, graph2):
                    unique_twoballs.append(graph1)
        return unique_twoballs


def generate_sph_edges(degrees, unsat_vertices, complete_graphs, g):
    """ Recursively generates the spherical edges one vertex at a time.

    :param degrees: list of the degrees of two sphere vertices
    :param unsat_vertices: unsaturated vertices in the two sphere
    :param complete_graphs: list of completions of the graph
    :param g: incomplete two ball
    :return: None
    """
    # Tail of recursion is reached when all vertices are saturated
    if not unsat_vertices:
        complete_graphs.append(g)
        return
    # Find possible vertex saturations for first unsaturated vertex
    subsets = list(combinations(unsat_vertices[1:], degrees[0]))
    vertex_saturation = []
    for comb in subsets:
        vertex_saturation.append(list(comb))
    # Adding spherical edges and repeat with updated values
    if vertex_saturation != [[]]:
        for choice in vertex_saturation:
            deg_new = degrees[1:]
            vert_new = unsat_vertices[1:]
            g_new = copy.deepcopy(g)
            for i in choice:
                g_new[2].append([i, unsat_vertices[0]])
                deg_new[-(i - 4)] -= 1
                if deg_new[-(i - 4)] == 0:
                    vert_new.remove(i)
            generate_sph_edges(deg_new, vert_new, complete_graphs, g_new)
    return


def generate_non_neg_twoballs():
    """ Generates all non-negatively curved four regular two balls and a list of their curvatures.

    :return: list of non-negative two balls and corresponding curvatures
    """
    # Generate incomplete two balls
    twoballs_incomp = generate_incomp_twoballs()
    # Create list of non-negatively curved two balls
    twoballs_non_neg = []
    for oneball in twoballs_incomp:
        for twoball in oneball:
            if curvature.curv_calc(adjmat(twoball), 0) >= 0:
                twoballs_non_neg.append(twoball)
    # Generate completions for each non-negative two ball
    twoballs_comp_non_neg = []
    for twoball in twoballs_non_neg:
        twoballs_comp = complete_twoball(twoball)
        # Remove graphs of negative curvature
        for graph in twoballs_comp:
            curv = curvatures(graph)
            only_curvatures = list(izip(*curv))[1]
            if min(only_curvatures) >= 0:
                twoballs_comp_non_neg.append([graph, curv])  # list of lists containing graph and its curvatures
    # Remove isomorphisms
    unique_graphs = [twoballs_comp_non_neg[0]]
    for graph1 in twoballs_comp_non_neg[1:]:
        for graph2 in unique_graphs:
            if not iso(graph1[0], graph2[0]):
                unique_graphs.append(graph1)
            else:
                print "an iso exists!"
    return unique_graphs


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
    # Ordering data as required
    curvature_sharp_graphs = []
    all_tables = []
    index = 0
    for one_ball_graphs in all_graphs:
        table = []
        oneball = [copy.deepcopy(one_ball_graphs[0][0])]
        outdegree = outdeg(oneball)
        s1out = s1_outreg(outdegree)
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
    # Writing data to file
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
            if table_len % 47 == 0 and not firstpage:
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
        f.write('%s\\\\ \\hline\n' % (graph))
    f.write('\\end{tabular}\n'
            '\\end{center}\n'
            '\\end{document}')
    f.close()

# graph1 = [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]]
# graph2 = [[0, 1, 0, 0, 1, 0], [[1, 2], [1, 4], [2, 3], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]]
# graph2 = standardise_oneball(graph2)
# print iso(graph1, graph2)
#
# graph1 = [[1, 0, 1, 1, 0, 1], [[1, 2], [3, 4]], []]
# graph1 = standardise_oneball(graph1)
# graph2 = [[0, 1, 1, 1, 1, 0], [[1, 3], [2, 4]], []]
# graph2 = standardise_oneball(graph2)
# print iso(graph1, graph2)
#
# graph1 = [[1, 1, 0, 0, 1, 1], [[1, 4], [2, 3]], []]
# graph1 = standardise_oneball(graph1)
# graph2 = [[1, 1, 0, 0, 1, 1], [[1, 2], [3, 4]], []]
# graph2 = standardise_oneball(graph2)
# print iso(graph1, graph2)

graph1 = [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]]
print graph1
graph2 = [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], []]
twoballs = generate_incomp_twoballs()
print twoballs