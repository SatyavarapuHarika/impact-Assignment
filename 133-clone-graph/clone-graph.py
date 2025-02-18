class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        clone_map = {}

        def dfs(original):
            if original in clone_map:
                return clone_map[original]
        
            cloned_node = Node(original.val)
            clone_map[original] = cloned_node
            
            for neighbor in original.neighbors: 
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node
        
        return dfs(node)
