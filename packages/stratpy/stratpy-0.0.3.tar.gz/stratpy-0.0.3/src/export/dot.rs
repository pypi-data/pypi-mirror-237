use petgraph::graph::{Graph, NodeIndex};
use petgraph::dot::Dot;
use pyo3::{Py, Python};
use crate::tree::game::Game;
use crate::tree::node::Decision;

pub fn export_dot(mut game: Game, py: Python) -> String {
    let mut graph = Graph::new();
    let mut new_root = game.root.borrow(py).clone();
    new_root.player.name = new_root.children[0].borrow(py).clone().player.name.clone();
    game.root = Py::new(py, new_root).unwrap();
    add_nodes_to_graph(game.root.clone(), &mut graph, py);
    Dot::new(&graph).to_string()
}

fn add_nodes_to_graph(decision: Py<Decision>, graph: &mut Graph<String, String>, py: Python) -> (NodeIndex, String) {
    // add nodes and edges
    let node = decision.borrow(py).clone();
    let index = if node.children.is_empty() {
        graph.add_node(format!("({}, {})", node.utility[0], node.utility[1]))
    } else {
        graph.add_node(node.children[0].borrow(py).clone().player.name.clone())
    };
    for child in node.children {
        let (node_index, name) = add_nodes_to_graph(child, graph, py);
        graph.extend_with_edges(&[
            (index, node_index, name)
        ]);
    }
    (index, node.name.clone())
}

#[cfg(test)]
mod tests {
    // importing names from outer scope.
    use super::*;
    #[test]
    fn test_graph() {
        //export_dot();
        assert_eq!(1,1);
    }

}
