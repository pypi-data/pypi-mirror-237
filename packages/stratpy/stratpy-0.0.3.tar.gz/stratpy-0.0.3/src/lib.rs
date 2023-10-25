use pyo3::prelude::*;
use crate::tree::game::*;
use crate::tree::node::*;
use crate::tree::utility::*;
pub mod tree;
pub mod export;

/// Packing all rust structs and functions into the stratpy module.
#[pymodule]
fn stratpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Game>()?;
    m.add_class::<Type>()?;
    m.add_class::<Variable>()?;
    m.add_class::<Decision>()?;
    m.add_class::<Player>()?;
    Ok(())
}