from InstructionFetch import InstructionFetch

class CPU( object ):

    def __init__( self, aInstructionMemory ):
        self.mInstructionMemory = aInstructionMemory
        self.IF = InstructionFetch( self.mInstructionMemory )

    def cycle( self ):
        for _ in self.mInstructionMemory:
            self.IF.execute()
