use std::io::{self, Write};

fn main() {
    // Ask the user for the matrix size
    print!("Enter the matrix size (N): ");
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    // Read decision names for both players
    let mut decision_names = Vec::with_capacity(n);
    for i in 0..n {
        print!("Enter name for decision {}: ", i + 1);
        io::stdout().flush().unwrap();
        let mut decision_name = String::new();
        io::stdin().read_line(&mut decision_name).unwrap();
        decision_names.push(decision_name.trim().to_string());
    }

    // Read the payoff matrix for Player 1
    let mut payoff_matrix = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            print!("Enter the payoff for Player 1 when they choose '{}' and Player 2 chooses '{}': ", decision_names[i], decision_names[j]);
            io::stdout().flush().unwrap();
            input.clear();
            io::stdin().read_line(&mut input).unwrap();
            payoff_matrix[i][j] = input.trim().parse().unwrap();
        }
    }

    // Use Minimax to determine the best strategy
    let player1_best_strategy = best_strategy_for_player1(&payoff_matrix);
    let player2_best_strategy = best_strategy_for_player2(&payoff_matrix);

    println!("Best strategy for Player 1: {}", decision_names[player1_best_strategy]);
    println!("Best strategy for Player 2: {}", decision_names[player2_best_strategy]);
}

fn best_strategy_for_player1(matrix: &Vec<Vec<i32>>) -> usize {
    let mut best_value = i32::MIN;
    let mut best_strategy = 0;

    for i in 0..matrix.len() {
        let value = matrix[i].iter().min().unwrap();
        if *value > best_value {
            best_value = *value;
            best_strategy = i;
        }
    }

    best_strategy
}

fn best_strategy_for_player2(matrix: &Vec<Vec<i32>>) -> usize {
    let mut best_value = i32::MAX;
    let mut best_strategy = 0;

    for j in 0..matrix[0].len() {
        let value = matrix.iter().map(|row| row[j]).max().unwrap();
        if *value < best_value {
            best_value = *value;
            best_strategy = j;
        }
    }

    best_strategy
}