## Tree Traversal
- Iteration
    - Preorder: append children to the end of stack in reverse order (right -> left)
        ```
        class Solution:
            def preorder(self, root: 'Node') -> List[int]:
                if not root:
                    return []

                stack, res = [root], []
                while stack:
                    node = stack.pop()
                    res.append(node.val)
                    stack += node.children[::-1]
                return res
        ```
    - Postorder: append children to the end in normal order (left -> right), reverse the final output
        ```
        class Solution:
            def postorder(self, root: 'Node') -> List[int]:
                if not root:
                    return []

                stack, res = [root], []
                while stack:
                    node = stack.pop()
                    res.append(node.val)
                    for c in node.children:
                        stack.append(c)
                return res[::-1]
        ```