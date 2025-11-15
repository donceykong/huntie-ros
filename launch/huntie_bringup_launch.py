from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Get the path to the xacro file
    xacro_file = PathJoinSubstitution([
        FindPackageShare('huntie_ros'),
        'urdf',
        'huntie.xacro'
    ])
    huntie_urdf = Node(
    	package='robot_state_publisher',
    	executable='robot_state_publisher',
    	name='robot_state_publisher',
    	parameters=[{'robot_description': Command(['xacro ', xacro_file])}]
    )
    
    # static tf from base_link to map
    baselink2map = Node(
    	package='tf2_ros',
    	executable='static_transform_publisher',
    	name='base_link_to_map_tf',
    	arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link']
    )
    
    # node_list = launch_ouster_driver()
    node_list = []
    node_list.append(huntie_urdf)
    node_list.append(baselink2map)
    
    return LaunchDescription(node_list)

