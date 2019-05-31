from sklearn.neighbors import NearestNeighbors

__all__ = (r_vox,)

def r_vox(pts_vox, pts_src):
    neigh = NearestNeighbors(1, n_jobs=-1)
    neigh.fit(pts_vox)
    return neigh.kneighbors(pts_src)[0].max()

if '__main__' == __name__:
    from open3d import read_point_cloud
    from time import time
    
    name_vox = input('voxel cloud: ')
    name_src = input('source cloud: ')
    
    t = time()
    
    vox = read_point_cloud(name_vox)
    src = read_point_cloud(name_src)
    radius = r_vox(vox.points, src.points)
    
    print(radius, time() - t)
