import java.io.*;

public class Main {
    public static void main(String[] args) {
        Integer numberOfCommands = 0;
        int numberOfSymbols = 16;
        String filePath = args[0];
        Parser parser = new Parser(filePath);
        Code code = new Code();
        SymbolTable symbolTable = new SymbolTable();

        while (parser.hasMoreCommands()) {
            parser.advance();
            if (parser.commandType().equals("A_COMMAND") || parser.commandType().equals("C_COMMAND")) {
                numberOfCommands++;
            }
            if (parser.commandType().equals("L_COMMAND")) {
                if (!symbolTable.contains(parser.symbol())) {
                    symbolTable.addEntry(parser.symbol(), numberOfCommands);
                }
            }
        }
        String fileName = parser.getFileName().replace("asm", "hack");
        String stringBin = "0000000000000000";
        try {
            File fout = new File(fileName);
            FileOutputStream fos = new FileOutputStream(fout);
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
            parser = new Parser(filePath);
            while (parser.hasMoreCommands()) {
                parser.advance();
                if (parser.commandType().equals("A_COMMAND")) {
                    String currentCommand = "null";
                    try {
                        currentCommand = Integer.toBinaryString(Integer.parseInt(parser.symbol()));
                    } catch (NumberFormatException exception) {
                        if (!symbolTable.contains(parser.symbol())) {
                            symbolTable.addEntry(parser.symbol(), numberOfSymbols++);
                        }
                        currentCommand = Integer.toBinaryString(symbolTable.getAddress(parser.symbol()));
                    } finally {
                        currentCommand = stringBin.substring(currentCommand.length()) + currentCommand;
                        bw.write(currentCommand);
                        bw.newLine();
                    }

                }
                if (parser.commandType().equals("C_COMMAND")) {
                    String out = "111" + code.comp(parser.comp()) + code.dest(parser.dest()) + code.jump(parser.jump());
                    bw.write(out);
                    bw.newLine();
                }
            }
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}