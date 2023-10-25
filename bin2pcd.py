import sys
import numpy as np
import pcl

def bin_to_pcd(bin_filename, pcd_filename):
    # Load KITTI bin file: x y z i
    lidar_points = np.fromfile(bin_filename, dtype=np.float32).reshape(-1, 4)

    # Convert to PCL PointXYZI format
    cloud = pcl.PointCloud_PointXYZI()
    points = np.zeros((lidar_points.shape[0], 4), dtype=np.float32)

    points[:, :3] = lidar_points[:, :3]
    points[:, 3] = lidar_points[:, 3]
    cloud.from_array(points)

    # Save to PCD file
    pcl.save(cloud, pcd_filename, format="pcd")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <bin_filename> <pcd_filename>")
        sys.exit(1)

    bin_filename = sys.argv[1]
    pcd_filename = sys.argv[2]

    bin_to_pcd(bin_filename, pcd_filename)