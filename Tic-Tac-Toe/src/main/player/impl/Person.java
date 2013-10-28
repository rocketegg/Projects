package main.player.impl;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.framework.menu.InGameMenu;
import main.player.Player;

/**
 * Manual player, doesn't employ any strategy
 * @author rocketegg
 *
 */
public class Person extends Player {

	private InGameMenu inGameMenu;
	
	public Person(String side) {
		setSide(side);
	}
	
	@Override
	public GridCell chooseMove(TicTacToeBoard board) {
		board.print();
		inGameMenu = new InGameMenu(board, getSide());
		return inGameMenu.getMove();
	}

	@Override
	public String toString() {
		return "Person [" + getSide() + "]";
	}
}
