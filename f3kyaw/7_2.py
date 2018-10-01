class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

class Player2:
    __slots__ = ['uid', 'name', 'level']
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

import tracemalloc
tracemalloc.start()
# start 
#la = [Player1(1,2,3) for _ in range(100000)]
lb = [Player2(1,2,3) for _ in range(100000)]
# end
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
for stat in top_stats[:10]: print(stat)
