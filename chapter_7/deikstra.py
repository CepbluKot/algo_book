init_graph = {}
init_graph["a"] = {"b": 6, "c": 2}
init_graph["b"] = {"c": 2, "d": 3}
init_graph["c"] = {"d": 10}
init_graph["d"] = {"a": 11}


init_point_from = "a"
init_point_to = "d"


def deikstraSearchRecursive(
    graph: dict,
    point_from: str,
    point_to: str,
    shortest_path_to: dict = None,
    checked_paths: dict = None,
    shorted_path_from: dict = None,
):
    if not shortest_path_to:
        shortest_path_to = {}

    if not checked_paths:
        checked_paths = {}

    if not shorted_path_from:
        shorted_path_from = {}

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
                        shorted_path_from[next_point] = point_from
                        checked_paths[point_from] = next_point

                        (
                            shortest_path_to,
                            checked_paths,
                            shorted_path_from,
                        ) = deikstraSearchRecursive(
                            graph,
                            next_point,
                            point_to,
                            shortest_path_to,
                            checked_paths,
                            shorted_path_from,
                        )
                else:
                    shortest_path_to[next_point] = (
                        shortest_path_to[point_from] + to_search[next_point]
                    )
                    shorted_path_from[next_point] = point_from
                    checked_paths[point_from] = next_point

                    (
                        shortest_path_to,
                        checked_paths,
                        shorted_path_from,
                    ) = deikstraSearchRecursive(
                        graph,
                        next_point,
                        point_to,
                        shortest_path_to,
                        checked_paths,
                        shorted_path_from,
                    )

    return shortest_path_to, checked_paths, shorted_path_from


def deikstraSearchFull(graph: dict, point_from: str, point_to: str):
    shortest_path_to, checked_paths, shorted_path_from = deikstraSearchRecursive(graph, point_from, point_to)

    final_path = ''
    curr_point = point_to
    while curr_point != point_from:
        final_path +=  curr_point + ' <- '
        curr_point = shorted_path_from[curr_point]

    final_path += curr_point 
    print( final_path)
    
print(deikstraSearchFull(init_graph, init_point_from, init_point_to))
