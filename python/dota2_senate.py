class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # dire or radiant strings:
        # in party everyone has their own voting right
        # each person can do one or the other
        # ban a person's right to vote
        # check to see if they win by unanimous

        senate_list = list(senate)
        index = len(senate_list)
        r_queue = []
        d_queue = []

        for i, senate in enumerate(senate_list):
            if senate == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                d_queue.pop(0)
                r_queue.append(r_queue.pop(0) + index)
            else:
                r_queue.pop(0)
                d_queue.append(d_queue.pop(0) + index)

        return "Radiant" if r_queue else "Dire"
