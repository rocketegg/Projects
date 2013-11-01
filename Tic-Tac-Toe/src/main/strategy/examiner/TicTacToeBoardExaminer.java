package main.strategy.examiner;

import java.util.ArrayList;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;

public class TicTacToeBoardExaminer {

	private static final int PLAYER_WIN = 1;
	private static final int OPPONENT_WIN = -1;
	private static final int TIE = 0;
	private static final int NO_WINNER_YET = 10;
	
	private TicTacToeBoard board;
	
	public TicTacToeBoardExaminer(TicTacToeBoard board) {
		this.board = board;
	}
	
	/**
	 * Returns a score (if possible) based on a board configuration and 
	 * if you are the side
	 * Scores:
	 * 		1: side has won
	 * 	   -1: other side has won
	 *      0: is tie
	 *  
	 * @param board
	 * @param side
	 * @return
	 */
	public static int getScore(TicTacToeBoard board, String side) {
		String otherSide = side.equals("X") ? "O" : "X";
		if (sideHasWon(board, "X"))
			return PLAYER_WIN;
		else if (sideHasWon(board, "O"))
			return OPPONENT_WIN;
		else if (board.getAllOpenCells().size() == 0)
			return TIE;
		else
			return NO_WINNER_YET;
	}
	
	private static boolean sideHasWon(TicTacToeBoard board, String side) {
		return isRowWinner(board, side) || isColumnWinner(board, side) || isDiagonalWinner(board, side);
	}
	
	/**
	 * Returns the player if there is a player who wins by row
	 * @return the Player, otherwise returns null
	 */
	private static boolean isRowWinner(TicTacToeBoard board, String side) {
		for (int row = 0; row < board.getRows(); row++) {
			boolean hasWinner = true;
			String iside = board.getCell(row, 0).getValue();
			if (iside.equals(side)) {
				for (int col = 1; col < board.getCols(); col++) {
					hasWinner &= iside.equals(board.getCell(row, col).getValue());
				}
				if (hasWinner) {
					return true;
				}
			} else {
				hasWinner = false;
			}
		}
		return false;
	}
	
	/**
	 * returns if there is a column winner
	 * @return
	 */
	private static boolean isColumnWinner(TicTacToeBoard board, String side) {
		for (int col = 0; col < board.getCols(); col++) {
			boolean hasWinner = true;
			String iside = board.getCell(0, col).getValue();
			if (iside.equals(side)) {
				for (int row = 1; row < board.getRows(); row++) {
					hasWinner &= iside.equals(board.getCell(row, col).getValue());
				}
				if (hasWinner) {
					return true;
				}
			} else {
				hasWinner = false;
			}
		}
		return false;
	}
	
	private static boolean isDiagonalWinner(TicTacToeBoard board, String side) {
		boolean hasWinner = true;
		String topLeft = board.getCell(0,0).getValue();
		if (topLeft.equals(side)) {
			for (int x = 1; x < board.getCols(); x++) {
				hasWinner &= topLeft.equals(board.getCell(x,x).getValue());
			}
			if (hasWinner) {
				return true;
			}
		}
		
		hasWinner = true;
		String topRight = board.getCell(0,board.getCols()-1).getValue();
		if (topRight.equals(side)) {
			for (int row = 1; row < board.getRows(); row++) {
				hasWinner &= topRight.equals(board.getCell(row,board.getCols()-1-row).getValue());
			}
			if (hasWinner) {
				return true;
			}
		}
		return false;
	}
	
	
	/**
	 * Returns an arraylist of winning positions for the side X or O
	 * @param side
	 * @return
	 */
	public ArrayList<GridCell> getWinningPositions(String side) {
		ArrayList<GridCell> winningPositions = new ArrayList<GridCell>();	
		GridCell winningPosition = new GridCell(0,0,false);	//dummy gridcell
		//Check columns for winning position
		for (int y = 0; y < board.getCols(); y++) {
			int sideCount = 0;
			int emptyCount = 0;
			for (int x = 0; x < board.getRows(); x++) {
				if (board.getCell(x, y).getValue().equals(side)) {
					sideCount++;
				} else if (board.getCell(x, y).isOpen()) {
					emptyCount++;
					winningPosition = new GridCell(x, y, false, side);
				}
			}
			if (sideCount == 2 && emptyCount == 1) {
				winningPositions.add(winningPosition);
			}
		}
		
		//Check rows for winning position
		for (int y = 0; y < board.getRows(); y++) {
			int sideCount = 0;
			int emptyCount = 0;
			for (int x = 0; x < board.getCols(); x++) {
				if (board.getCell(y, x).getValue().equals(side)) {
					sideCount++;
				} else if (board.getCell(y, x).isOpen()) {
					emptyCount++;
					winningPosition = new GridCell(y, x, false, side);
				}
			}
			if (sideCount == 2 && emptyCount == 1) {
				winningPositions.add(winningPosition);
			}
		}
		
		//check diagonals for winning position (top left)
		int sideCount = 0;
		int emptyCount = 0;
		for (int y = 0; y < board.getRows(); y++) {
				if (board.getCell(y, y).getValue().equals(side)) {
					sideCount++;
				} else if (board.getCell(y, y).isOpen()) {
					emptyCount++;
					winningPosition = new GridCell(y, y, false, side);
				}
			if (sideCount == 2 && emptyCount == 1) {
				winningPositions.add(winningPosition);
			}
		}
		
		//check diagonal top right for winning position
		sideCount = 0;
		emptyCount = 0;
		for (int y = 0; y < board.getCols(); y++) { //(0,2), (1,1), (2,0)
			if (board.getCell(y, board.getCols()-1-y).getValue().equals(side)) {
				sideCount++;
			} else if (board.getCell(y, board.getCols()-1-y).isOpen()) {
				emptyCount++;
				winningPosition = new GridCell(y, board.getCols()-1-y, false, side);
			}
			if (sideCount == 2 && emptyCount == 1) {
				winningPositions.add(winningPosition);
			}
		}
		
		return winningPositions;
	}
	
	/**
	 * gets the losing positions for a side, if any
	 * @param side
	 * @return
	 */
	public ArrayList<GridCell> getLosingPositions(String side) {
		String otherSide = side.equals("X") ? "O" : "X"; 
		ArrayList<GridCell> losingPositions = getWinningPositions(otherSide);
		for (GridCell g : losingPositions) {
			g.setValue(side);
		}
		return losingPositions;
	}
	
	/**
	 * Will return an adjacent
	 * @param side
	 * @return
	 */
	public GridCell getOptimal(String side) {
		GridCell center = getCenter(side);
		if (center != null) 
			return center;
		
		GridCell cornerMove = getCorner(side);
		if (cornerMove != null)
			return cornerMove;
		
		return null;
		
	}
	
	public GridCell getCenter(String side) {
		if (board.getCell(1, 1).isOpen()) 
			return new GridCell(1,1,false,side);
		else 
			return null;
	}
	
	/**
	 * Returns first open corner
	 * @param side
	 * @return
	 */
	private GridCell getCorner(String side) {
		if (board.getCell(0, 2).isOpen()) {
			return new GridCell(0,2,false,side);
		} else if (board.getCell(2,2).isOpen()) {
			return new GridCell(2,2,false,side);
		} else if (board.getCell(2,0).isOpen()) {
			return new GridCell(2,0,false,side);
		} else if (board.getCell(0,0).isOpen()) {
			return new GridCell(0,0,false,side);
		} else 
			return null;
	}
	
	/**
	 * Gets a list of non-winning positions, which is basically a delta
	 * between the open move and the winning moves.
	 * @param side
	 * @return
	 */
	public ArrayList<GridCell> getNonWinningPosition(String side) {
		ArrayList<GridCell> openMoves = getAllOpenMoves(side);
		ArrayList<GridCell> winningMoves = getWinningPositions(side);
		boolean movesRemoved = openMoves.removeAll(winningMoves);
		return openMoves;
	}
	
	/**
	 * Returns all open moves for a side
	 * @param side
	 * @return
	 */
	public ArrayList<GridCell> getAllOpenMoves(String side) {
		ArrayList<GridCell> openBoard = board.getAllOpenCells();
		ArrayList<GridCell> openMoves = new ArrayList<GridCell>();
		for (GridCell g : openBoard) {
			openMoves.add(new GridCell(g.getRow(), g.getCol(), false, side));
		}
		return openMoves;
	}
	
	/**
	 * TODO: implement logic for whether there is a possible fork
	 * @param side
	 * @return
	 */
	public boolean canFork(String side) {
		return false;
	}
}
