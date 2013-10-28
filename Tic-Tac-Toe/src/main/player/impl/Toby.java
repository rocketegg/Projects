package main.player.impl;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.player.Player;
import main.strategy.Strategy;
import main.strategy.StrategyFactory;

/**
 * Player who always tries to tie
 * @author rocketegg
 *
 */
public class Toby extends Player {

	/**
	 * Should be set with "X" or "O"
	 * @param side
	 */
	public Toby(String side) {
		setSide(side);
	}
	
	@Override
	public GridCell chooseMove(TicTacToeBoard board) {
		StrategyFactory sf = new StrategyFactory();
		Strategy strategy = sf.getNewStrategy("tie", board, getSide());
		return strategy.execute();
	}
	
	@Override
	public String toString() {
		return "Toby [" + getSide() + "]";
	}

}
