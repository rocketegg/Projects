package main.framework.menu;

import java.util.Scanner;

import main.framework.PlayerFactory;
import main.framework.TicTacToeGame;
import main.player.Player;
import main.player.impl.Champ;

/**
 * An entire encapsulated tic-tac-toe application with menu
 * @author Gamer
 *
 */
public class MainMenu implements Menu{

	private PlayerFactory playerFactory; 
	private Scanner in;
	
	public MainMenu() {
		playerFactory = new PlayerFactory();
		in = new Scanner(System.in);
	}
	
	@Override
	public void print() {
		System.out.println("\n\nWelcome to Tic-Tac-Toe.  Option 1 defaults to manual vs an opponent of your choice.");
        System.out.println("1.     Start a new game & select opponent."); 
        System.out.println("2.     Play computer vs computer.");
        System.out.println("3.     Exit.");
        System.out.println("==============================================");
	}
	
	@Override
	public void start() {
        boolean quit = false;
        do {
        	int menuItem = printAndGetOption();
            Player player1 = new Champ("X");
            Player player2 = new Champ("O");
            
            switch (menuItem) {
            case 1:
                player1 = playerFactory.getNewPlayer("person", "X");
                player2 = getPlayerFromMenu("O");
      			TicTacToeGame game = new TicTacToeGame(player1, player2);
      			game.playEntireGame();
                  break;
            case 2:
            	player1 = getPlayerFromMenu("X");
            	player2 = getPlayerFromMenu("O");
            	int numGames = getNumberGames();
            	int player1wins = 0;
            	int player2wins = 0;
            	int ties = 0;
            	long startTime   = System.currentTimeMillis();
            	//without pruning - 13 seconds to run 50 games
            	//with basic pruning - 
            	//with alpha-beta pruning - 
            	for (int x = 1; x < numGames+1; x++) {
            		System.out.println("Game " + x + ": ");
            		TicTacToeGame g = (x % 2 == 0) ? new TicTacToeGame(player1, player2) : new TicTacToeGame(player2, player1);
        			int winner = g.playEntireGame();
        			switch(winner) {
        			case 1:
        				if (x % 2 == 0) player1wins++; else player2wins++;
        				break;
        			case 2:
        				if (x % 2 == 0) player2wins++; else player1wins++;
        				break;
        			case 0:
        				ties++;
        				break;
        			default:
        				System.out.println("ERROR");
        			}
            	}
            	System.out.println("==========================================================");
            	System.out.println("RESULTS:");
                System.out.println("Player 1 " + player1 + " wins: " + player1wins + "\nPlayer 2 " + player2 +
                		" wins: " + player2wins + "\nTies: " + ties);
        		long endTime   = System.currentTimeMillis();
        		long totalTime = endTime - startTime;
        		System.out.println("Total time taken: " + totalTime);
                  break;
            case 3:
            	  quit = true;
                  break;
            default:
                  System.out.println("Invalid choice.");
            }
      } while (!quit);
      System.out.println("Thanks for playing!");
	}
	
	private int printAndGetOption() {
		print();
		return getMenuOption();
	}
	
	private int getMenuOption() {
		System.out.print("Choose menu item: ");
		int menuItem = in.nextInt();
		return menuItem;
	}
	
	private Player getPlayerFromMenu(String side) {
		 System.out.print("Select " + side + " player - [Champ = 'C', George = 'G', Toby = 'T', Minimax = 'B', Manual = 'M']: ");
         String option = in.next();
         if (option.equalsIgnoreCase("C")) {
         	return playerFactory.getNewPlayer("Champ", side);
         } else if (option.equalsIgnoreCase("G")) {
         	return playerFactory.getNewPlayer("George", side);
         } else if (option.equalsIgnoreCase("T")) {
         	return playerFactory.getNewPlayer("Toby", side);
         } else if (option.equalsIgnoreCase("B")) {
          	return playerFactory.getNewPlayer("Computer", side);
         } else {
        	 return playerFactory.getNewPlayer("Person", side);
         }
	}
	
	private int getNumberGames() {
		System.out.print("Select number of games to play? [e.g. 100]: ");
        int numGames = in.nextInt();
        return numGames;
	}
}
