package main.framework;

import main.player.Player;
import main.player.impl.Champ;
import main.player.impl.George;
import main.player.impl.Person;
import main.player.impl.Toby;

public class PlayerFactory {
	
	/**
	 * Returns a new player and the side that player is on
	 * @param player
	 * @param side
	 * @return
	 */
	public Player getNewPlayer(String player, String side) {
		if (player.equalsIgnoreCase("champ")) {
			return new Champ(side);
		} else if (player.equalsIgnoreCase("toby")) {
			return new Toby(side);
		} else if (player.equalsIgnoreCase("george")){
			return new George(side);
		} else {
			return new Person(side);
		}
	}
}
