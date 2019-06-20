from sklearn.neighbors import NearestNeighbors
from numpy import array

__all__ = ('dist_pcd',)

def dist_pcd(dense, sparse):
    neigh = NearestNeighbors(1, n_jobs=-1)
    neigh.fit(sparse.points)
    dist, ind = neigh.kneighbors(dense.points)
    dist_colors = abs(array(sparse.colors)[ind.flat] - dense.colors).sum(1)
    return (
        dist.max(),
        dist.sum(),
        dist_colors.max(),
        dist_colors.sum(),
    )

if '__main__' == __name__:
    from open3d import read_point_cloud
    from time import time
    name_dense = input('dense cloud: ')
    name_sparse = input('sparse cloud: ')
    
    t = time()
    pcd_dense = read_point_cloud(name_dense)
    print(*dist_pcd(pcd_dense, read_point_cloud(name_sparse)))
    print(time() - t)
