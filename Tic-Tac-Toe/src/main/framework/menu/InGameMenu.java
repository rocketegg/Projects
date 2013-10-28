package main.framework.menu;

import java.util.ArrayList;
import java.util.Scanner;

import main.framework.GridCell;
import main.framework.TicTacToeBoard;
import main.strategy.examiner.TicTacToeBoardExaminer;
import main.strategy.impl.RandomStrategy;
import main.strategy.impl.TieStrategy;
import main.strategy.impl.WinStrategy;

/**
 * InGameMenu presents a player (of type person) with in game menu options
 * e.g. the user can play a move
 * @author rocketegg
 *
 */
public class InGameMenu implements Menu {

	private TicTacToeBoard board;
	private Scanner in;
	private GridCell move;
	private String side;
	
	public InGameMenu(TicTacToeBoard board, String side) {
		this.board = board;
		in = new Scanner(System.in);
		this.side = side;
		move = null;
	}
	
	@Override
	public void print() {
		System.out.println("Player " + side + " turn ---------------------");
		System.out.println("1.   Pick move.");
		System.out.println("2.   See if game is winnable.");
		System.out.println("3.   See different strategy.");
		System.out.println("4.   Quit game.");
	}
	
	@Override
	public void start() {
		// TODO Auto-generated method stub
		boolean quit = false;
		do {
        	int menuItem = printAndGetOption();
            switch (menuItem) {
            case 1:
            	move = getPlayerMove();
            	quit = true;
        		break;
            case 2:
            	isGameWinnable();
                break;
            case 3:
            	//see what a strategy would do
            	getStrategyMove();
                break;
            case 4:
            	System.exit(1);
                break;
            default:
            	System.out.println("Invalid choice.");
            }
      } while (!quit);
	}
	
	private int printAndGetOption() {
		print();
		return getMenuOption();
	}
	
	private int getMenuOption() {
		System.out.print("Choose menu item: ");
		try {
			int menuItem = in.nextInt();
			return menuItem;
		} catch (Exception e) {
			return -1;
		}
	}
	
	/**
	 * Gets the (manual) player's move 
	 * @return
	 */
	private GridCell getPlayerMove() {
		board.printWithMovesOptions();
		ArrayList<GridCell> openMoves = board.getAllOpenCells();
		int option = 0;
		boolean validOption = false;
		do {
			System.out.println("Choose Move:");
			option = in.nextInt();
			for (GridCell g: openMoves) {
				if (g.getPosition() == option)
					return g;
			}
			System.out.println("Invalid move, please choose another.");
		} while (!validOption);
		
		return null;
	}

	public GridCell getMove() {
		if (move == null) {
			start();
		}
		return new GridCell(move.getRow(), move.getCol(), false, side);
	}
	
	public boolean isGameWinnable() {
		TicTacToeBoardExaminer examiner = new TicTacToeBoardExaminer(board);
		ArrayList<GridCell> winningMoves = examiner.getWinningPositions(side);
		if (winningMoves.size() > 0) {
			System.out.println("The game is winnable.  You can move to any of these: ");
			for (GridCell g : winningMoves) 
				System.out.println("\t" + g.toLongString());
			return true;
		} else {
			System.out.println("The game is not currently winnable.");
			return false;
		}
	}
	
	private void getStrategyMove() {
		 System.out.print("Select player to see strategy - [Win 'W', Tie 'T', Random 'R']: ");
         String option = in.next();
         if (option.equalsIgnoreCase("W")) {
        	 System.out.println("Win strategy would choose: " + new WinStrategy(board, side).execute().toLongString());
         } else if (option.equalsIgnoreCase("T")) {
        	 System.out.println("Tie strategy would choose: " + new TieStrategy(board, side).execute().toLongString());
         } else if (option.equalsIgnoreCase("R")) {
        	 System.out.println("Random strategy would choose: " + new RandomStrategy(board, side).execute().toLongString());
         } else {
        	 System.out.println("Invalid strategy.");
         }
	}
	
}
