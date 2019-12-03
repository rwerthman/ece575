class InstructionDecode( object ):

    def __init__( self, controlUnit, instructionFetch ):

        self.IF = instructionFetch

        self.controlUnit = controlUnit

        self.registerFile = {
            "r1" : 2,
            "r2" : 1,
            "r3" : 0
        }

        self.readRegister1 = None
        self.readRegister2 = None
        self.address = None
        self.writeRegister = None
        self.writeData = None

        self.supportedInstrutions = {
            "add" : "rtype",
            "lw"  : "itype",
            "sw"  : "itype"
        }
    
    def execute( self ):
        self.controlUnit.setControlSignals( self.IF.instruction[0] )

        instructionType = self.supportedInstrutions[self.IF.instruction[0]]

        self.readRegister1 = self.IF.instruction[1] # rs
        self.readRegister2 = self.IF.instruction[2] # rt

        if self.controlUnit.RegDst == 0:
            self.writeRegister = self.IF.instruction[2] # rt
        else:
            self.writeRegister = self.IF.instruction[3] # rd

        if instructionType == "itype":
            self.address = self.IF.instruction[3] # address


    def readFromRegister( self, register ):
        return self.registerFile[register]

    def writeToRegister( self, data ):
        self.registerFile[self.writeRegister] = data