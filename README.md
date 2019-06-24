# 2-Means-Simplification
2-Means Simplification for Point Cloud

Tested in Python 3.6

Dependencies: NumPy, scikit-learn, Open3D

---
Original Point Cloud → Effective-Point Cloud:

```
PATH/TO/python.exe epc_pcd.py [input.pcd r_min scale]
```

Convert the original point cloud [input.pcd] into an effective-point cloud epc_[input].npy by recursive 2-means clusterings.  The resolution of the effective-point cloud is shorter than [r_min].  Clusterings are performed in 6D XYZRGB spaces, the RGB scales of which are directly proportional to [scale].  There will be an input dialogue if arguments are insufficient.

An r_pts_[input].npy will also be generated presenting the relation between the number of points and the radius.  The number of rows in epc_[input].npy and the processing time will be printed on the standard output after running this script.  The effective-point cloud epc_[input].npy is a 2D array, one point per row.  The columns in epc_[input].npy represent the following data:
```
X Y Z R G B r_color_sum r_color r_sum r_sup r
```
r_color_sum, r_color, and r_sum are statistical data for comparisons with different algorithms.

---
Effective-Point Cloud → Simplified Point Cloud:

given resolution [r]:
```
PATH/TO/python.exe pcd_epc.py [epc_input.npy r output.pcd]
```

given number of [points] and relation to radius [r_pts_input.npy]:
```
PATH/TO/python.exe pcd_epc_pts.py [epc_input.npy r_pts_input.npy points output.pcd]
```

Extract a simplified point cloud [output.pcd] from the effective-point cloud [epc_input.npy].  There will be an input dialogue if arguments are insufficient.  The number of points in [output.pcd] and the statistical data r, r_sum, r_color, r_color_sum will be printed on the standard output after running this script.

---
2019-06-20 by 1803031@narlabs.org.tw
