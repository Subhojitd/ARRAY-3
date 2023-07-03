class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(s):
    if not s:
        return None

    # Find the index of the first parenthesis
    first_paren_idx = s.find("(")

    if first_paren_idx == -1:
        # No parenthesis found, so the entire string is just a single value
        return TreeNode(int(s))

    # The value before the first parenthesis is the root value
    root_val = int(s[:first_paren_idx])
    root = TreeNode(root_val)

    # Find the index of the matching closing parenthesis for the left child
    open_count = 0
    close_count = 0
    left_end_idx = first_paren_idx
    for i in range(first_paren_idx, len(s)):
        if s[i] == "(":
            open_count += 1
        elif s[i] == ")":
            close_count += 1

        if open_count > 0 and open_count == close_count:
            left_end_idx = i
            break

    # Recursively construct the left child
    root.left = construct_binary_tree(s[first_paren_idx+1:left_end_idx])

    if left_end_idx < len(s) - 1:
        # Recursively construct the right child
        root.right = construct_binary_tree(s[left_end_idx+2:-1])

    return root


def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result += inorder_traversal(root.left)
    result.append(root.val)
    result += inorder_traversal(root.right)
    
    return result


# Example usage:
s = "4(2(3)(1))(6(5))"
tree = construct_binary_tree(s)
inorder = inorder_traversal(tree)
print(inorder)
