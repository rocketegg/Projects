package main.player.impl;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.player.Player;
import main.strategy.Strategy;
import main.strategy.impl.WinStrategy;

/**
 * Player who always tries to win
 * @author rocketegg
 *
 */
public class Champ extends Player {

	/**
	 * Should be set with "X" or "O"
	 * @param side
	 */
	public Champ(String side) {
		setSide(side);
	}
	
	@Override
	public GridCell chooseMove(TicTacToeBoard board) {
		Strategy strategy = new WinStrategy(board, getSide());
		return strategy.execute();
	}

	@Override
	public String toString() {
		return "Champ [" + getSide() + "]";
	}
}
