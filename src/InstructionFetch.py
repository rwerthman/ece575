class InstructionFetch( object ):

    def __init__( self, aInstructionMemory ):
        self.mInstructionMemory = aInstructionMemory
        self.mInstruction = ""
        self.mPC = 0
    
    def execute( self ):

        # Assert the program counter doesn't exceed the number of instructions in
        # program memory
        assert self.mPC < len( self.mInstructionMemory )

        # Fetch an instruction
        self.mInstruction = self.mInstructionMemory[ self.mPC ]

        # Increment the program counter
        self.mPC += 1