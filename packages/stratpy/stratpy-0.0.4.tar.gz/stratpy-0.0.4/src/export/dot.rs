use petgraph::graph::{Graph, NodeIndex};
use petgraph::dot::Dot;
use pyo3::{Py, Python};
use crate::tree::game::Game;
use crate::tree::node::Decision;
use crate::tree::utility::Utility::Numeral;

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

    let index = match node.utility {
        Numeral(x) => {
            let utility = format!("({}, {})", x[0], x[1]);
            graph.add_node(format!("label=below:{{${utility})$}}"))
        },
        _ => graph.add_node(node.children[0].borrow(py).clone().player.name.clone())
    };

    for child in node.children {
        let (node_index, name) = add_nodes_to_graph(child, graph, py);
        graph.extend_with_edges(&[
            (index, node_index, name)
        ]);
    }
    (index, node.name.clone())
}

// do this for both information sets and string!
fn test_string(){
    let mut owned_string: String = "hello ".to_owned();
    push_string(&mut owned_string);
    println!("{owned_string}");
}
fn push_string(test: &mut String){
    test.push_str("World!")
}

#[cfg(test)]
mod tests {
    use crate::export::dot::test_string;

    // importing names from outer scope.
    #[test]
    fn test_graph() {
        test_string();
    }

}
