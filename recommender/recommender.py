import networkx as nx
import matplotlib as plt
import json
import operator
from app.helpers import get_jobs_data, get_users_array 

# TODO: REFACTOR THIS CODE 
# Consider a recommender class
# Condider alternative data model/handling

def load_wordlists():
    with open('app/data/wordlists.json', 'r') as infile:
        wordlists = json.load(infile)
    return wordlists

def get_skill_group(skill):
    """ returns the keyword or category
        associated with a given skill
        from the wordlists data
    """
    wordlists = load_wordlists()
    for ss in wordlists['soft_skills']:
        if skill in ss['phrases']:
            return ss['term']
    for hs in wordlists['hard_skills']:
        if skill in hs['tools']:
            return hs['keyword']
    return skill

def draw_graph():
    """ for visualising the graph """
    job_nodes = [ node for node,attr in G.nodes(data=True) if 'job' in attr.values() ]
    user_nodes = [ node for node,attr in G.nodes(data=True) if 'user' in attr.values() ]
    hs_nodes = [ node for node,attr in G.nodes(data=True) if 'hard_skill' in attr.values() ]
    ss_nodes = [ node for node,attr in G.nodes(data=True) if 'soft_skill' in attr.values() ]
    pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, 
            nodelist=ss_nodes, 
            node_color='r', 
            node_size=30, 
            with_labels=False, 
            font_weight='normal')
    nx.draw_networkx_nodes(G, pos, 
            nodelist=n_highest_betweenness(G, 5),
            node_color='m', 
            node_size=60, 
            with_labels=True, 
            font_weight='normal')
    nx.draw_networkx_nodes(G, pos, 
            nodelist=hs_nodes, 
            node_color='g', 
            node_size=10, 
            with_labels=False, 
            font_weight='normal')
    nx.draw_networkx_nodes(G, pos, 
            nodelist=job_nodes, 
            node_color='b', 
            node_size=20, 
            with_labels=False, 
            font_weight='normal')
    nx.draw_networkx_nodes(G, pos, 
            nodelist=user_nodes, 
            node_color='m', 
            node_size=20, 
            with_labels=True, 
            font_weight='normal')
    labels = { node:node for node in n_highest_betweenness(G, 5) }
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G,pos,labels,font_size=16)
    plt.show()

def get_skills(G, n):
    """ gets skills associated with a given node """
    return [node for node in G.neighbors(n)]

def common_neighbors(G, n1, n2, ss_th=5):
    """ takes 2 nodes as input and returns a list
        of common neighbouring skills nodes
        input ss_th: weight threshold for soft skill edges
    """
    n1_neighbors = [n for n in G.neighbors(n1)]
    n2_neighbors = [n for n in G.neighbors(n2)]
    # eliminate soft skills exceeding weight threshold
    for n in n1_neighbors:
        if G[n1][n]['weight'] > ss_th and G.nodes[n]['node_type'] == 'soft_skill':
            n1_neighbors.remove(n)
    for n in n2_neighbors:
        if G[n2][n]['weight'] > ss_th and G.nodes[n]['node_type'] == 'soft_skill':
            n2_neighbors.remove(n)
    return list(set(n1_neighbors).intersection(set(n2_neighbors)))

def n_highest_betweenness(G, n):
    """ 
    returns n nodes with highest betweenness-centrality
    """
    d = nx.betweenness_centrality(G)
    v=list(d.values())
    k=list(d.keys())
    return [ k[v.index(i)] for i in sorted(v, reverse=True)[:n] ]

def closest_neighbor(G, n, level=None):
    """ takes a node as input and returns the job node with
        which it shares most common neighbours
    """
    if level != 'null':
        job_nodes = [ node for node,attr in G.nodes(data=True) if 'job' in attr.values() 
                and level in attr.values() and node != n ]
    else:
        job_nodes = [ node for node,attr in G.nodes(data=True) if 'job' in attr.values() and node != n ]
    best_cnt = 0
    best_match = ""
    for job in job_nodes:
        cnt = len(common_neighbors(G, n, job))
        if cnt > best_cnt:
            best_cnt = cnt
            best_match = job
    return best_match

def n_closest_neighbors(G, n, N, level=None):
    """ function returns N jobs with most shared neighbors
        ordered from closest to least close
    """
    if level != 'null':
        job_nodes = [ node for node,attr in G.nodes(data=True) if 'job' in attr.values() 
                and level in attr.values() and node != n ]
    else:
        job_nodes = [ node for node,attr in G.nodes(data=True) if 'job' in attr.values() and node != n ]
    node_list = [(n, 0)]
    for i, job in enumerate(job_nodes):
        if n != job:
            cnt = len(common_neighbors(G, n, job))
            for j in range(0, len(node_list)):
                if cnt > node_list[j][1]:
                    node_list.insert(j, (job, cnt))
                    break
    return node_list[0:N]

def n_best_matches(G, n_user, N, level=None):
    """ function returns the N best matches for a user
        taking into account edge weights and number
        of common neighbors, prioritising common neighbours
    """
    node_list = n_closest_neighbors(G, n_user, N, level=level)
    best_matches = []
    for i, node in enumerate(node_list):
        # check if current and next node in list have same 
        # number of common neighbours
        if i < len(node_list)-1 and node[1] > node_list[i+1][1]:
            best_matches.append( (node[0], node[1] ) )
        else:
            c_neighbors = common_neighbors(G, n_user, node[0])
            # calc total path length differences
            dif = 0
            for neighbor in c_neighbors:
                d_user = G.get_edge_data(n_user, neighbor)['weight']
                d_job = G.get_edge_data(node[0], neighbor)['weight']
                dif += abs(d_user - d_job)
            # divide difference by n shared edges
            dif = dif/len(c_neighbors)
            # calculate a proximity value that will allow us to order them
            # add it to the n common neighbours so result is a decimal
            p = ((10 - dif) / 10 ) + node[1]
            # add it to the list
            best_matches.append( (node[0], p) )
    return sorted(best_matches, key=lambda x: x[1], reverse=True)

def initialise_graph(users_array):
    # 1. Define an undirected graph
    G = nx.Graph()

    # 2. Model the data points as nodes
    jobs_array = get_jobs_data()

    # start with jobs...
    for job in jobs_array:
        # each job is a data point
        try:
            if not G.has_node(job['title']):
                G.add_node(job['title'], node_type="job", level=job['career_level'])
        except:
            pass
        else:
        # each soft skill is modelled as a skill
            if 'soft_skills' in job:
                for skill in job['soft_skills']:
                    # find out the soft skill grouping
                    group = get_skill_group(skill)
                    # check if skill exists already, if not add it
                    if not G.has_node(group):
                        G.add_node(group, node_type="soft_skill")
                    # check if there's an edge, if not add it
                    if not G.has_edge(job['title'], group):
                        G.add_edge(job['title'], group, weight=10)
                    # there is, so decrease the weight
                    else:
                        if G[job['title']][group]['weight'] > 1:
                            G[job['title']][group]['weight'] += -1
        # each hard skill is modelled as a skill
            if 'hard_skills' in job:
                for skill in job['hard_skills']:
                    # check if skill exists already, if not add it
                    if not G.has_node(skill):
                        G.add_node(skill, node_type="hard_skill",
                                cat=get_skill_group(skill))
                    # also add an edge, weighted by career level
                    # on assumption more senior will be more skilled
                    if 'career_level' in job:
                        if job['career_level'] == 'peak':
                            w = 3
                        elif job['career_level'] == 'senior':
                            w = 5
                        elif job['career_level'] == 'mid-level':
                            w = 7
                        else:
                            w = 10
                    G.add_edge(job['title'], skill, weight=w)

    # now users
    for obj in users_array:
        G.add_node(obj['username'], node_type='user')
        if 'soft_skills' in obj:
            for key, value in obj['soft_skills'].items():
                # check if skill exists already, if not add it
                if not G.has_node(key):
                    G.add_node(key, node_type='soft_skill')
                # also add an edge (inverting distance value)
                G.add_edge(obj['username'], key, weight=(11-value))
            for key, value in obj['hard_skills'].items():
                # check if skill exists already, if not add it
                if not G.has_node(key):
                    G.add_node(key, node_type='hard_skill')
                # also add an edge
                G.add_edge(obj['username'], key, weight=(11-value))
    return G

