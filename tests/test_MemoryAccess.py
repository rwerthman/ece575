from src.MemoryAccess import MemoryAccess
from src.ControlUnit import ControlUnit
from src.InstructionDecode import InstructionDecode
from src.InstructionFetch import InstructionFetch
from src.Execution import Execution

import unittest

class MemoryAccessTestCase( unittest.TestCase ):
    
    def testExecuteMemRead( self ):
        controlUnit = ControlUnit()
        IF = InstructionFetch( [] )
        ID = InstructionDecode( controlUnit, IF )
        EX = Execution( controlUnit, ID )
        MEM = MemoryAccess( controlUnit, ID, EX )

        controlUnit.MemRead = 1
        EX.ALUResult = 3

        MEM.execute()

        self.assertEqual( MEM.readData, 4 )

    def testExecuteMemWrite( self ):
        controlUnit = ControlUnit()
        IF = InstructionFetch( [] )
        ID = InstructionDecode( controlUnit, IF )
        EX = Execution( controlUnit, ID )
        MEM = MemoryAccess( controlUnit, ID, EX )

        controlUnit.MemWrite = 1
        EX.ALUResult = 3
        ID.writeRegister = "r1"
        ID.writeToRegister( 6 )
        ID.readRegister2 = "r1"

        MEM.execute()

        self.assertEqual( MEM.dataMemory[3], 6 )

if __name__ == '__main__':  
    unittest.main()