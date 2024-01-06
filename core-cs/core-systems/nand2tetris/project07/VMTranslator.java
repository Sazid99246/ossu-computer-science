
/*
 * Author: Kevin Wong
 * Assignment: NAND2TETRIS Project 7
 * Date: 11/2/2023
 * Professor: Nima Davarpanah
 * Course: CS3650-01
 * File: CodeWriter.java
 * File Description: The `VMTranslator` class functions as the main entry point for a Virtual Machine (VM) to HACK assembly 
 * translator program. It offers a `getVMFiles` method to gather VM files within a directory and a `main` method for translation. 
 * In the main method, it identifies whether the input is a single VM file or a directory containing VM files. For a single file, 
 * it checks its extension and adds it to a processing list, determining the output file's path. In the case of a directory, it 
 * compiles all the VM files and sets the output file path accordingly. A `CodeWriter` object is used to generate assembly code, 
 * with a `Parser` handling the parsing of VM commands. The translated assembly code is saved to the output file, and a message 
 * confirms the file's creation.
 */
import java.io.File;
import java.util.ArrayList;

/**
 * 
 */
public class VMTranslator {

    /**
     * Return all the .vm files in a directory
     * 
     * @param dir
     * @return
     */
    public static ArrayList<File> getVMFiles(File dir) {
        File[] files = dir.listFiles();
        ArrayList<File> result = new ArrayList<File>();
        for (File f : files) {
            if (f.getName().endsWith(".vm")) {
                result.add(f);
            }
        }
        return result;
    }

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Usage:java VMtranslator [filename|directory]");
        } else {
            File fileIn = new File(args[0]);
            String fileOutPath = "";
            File fileOut;
            CodeWriter writer;
            ArrayList<File> vmFiles = new ArrayList<File>();
            if (fileIn.isFile()) {
                String path = fileIn.getAbsolutePath();
                if (!Parser.getExt(path).equals(".vm")) {
                    throw new IllegalArgumentException(".vm file is required!");
                }
                vmFiles.add(fileIn);
                fileOutPath = fileIn.getAbsolutePath().substring(0, fileIn.getAbsolutePath().lastIndexOf(".")) + ".asm";
            } else if (fileIn.isDirectory()) {
                // if it is a directory get all vm files under this directory
                vmFiles = getVMFiles(fileIn);
                // if no vm file in this directory
                if (vmFiles.size() == 0) {
                    throw new IllegalArgumentException("No vm file in this directory");
                }
                fileOutPath = fileIn.getAbsolutePath() + "/" + fileIn.getName() + ".asm";
            }
            fileOut = new File(fileOutPath);
            writer = new CodeWriter(fileOut);
            for (File f : vmFiles) {
                Parser parser = new Parser(f);
                int type = -1;
                // start parsing
                while (parser.hasMoreCommands()) {
                    parser.advance();
                    type = parser.commandType();
                    if (type == Parser.ARITHMETIC) {
                        writer.writeArithmetic(parser.arg1());
                    } else if (type == Parser.POP || type == Parser.PUSH) {

                        writer.writePushPop(type, parser.arg1(), parser.arg2());
                    }
                }
            }
            // save file
            writer.close();
            System.out.println("File created : " + fileOutPath);
        }
    }

}