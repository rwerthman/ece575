class InstructionFetch( object ):

    def __init__( self, instructionMemory ):
        self.instructionMemory = instructionMemory
        self.instruction = ""
        self.PC = 0
    
    def execute( self ):

        # Assert the program counter doesn't exceed the number of instructions in
        # program memory
        assert self.PC < len( self.instructionMemory )

        # Fetch an instruction
        self.instruction = self.instructionMemory[ self.PC ]

        # Increment the program counter
        self.PC += 1