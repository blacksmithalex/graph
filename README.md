# Алгоритмы на графах:

1. Открытое-сообщество Telegram: https://t.me/+HOeZ1nMoYnUzMDg6 
2. Личный Telegram: https://t.me/analitiqq

- dfs1.py классический алгоритм dfs, граф задан через матрицу смежности W, дополнительно в коде собираются номера вершины, из которых произошел переход в список prev. Подходит для ориентированных и неориентированных графов.
- dfs2.py поиск компонент связности, используя dfs. Подходит для ориентированных и неориентированных графов.
- dfs3.py проверка графа на двудольность, используя dfs. Обычно в данных задачах речь про ориентированность графа не идет.
- dfs4.py поиск цикла в ОРИЕНТИРОВАННОМ графе, используя dfs. Для неориентированных графов алгоритм не подходит.
- dfs5.py топологическая сортироввка. Для ориентированных графов без циклов.
- dfs6.py определение мостов. Граф неориентированный.
- bfs1.py классический алгоритм BFS в неориентированном графе. Ищет кратчайшие расстояние от стартовой вершины до остальных в невзвешенном графе (все ребра имеют длину 1). 
- bfs2.py поиск количества путей из стартовой вершины во все остальные в ориентированном графе.
- dijkstra.py алгоритм Дейкстры поиска кратчайшего пути от заданной вершины в неориентированном графе. Граф задается через матрицу весов.


