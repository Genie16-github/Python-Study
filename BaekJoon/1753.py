# [G4]최단경로
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for n_dist in graph[node]:
            weight = dist + n_dist[1]
            if weight < distance[n_dist[0]]:
                distance[n_dist[0]] = weight
                heapq.heappush(q, (weight, n_dist[0]))


v, e = map(int, input().split())
s_node = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(s_node)

for n in range(1, v + 1):
    print("INF") if distance[n] == INF else print(distance[n])
