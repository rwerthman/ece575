class ControlUnit( object ):
    
    def __init__( self ):
        
        self.RegDst = 0
        self.RegWrite = 0
        self.ALUSrc = 0
        self.ALUOp = None
        self.MemWrite = 0
        self.MemRead = 0
        self.MemToReg = 0
    
    def setControlSignals( self, operation ):
        if operation == "add":
            self.RegDst = 1
            self.RegWrite = 1
            self.ALUSrc = 0
            self.ALUOp = 0 # Add
            self.MemWrite = 0
            self.MemRead = 0
            self.MemToReg = 0