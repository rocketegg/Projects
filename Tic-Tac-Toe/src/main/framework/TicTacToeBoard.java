package main.framework;

import java.util.ArrayList;

/**
 * Basic 3x3 tic tac toe board
 * @author rocketegg
 *
 */
public class TicTacToeBoard {
	
	private int rows = 3;
	private int cols = 3;
	private GridCell[][] board;
	
	public TicTacToeBoard() {
		board = new GridCell[rows][cols];
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				board[row][col] = new GridCell(row, col, true);
			}
		}
	}
	
	public void update(GridCell g) {
		board[g.getRow()][g.getCol()] = g;
	}

	/*
	 * Getters and Setters
	 */
	
	public int getRows() {
		return rows;
	}

	public void setRows(int rows) {
		this.rows = rows;
	}

	public int getCols() {
		return cols;
	}

	public void setCols(int cols) {
		this.cols = cols;
	}
	
	public GridCell getCell(int row, int col) {
		return board[row][col];
	}
	
	/**
	 * Returns all open cells in a java collection
	 * @return
	 */
	public ArrayList<GridCell> getAllOpenCells() {
		ArrayList<GridCell> openCells = new ArrayList<GridCell>();
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				if (board[row][col].isOpen()) {
					openCells.add(board[row][col]);
				}
			}
		}
		return openCells;
	}
	
	/**
	 * Returns if the board is empty
	 * @return
	 */
	public boolean isEmpty() {
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				if (!board[row][col].isOpen()) {
					return false;
				}
			}
		}
		return true;
	}
	
	/**
	 * Prints Board
	 */
	public void print() {
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				if (col < cols - 1) {
					System.out.print("[" + board[row][col] + "] ");
				} else {
					System.out.print("[" + board[row][col] + "]");
				}
			}
			if (row < rows - 1) {
				System.out.println("\n------------");
			}
		}
		System.out.println();
	}
	
	/**
	 * Prints Board With Moves
	 */
	public void printWithMovesOptions() {
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				if (col < cols - 1) {
					if (board[row][col].isOpen()) {
						System.out.print("[" + board[row][col].getPosition() + "] ");
					} else {
						System.out.print("[" + board[row][col] + "] ");
					}
				} else {
					if (board[row][col].isOpen()) {
						System.out.print("[" + board[row][col].getPosition() + "] ");
					} else {
						System.out.print("[" + board[row][col] + "] ");
					}
				}
			}
			if (row < rows - 1) {
				System.out.println("\n------------");
			}
		}
		System.out.println();
	}
	
	public String getStringRepresentation() {
		StringBuilder sb = new StringBuilder();
		for (int row = 0; row < rows; row++) {
			for (int col = 0; col < cols; col++) {
				sb.append(board[row][col]);
			}
		}
		return sb.toString();
	}
	
}
