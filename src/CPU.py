from .ControlUnit import ControlUnit
from .InstructionDecode import InstructionDecode
from .InstructionFetch import InstructionFetch
from .Execution import Execution
from .MemoryAccess import MemoryAccess
from .WriteBack import WriteBack

class CPU( object ):

    def __init__( self, instructionMemory ):
        self.controlUnit = ControlUnit()
        self.instructionMemory = instructionMemory
        self.IF = InstructionFetch( self.instructionMemory )
        self.ID = InstructionDecode( self.controlUnit, self.IF )
        self.EX = Execution( self.controlUnit, self.ID )
        self.MEM = MemoryAccess( self.controlUnit, self.ID, self.EX )
        self.WB = WriteBack( self.controlUnit, self.ID, self.EX, self.MEM )

    def cycle( self ):
        for _ in self.instructionMemory:
            self.IF.execute()
            self.ID.execute()
            self.EX.execute()
            self.MEM.execute()
            self.WB.execute()
    
