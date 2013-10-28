package main.player;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;

public abstract class Player {

	//Based on a grid state, choose the best move based on the players strategy
	private String side;
	
	public String getSide() {
		return side;
	}

	public void setSide(String side) {
		this.side = side;
	}

	/*
	 * abstract methods
	 */
	public abstract GridCell chooseMove(TicTacToeBoard board);
}
