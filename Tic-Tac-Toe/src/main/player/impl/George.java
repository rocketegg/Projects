package main.player.impl;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.player.Player;
import main.strategy.Strategy;
import main.strategy.StrategyFactory;

/**
 * Player who plays randomly
 * @author rocketegg
 *
 */
public class George extends Player {

	/**
	 * Should be set with "X" or "O"
	 * @param side
	 */
	public George(String side) {
		setSide(side);
	}
	
	@Override
	public GridCell chooseMove(TicTacToeBoard board) {
		StrategyFactory sf = new StrategyFactory();
		Strategy strategy = sf.getNewStrategy("random", board, getSide());
		return strategy.execute();
	}

	@Override
	public String toString() {
		return "George [" + getSide() + "]";
	}
}
