from numpy import load
from open3d import PointCloud, Vector3dVector, write_point_cloud
from sys import argv

if len(argv) > 3:
    name_epc, r, name_output = argv[1:4]
    r = float(r)
else:
    name_epc = input('input epc: ')
    r = float(input('radius: '))
    name_output = input('output: ')

epc = load(name_epc)

def main(radius, name):
    cloud = epc.compress((epc[:,-2] > radius) & (radius >= epc[:,-1]), 0)
    pcd = PointCloud()
    pcd.points = Vector3dVector(cloud[:,:3])
    pcd.colors = Vector3dVector(cloud[:,3:6])
    write_point_cloud(name, pcd)
    print(
        pcd,
        cloud[:,-1].max(),
        cloud[:,-3].sum(),
        cloud[:,-4].max(),
        cloud[:,-5].sum(),
    )
    return None

main(r, name_output)
