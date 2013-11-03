package main.strategy.impl;

import java.util.ArrayList;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.strategy.Strategy;
import main.strategy.examiner.TicTacToeBoardExaminer;

public class WinStrategy implements Strategy {

	private TicTacToeBoard board;
	private String side;
	
	public WinStrategy(TicTacToeBoard board, String mySide) {
		this.board = board;
		this.side = mySide;
	}
	
	/**
	 * Tries to win against the opponent based on the board state and side
	 */
	@Override
	public GridCell execute() {
		//1. if there is a winning position, take it
		ArrayList<GridCell> winningCell = TicTacToeBoardExaminer.getWinningPositions(board, side);
		if (winningCell.size() > 0) {
			GridCell move = winningCell.get(0);
			return move;
		}
		
		//2. if there is a losing position, block it
		ArrayList<GridCell> losingCell = TicTacToeBoardExaminer.getLosingPositions(board, side);
		if (losingCell.size() > 0) {
			GridCell move = losingCell.get(0);
			return move;
		}
		
		//TODO: Implement checking of forks. This will get you to 100% win or tie rate
		
		//3. Otherwise get the optimal position
		GridCell optimal = TicTacToeBoardExaminer.getOptimal(board, side);
		if (optimal != null)
			return optimal;
		
		//4. Otherwise just move randomly
		else  
			return new RandomStrategy(board, side).execute();
		
	}

}
