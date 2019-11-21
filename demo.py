from open3d import *
from numpy import load

epc = load('epc_mm.npy')
r_pts = load('r_pts_mm.npy')

def pcd_epc(pts):
    radius = r_pts[-pts]
    cloud = epc.compress((epc[:,-2] > radius) & (radius >= epc[:,-1]), 0)
    pcd = PointCloud()
    pcd.points = Vector3dVector(cloud[:,:3])
    pcd.colors = Vector3dVector(cloud[:,3:6])
    return pcd

m = 22
old = pcd_epc(1 << m)
vis = Visualizer()
vis.create_window('Open3D', 720, 720)
vis.add_geometry(old)
opt = vis.get_render_option()
opt.point_size = 2
opt.background_color = 0, 0, 0
ctr = vis.get_view_control()
vis.update_geometry()
vis.poll_events()
vis.update_renderer()
i = 0
vis.capture_screen_image('img/{:03d}.png'.format(i), False)
for __ in range(4):
    for n in range(m-1, -m-1, -1):
        ctr.rotate(12, 0)
        new = pcd_epc(1 << abs(n))
        old.points = new.points
        old.colors = new.colors
        vis.update_geometry()
        vis.poll_events()
        vis.update_renderer()
        i += 1
        vis.capture_screen_image('img/{:03d}.png'.format(i), False)
input()
vis.destroy_window()
