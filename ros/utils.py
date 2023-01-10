import numpy as np 

def get_center_point(depth_pixel, label_pixel):
    total_cluster_lst = []; total_cluster_center_point=[]
    clustering_num=len(np.unique(label_pixel))
    for idx in range(clustering_num):
        if idx==0: pass # Background, Except clustered objects
        else: 
            cluster_xlst, cluster_ylst = np.where(label_pixel==idx)
            total_cluster_lst.append(depth_pixel[:,cluster_xlst, cluster_ylst])
    for cluster in total_cluster_lst:
        x_total = 0; y_total = 0; z_total = []
        for i in range(len(cluster)):
            x_total += cluster[0,i]
            y_total += cluster[1,i]
            z_total.append(cluster[2,i])
        x = x_total / len(cluster)
        y = y_total / len(cluster)
        z = (max(z_total)+(min(z_total)))/2 
        total_cluster_center_point.append([z,x,y])
    return total_cluster_center_point

