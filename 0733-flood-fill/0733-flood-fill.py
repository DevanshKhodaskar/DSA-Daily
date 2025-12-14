from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        a = len(image)
        b = len(image[0])
        start = image[sr][sc]

        if start == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color

        while q:
            i, j = q.pop()

            if i + 1 < a and image[i + 1][j] == start:
                image[i + 1][j] = color
                q.append((i + 1, j))

            if i - 1 >= 0 and image[i - 1][j] == start:
                image[i - 1][j] = color
                q.append((i - 1, j))

            if j + 1 < b and image[i][j + 1] == start:
                image[i][j + 1] = color
                q.append((i, j + 1))

            if j - 1 >= 0 and image[i][j - 1] == start:
                image[i][j - 1] = color
                q.append((i, j - 1))




                

        return image
