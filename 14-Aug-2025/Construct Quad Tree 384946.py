# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def sum_region(top, left, bottom, right):
            total = 0
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    total += grid[r][c]
            return total

        def recursive(top, left, bottom, right):
            total_sum = sum_region(top, left, bottom, right)
            total_cells = (bottom - top + 1) * (right - left + 1)

            # Leaf node check
            if total_sum == 0 or total_sum == total_cells:
                return Node(val=1 if total_sum > 0 else 0, isLeaf=True,
                            topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)

            # Internal node: split into 4 quadrants
            row_mid = (top + bottom) // 2
            col_mid = (left + right) // 2

            return Node(
                val=1,  # This value is ignored for internal nodes
                isLeaf=False,
                topLeft=recursive(top, left, row_mid, col_mid),
                topRight=recursive(top, col_mid+1, row_mid, right),
                bottomLeft=recursive(row_mid+1, left, bottom, col_mid),
                bottomRight=recursive(row_mid+1, col_mid+1, bottom, right)
            )

        n = len(grid)
        return recursive(0, 0, n-1, n-1)
