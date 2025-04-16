# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total_room = len(rooms) 
        visited = set()
        visited.add(0)
        queue = deque()
        for i in rooms[0]:
            queue.append(i)
            visited.add(i)
        level = 1
        while queue:

            for i in range(len(queue)):
                room = queue.popleft()
                level += 1
                for key in rooms[room]:
                    if key not in visited:
                        queue.append(key)
                        visited.add(key)
            if total_room == level:
                return True
        return False
        