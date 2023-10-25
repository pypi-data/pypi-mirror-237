use pyo3::{prelude::*};
use pyo3::types::PyTuple;

#[pyclass]
#[derive(Clone)]
pub struct Decision {
    #[pyo3(get)] pub player: Player, // make nature own struct?
    #[pyo3(get, set)] pub name: String,
    #[pyo3(get)] pub children: Vec<Py<Decision>>,
    #[pyo3(get, set)] pub utility: Vec<i32>,
}


#[pymethods]
impl Decision {
    #[new]
    pub fn new(player: Player, name: String, utility: Option<Vec<i32>>, py: Python) -> Py<Decision> {
        Py::new(py, Decision{
            player,
            name,
            children: Vec::new(),
            utility: utility.unwrap_or(vec![0, 0])
        }).unwrap()
    }
    pub fn add_node(slf: Py<Decision>, other: Py<Decision>, py: Python) -> Py<Decision>{
        slf.borrow_mut(py).children.push(other.clone());
        slf
    }
    #[pyo3(signature = (*args))]
    pub fn add_nodes(slf: Py<Decision>, py: Python, args: &PyTuple,) -> Py<Decision>{
        for arg in args{
            let decision: Py<Decision> = arg.extract().unwrap();
            slf.borrow_mut(py).children.push(decision);
        }
        slf
    }
    /*
    pub fn add_utility(&mut self, utility: PyObject){
        // TODO: Get values from enum
        self.utility = Option::from(utility);
    }*/

    // overloads + operator making it possible to push new nodes with +.
    // returns a reference to self for continurd pushing with additional +s
    fn __add__(slf: Py<Decision>, other: Py<Decision>, py: Python) -> Py<Decision> {
        slf.borrow_mut(py).children.push(other.clone());
        slf
    }
    pub fn __str__(&self) -> String {
        format!("(player: {} action: {})", self.player.name, self.name)
    }
}

#[pyclass]
#[derive(Clone)]
pub struct Player {
    #[pyo3(get, set)] pub name: String,
}


#[pymethods]
impl Player {
    #[new]
    pub fn new(name: Option<String>) -> Self {
        Player{ name: name.unwrap_or("player".to_string()), }
    }
}