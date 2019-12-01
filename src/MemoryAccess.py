class MemoryAccess( object ):

    def __init__( self, controlUnit, instructionDecode, execution ):
        self.controlUnit = controlUnit
        self.ID = instructionDecode
        self.EX = execution

        self.dataMemory = [1, 2, 3, 4]
        self.readData = None
    
    def execute( self ):

        if self.controlUnit.MemRead:
            self.readData = self.dataMemory[self.EX.ALUResult]
        elif self.controlUnit.MemWrite:
            self.dataMemory[self.EX.ALUResult] = self.ID.readFromRegister( self.ID.readRegister2 )