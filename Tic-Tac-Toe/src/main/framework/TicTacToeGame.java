package main.framework;

import main.player.Player;

/**
 * A fully encapsulated tic tac toe game, with a board, two players.
 * The function playEntireGame will run through the game.
 * To play manually, create a game with a player of type Person
 * @author rocketegg
 *
 */
public class TicTacToeGame {

	private TicTacToeBoard board;
	private Player player1;
	private Player player2;
	private boolean player1Turn;
	private int winner;	//-1 = no winner, 0 = tie, 1 = player1, 2 = player2
	
	public TicTacToeGame() {
		board = new TicTacToeBoard();
		winner = -1;
	}
	
	public TicTacToeGame(Player player1, Player player2) {
		this();
		this.player1Turn = true;
		this.player1 = player1;
		this.player2 = player2;
	}
	
	/**
	 * Returns whether there is a winner
	 * @return
	 */
	public boolean hasWinner() {
		return hasRowWinner() || hasColWinner() || checkDiagonals();
	}
	
	public boolean hasTie() {
		boolean hasTie = (board.getAllOpenCells().size() == 0) && (!hasWinner());
		if (hasTie) {
			System.out.println("found a tie and no winner");
			winner = 0;
		}
		return hasTie;
	}
	
	/**
	 * Makes the current player take a turn
	 */
	public void takeTurn() {
		if (player1Turn) {
			updateGrid(player1.chooseMove(board));
		} else {
			updateGrid(player2.chooseMove(board));
		}
		player1Turn = !player1Turn;
	}
	
	/**
	 * Updates the board with the currentMove
	 * @param currentMove
	 */
	private void updateGrid(GridCell currentMove) {
		board.update(currentMove);
	}
	
	/**
	 * Plays through the entire game and returns the winner
	 */
	public int playEntireGame() {
		while (!hasWinner() && !hasTie()) {
			takeTurn();
		}
		board.print();
		System.out.println("Game over.");
		switch(winner) {
			case 0:
				System.out.println("Game was a tie.");
				break;
			case 1: 
				System.out.println("Player 1 " + player1 + " is the winner.");
				break;
			case 2: 
				System.out.println("Player 2 " + player2 + " is the winner.");
				break;
			default:
				System.out.println("Error");
				break;
		}
		return winner;
	}
	
	/**
	 * Returns the player if there is a player who wins by row
	 * @return the Player, otherwise returns null
	 */
	private boolean hasRowWinner() {
		for (int row = 0; row < board.getRows(); row++) {
			boolean hasWinner = true;
			String side = board.getCell(row, 0).getValue();
			if (side.equals(player1.getSide()) || side.equals(player2.getSide())) {
				for (int col = 1; col < board.getCols(); col++) {
					hasWinner &= side.equals(board.getCell(row, col).getValue());
				}
				if (hasWinner) {
					winner = (player1.getSide().equals(side)) ? 1 : 2;
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
	private boolean hasColWinner() {
		for (int col = 0; col < board.getCols(); col++) {
			boolean hasWinner = true;
			String side = board.getCell(0, col).getValue();
			if (side.equals(player1.getSide()) || side.equals(player2.getSide())) {
				for (int row = 1; row < board.getRows(); row++) {
					hasWinner &= side.equals(board.getCell(row, col).getValue());
				}
				if (hasWinner) {
					winner = player1.getSide().equals(side) ? 1 : 2;
					return true;
				}
			} else {
				hasWinner = false;
			}
		}
		return false;
	}
	
	private boolean checkDiagonals() {
		boolean hasWinner = true;
		String topLeft = board.getCell(0,0).getValue();
		if (topLeft.equals(player1.getSide()) || topLeft.equals(player2.getSide())) {
			for (int x = 1; x < board.getCols(); x++) {
				hasWinner &= topLeft.equals(board.getCell(x,x).getValue());
			}
			if (hasWinner) {
				winner = player1.getSide().equals(topLeft) ? 1 : 2;
				return true;
			}
		}
		
		hasWinner = true;
		String topRight = board.getCell(0,board.getCols()-1).getValue();
		if (topRight.equals(player1.getSide()) || topRight.equals(player2.getSide())) {
			for (int row = 1; row < board.getRows(); row++) {
				hasWinner &= topRight.equals(board.getCell(row,board.getCols()-1-row).getValue());
			}
			if (hasWinner) {
				winner = player1.getSide().equals(topRight) ? 1 : 2;
				return true;
			}
		}
		return false;
	}
	

	
}
