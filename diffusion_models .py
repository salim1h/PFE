import networkx as nx
import matplotlib.pyplot as p
import random
def draw(G,infected):
    position = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,position, nodelist=infected, node_color="r")
    nx.draw_networkx_nodes(G,position, nodelist=G.nodes-infected, node_color="g")

    nx.draw_networkx_edges(G,position)
    nx.draw_networkx_labels(G,position)
    p.show() 
        
def ic(G,s):
    jst_inf=list(s)
    infected=list(s)
    while(1):
        if len(jst_inf)==0:
            return infected
        tmp=[]
        for each in jst_inf:
            for each1 in G.neighbors(each):
                
                r=random.uniform(0,1)
                if r<0.5 and each1 not in infected and each1 not in tmp:
                    tmp.append(each1)
        draw(G,infected)       
        for each in tmp:
             infected.append(each)
        jst_inf=list(tmp)
        
def LT(G,s):
    jst_in=list(s)
    for each in jst_in:
        
        G.node[each]['infected']='true'
        
    for each in jst_in:
        to_infect=G.neighbors(each)
        for eachi in to_infect:
            
            if(G.node[eachi]['infected']=='false'):
                
                G.node[eachi]['value']+=1
                h=set(G.neighbors(eachi))
                if(((G.node[eachi]['value'])/len(h))>0.3):
                    
                    G.node[eachi]['infected']='true'
                    jst_in.append(eachi)
                    print(eachi)
            
            
            
           
        draw(G,jst_in)           
        
            
    
         
    
    

    
G=nx.Graph()
H=nx.path_graph(17)
G.add_nodes_from(H,value=0,infected='false')
G.add_edges_from([(0,16),(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,16),(14,15),(14,16),(15,16)])
seed=[3,8]
print("Ic model")
list1=ic(G,seed)

print("Lt model")
LT(G,seed)
