from open3d import read_point_cloud
from numpy import array, concatenate, append, save
from sklearn.cluster import k_means
from sys import argv
from time import time

if len(argv) > 3:
    name_pcd = argv[1]
    r_min = float(argv[2])
    s = float(argv[3])
else:
    name_pcd = input('input cloud: ')
    r_min = float(input('min radius: '))
    s = float(input('color scale: '))

t = time()

radius1_sum = lambda p: abs(p - p.mean(0)).sum()
radius1 = lambda p: abs(p - p.mean(0)).sum(1).max()
radius_sum = lambda p: (((p - p.mean(0)) ** 2).sum(1) ** 0.5).sum()
radius = lambda p: ((p - p.mean(0)) ** 2).sum(1).max() ** 0.5

pcd = read_point_cloud(name_pcd)
epc = [(concatenate((pcd.points, pcd.colors), 1), float('inf'))]

i = 0
for cloud, r_sup in epc:
    r_color_sum = radius1_sum(cloud[:,3:])
    r_color = radius1(cloud[:,3:])
    r_sum = radius_sum(cloud[:,:3])
    r = min(radius(cloud[:,:3]), r_sup)
    if r > r_min:
        label = k_means(
            concatenate((cloud[:,:3], cloud[:,3:] * r * s), 1), 2, n_init=2)[1]
        epc.append((cloud.compress(1 - label, 0), r))
        epc.append((cloud.compress(label, 0), r))
    else:
        r = float('-inf')
    epc[i] = append(cloud.mean(0), (r_color_sum, r_color, r_sum, r_sup, r))
    i += 1

epc = array(epc)
r_pts = sorted(epc[:,-1]) # r_pts[-n] <= radius < r_pts[1-n]

print(len(epc), time() - t)
save('epc_' + name_pcd.rpartition('.')[0], epc)
save('r_pts_' + name_pcd.rpartition('.')[0], r_pts)
