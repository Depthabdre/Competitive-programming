# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()
        for card in reversed(deck):
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        return list(queue)