class WriteBack( object ):

    def __init__( self, controlUnit, instructionDecode, execution, memoryAccess ):
        self.controlUnit = controlUnit
        self.ID = instructionDecode
        self.EX = execution
        self.MEM = memoryAccess

    def execute( self ):
        if self.controlUnit.MemToReg:
            self.ID.writeToRegister( self.MEM.readData )
        else:
            self.ID.writeToRegister( self.EX.ALUResult )