#include <stdio.h>
#include <stdlib.h>
#include <float.h>

#define INFINITY FLT_MAX

void solve() {
    int number_of_nodes, number_of_edges;
    scanf("%d %d", &number_of_nodes, &number_of_edges);

    int edges[number_of_edges][3];
    for (int i = 0; i < number_of_edges; i++) {
        scanf("%d %d %d", &edges[i][0], &edges[i][1], &edges[i][2]);
    }

    const int DEFAULT_DISCONNECTED_VALUE = 30000;
    float distances[number_of_nodes];
    for (int i = 0; i < number_of_nodes; i++) {
        distances[i] = INFINITY;
    }
    distances[0] = 0.0;

    const int RELAXATIONS = number_of_nodes - 1;
    for (int k = 0; k < RELAXATIONS; k++) {
        for (int i = 0; i < number_of_edges; i++) {
            int from = edges[i][0] - 1;
            int to = edges[i][1] - 1;
            int weight = edges[i][2];

            if (distances[from] != INFINITY && distances[from] + weight < distances[to]) {
                distances[to] = distances[from] + weight;
            }
        }
    }

    for (int i = 0; i < number_of_nodes; i++) {
        if (distances[i] != INFINITY) {
            printf("%d ", (int)distances[i]);
        } else {
            printf("%d ", DEFAULT_DISCONNECTED_VALUE);
        }
    }
    printf("\n");
}

int main() {
    solve();
    return 0;
}
