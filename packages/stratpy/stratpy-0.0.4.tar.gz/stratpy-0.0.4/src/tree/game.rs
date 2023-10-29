use std::io::Error;
use pyo3::{prelude::*};
use crate::export::dot;
use crate::export::latex;
use crate::tree::node::*;

#[pyclass]
#[derive(Clone)]
pub struct Game {
    #[pyo3(get)]
    title: String,
    #[pyo3 (get)]
    pub player: Vec<Player>,
    #[pyo3(get)]
    gametype: Type,
    #[pyo3(get)]
    pub root: Py<Decision>,
}

#[pymethods]
impl Game {
    #[new]
    // currently all fields are optional and will create sensible defaults.
    // TODO: infer gametype based on input.
    // TODO: overload new function with support for matrix input
    fn new(title: Option<String>, players: Option<usize>, gametype: Option<Type>,  py:Python) -> Self {
        Game{
            title: title.unwrap_or("Untitled Game".parse().unwrap()),
            gametype: gametype.unwrap_or(Type::Normal),
            player: create_players(players.unwrap_or(2)),
            root: Decision::new(Player::new(None), String::from("root"),
                                None, None, None, py),
        }
    }
    pub fn export(&self, py: Python) -> String {
        dot::export_dot(self.clone(), py)
    }
    pub fn export_latex(&self, scale: Option<f32>, filename: Option<&str>, py: Python) -> Result<(), Error>{
        let scale = scale.unwrap_or(2.5);
        match filename {
            None => {
                latex::generate_latex(self.clone(), scale, py);
                Ok(())
            },
            Some(filename) => latex::write_to_file(self.clone(), scale, filename, py),
        }.expect("Error");
        Ok(())
    }


    // TODO: consider removing the abstraction
    pub fn get_ref(&self, py: Python) -> Py<Game>{
        Py::new(py, self.clone()).unwrap()
    }
    // overloads + to be used to for adding nodes to game.
    // returns a python reference to game in order to continue adding
    // nodes successively. The reference to root is borrowed temporarily
    // as a mutable in order to push nodes to children.
    fn __add__(&mut self, other: Py<Decision>, py: Python) -> Py<Game> {
        self.root.borrow_mut(py).children.push(other.clone());
        self.get_ref(py)
    }
    // python's toString method
    // currently returns a string representation of game, and root's children
    fn __str__(&self, py: Python) -> String {
        let mut str = format!("title: {} root: {} children: ", self.title, self.root.borrow_mut(py).name);
        let children = self.root.borrow_mut(py).children.clone();
        for child in children{
            str.push_str(&*child.borrow_mut(py).__str__());
        }
        str
    }
    // The length of root's children used during testing.
    pub fn length(&self, py: Python) -> usize {
        self.root.borrow_mut(py).children.len()
    }
}

// Creates a vector of players, where the 0th element is reserved for nature
pub fn create_players(player_num: usize) -> Vec<Player>{
    let mut players: Vec<Player> = Vec::new();
    players.push(Player::new(Option::from("Nature".to_string())));
    for i in 0..player_num {players.push(Player::new(format!("Player {}", i+1).into()))}
    players
}

// Consider: This might not have to be exposed to the user
// but can be inferred and methods can be adjusted accordingly
#[pyclass]
#[derive(Clone)]
pub enum Type {
    Normal,
    Extensive,
}

pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    // importing names from outer scope.
    use super::*;
    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

}