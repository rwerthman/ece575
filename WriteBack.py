class WriteBack( object ):

    def __init__( self, aInstructionDecode ):
        self.mMemToReg = False
        self.mInstructionDecode = aInstructionDecode 

    def execute( self, aALUResult, aReadData ):
        if self.mMemToReg:
            self.mInstructionDecode.writeRegister( self.mInstructionDecode.mWriteRegister, aReadData )
        else:
            self.mInstructionDecode.writeRegister( self.mInstructionDecode.mWriteRegister, aALUResult )