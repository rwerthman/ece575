class InstructionDecode( object ):

    def __init__( self ):
        # Control signal for the register file
        self.mRegWrite = False

        self.mRegisterFile = {
            "r1" : 1,
            "r2" : 2,
            "r3" : 0
        }

        self.mReadRegister1 = None
        self.mReadRegister2 = None
        self.mWriteRegister = None
        self.mWriteData = None

        self.mSupportedInstrutions = {
            "add" : "rtype"
        }

        self.currentOpCode = None
    
    def getInstructionType( self, instruction ):
        self.currentOpCode = instruction[0]
        return self.mSupportedInstrutions[self.currentOpCode]

    
    def execute( self, instruction ):
        instructionType = self.getInstructionType( instruction )

        if instructionType == 'rtype':
            self.mReadRegister1 = instruction[1] # rs
            self.mReadRegister2 = instruction[2] # rt
            self.mWriteRegister = instruction[3] # rd
            self.mRegWrite = True

    def readRegister( self, register ):
        return self.mRegisterFile[register]

    def writeRegister( self, register, data ):
        if self.mRegWrite:
            self.mRegisterFile[register] = data