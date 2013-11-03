package main.framework;

/**
 * A class representing the state of a cell
 * @author rocketegg
 *
 */
public class GridCell {

	private int row;
	private int col;
	private boolean isOpen;
	private String value;
	
	/*
	 * Constructors
	 */
	
	public GridCell(int row, int col, boolean isOpen, String value) {
		this(row, col, isOpen);
		this.value = value;
	}
	
	public GridCell(int row, int col, boolean isOpen) {
		this.row = row;
		this.col = col;
		this.isOpen = isOpen;
		this.value = " ";
	}
	
	/*
	 * Getters and Setters
	 */
	public int getRow() {
		return row;
	}
	public void setRow(int row) {
		this.row = row;
	}
	public int getCol() {
		return col;
	}
	public void setCol(int col) {
		this.col = col;
	}
	public boolean isOpen() {
		return isOpen;
	}
	public void setOpen(boolean isOpen) {
		this.isOpen = isOpen;
	}
	public String getValue() {
		return value;
	}
	public void setValue(String value) {
		if (value.equalsIgnoreCase("X")) {
			this.value = "X";
		} else if (value.equalsIgnoreCase("O")) {
			this.value = "O";
		} else {
			System.out.println("ERROR in trying to set invalid value.");
		}
	}
	
	public String toLongString() {
		return "(" + row + "," + col + "): [" + this.value + "]";
	}
	
	public int getPosition() {
		return row * 3 + col;
	}
	
	@Override
	public String toString() {
		return this.value;
	}
	
	@Override
	public boolean equals(Object object)
    {
        boolean equal = false;
        if (object != null && object instanceof GridCell) {
        	GridCell comp = (GridCell) object;
            if (this.row == comp.getRow() && this.col == comp.getCol() && this.value.equals(comp.getValue()))
            	equal = true;
        }
        return equal;
    } 
}
