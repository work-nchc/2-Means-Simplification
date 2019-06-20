from open3d import PointCloud, Vector3dVector
from sklearn.cluster import k_means
from numpy import concatenate

__all__ = ('radius', 'pcd_array', 'split_cloud')

radius = lambda p: ((p - p.mean(0)) ** 2).sum(1).max() ** 0.5

def pcd_array(cloud):
    pcd = PointCloud()
    pcd.points = Vector3dVector(cloud[:,:3])
    pcd.colors = Vector3dVector(cloud[:,3:6])
    return pcd

def split_cloud(cloud, s=0.5):
    r = radius(cloud[:,:3])
    label = k_means(
        concatenate((cloud[:,:3], cloud[:,3:] * r * s), 1), 2, n_init=2)[1]
    return cloud.compress(1 - label, 0), cloud.compress(label, 0)

if '__main__' == __name__:
    from open3d import read_point_cloud, write_point_cloud
    
    name, __, ext = input('input cloud: ').rpartition('.')
    scale = input('color scale: ')
    scale = float(scale) if scale else 0.5

    pcd = read_point_cloud(name + '.' + ext)
    cloud = concatenate((pcd.points, pcd.colors), 1)

    cloud0, cloud1 = split_cloud(cloud, scale)
    write_point_cloud(name + '0.' + ext, pcd_array(cloud0))
    write_point_cloud(name + '1.' + ext, pcd_array(cloud1))
