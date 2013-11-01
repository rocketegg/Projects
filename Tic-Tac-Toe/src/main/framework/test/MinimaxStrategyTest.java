package main.framework.test;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.framework.TicTacToeGame;
import main.player.Player;
import main.player.impl.Computer;
import main.strategy.Strategy;
import main.strategy.StrategyFactory;

import org.junit.Before;

import junit.framework.TestCase;

public class MinimaxStrategyTest extends TestCase {

	private TicTacToeBoard board = null;
	
	@Before
	public void setUp() {
		board = new TicTacToeBoard();
		/*
		 *  [X] [X] [O]
			------------
			[O] [X] [O]
			------------
			[_] [_] [_]
		 */
		board.update(new GridCell(0,0,false,"X"));
		board.update(new GridCell(0,1,false,"X"));
		board.update(new GridCell(0,2,false,"O"));
		board.update(new GridCell(1,0,false,"O"));
		board.update(new GridCell(1,1,false,"X"));
		board.update(new GridCell(1,2,false,"O"));

		System.out.println("Setting up board.");
		board.print();
	}
	
	public void testMinimaxStrategy() {
		System.out.println("MINIMAX TEST ==========");
		//System.out.println("Assuming O's Turn:");
		//StrategyFactory sf = new StrategyFactory();
		Player computer1 = new Computer("O");
		Player computer2 = new Computer("X");
		TicTacToeGame newGame = new TicTacToeGame(board, computer1, computer2);
		newGame.playEntireGame();
	}
}
