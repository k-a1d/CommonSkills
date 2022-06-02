unweightedGraph = {
  '5' : ['3','7'],
  '3' : ['2','4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def bfs(tree, node):
  queue = [node]
  visited = []

  while queue:
    current_node = queue.pop(0)

    for neighbour in tree[current_node]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(unweightedGraph, '5')

