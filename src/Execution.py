class Execution( object ):

    def __init__( self, controlUnit, instructionDecode ):
        self.controlUnit = controlUnit
        self.ID = instructionDecode

        self.ALUResult = None
    
    def execute( self ):

        # Add
        if self.controlUnit.ALUOp == 0:
            if self.controlUnit.ALUSrc == 0:
                self.ALUResult = self.ID.readFromRegister( self.ID.readRegister1 ) + self.ID.readFromRegister( self.ID.readRegister2 )
            else:
                self.ALUResult = self.ID.readFromRegister( self.ID.readRegister1 ) + self.ID.address


