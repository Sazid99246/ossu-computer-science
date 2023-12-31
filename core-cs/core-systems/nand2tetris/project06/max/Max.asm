// D = R0 - R1

   @R0

   D=M

   @R1

   D=D-M

   // If (D > 0) goto ITSR0

   @ITSR0

   D;JGT

   // Its R1

   @R1

   D=M

   @SET_RESULT

   0;JMP

(ITSR0)

   @R0

   D=M

(SET_RESULT)

   @R2

   M=D

(END)

   @END

   0;JMP