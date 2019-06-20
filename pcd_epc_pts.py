from numpy import load
from open3d import PointCloud, Vector3dVector, write_point_cloud
from sys import argv

if len(argv) > 4:
    name_epc, name_r_pts, points, name_output = argv[1:5]
    points = int(points)
else:
    name_epc = input('input epc: ')
    name_r_pts = input('input r_pts: ')
    points = int(input('number of points: '))
    name_output = input('output: ')

epc = load(name_epc)
r_pts = load(name_r_pts)

def main(pts, name):
    radius = r_pts[-pts]
    cloud = epc.compress((epc[:,-2] > radius) & (radius >= epc[:,-1]), 0)
    pcd = PointCloud()
    pcd.points = Vector3dVector(cloud[:,:3])
    pcd.colors = Vector3dVector(cloud[:,3:6])
    write_point_cloud(name, pcd)
    print(
        pcd,
        radius,
        cloud[:,-3].sum(),
        cloud[:,-4].max(),
        cloud[:,-5].sum(),
    )
    return None

main(points, name_output)
