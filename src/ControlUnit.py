class ControlUnit( object ):
    
    def __init__( self ):
        
        self.RegDst = False
        self.RegWrite = False
        self.ALUSrc = False
        self.ALUOp = False
        self.MemWrite = False
        self.MemRead = False
        self.MemToReg = False