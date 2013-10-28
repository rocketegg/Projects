package main.strategy;

import main.framework.GridCell;

public interface Strategy {
	
	/**
	 * This function takes a game board and executes the strategy based on the opponent
	 * and the state of the game board.
	 * 
	 * @param board
	 * @param opponent
	 * @return
	 */
	public GridCell execute();
}
