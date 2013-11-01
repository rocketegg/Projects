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
		// TODO Auto-generated method stub
		GridCell bestMove = chooseMinimaxMove(board, side).getMove();
		System.out.println("Executing minimax on side: " + side + " Move: " + bestMove.toLongString());
		return bestMove;
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
	private BestMove chooseMinimaxMove(TicTacToeBoard board, String side) {
		int bestScore;
		GridCell bestMove = null;
		String otherSide = side.equals("X") ? "O" : "X";
		//System.out.println("It's " + side + " turn");
		if ((bestScore = TicTacToeBoardExaminer.getScore(board, side)) != 10) {
			//System.out.println("Grid is scorable SCORE: " + bestScore);
			//board.print();
			return new BestMove(null, bestScore);
		}
		
		//System.out.println("Board is not scorable yet.");
		//board.print();
		ArrayList<GridCell> possibleMoves = new TicTacToeBoardExaminer(board).getAllOpenMoves(side);

		if (this.side.equals("X"))	{ //Player's turn
			bestScore = -2;
		} else {	//Opponent's turn
			bestScore = 2;
		}
		//System.out.println("best score:" + bestScore);
		
		for (GridCell move : possibleMoves) {
			//System.out.println("TRYING MOVE: " + move.toLongString());
			board.update(move);
			GridCell undoMove = new GridCell(move.getRow(), move.getCol(), true, "_");
			BestMove b = chooseMinimaxMove(board, otherSide);
			board.update(undoMove);
			if (this.side.equals("X")) {	//player turn
				if (b.getScore() > bestScore) {
					bestScore = b.getScore();
					bestMove = move;
				}
			} else {	//opponent turn
				if (b.getScore() < bestScore) {
					bestScore = b.getScore();
					bestMove = move;
				}
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
	}

}
