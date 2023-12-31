import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Parser {
    String fileName;
    Scanner scanner;
    String currentCommand;
    private static final String C_COMMAND = "C_COMMAND";
    private static final String A_COMMAND = "A_COMMAND";
    private static final String L_COMMAND = "L_COMMAND";

    public String getCurrentCommand() {
        return currentCommand;
    }

    public String getFileName() {
        return fileName;
    }

    public Parser(String filePath) {
        this.fileName = filePath;
        try {
            scanner = new Scanner(new File(filePath));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public boolean hasMoreCommands() {
        return scanner.hasNextLine();
    }

    public void advance() {
        if (hasMoreCommands()) {
            String line = scanner.nextLine();
            line = line.replaceAll(" ", "");
            Integer index = line.indexOf("//");
            if (line.isEmpty() || index == 0) {
                advance();
            } else if (index != -1) {
                line = line.substring(0, index);
                currentCommand = line;
            } else
                currentCommand = line;
        }
        return;
    }

    public void close() {
        scanner.close();
    }

    public String commandType() {
        if (currentCommand.startsWith("@")) {
            return A_COMMAND;
        } else if (currentCommand.contains("=") || currentCommand.contains(";")) {
            return C_COMMAND;
        } else if (currentCommand.contains(")")) {
            return L_COMMAND;
        } else {
            return null;
        }
    }

    public String symbol() {
        if (commandType() == A_COMMAND) {
            return currentCommand.replace("@", "");
        } else if (commandType() == L_COMMAND) {
            String tempCommand = currentCommand.replace("(", "");
            return tempCommand.replace(")", "");
        }
        return null;
    }

    public String dest() {
        if (commandType() == C_COMMAND) {
            Integer index = currentCommand.indexOf("=");
            if (index != -1)
                return currentCommand.substring(0, index);
        }
        return "null";
    }

    public String comp() {
        if (commandType() == C_COMMAND) {
            Integer indexStart = currentCommand.indexOf("=");
            Integer indexEnd = currentCommand.indexOf(";");
            if (indexEnd == -1) {
                return currentCommand.substring(indexStart + 1);
            } else {
                return currentCommand.substring(indexStart + 1, indexEnd);
            }
        }
        return "null";
    }

    public String jump() {
        if (commandType() == C_COMMAND) {
            if (currentCommand.contains(";")) {
                Integer index = currentCommand.indexOf(";");
                return currentCommand.substring(index + 1);
            }
        }
        return "null";
    }

}