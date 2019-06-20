# 2-Means-Simplification
2-Means Simplification for Point Cloud

Tested in Python 3.6

Dependencies: NumPy, scikit-learn, Open3D

---
Original Point Cloud → Effective-Point Cloud:

```
PATH/TO/python.exe epc_pcd.py [input.pcd r_min scale]
```

Convert the original point cloud [input.pcd] into an effective-point cloud epc_[input].npy by recursive 2-means clusterings.  The resolution of the effective-point cloud is shorter than [r_min].  Clusterings are performed in 6D xyzrgb spaces, the rgb scales of which are directly proportional to [scale].  There will be an input dialogue if arguments are insufficient.

An r_pts_[input].npy will also be generated presenting the relationship between the number of points and the radius.  The length of epc_[input].npy and the processing time will be printed on the standard output after running this script.  The effective-point cloud is a 2D array, one point per row.  

---
Effective-Point Cloud → Simplified Point Cloud:

given resolution:
```
PATH/TO/python.exe pcd_epc.py [epc_input.npy r output.pcd]
```

given number of points:
```
PATH/TO/python.exe pcd_epc_pts.py [epc_input.npy r_pts_input.npy points output.pcd]
```

Extract a simplified point cloud [output.pcd] from the effective-point cloud [epc_input.npy].  There will be an input dialogue if arguments are insufficient.

---
2019-06-20 by 1803031@narlabs.org.tw
