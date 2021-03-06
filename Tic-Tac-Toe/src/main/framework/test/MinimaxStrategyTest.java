package main.framework.test;

import junit.framework.TestCase;
import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.framework.TicTacToeGame;
import main.player.Player;
import main.player.impl.Minimax;

import org.junit.Before;

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
		//board.update(new GridCell(0,1,false,"X"));
		//board.update(new GridCell(0,2,false,"O"));
		//board.update(new GridCell(1,1,false,"O"));
		//board.update(new GridCell(1,1,false,"X"));
		//board.update(new GridCell(1,2,false,"O"));
		//board.update(new GridCell(2,0,false,"X"));
		//board.update(new GridCell(2,1,false,"_"));
		//board.update(new GridCell(2,2,false,"X"));

		System.out.println("Setting up board.");
		board.print();
	}
	
	public void testMinimaxStrategy() {
		System.out.println("MINIMAX TEST ==========");
		//System.out.println("Assuming O's Turn:");
		//StrategyFactory sf = new StrategyFactory();
		Player computer1 = new Minimax("O");
		//GridCell move = computer1.chooseMove(board);
		//System.out.println(move.toLongString());
		Player computer2 = new Minimax("X");
		TicTacToeGame newGame = new TicTacToeGame(board, computer1, computer2);
		newGame.playEntireGame();
	}
}
