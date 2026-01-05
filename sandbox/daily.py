from typing import List
from collections import defaultdict

class Solution:
  def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    meeting_map = defaultdict(list)
    secret_person = set([0, firstPerson])

    def construir_grafo(arestas):
      grafo = defaultdict(list)
      print(grafo)
      for u, v in arestas:
          grafo[u].append(v)
          grafo[v].append(u) # Se for não-direcionado (a reunião é mútua)
      return grafo

    for [x, y, time] in meetings:
      if not meeting_map.get(time):
        meeting_map[time] = []

      for group in meeting_map[time]:
        if len(group.intersection(current_meet_group)) > 0:
          group.update(current_meet_group)
          merged = True
        
        
      if merged == False:
        meeting_map[time].append(current_meet_group)
        
            
    for time in sorted(meeting_map):
      for current_group in meeting_map[time]: 
        for group in meeting_map[time]: 
          inter = current_group.intersection(group)
          if len(inter) > 0:
            current_group.update(group)

    for time in sorted(meeting_map):
      for group in meeting_map[time]: 
        inter = secret_person.intersection(group)
        if len(inter) > 0:
          secret_person.update(group)

    return list(secret_person)

n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
expect = [0,1,2,3,5]


findAllPeople = Solution.findAllPeople(None, n, meetings, firstPerson)
result = "Success" if findAllPeople == expect else "Error"

print(f"1 - {result}! Expect: {expect} to Equal: {findAllPeople}")  

n = 4
meetings = [[3,1,3],[1,2,2],[0,3,3]]
firstPerson = 3
expect = [0,1,3]

findAllPeople = Solution.findAllPeople(None, n, meetings, firstPerson)
result = "Success" if findAllPeople == expect else "Error"

print(f"2 - {result}! Expect: {expect} to Equal: {findAllPeople}")  



n = 5
meetings = [[3,4,2],[1,2,1],[2,3,1]]
firstPerson = 1
expect = [0,1,2,3,4]

findAllPeople = Solution.findAllPeople(None, n, meetings, firstPerson)
result = "Success" if findAllPeople == expect else "Error"

print(f"3 - {result}! Expect: {expect} to Equal: {findAllPeople}")  

n = 6
meetings = [[0,2,1],[1,3,1],[4,5,1]]
firstPerson = 1
expect = [0,1,2,3]

findAllPeople = Solution.findAllPeople(None, n, meetings, firstPerson)
result = "Success" if findAllPeople == expect else "Error"

print(f"4 - {result}! Expect: {expect} to Equal: {findAllPeople}")  

n = 5
meetings = [[1,3,3],[2,0,3],[2,3,3]]
firstPerson = 4
expect = [0,1,2,3,4]

findAllPeople = Solution.findAllPeople(None, n, meetings, firstPerson)
result = "Success" if findAllPeople == expect else "Error"

print(f"5 - {result}! Expect: {expect} to Equal: {findAllPeople}")  