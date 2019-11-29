from InstructionDecode import InstructionDecode
from InstructionFetch import InstructionFetch
from Execution import Execution
from MemoryAccess import MemoryAccess
from WriteBack import WriteBack

class CPU( object ):

    def __init__( self, aInstructionMemory ):
        self.mInstructionMemory = aInstructionMemory
        self.IF = InstructionFetch( self.mInstructionMemory )
        self.ID = InstructionDecode()
        self.Execution = Execution()
        self.MemoryAccess = MemoryAccess()
        self.WriteBack = WriteBack( self.ID )

    def cycle( self ):
        for _ in self.mInstructionMemory:
            self.IF.execute()

            self.ID.execute( self.IF.mInstruction )

            self.Execution.execute(
                self.ID.currentOpCode,
                self.ID.readRegister( self.ID.mReadRegister1 ),
                self.ID.readRegister( self.ID.mReadRegister2)
            )

            self.MemoryAccess.execute( self.Execution.mALUResult )

            self.WriteBack.execute( self.MemoryAccess.mALUResult, self.MemoryAccess.mReadData )
    
