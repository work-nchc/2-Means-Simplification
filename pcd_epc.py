from numpy import load
from open3d import PointCloud, Vector3dVector, write_point_cloud
from sys import argv

if len(argv) > 3:
    name_epc = argv[1]
    radius = float(argv[2])
    name_output = argv[3]
else:
    name_epc = input('input npy: ')
    radius = float(input('radius: '))
    name_output = input('output: ')

epc = load(name_epc)
cloud = epc[:,:-2].compress((epc[:,-2] > radius) & (radius >= epc[:,-1]), 0)
pcd = PointCloud()
pcd.points = Vector3dVector(cloud[:,:3])
pcd.colors = Vector3dVector(cloud[:,3:])
write_point_cloud(name_output, pcd)
print(pcd)
