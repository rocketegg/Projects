package main.strategy.impl;

import java.util.ArrayList;
import java.util.Random;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.strategy.Strategy;
import main.strategy.examiner.TicTacToeBoardExaminer;

public class RandomStrategy implements Strategy {

	private String side;
	private TicTacToeBoardExaminer examiner;
	
	public RandomStrategy(TicTacToeBoard board, String mySide) {
		this.side = mySide;
		this.examiner = new TicTacToeBoardExaminer(board);
	}
	
	@Override
	public GridCell execute() {
		ArrayList<GridCell> openMoves = examiner.getAllOpenMoves(side);
		return getRandom(openMoves);
	}
	
	private static int randomInt(int min, int max) {
	    Random rand = new Random();
	    return rand.nextInt((max - min) + 1) + min;
	}
	
	/**
	 * Returns a random move given a list of moves
	 * @param listOfMoves
	 * @return
	 */
	public static GridCell getRandom(ArrayList<GridCell> listOfMoves) {
		int randomIndex = randomInt(0, listOfMoves.size()-1);
		GridCell spot = listOfMoves.get(randomIndex);
		return spot;
	}

}
