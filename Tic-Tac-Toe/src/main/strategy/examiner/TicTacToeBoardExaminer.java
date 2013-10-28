package main.strategy.examiner;

import java.util.ArrayList;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;

public class TicTacToeBoardExaminer {

	private TicTacToeBoard board;
	
	public TicTacToeBoardExaminer(TicTacToeBoard board) {
		this.board = board;
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
