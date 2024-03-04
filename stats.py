from shdw_node_stats import NodeStats

# Assuming you have a 'nodes.txt' or 'nodes.json' file in your current directory
node_stats = NodeStats('nodes.txt')  # or NodeStats('nodes.json')
node_stats.run()
