package main.player.impl;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.player.Player;
import main.strategy.Strategy;
import main.strategy.StrategyFactory;

/**
 * This player chooses the best move based on minimax algorithm
 * @author Gamer
 *
 */
public class Minimax extends Player {

	/**
	 * Should be set with "X" or "O"
	 * @param side
	 */
	public Minimax(String side) {
		setSide(side);
	}
	
	@Override
	public GridCell chooseMove(TicTacToeBoard board) {
		StrategyFactory sf = new StrategyFactory();
		Strategy strategy = sf.getNewStrategy("minimax", board, getSide());
		return strategy.execute();
	}
	
	@Override
	public String toString() {
		return "Computer [" + getSide() + "]";
	}

}
