# LC437: Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    count = {0:1}
    result = 0
    
    def dfs(node, prefix):
        nonlocal result
        if not node:
            return
        
        #1. Update prefix sum with node value
        prefix += node.val

        #2. Get prefix_sum - target and Add to result: This is to count paths ending at this node
        result += count.get(prefix - targetSum, 0)

        #3. Update the count of prefix_sum in the hashmap: this is to record current prefix
        count[prefix] = count.get(prefix, 0) + 1

        #4. Recursion
        dfs(node.left, prefix)
        dfs(node.right, prefix)

        #5. Backtrack: decrement the count of prefix_sum
        count[prefix] -= 1

    dfs(root, 0)
    return result

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    print(pathSum(root, 7))
