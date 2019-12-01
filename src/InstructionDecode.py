class InstructionDecode( object ):

    def __init__( self, controlUnit, instructionFetch ):

        self.IF = instructionFetch

        self.controlUnit = controlUnit

        self.registerFile = {
            "r1" : 1,
            "r2" : 2,
            "r3" : 0
        }

        self.readRegister1 = None
        self.readRegister2 = None
        self.writeRegister = None
        self.writeData = None

        self.supportedInstrutions = {
            "add" : "rtype"
        }
    
    def execute( self ):
        
        # Determine which control unit signals need to be asserted
        # based on the instruction operation
        self.controlUnit.setControlSignals( self.IF.instruction[0] )

        instructionType = self.supportedInstrutions[self.IF.instruction[0]]

        if instructionType == 'rtype':
            self.readRegister1 = self.IF.instruction[1] # rs
            self.readRegister2 = self.IF.instruction[2] # rt
            self.writeRegister = self.IF.instruction[3] # rd

    def readFromRegister( self, register ):
        return self.registerFile[register]

    def writeToRegister( self, data ):
        self.registerFile[self.writeRegister] = data