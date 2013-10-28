package main.strategy.impl;

import java.util.ArrayList;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.strategy.Strategy;
import main.strategy.examiner.TicTacToeBoardExaminer;

public class TieStrategy implements Strategy {

	private TicTacToeBoard board;
	private String side;
	private TicTacToeBoardExaminer examiner;
	
	public TieStrategy(TicTacToeBoard board, String mySide) {
		this.board = board;
		this.side = mySide;
		this.examiner = new TicTacToeBoardExaminer(board);
	}
	
	@Override
	public GridCell execute() {
		//1. if there is a losing position, block it
		ArrayList<GridCell> losingPosition = examiner.getLosingPositions(side);
		if (losingPosition.size() > 0) {
			board.print();
			System.out.println("found a losing cell: " + losingPosition.get(0).toLongString());
			return losingPosition.get(0);
		}
		
		//2. if center position is available, take it.
		GridCell center = examiner.getCenter(side);
		if (center != null) {
			System.out.println("taking center.");
			return center;
		}
		
		//3. if there is a non-winning position, take it
		ArrayList<GridCell> nonWinning = examiner.getNonWinningPosition(side);
		if (nonWinning.size() > 0) {
			board.print();
			GridCell move = RandomStrategy.getRandom(nonWinning);
			System.out.println("found a non winning cell: " + move.toLongString());
			return move;
		} else
			return new RandomStrategy(board, side).execute();
	}

}
