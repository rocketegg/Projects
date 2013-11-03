package main.strategy.impl;

import java.util.ArrayList;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.strategy.Strategy;
import main.strategy.examiner.TicTacToeBoardExaminer;

public class MinimaxStrategy implements Strategy {
	private TicTacToeBoard board;
	private String side;
	private TicTacToeBoardExaminer examiner;
	
	public MinimaxStrategy(TicTacToeBoard board, String side) {
		this.board = board;
		this.side = side;
		this.examiner = new TicTacToeBoardExaminer(board);
	}
	
	@Override
	public GridCell execute() {
		//1. if there is a winning position, take it
		/*ArrayList<GridCell> winningCell = examiner.getWinningPositions(side);
		if (winningCell.size() > 0) {
			GridCell move = winningCell.get(0);
			return move;
		}
		
		//2. if there is a losing position, block it
		ArrayList<GridCell> losingCell = examiner.getLosingPositions(side);
		if (losingCell.size() > 0) {
			GridCell move = losingCell.get(0);
			return move;
		}*/
		
		BestMove bestMove = chooseMinimaxMove(board, side, 0);
		System.out.println("Executing minimax on side: " + side + " Move: " + bestMove.getMove().toLongString() + " score: " + bestMove.getScore());
		return bestMove.getMove();
	}
	
	/**
	 * 	The minimax algorithm to get the best move 
	 *  Basically, the algorithm works like this:
	 *    IF 
	 *    	The grid is scorable, return the last move and the score (1, 0, -1) for 
	 *    	player wins, tie, opponent wins, respectively.
	 *    ELSE
	 *    	For all the moves, find the lowest or highest score based on whose side it is
	 *      and return that move and score combination.
	 *  Note that if there are two paths that have an equal score, minimax is too dumb to take the immediate win path.
	 *  Thus it could be enhanced by adding in a more sophisticated scoring mechanism (e.g. if a winning path
	 *  is available, take it first)
	 * @param board
	 * @param lastMove
	 * @param side
	 * @return
	 */
	private BestMove chooseMinimaxMove(TicTacToeBoard board, String side, int depth) {
		int bestScore;
		GridCell bestMove = null;
		String otherSide = side.equals("X") ? "O" : "X";
		//System.out.println("It's " + side + " turn");
		if ((bestScore = TicTacToeBoardExaminer.getScore(board, side, depth)) != 100) {
			//System.out.println("\tSCORABLE -> SCORE: " + bestScore);
			//board.print();
			return new BestMove(null, bestScore);
		}
		
		//System.out.println("Board is not scorable yet.");
		//board.print();
		ArrayList<GridCell> possibleMoves = new TicTacToeBoardExaminer(board).getAllOpenMoves(side);
		
		if (side.equals("X"))	{ //Player's turn
			bestScore = -11;
		} else {	//Opponent's turn
			bestScore = 11;
		}
		//System.out.println("best score:" + bestScore);
		BestMove b = null;
		for (GridCell move : possibleMoves) {
			if (depth == 0) {
				System.out.println("TRYING MOVE: " + move.toLongString());
			}
			//
			board.update(move);
			GridCell undoMove = new GridCell(move.getRow(), move.getCol(), true, " ");
			if (depth == 0) {
				board.print();
			}
			b = chooseMinimaxMove(board, otherSide, depth+1);
			board.update(undoMove);
			if (side.equals("X")) {	//player turn
				//System.out.println("Finding max: " + b.getScore() + " vs " + bestScore);
				if (b.getScore() > bestScore) {
					//System.out.println("setting new max score: " + b.getScore());
					bestScore = b.getScore();
					bestMove = move;
				}
			} else if (side.equals("O")){	//opponent turn
				//System.out.println("Finding min: " + b.getScore() + " vs " + bestScore);
				if (b.getScore() < bestScore) {
					//System.out.println("setting new min score: " + b.getScore());
					bestScore = b.getScore();
					bestMove = move;
				}
			}
			
			if (depth == 0) {
				System.out.println("\tmove: " + move.toLongString());
				System.out.println("\tmove score: " + b.getScore());
			}
		}
		
		return new BestMove(bestMove, bestScore);
	}
	
	/**
	 * Just a wrapper class to hold a gridcell and a score
	 * @author Gamer
	 *
	 */
	private class BestMove {
		private GridCell move;
		private int score;
		
		public BestMove(GridCell move, int score) {
			this.move = move;
			this.score = score;
		}

		public GridCell getMove() {
			return move;
		}
		
		public int getScore() {
			return score;
		}
		
		@Override
		public String toString() {
			return move.toLongString() + " score: " + score;
		}
	}

}
