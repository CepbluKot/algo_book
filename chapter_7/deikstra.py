init_graph = {}
init_graph["a"] = {"b": 6, "c": 2}
init_graph["b"] = {"c": 2, "d": 3}
init_graph["c"] = {"d": 10}
init_graph["d"] = {}


init_point_from = "a"
init_point_to = "d"


def deikstraSearch(
    graph: dict,
    point_from: str,
    point_to: str,
    shortest_path_to: dict = None,
    checked_paths: dict = None,
):
    if not shortest_path_to:
        shortest_path_to = {}

    if not checked_paths:
        checked_paths = {}

    to_search = {}

    for x in graph[point_from]:
        to_search[x] = graph[point_from][x]

    if to_search:
        to_search = dict(sorted(to_search.items(), key=lambda item: item[1]))


        for next_point in to_search:
            if (point_from not in checked_paths) or (
                point_from in checked_paths and checked_paths[point_from] != next_point
            ):
                if point_from not in shortest_path_to:
                    shortest_path_to[point_from] = 0

                if next_point in shortest_path_to:
                    if (
                        shortest_path_to[point_from] + to_search[next_point]
                        < shortest_path_to[next_point]
                    ):
                        shortest_path_to[next_point] = (
                            shortest_path_to[point_from] + to_search[next_point]
                        )
                        checked_paths[point_from] = next_point

                        shortest_path_to, checked_paths = deikstraSearch(
                            graph, next_point, point_to, shortest_path_to, checked_paths
                        )
                else:
                    shortest_path_to[next_point] = (
                        shortest_path_to[point_from] + to_search[next_point]
                    )
                    checked_paths[point_from] = next_point

                    shortest_path_to, checked_paths = deikstraSearch(
                            graph, next_point, point_to, shortest_path_to, checked_paths
                        )

    return shortest_path_to, checked_paths
    #         for x in graph[point]:
    #             if x != point_from and not to_search.isIn(x) and not x in checked:
    #                 to_search.add(x)
    #                 path_history[x] = point

    #         checked.add(point)
    #         point = to_search.get()


print(deikstraSearch(init_graph, init_point_from, init_point_to))
