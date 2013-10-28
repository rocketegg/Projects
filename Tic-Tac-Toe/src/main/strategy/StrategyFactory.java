package main.strategy;

import main.framework.TicTacToeBoard;
import main.strategy.impl.RandomStrategy;
import main.strategy.impl.TieStrategy;
import main.strategy.impl.WinStrategy;

public class StrategyFactory {

	/**
	 * Returns a new player and the side that player is on
	 * @param player
	 * @param side
	 * @return
	 */
	public Strategy getNewStrategy(String strategy, TicTacToeBoard board, String side) {
		if (strategy.equalsIgnoreCase("win")) {
			return new WinStrategy(board, side);
		} else if (strategy.equalsIgnoreCase("tie")) {
			return new TieStrategy(board, side);
		} else if (strategy.equalsIgnoreCase("random")){
			return new RandomStrategy(board, side);
		} else {
			return null;
		}
	}
}
